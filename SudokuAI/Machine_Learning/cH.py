from Libraries.AIclass import AIbasic
import random, logging

# This class contains Logging, allowing for a dubug mode
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

"""
Testing:
Running Cross-Hatching without a priority System
Instead selecting at random a empty cell, selecting at random one of its available values.
Currently has yielded no successful solutions
"""

class CrossHatchingR:
    def __init__(self, grid):
        self._size = 9
        self._sudoku = grid
        self._original = self.__copyGrid(grid)
        self._spacesIndex = []
        self._priorityCell = []
        self._notes = [[0 for i in range(9)] for y in range(9)]
        self.attempts = 1
        self._state = None


        self._AIBasic = AIbasic()
        self.CalculateSpacesIndex()

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

    def CalculateSpacesIndex(self):
        self._spacesIndex = []
        for x in range(self._size):
            for y in range(self._size):
                if self._sudoku[x][y] == 0:
                    self._spacesIndex.append([x,y])
        return self._spacesIndex

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

    def loadPriority(self):
        """
        Loads the cells and predicts the next cell to edit
        @return: cell to edit
        """
        self.loadAllNotes()
        if len(self._spacesIndex) == 0:
            #print("Reached spaces limit")
            return False
        self._priorityCell = self._spacesIndex.pop(random.randint(0, len(self._spacesIndex)-1))

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
        self.CalculateSpacesIndex()
        while con and self._state != "Success":
            #basic.printGrid(9, self._sudoku)
            priorityCell = self.loadPriority()
            #print(priorityCell)
            if priorityCell != False:
                if self.attempts >= 250:
                    #print("Error 100 - Too many Cycles")
                    #exit()
                    return False

                elif priorityCell == []:
                    self._state = "Success"
                    con = False
                    return True

                elif not self.single():
                    row = priorityCell[0]
                    col = priorityCell[1]
                    logging.debug(f"Available Values: {self.availableValues(row, col)}")
            else:
                return False
        return True

    def getGrid(self):
        """
        return Grid
        @return: 2D array - Sudoku Grid
        """
        return self._sudoku

from Libraries.container import container

arr = [
    [9, 7, 8, 0, 0, 6, 0, 0, 0],
    [5, 0, 0, 0, 8, 4, 0, 3, 0],
    [0, 3, 0, 0, 0, 7, 0, 2, 6],
    [0, 0, 0, 0, 0, 8, 0, 0, 5],
    [8, 0, 4, 6, 0, 0, 2, 1, 0],
    [6, 5, 0, 0, 0, 0, 4, 0, 0],
    [2, 0, 0, 0, 6, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 5, 0, 3, 0, 0, 0]
]
AIbasic().printGrid(9, arr)

cont = container(9)
cont.Grid(arr)
success = 0
fails = 0

cross = CrossHatchingR(cont.getGrid())
print(len(cross.CalculateSpacesIndex()))
while success == 0 or fails > 1000:
    cross = CrossHatchingR(cont.getGrid())
    cross.CalculateSpacesIndex()
    if cross.start():
        success += 1
        grid = cross.getGrid()
        #print(grid)
        AIbasic().printGrid(9, grid)
    else:
        fails += 1
        #print("Failed")
        grid = cross.getGrid()
        #print(grid)
        #AIbasic().printGrid(9, grid)
        """if grid == arr:
            print("No Change")
        else:
            print("Change")
            #AIbasic().printGrid(9, arr)
            temp = []
            for r in range(9):
                for c in range(9):
                    if arr[r][c] != grid[r][c]:
                        temp.append([r, c, grid[r][c]])
            print(len(temp), temp)
            print(len(cross.CalculateSpacesIndex()))"""

print(f"Successes: {success} / {fails}")
