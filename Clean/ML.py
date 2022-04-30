from Machine_Learning import ML_Save

class ML:
    def __init__(self, grid):
        self._grid = grid
        self.attempts = 1


    def start(self):
        ml = ML_Save.ML_Accessor()
        ml.changeFile("Without_Training/ML_250000")

        if ml.load(self._grid):
            #print(self._grid)
            #print(ml.getSolution())
            return True
        else:
            return False