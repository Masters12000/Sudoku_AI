from Libraries.container import container
from Machine_Learning.ML_Save import ML_Accessor
import backtracking, CrossHatching_Random

class ML_Trainer:
    def __init__(self, grid):
        self._grid = grid
        self.attempts = 1


    def start(self):
        ml = ML_Accessor()
        ml.changeFile("With_Training/ML_1000000")

        if ml.load(self._grid):
            return True

        else:
            ai = backtracking.backtrackingAI(self._grid)
            if (ai.solveSudoku(0, 0)):
                btGrid = ai.getGrid()
                ml.save(btGrid)
            else:
                cH = CrossHatching_Random.CrossHatchingR(self._grid)
                if (cH.start()):
                    ml.save(cH.getGrid())
            return False