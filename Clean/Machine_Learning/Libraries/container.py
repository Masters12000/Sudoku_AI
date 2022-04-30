
class container:
    def __init__(self, max_size):
        self._string = ""
        self._grid = [[0 for x in range(max_size)] for y in range(max_size)]

    #private methods
    def __stringToGrid(self):
        counter = 0
        row = 0
        arr = self._string
        for i in range(len(arr)-1):
            if counter == 9:
                row+=1
                counter = 0
            self._grid[row][counter] = int(arr[i])
            counter+=1

    #public methods
    #Inputs
    def stringInput(self, value):
        self._string = str(value)
        self.__stringToGrid()
        return True

    def Grid(self, val):
        self._grid = val

    #Outputs
    def getGrid(self):
        return self._grid

    def getGridS(self):
        return self._string

    def printGridBasic(self):
        for r in self._grid:
            print(r)
        return 0

    def printGrid(self): #Automatically scales to the size of the grid, while keeping 3 by 3 chunks
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
        counter = 0
        for r in range(len(self._grid)):
            for c in range(len(self._grid)):
                if self._grid[r][c] == "0":
                    counter += 1
        return counter
