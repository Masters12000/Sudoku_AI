
from Libraries.container import container

class backtrackingAI:
    def __init__(self, grid):
        # N is the size of the 2D matrix N*N
        self._N = 9
        self._sudoku = grid
        self.attempts = 1


    # return false
    # A utility function to print grid
    def printing(self):
        """
        for i in range(N):
            for j in range(N):
                print(arr[ i ][ j ], end=" ")
            print()
        """
        con = container(self._N)
        con.Grid(self._sudoku)
        con.printGrid()


    # Checks whether it will be
    # legal to assign num to the
    # given row, col
    def isSafe(self, row, col, num):
        # Check if we find the same num
        # in the similar row , we
        for x in range(9):
            if self._sudoku[ row ][ x ] == num:
                return False

        # Check if we find the same num in
        # the similar column , we
        # return false
        for x in range(9):
            if self._sudoku[ x ][ col ] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self._sudoku[ i + startRow ][ j + startCol ] == num:
                    return False
        return True


    # Takes a partially filled-in grid and attempts
    # to assign values to all unassigned locations in
    # such a way to meet the requirements for
    # Sudoku solution (non-duplication across rows,
    # columns, and boxes) */
    def solveSuduko(self, row, col):
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if (row == self._N - 1 and col == self._N):
            return True

        # Check if column value becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == self._N:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value > 0, we iterate for next column
        if self._sudoku[ row ][ col ] > 0:
            return self.solveSuduko(row, col + 1)
        for num in range(1, self._N + 1, 1):

            # Check if it is safe to place
            # the num (1-9) in the
            # given row ,col ->we
            # move to next column
            if self.isSafe(row, col, num):

                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                self._sudoku[ row ][ col ] = num

                # Checking for next possibility with next
                # column
                if self.solveSuduko(row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            self._sudoku[ row ][ col ] = 0
        return False

    def start(self):
        return self.solveSuduko(0, 0)

    def getGrid(self):
        return self._sudoku
"""

grid = [
    [ 9, 7, 8, 0, 0, 6, 0, 0, 0 ],
    [ 5, 0, 0, 0, 8, 4, 0, 3, 0 ],
    [ 0, 3, 0, 0, 0, 7, 0, 2, 6 ],
    [ 0, 0, 0, 0, 0, 8, 0, 0, 5 ],
    [ 8, 0, 4, 6, 0, 0, 2, 1, 0 ],
    [ 6, 5, 0, 0, 0, 0, 4, 0, 0 ],
    [ 2, 0, 0, 0, 6, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 6, 0 ],
    [ 0, 0, 0, 5, 0, 3, 0, 0, 0 ]
]

printing(grid)

if (solveSuduko(grid, 0, 0)):
    printing(grid)
else:
    print("no solution exists ")

# This code is contributed by sudhanshgupta2019a
# Source Code: https://www.geeksforgeeks.org/sudoku-backtracking-7/

"""