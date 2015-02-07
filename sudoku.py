#sudoku.py
#Sudoku class

from random import*

class Sudoku:

    """This class creates the prime table"""
    def __init__(self):
        self.seed=[[1,2,3,9,5,6,8,7,4],[7,4,8,2,1,3,6,5,9],[6,5,9,8,7,4,3,1,2],
                   [8,1,6,4,2,5,9,3,7],[9,7,4,3,8,1,5,2,6],[5,3,2,6,9,7,1,4,8],
                   [4,9,1,7,3,8,2,6,5],[3,8,7,5,6,2,4,9,1],[2,6,5,1,4,9,7,8,3]]
        self.problem=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        self.randomlist=self.__randomArray()

    "This function creates a random list containing 1~9"
    def __randomArray(self):
        randlist=[0,0,0,0,0,0,0,0,0]
        for i in range(9):
            flag=1
            while flag:
                flag=0
                randlist[i]=randrange(1,10)
                for j in range(i):
                    if randlist[j]==randlist[i]:
                        flag=1
        return randlist

    "This function creates a random sudoku table"
    def CreateSudoku(self):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if self.seed[i][j]==self.randomlist[k]:
                        self.seed[i][j]=self.randomlist[(k+1)%9]
                        break
        return self.seed

    "This function creates a sudoku problem table"
    def getblanks(self,level):
        for i in range(9):
            for j in range(9):
                if random()<float(level+6)/24:
                    self.problem[i][j]=0
                else :
                    self.problem[i][j]=self.seed[i][j]
        return self.problem




                        
        

