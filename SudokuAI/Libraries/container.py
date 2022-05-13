
class container:
    def __init__(self, max_size):
        self._string = ""
        self._grid = [[0 for x in range(max_size)] for y in range(max_size)]
        self._size = max_size

    #private methods
    def __stringToGrid(self):
        """
        Convert string from dokusan into a 2d array
        @return: None
        """
        counter = 0
        row = 0
        arr = self._string
        for i in range(len(arr)-1):
            if counter == 9:
                row += 1
                counter = 0
            self._grid[row][counter] = int(arr[i])
            counter += 1

    #public methods
    #Inputs
    def stringInput(self, value):
        """
        String Input
        @param value: string sudoku
        @return: Bool - True: Updated container
        """
        self._string = str(value)
        self.__stringToGrid()
        return True

    def Grid(self, val):
        """
        Update container with a 2d array
        @param val: 2d array - Sudoku
        @return: None
        """
        self._grid = val

    #Outputs
    def getGrid(self):
        """
        Return the sudoku grid
        @return: 2d array - sudoku grid
        """
        return self._grid

    def getGridS(self):
        """
        Return the sudoku grid
        @return: string - sudoku grid
        """
        return self._string

    def printGridBasic(self):
        """
        Print raw grid in rows
        @return: None
        """
        for r in self._grid:
            print(r)

    def printGrid(self): #Automatically scales to the size of the grid, while keeping 3 by 3 chunks
        """
        Print the grid in an easy-to-read format, scalable by 3
        @return: None
        """
        size = int(len(self._grid)/3)
        row = ""

        #Top Row
        row += "|"
        for x in range((len(self._grid)*3)+(size-1)):
            row += "-"
        row += "|"
        print(row)
        row = ""
        #Middle Rows
        for r in range(len(self._grid)):
            row += "|"
            if (r+1) % 3 == 1 and r >= 3:
                print("|" + (("-" * 9) + "+") * (size-1) + ("-" * 9) + "|")

            for c in range(len(self._grid[r])):
                if (c+1) % 3 == 1 and c >= 3:
                    row += "|"
                row += (" " + str(self._grid[r][c]) + " ")
            row += "|"
            print(row)
            row = ""
        #Bottom Row
        row += "|"
        for x in range((len(self._grid) * 3) + (size - 1)):
            row += "-"
        row += "|"
        print(row)
        row = ""
        
    def emptySpaces(self):
        """
        return number of empty spaces
        @return: int - empty spaces
        """
        counter = 0
        for r in range(len(self._grid)):
            for c in range(len(self._grid)):
                if self._grid[r][c] == "0":
                    counter += 1
        return counter

    def copyGrid(self, grid):
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