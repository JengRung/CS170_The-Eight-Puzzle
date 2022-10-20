import numpy    # Help to handle array


class pazzle:
    def __init__(self, customMatrix):
        self.matrix = customMatrix
        
    def printMatrix(self):
        for row in self.matrix:
            print(row)
            
    # Return an array of all the possible child from the current matrix
    def getChild(self):
        
        # Set x and y for 0's position
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    x, y = i, j
                    break

        # Swap 2 number then return a new matrix
        def swap(x1,y1,x2,y2):
            temp = self.matrix.copy()
            temp[x1][y1], temp[x2][y2] = temp[x2][y2], temp[x1][y1]
            return temp
        
        # Check all 4 childs and add to the array if psosible
        child = []
        if x+1 < len(self.matrix):
            child.append(swap(x, y, x+1, y))
        if x-1 >= 0:
            child.append(swap(x, y, x-1, y))
        if y+1 < len(self.matrix[x]):
            child.append(swap(x, y, x, y+1))
        if y-1 >= 0:
            child.append(swap(x, y, x, y-1))

        return child

    
    def get0(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    return [i,j]
            
            
puzzle1=numpy.array(
         [[1,2,3],
         [4,5,6],
         [7,8,0]])

puzzle2=numpy.array(
         [[1,2,3],
         [4,0,6],
         [7,5,8]])

p1 = pazzle(puzzle2)
p1.printMatrix()
child = p1.getChild()

print()

for c in child:
    for r in c:
        print(r)
    print()
