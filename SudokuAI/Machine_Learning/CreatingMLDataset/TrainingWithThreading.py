from Libraries.container import container
import ML_Save, backtracking
from dokusan import generators
from threading import Thread
from Libraries.Timer import Timer

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
cycles = 10
noOfThreads = 10
timer = Timer()
logging.info(f"Program Started at: {timer.current()}")


def threadedFunction(cycles, threadName):
    logging.info(f"Starting: {threadName}")
    solved, fails = 0, 0
    for c in range(1, cycles + 1):
        if c == cycles / 2:
            logging.info(f"{threadName} is half way there.")
        arr = generators.random_sudoku(avg_rank=150)
        cont = container(9)
        cont.stringInput(arr)

        grid = cont.getGrid()

        ml = ML_Save.ML_Accessor()

        if ml.load(grid):
            logging.debug(f"{threadName} :: Found a Solution - {ml.getSolution()}")
            solved += 1

        else:
            ai = backtracking.backtrackingAI(grid)
            fails += 1
            if (ai.solveSudoku(0, 0)):
                btGrid = ai.getGrid()
                ml.save(btGrid)

    logging.debug(f"{threadName}: Solved - {solved}, Failed - {fails}")
    logging.critical(f"{threadName}: shutting down!!")


threads = [ ]

for i in range(1, noOfThreads + 1):
    t = Thread(target=threadedFunction, args=(cycles, "Thread->" + str(i)))
    t.start()
    threads.append(t)
