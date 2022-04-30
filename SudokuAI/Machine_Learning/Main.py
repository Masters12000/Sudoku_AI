from Libraries.AIclass import AIbasic
from Libraries.container import container
import ML_Save, backtracking, CrossHatching_Random
from dokusan import generators

"""
Issues with ML:
- Sudoku has 6,670,903,752,021,072,936,960 possible Solutions
- With the current storage system, you need 402896787.17 Petabytes to store every solution
- More solutions increase the number of values that need to be checked, even with an efficient design
- Time Taken to Learn sufficient values for a successful result (at point of writing has 6500 solutions)
"""

solved = 0
fails = 0
cycles = 5000
cont = container(9)
loading_bar = [0]

def createLoadBar(gap = 5, cycles = 1000):
    """
    Input: Percentage Gap between updates
    """
    incriments = cycles * (gap/100)
    temp = incriments
    while temp <= cycles:
        loading_bar.append(temp)
        temp += incriments
    #print(incriments, loading_bar)

def printLoadBar(currentCycle = 0):
    #print(currentCycle)
    for i in range(len(loading_bar)):
        if currentCycle == loading_bar[i]:
            percentage = (currentCycle / cycles) * 100
            print(f"Loading: {percentage}%")
            if percentage == 100:
                print("Completed")
createLoadBar(5, cycles)

for i in range(cycles):
        printLoadBar(i+1)
        arr = generators.random_sudoku(avg_rank=150)
        cont = container(9)
        cont.stringInput(arr)
        if False:
                arr = [
                        [9, 7, 8, 0, 0, 6, 0, 0, 0],
                        [5, 0, 0, 0, 8, 4, 0, 3, 0],
                        [0, 3, 0, 0, 0, 7, 0, 2, 6],
                        [0, 0, 0, 0, 0, 8, 0, 0, 5],
                        [8, 0, 4, 6, 0, 0, 2, 1, 0],
                        [6, 5, 0, 0, 0, 0, 4, 0, 0],
                        [2, 0, 0, 0, 6, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 6, 0],
                        [0, 0, 0, 5, 0, 3, 0, 0, 0]]
                cont.Grid(arr)

        if False:
            testing = "6789023192308546415307891324980789457612567013982816340535972064"
            cont.stringInput(testing)


        grid = cont.getGrid()

        ml = ML_Save.ML_Accessor()
        #grid = "6700000000000000000000001324980789407602567213902016347505970164"
        #ml.test(grid)

        if ml.load(grid):
            print("Found a Solution")
            print(ml.getSolution())
            solved += 1

        else:
            ai = backtracking.backtrackingAI(grid)
            fails += 1
            if (ai.solveSuduko(0, 0)):
                btGrid = ai.getGrid()
                #ai.printing()
                ml.save(btGrid)

            else:
                #fails += 1
                cH = CrossHatching_Random.CrossHatchingR(grid)
                if (cH.start()):
                    #printGrid(ai.getGrid())
                    ml.save(cH.getGrid())

                #print("no solution exists ")
print(solved, fails)#, f"Success Rate: {solved/fails * 100}")