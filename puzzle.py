
class pazzle:
    def __init__(self, customMatrix):
        self.matrix = customMatrix
        
    def printMatrix(self):
        for row in self.matrix:
            print(row)
            
            
puzzle1=[[1,2,3],[4,5,6],[7,8,0]]
p1 = pazzle(puzzle1)
p1.printMatrix()