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

def aICaller(ai, grid):
    """
    Calls the AI's using a dictionary switch
    @param ai: AI algorithm chosen
    @param grid: Sudoku Grid
    @return: result
    """
    available = {
        "Backtracking": backtracking.backtrackingAI,
        "CrossHatching-Random": CrossHatching_Random.CrossHatchingR,
        "Machine Learning without Training": ML.ML,
        "Machine Learning with Training": ML_Trainer.ML_Trainer
    }
    r = RawData()
    t = Timer()
    link = available[ai](grid)
    if link.start():
        r.success = True
    else:
        r.success = False

    r.method = ai
    r.timeSpent = t.exit()
    r.percentage = c.getLatestPercent()
    r.frequency = c.getLatestFrequency()
    r.attemptsTaken = link.attempts

    return r
max_size = 9  # Must be a multiple of 3
ML_Range = 250000
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
cycleList = [1000, 2500]
cycleList = [cycles]
print(f"Started at: {Timer().current()}")
for cycles in cycleList:
    for x in range(1, 4):
        print("Cycle => " + str(cycles) + ":" + str(x))
        results = []

        timer = Timer()
        lB = Load_Bar(cycles, 1)

        c = CPUThreaded()
        interval = 1
        cpuT = Thread(target=c.run, args=(interval,))
        cpuT.start()

        ram = RamDetection()
        ramT = Thread(target=ram.start, args=(interval,))
        ramT.start()

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
                                results.append(aICaller(method, grid))

                            elif method != choices[idx]:
                                method = choices[idx]
                                rdp = ram.differencePercent()
                                rdb = ram.differenceUsed()
                                results[-1].ramPercent = rdp
                                results[-1].ramBytes = rdb
                                results.append(aICaller(method, grid))

                            else:
                                results.append(aICaller(method, grid))

                elif choice == 6:
                    ml_List = [3, 4]
                    for idx in ml_List:
                        grid = cont.copyGrid(orig)
                        # print(grid)
                        if method == None:
                            method = choices[ idx ]
                            results.append(aICaller(method, grid))

                        elif method != choices[idx]:
                            method = choices[idx]
                            rdp = ram.differencePercent()
                            rdb = ram.differenceUsed()
                            results[ -1 ].ramPercent = rdp
                            results[ -1 ].ramBytes = rdb
                            results.append(aICaller(method, grid))

                        else:
                            results.append(aICaller(method, grid))

                else:
                    method = choices[choice]

                    results.append(aICaller(method, grid))

            lB.updateLoadBar(i, choices[choice])
        lB.updateLoadBar(cycles, choices[choice])

        #Ending Threaded Functions
        c.terminate()
        ram.end()

        rdp = ram.differencePercent()
        rdb = ram.differenceUsed()
        results[-1].ramPercent = rdp
        results[-1].ramBytes = rdb

        #for r in results:
        #    print(f"{r.method, r.timeSpent}")

        gen = GenResults()
        gen.listOfResults = results
        result = gen.getResult() # returns dictionary, mainly used in all
        #print(f"r: {result}")

        saveResult = Result()
        for method in result:
            saveResult.results = result[method]
            saveResult.saveID(str(cycles) + ":" + str(x))
            saveResult.updateMLSaved(ML_Range)
            saveResult.csvSave()
        print(f"Program took: {timer.exit()}")
        print(f"Finished at: {timer.current()}")

        refreshMLStorage.refresh()