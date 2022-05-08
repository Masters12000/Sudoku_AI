from multiprocessing import Process
import os, logging, backtracking, ML_Save
from dokusan import generators
from Libraries.container import container
from Libraries.LoadBar import Load_Bar
import time
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

def test(a,b,c):
    logging.debug(f"Start: {b}")
    time.sleep(3)
    logging.debug(f"Ending: {b}")

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def threadedFunction(cycles, threadName, lB):
    logging.info(f"Starting: {threadName}")
    solved, fails = 0, 0
    for c in range(1, cycles + 1):
        lB.updateLoadBar(c, threadName)
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
                # ai.printing()
                ml.save(btGrid)

    logging.debug(f"{threadName}: Solved - {solved}, Failed - {fails}")
    logging.critical(f"{threadName}: shutting down!!")

if __name__ == '__main__':
    cycles = 20000
    NoRunning = 10
    print("Predicted number created: ", cycles * NoRunning)
    proc = []
    lB = Load_Bar(cycles, 5)
    info('main line')
    for t in range(1, NoRunning+1):
        p = Process(target=threadedFunction, args=(cycles, 'Proc-' + str(t), lB, ))
        p.start()
        proc.append(p)