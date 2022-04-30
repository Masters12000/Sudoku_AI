from Libraries.AIclass import AIbasic
import random, logging

# This class contains Logging, allowing for a dubug mode
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

class CrossHatchingR:
    def __init__(self, grid):
        self._size = 9
        self._sudoku = grid
        self._original = self.__copyGrid(grid)
        self._priorityCell = []
        self._notes = [[0 for i in range(9)] for y in range(9)]
        self.attempts = 1
        self._state = None


        self._AIBasic = AIbasic()

    def __copyGrid(self, grid):
        """
        Copy the grid, avoiding pointer collisions
        Used in:
        :param grid: grid to copy
        :return: copied grid
        """
        rtrn = [[0 for x in range(self._size)] for y in range(self._size)]

        for row in range(0, self._size):
            for col in range(0, self._size):
                rtrn[ row ][ col ] = grid[ row ][ col ]

        return rtrn

    def availableValues(self, rowIndex, colIndex):
        """
        calculates the values not yet in the row, column or segment
        :param rowIndex: row index to check
        :param colIndex: column index to check
        :return: list of integers
        """
        available = []
        row = self._sudoku[rowIndex]
        col = self._AIBasic.getColumn(self._sudoku, colIndex)
        segment = self._AIBasic.getSegment(self._sudoku, rowIndex, colIndex)

        for a in range(1, self._size+1):
            available.append(a)

        for r in row:
            if r in available:
                available.remove(r)

        for c in col:
            if c in available:
                available.remove(c)

        for s in segment:
            if s in available:
                available.remove(s)

        return available


    def loadAllNotes(self):
        """
        Loop through the cells, saving the available values in each cell to notes
        """
        for colIndex in range(self._size):
            for rowIndex in range(self._size):
                self._notes[rowIndex][colIndex] = self.availableValues(rowIndex, colIndex)

    def save(self, rowIndex, colIndex, value):
        """
        Saves the value into the row/col cell if it is valid
        :param rowIndex: row index to check
        :param colIndex: column index to check
        :param value: value to enter into the cell
        :return: None
        """
        if self.isValid(rowIndex, colIndex, value):
            self._sudoku[rowIndex][colIndex] = value
            self.loadAllNotes()

        else:
            row = self._sudoku[ rowIndex ]
            col = self._AIBasic.getColumn(self._sudoku, colIndex)
            segment = self._AIBasic.getSegment(self._sudoku, rowIndex, colIndex)
            logging.debug(f"Row: {row}\nCol:{col}\nSegment:{segment}")

    def isValid(self, rowIndex, colIndex, value):
        """
        checks if the value is in the row, column or segment
        @param rowIndex: row index to check
        @param colIndex: col index to check
        @param value: value to check
        @return: Bool True if valid else False if its already appears
        """
        row = self._sudoku[rowIndex]
        col = self._AIBasic.getColumn(self._sudoku, colIndex)
        segment = self._AIBasic.getSegment(self._sudoku, rowIndex, colIndex)

        if value in row:
            return False
        if value in col:
            return False
        if value in segment:
            return False
        return True

    def __getSpacesUsed(self, arr):
        """
        Number of spaces used within the sudoku grid so far
        @param arr: sudoku grid
        @return: int - number of spaces
        """
        spaces = 0
        for a in arr:
            if a != 0:
                spaces += 1
        return spaces

    def __priorityCalculation(self, rowIndex, colIndex):#
        """
        Calculates the next best cell to edit
        @param rowIndex: row to check
        @param colIndex: col to check
        @return: float - priority calculated
        """
        rowUsed = self.__getSpacesUsed(self._sudoku[rowIndex])
        colUsed = self.__getSpacesUsed(self._AIBasic.getColumn(self._sudoku, colIndex))

        spaces = ((self._size * 2) - 1)
        calc = spaces / (spaces - rowUsed - colUsed) - 1
        if type(self._notes[rowIndex][colIndex]) == int:
            calc += self._size - 1
            self._notes[rowIndex][colIndex] = [self._notes[rowIndex][colIndex]]
        else:
            calc += self._size - len(self._notes[rowIndex][colIndex])
        return calc

    def __highest(self, rowIndex, colIndex):
        """
        Searches for the highest priority in the provided grid
        returning the cells that can be changed as they all have the highest priority
        @param rowIndex: row to check
        @param colIndex: column to check
        @return: None
        """
        priorityCellRow = self._priorityCell[0]
        priorityCellColumn = self._priorityCell[1]

        if self.__priorityCalculation(rowIndex, colIndex) > self.__priorityCalculation(priorityCellRow, priorityCellColumn):
            self._priorityCell = [rowIndex, colIndex]

    def loadPriority(self):
        """
        Loads the cells and predicts the next cell to edit
        @return: cell to edit
        """
        self.loadAllNotes()
        self._priorityCell = []

        for colIndex in range(self._size):
            for rowIndex in range(self._size):
                if self._sudoku[rowIndex][colIndex] == 0:
                    if colIndex == 5 and rowIndex == 4 and self._notes[4][1] == 9:
                        logging.debug(rowIndex, colIndex)
                        logging.debug("Notes: ", self._notes[rowIndex][colIndex])
                        logging.debug("Sudoku:", self._sudoku[rowIndex][colIndex])
                        #breakpoint()
                    if self._priorityCell == []:
                        self._priorityCell = [rowIndex, colIndex]
                    else:
                        self.__highest(rowIndex, colIndex)
        logging.debug(f"Priority: {self._priorityCell}") # Notes:{self._notes[self._priorityCell[0]][self._priorityCell[1]]}")
        return self._priorityCell

    def single(self):
        prow = self._priorityCell[0]
        pcol = self._priorityCell[1]
        value = self._notes[prow][pcol]
        logging.debug(f"row: {prow}, col: {pcol}, value: {value}")
        if len(value) == 1:
            self.save(prow, pcol, value[0])
            return True
        elif len(value) == 0:
            logging.debug("Failed - Retrying")
            self.attempts += 1
            self._sudoku = self.__copyGrid(self._original)
            self.start()
        else:
            logging.debug(f"values: {value}")
            rand = random.randint(0, len(value)-1)
            value = value[rand]
            logging.debug(value)
            self.save(prow, pcol, value)

            return True
        return False

    def getCycles(self):
        """
        return the number of attempts
        @return: attempts
        """
        return self.attempts

    def start(self):
        """
        Main AI
        @return: Bool - True: Found a Solution, False: Passed number of attempts/fails
        """
        con = True
        while con and self._state != "Success":
            #basic.printGrid(9, self._sudoku)
            priorityCell = self.loadPriority()
            if self.attempts >= 200:
                #Error 100 - Too many Cycles
                return False

            elif priorityCell == []:
                self._state = "Success"
                con = False
                return True

            elif not self.single():
                row = priorityCell[0]
                col = priorityCell[1]
                logging.debug(self.availableValues(row, col))

        return True

    def getGrid(self):
        """
        return Grid
        @return: 2D array - Sudoku Grid
        """
        return self._sudoku
