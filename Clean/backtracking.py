from Libraries.AIclass import AIbasic

class backtrackingAI:
    def __init__(self, grid):
        self._sudoku = grid
        self._size = len(grid[0])
        self._notes = [[0 for x in range(9)]for y in range(9)]
        self._aiBasic = AIbasic()
        self.attempts = 1

    def start(self):
        """
        Public Accessor for the AI, labelled start to match other AI algorithms when called
        returns: sudoku solution generated
        """
        return self.__AI(0, 0)

    def __AI(self, row, col):
        """
        Recursive AI, loops through the row and column, checking and setting value in next available cell
        """
        if col == self._size and row == self._size-1:
            return True

        if col == self._size:
            row += 1
            col = 0

        if self._sudoku[row][col] > 0:
            return self.__AI(row, col+1)

        for value in range(1, self._size+1):
            if self.__valid(row, col, value):
                self._sudoku[row][col] = value

                if self.__AI(row, col+1):
                    return True

        self._sudoku[row][col] = 0

    def __valid(self, row, col, value):
        """
        Check if the value appears in the row, column or segment
        if value appears then returns False else True
        """

        if value in self._sudoku[row]:
            return False

        if value in self._aiBasic.getColumn(self._sudoku, col):
            return False

        if value in self._aiBasic.getSegment(self._sudoku, row, col):
            return False

        return True

    def solveSudoku(self, row, col):
        """
        Accessor for Machine Learning
        @param row: row Index (0)
        @param col: col Index (0)
        @return: solved solution
        """
        return self.__AI(row, col)

    def getGrid(self):
        """
        returns the Grid, used in ML
        @return: solved sudoku
        """
        return self._sudoku
