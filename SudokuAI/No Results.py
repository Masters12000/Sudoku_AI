#Custom Libraries
from Libraries.container import container
from Libraries.Timer import Timer
from Libraries.CPUThreaded import CPUThreaded
from Libraries.RAM import RamDetection
from Libraries.LoadBar import Load_Bar
from Results.RawData import RawData
from Results.GenerateResults import GenResults
from Results.Result import Result
import refreshMLStorage

# Imports of AI
import backtracking, CrossHatching_Random, ML, ML_Trainer
#Python Libraries
from dokusan import generators
from threading import Thread

success = 0

def aICaller(ai, grid):
    """
    Calls the AI's using a dictionary switch
    @param ai: AI algorithm chosen
    @param grid: Sudoku Grid
    @return: If found a solution (True/False)
    """
    available = {
        "Backtracking": backtracking.backtrackingAI,
        "CrossHatching-Random": CrossHatching_Random.CrossHatchingR,
        "Machine Learning without Training": ML.ML,
        "Machine Learning with Training": ML_Trainer.ML_Trainer
    }
    link = available[ai](grid)
    if link.start():
        r = True
    else:
        r = False

    return r
max_size = 9  # Must be a multiple of 3
ML_Range = 10000
success = 0
choices = {
    1: "Backtracking",
    2: "CrossHatching-Random",
    3: "Machine Learning without Training",
    4: "Machine Learning with Training",
    5: "All",
    6: "Machine Learning Only"
}

choiceList = list(choices.keys())

print("Available Solvers:")
for key, value in choices.items():
    print(f"{key} - {value}")
choice = int(input(""))
#choice = 5

cycles = int(input("How many cycles? "))
#cycles = 1000
print(f"Started at: {Timer().current()}")

timer = Timer()
lB = Load_Bar(cycles, 1)

method = None
for i in range(cycles):
    #Creating the Sudoku
    grid = [[0 for x in range(max_size)] for y in range(max_size)]
    cont = container(9)

    arr = generators.random_sudoku(avg_rank=150)
    cont.stringInput(arr)

    grid = cont.getGrid()
    orig = cont.copyGrid(grid)

    if choice >= min(choiceList) and choice <= max(choiceList):
        if choice == 5:
            for idx in range(1, 5):
                if idx != choice:
                    grid = cont.copyGrid(orig)
                    if method == None:
                        method = choices[idx]
                        if aICaller(method, grid):
                            success += 1

                    elif method != choices[idx]:
                        method = choices[idx]
                        if aICaller(method, grid):
                            success += 1
                    else:
                        if aICaller(method, grid):
                            success += 1

        elif choice == 6:
            ml_List = [3, 4]
            for idx in ml_List:
                grid = cont.copyGrid(orig)
                if method == None:
                    method = choices[ idx ]
                    if aICaller(method, grid):
                        success += 1

                elif method != choices[idx]:
                    method = choices[idx]
                    if aICaller(method, grid):
                        success += 1

                else:
                    if aICaller(method, grid):
                        success += 1

        else:
            method = choices[choice]
            if aICaller(method, grid):
                success += 1

    lB.updateLoadBar(i, choices[choice])
lB.updateLoadBar(cycles, choices[choice])

print(f"\nSuccesses: {success} of {cycles} Sudoku's\n")
print(f"Program took: {timer.exit()}")
print(f"Finished at: {timer.current()}")

refreshMLStorage.refresh()