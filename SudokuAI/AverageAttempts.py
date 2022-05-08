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
attempts = {}
print("Welcome to the Cross-Hatching Average Attempt Reader")
cycles = int(input("How many cycles? "))
#cycles = 1000
cycleList = [cycles]
print(f"Started at: {Timer().current()}")
for cycles in cycleList:
    for x in range(1, 2):
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

            results.append(aICaller("CrossHatching-Random", grid))
            lB.updateLoadBar(i, "CrossHatching-Random")
        lB.updateLoadBar(cycles, "CrossHatching-Random")

        #Ending Threaded Functions
        c.terminate()
        ram.end()

        rdp = ram.differencePercent()
        rdb = ram.differenceUsed()
        results[-1].ramPercent = rdp
        results[-1].ramBytes = rdb

        print(f"Program took: {timer.exit()}")
        print(f"Finished at: {timer.current()}")

        for r in results:
            if r.attemptsTaken not in attempts.keys():
                attempts[r.attemptsTaken] = 1
            else:
                attempts[r.attemptsTaken] += 1
        attempts = dict(sorted(attempts.items()))
        print(attempts)

