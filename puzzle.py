import re
import numpy    # Help to handle array


class pazzle:
    def __init__(self, customMatrix):
        self.matrix = customMatrix
        self.path = []
        
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
            child.append(pazzle(swap(x, y, x+1, y)))
        if x-1 >= 0:
            child.append(pazzle(swap(x, y, x-1, y)))
        if y+1 < len(self.matrix[x]):
            child.append(pazzle(swap(x, y, x, y+1)))
        if y-1 >= 0:
            child.append(pazzle(swap(x, y, x, y-1)))

        return child
    
    # Check if the current matrix is the same as goal
    def checkGoalState(self, goal):
        if numpy.array_equal(self.matrix, goal):
            return True
        else:
            return False

    # Get matrix
    def getMatrix(self):
        return self.matrix

    # TODO Get path from start to now
    def getPath():
        pass

def uniformCostSearch(start, goal):
    
    # Check if the start and goal are the same
    if start.checkGoalState(goal):
        return start
    
    # Create a queue to store all the possible path
    queue = []
    queue.append(start)
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:
            # Check if the child is the same as goal
            if c.checkGoalState(goal):
                return c
            else:
                # Add the child to the queue
                queue.append(c)


goal=numpy.array(
         [[1,2,3],
         [4,5,6],
         [7,8,0]])

puzzle1=numpy.array(
         [[1,2,3],
         [4,5,6],
         [7,8,0]])

puzzle2=numpy.array(
         [[1,2,3],
         [4,0,6],
         [7,5,8]])

puzzle3=numpy.array(
         [[4,0,1],
         [2,6,3],
         [7,5,8]])

p1 = pazzle(puzzle3)
p1.printMatrix()
child = p1.getChild()

print()

# for c in child:
#     for r in c:
#         print(r)
#     print()


print(uniformCostSearch(p1, goal).getMatrix())