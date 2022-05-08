from Libraries.container import container
from Machine_Learning.ML_Save import ML_Accessor
import backtracking, CrossHatching_Random

class ML_Trainer:
    def __init__(self, grid):
        self._grid = grid
        self.attempts = 1


    def start(self):
        ml = ML_Accessor()
        #ml.changeFile("With_Training/ML_10000")

        if ml.load(self._grid):
            #print("Found a Solution")
            #print(ml.getSolution())
            return True

        else:
            ai = backtracking.backtrackingAI(self._grid)
            if (ai.solveSudoku(0, 0)):
                btGrid = ai.getGrid()
                ml.save(btGrid)
            else:
                cH = CrossHatching_Random.CrossHatchingR(self._grid)
                if (cH.start()):
                    # printGrid(ai.getGrid())
                    ml.save(cH.getGrid())
            return False