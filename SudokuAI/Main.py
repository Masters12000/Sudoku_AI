from Libraries.container import container
from Libraries.Timer import Timer
from Libraries.CPUThreaded import CPUThreaded
import logging
from threading import Thread
# Imports of AI
import backtracking, CrossHatching_Random
from Results.Result import Result

from dokusan import generators

max_size = 9  # Must be a multiple of 3

choices = {
    1: "Backtracking",
    2: "CrossHatching-Random",
    3: "Machine Learning without Training",
    4: "Machine Learning with Training",
    5: "All"
}

choiceList = list(choices.keys())

print("Available Solvers:")
for key, value in choices.items():
    print(f"{key} - {value}")
choice = int(input(""))
choice = 1

#cycles = int(input("How many cycles? "))
cycles = 5

results = {}

timer = Timer()

c = CPUThreaded()
interval = 1
cpuT = Thread(target=c.run, args=(interval,))
cpuT.start()

for i in range(cycles):
    #Creating the Sudoku
    grid = [[0 for x in range(max_size)] for y in range(max_size)]
    cont = container(9)

    arr = generators.random_sudoku(avg_rank=150)
    cont.stringInput(arr)

    grid = cont.getGrid()

    if choice >= min(choiceList) and choice <= max(choiceList):
        if choice == 1:
            #Backtracking
            method = choices[1]
            if method in results.keys():
                r = results[method]
            else:
                results[method] = Result()
                r = results[method]

            ai = backtracking.backtrackingAI(grid)
            if (ai.start(0, 0)):
                btGrid = ai.getGrid()

                #ai.printing()
                r.success = 1
            else:
                r.fails = 1
            r.method = method
            r.cycles = cycles
            r.attemptsTaken = 1
            r.timeSpent = timer.lap()
            r.frequency = c.getLatestFrequency()
            r.percentage = c.getLatestPercent()

        elif choice == 2:
            #CrossHatching_Random
            ai = CrossHatching_Random.CrossHatchingR(grid)

            if (ai.start()):
                print("Success")

            else:
                print("Failed to Solve")

        elif choice == 3:
            # Machine Learning without Training
            print("")

        elif choice == 4:
            # Machine Learning with Training
            print("")

        elif choice == 5:
            # All
            print("")

        # Save Results
    else:
        logging.critical("Invalid Input")
        i = cycles

c.terminate() # Ends the CPU Thread
timer.exit() # Ending of Timer class

print(f"Frequency: {c.getAverageFrequency()}Mhz") #Only updates in real time on Linux, no solution for windows or mac

print(f"Percentage: {c.getAveragePercent()}%")

print(results["Backtracking"].timeSpent)