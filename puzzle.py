import time
import numpy    # Help to handle array

class puzzle:
    def __init__(self, customMatrix):
        self.matrix = customMatrix
        self.parent = None
        self.height = 0
        self.cost = 0
        
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
        
        # Right
        if x+1 < len(self.matrix):
            newChild = puzzle(swap(x, y, x+1, y))
            
            # Update path and cost for new child
            newChild.parent = self
            newChild.height = self.height + 1
            
            child.append(newChild)
            
        # Left
        if x-1 >= 0:
            newChild = puzzle(swap(x, y, x-1, y))
            
            # Update path and cost for new child
            newChild.parent = self
            newChild.height = self.height + 1
            
            child.append(newChild)
           
        # Down 
        if y+1 < len(self.matrix[x]):
            newChild = puzzle(swap(x, y, x, y+1))
            
            # Update path and cost for new child
            newChild.parent = self
            newChild.height = self.height + 1
            
            child.append(newChild)
            
        # Up
        if y-1 >= 0:
            newChild = puzzle(swap(x, y, x, y-1))
            
            # Update path and cost for new child
            newChild.parent = self
            newChild.height = self.height + 1
            
            child.append(newChild)

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


def uniform_cost_search(start, goal):
    
    # Check if the start and goal are the same
    if start.checkGoalState(goal):
        return start
    
    # Create a queue to store all the possible path
    queue = []
    queue.append(start)
    
    # An array to keep track of all the visited matrix
    seen = []
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        
        # dynamic print the seen list size
        print("Seen: " + str(len(seen)) + " Queue: " + str(len(queue)), end="\r")

        # Add current to seen, convert numpy array to list to be able to compare
        seen.append(current.getMatrix().tolist())
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:
            # Check if the child is the same as goal
            if c.checkGoalState(goal):
                return c
        
            # If child not in seen, Add the child to the queue
            if c.getMatrix().tolist() not in seen:
                queue.append(c)

# Helper function to calculate the misplaced tiles
def misplaced_tiles(matrix, goal):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != goal[i][j]:
                count += 1
    return count

def a_star_with_misplaced_tiles(start, goal):
    
    # Check if the start and goal are the same
    if start.checkGoalState(goal):
        return start
    
    # Create a queue to store all the possible path
    queue = []
    queue.append(start)
    
    # An array to keep track of all the visited matrix
    seen = []
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        
        # dynamic print the seen list size
        print("Seen: " + str(len(seen)) + " Queue: " + str(len(queue)), end="\r")

        # Add current to seen, convert numpy array to list to be able to compare
        seen.append(current.getMatrix().tolist())
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:
            # Check if the child is the same as goal
            if c.checkGoalState(goal):
                return c
        
            # If child not in seen, Add the child to the queue with the cost
            if c.getMatrix().tolist() not in seen:
                # Calculate the cost of the child base on misplaced tiles
                c.cost = misplaced_tiles(c.getMatrix(), goal)
                queue.append(c)
                
        # Sort the queue by cost
        queue = sorted(queue, key=lambda x: x.cost, reverse=False)
    


# Goal state            
goal=numpy.array(
         [[1,2,3],
         [4,5,6],
         [7,8,0]])

# Depth 0
puzzle0=numpy.array(
         [[1,2,3],
         [4,5,6],
         [7,8,0]])

# Depth 2
puzzle2=numpy.array(
         [[1,2,3],
         [4,5,6],
         [0,7,8]])

# Depth 4
puzzle3=numpy.array(
         [[1,2,3],
         [5,0,6],
         [4,7,8]])


# Depth 8
puzzle8=numpy.array(
         [[1,3,6],
         [5,0,2],
         [4,7,8]])

# Depth 16
puzzle16=numpy.array(
         [[1,6,7],
         [5,0,3],
         [4,8,2]])

# Depth 20
puzzle20=numpy.array(
         [[7,1,2],
         [4,8,5],
         [6,3,0]])

# Depth 24
puzzle24=numpy.array(
         [[0,7,2],
         [4,6,1],
         [3,5,8]])

# Depth x
puzzleX=numpy.array(
         [[4,1,2],
         [5,3,0],
         [7,8,6]])

p1 = puzzle(puzzle24)
p1.printMatrix()
print()

# # Tester for uniform cost search
# start = time.time()
# final = uniform_cost_search(p1, goal)
# end = time.time()
# print(f"Finish! Taking {end - start} seconds \n \n")

# print(f"COST: {final.height}")

# path = []
# while(final.parent != None):
#     path.append((final.getMatrix(), final.height))
#     final = final.parent

# path.reverse()
# for p in path:
#     print(f"Matrix: \n {p[0]} \nCost: {p[1]} \n")
    
    
# Tester for A* with misplaced tiles
start = time.time()
final = a_star_with_misplaced_tiles(p1, goal)
end = time.time()
print(f"Finish! Taking {end - start} seconds \n \n")

print(f"COST: {final.cost}")

path = []
while(final.parent != None):
    path.append((final.getMatrix(), final.cost))
    final = final.parent

path.reverse()
for p in path:
    print(f"Matrix: \n {p[0]} \nCost: {p[1]} \n")
    