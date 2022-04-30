from Libraries.container import container

class AIbasic:
    def __init__(self):
        self._soduku = []
        self._size = 9
        self._notes = [[0 for x in range(self._size)]for y in range(self._size)]
        self._priority = [[0 for x in range(self._size)]for y in range(self._size)]

    def getColumn(self, grid, y):
        """
        get the column from the current grid (2d array)
        @param grid: 2d array
        @param y: column index
        @return: array - column
        """
        rtrn = [ ]
        for i in range(self._size):
            rtrn.append(grid[i][y])
        return rtrn

    def getSegment(self, grid, row, col):
        """
        returns the segments
        @param grid: 2d array
        @param row: row index
        @param col: column index
        @return: array - segment
        """
        arr = [ ]
        segment = [ ]
        segmentPos = []
        for s in range(1,self._size, 3):
            segmentPos.append(s)

        if row not in segmentPos:
            temp = (row % 3) - 1
            if temp == -1:
                row += 1
            if temp == 1:
                row -= 1
        if col not in segmentPos:
            temp = (col % 3) - 1
            if temp == -1:
                col += 1
            if temp == 1:
                col -= 1

        for x in range(-1, 2, 1):
            if (x == -1 and row == 0):
                arr.append(0)
            else:
                for y in range(-1, 2, 1):
                    if (y == -1 and col == 0):
                        arr.append(0)
                    else:
                        arr.append(grid[row + x][col + y])

        for i in range(self._size):
            if arr[i] != '0':
                segment.append(arr[i])
        return segment

    def printGrid(self, size, grid):
        """
        Working link to container class, merging all of the print requirements into one function, suitable for testing and debugging.
        @param size: sudoku grid size
        @param grid: sudoku grid
        @return: None
        """
        con = container(size)
        con.Grid(grid)
        con.printGrid()

    def printGridBasic(self, grid):
        """
        print the grid in its raw array format, useful for testing new algorithms
        @param grid: sudoku grid
        @return: None
        """
        con = container(9)
        con.Grid(grid)
        con.printGridBasic()

