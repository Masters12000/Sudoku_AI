from Libraries.container import container

class ML_Accessor:
    def __init__(self):
        self._sudoku = []
        self._fileLocation = "Machine_Learning/ML_Storage.txt"

    def save(self, grid):
        """
        Save solution into File
        @param grid: sudoku solution
        @return: None
        """
        file = open(self._fileLocation, "a")
        strGrid = self._grid2String(grid)
        file.writelines(strGrid+"\n")
        file.close()

    def _grid2String(self, grid):
        """
        Convert from 2d array into a string
        @param grid: sudoku grid
        @return: sudoku as String
        """
        size = len(grid[0])
        rtrn = ""
        for c in range(0, size):
            for r in range(0, size):
                rtrn += str(grid[c][r])

        return rtrn

    def load(self, grid):
        """
        Load the solutions from the dataset
        @param grid: Incomplete Sudoku
        @return: Bool - True: Found in dataset, False: Not yet learnt
        """
        self._sudoku = self._grid2String(grid)
        file = open(self._fileLocation, "r")
        lines = file.readlines()
        cont = container(9)
        for line in lines:
            if self._compare(line):
                cont.stringInput(line)
                file.close()
                self._sudoku = cont.getGrid()
                return True

        file.close()
        return False

    def _compare(self, grid):
        """
        Compare the unsolved sudoku against a solved solution
        @param grid: unsolved sudoku
        @return: Bool - True: Matches, False: No Match
        """
        valid = True
        size = min(len(self._sudoku), len(grid))

        for idx in range(size):
            if self._sudoku[idx] != grid[idx] and self._sudoku[idx] != '0':
                return False

        return valid

    def getSolution(self):
        """
        return the sudoku
        @return: 2d array - sudoku grid
        """
        return self._sudoku

    def changeFile(self, filename):
        """
        Edit the File Accessed, used in generating results
        @param filename: updated filename, e.g. ML_10000
        @return: complete file address
        """
        self._fileLocation = "Machine_Learning/" + filename + ".txt"
        return self._fileLocation
