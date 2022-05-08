from Libraries.container import container
from Libraries.LoadBar import Load_Bar
import ML_Save, backtracking
from dokusan import generators
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

cycles = 100
name = "Trainer"
lB = Load_Bar(cycles, 1)

solved, fails = 0, 0
for c in range(1, cycles + 1):
    lB.updateLoadBar(c, name)

    arr = generators.random_sudoku(avg_rank=150)
    cont = container(9)
    cont.stringInput(arr)

    grid = cont.getGrid()

    ml = ML_Save.ML_Accessor()

    if ml.load(grid):
        logging.debug(f"{name} :: Found a Solution - {ml.getSolution()}")
        solved += 1

    else:
        ai = backtracking.backtrackingAI(grid)
        fails += 1
        if (ai.solveSudoku(0, 0)):
            btGrid = ai.getGrid()
            ml.save(btGrid)

logging.debug(f"{name}: Solved - {solved}, Failed - {fails}")
logging.critical(f"{name}: shutting down!!")
