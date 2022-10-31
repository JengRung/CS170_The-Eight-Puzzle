import time
import numpy    # Help to handle array

class puzzle:
    def __init__(self, customMatrix):
        self.matrix = customMatrix
        self.parent = None
        self.height = 0
        self.cost = 0
        self.expended = 0   # Number of expended node
        
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

# Searching function: uniform_cost_search, misplaced_tiles, manhattan_distance

def uniform_cost_search(start, goal):
    
    # Check if the start and goal are the same
    if start.checkGoalState(goal):
        return start
    
    # Create a queue to store all the possible path
    queue = []
    queue.append(start)
    
    # An array to keep track of all the visited matrix
    seen = []
    
    # Count the expended node, increment 1 when a node is pop from the queue 
    expendCnt = 0
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        expendCnt += 1
        
        # Check for the goal state
        if current.checkGoalState(goal):
            return current

        # Add current to seen, convert numpy array to list to be able to compare
        seen.append(current.getMatrix().tolist())
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:
            # If child not in seen, Add the child to the queue
            if c.getMatrix().tolist() not in seen:
                # Update expend node count
                c.expended = expendCnt
                queue.append(c)

# Helper function to calculate the misplaced tiles
# Logic: Calculate the total number of misplaced tiles
def misplaced_tiles(matrix, goal):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != goal[i][j] and matrix[i][j] != 0:
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
    
    # Count the expended node, increment 1 when a node is pop from the queue 
    expendCnt = 0
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        expendCnt += 1
        
        # Check for the goal state
        if current.checkGoalState(goal):
            return current

        # Add current to seen, convert numpy array to list to be able to compare
        seen.append(current.getMatrix().tolist())
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:      
            # If child not in seen, Add the child to the queue with the cost
            if c.getMatrix().tolist() not in seen:
                # Calculate the cost of the child base on misplaced tiles
                c.cost = misplaced_tiles(c.getMatrix(), goal) + c.height
                # Update expend node count
                c.expended = expendCnt
                queue.append(c)
                
        # Sort the queue by cost
        queue = sorted(queue, key=lambda x: x.cost, reverse=False)
    
    
# Logic: Iterate through the matrix and find the number that is not in the right position, calcyulate the distance between the current position and the goal position, then add the distance to the total count
def manhattan_distance(matrix, goal):
    count = 0
    for x1 in range(len(matrix)):
        for y1 in range(len(matrix[x1])):
            # Ignore 0 in the matrix
            if matrix[x1][y1] != 0:
                # Find the position of the number in the goal
                for x2 in range(len(goal)):
                    for y2 in range(len(goal[x2])):
                        if goal[x2][y2] == matrix[x1][y1]:
                            count += abs(x1-x2) + abs(y1-y2)
    return count

    
def a_star_with_manhattan_distance(start, goal):
    
    # Check if the start and goal are the same
    if start.checkGoalState(goal):
        return start
    
    # Create a queue to store all the possible path
    queue = []
    queue.append(start)
    
    # An array to keep track of all the visited matrix
    seen = []
    
    # Count the expended node, increment 1 when a node is pop from the queue 
    expendCnt = 0
    
    # Loop until the queue is empty
    while(True):
        # Check if queue is empty, then return failure
        if len(queue) == 0:
            return False
        
        # Get the first element in the queue
        current = queue.pop(0)
        expendCnt += 1
        
        # Check for the goal state
        if current.checkGoalState(goal):
            return current

        # Add current to seen, convert numpy array to list to be able to compare
        seen.append(current.getMatrix().tolist())
        
        # Get all the child of the current matrix
        child = current.getChild()
        
        # Loop through all the child
        for c in child:      
            # If child not in seen, Add the child to the queue with the cost
            if c.getMatrix().tolist() not in seen:
                # Calculate the cost of the child base on misplaced tiles
                c.cost = manhattan_distance(c.getMatrix(), goal) + c.height
                # Update expend node count
                c.expended = expendCnt
                queue.append(c)
                
        # Sort the queue by cost
        queue = sorted(queue, key=lambda x: x.cost, reverse=False)

# A helper function to print the matrix
def printMatrix(matrix):
    for m in matrix:
        print(m)
   
# Main function start here
def main():
    # Default puzzle set
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
    puzzle4=numpy.array(
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
    
    print("Welcome to my 8-Puzzle Solver: \nType '1' to use a default puzzle  \nType '2' to create your own.")
    choice = int(input())
    
    if choice == 1:
        print("\nYou select to use the default puzzle. \nType '1' for Depth 0  \nType '2' for Depth 2 \nType '3' for Depth 4 \nType '4' for Depth 8 \nType '5' for Depth 16 \nType '6' for Depth 20 \nType '7' for Depth 24. \n**Error input will automatically use Depth 16.\n")
        choice = int(input())
        if choice == 1:
            print("You select Depth 0")
            puzzleChoice = puzzle0
        elif choice == 2:
            print("You select Depth 2")
            puzzleChoice = puzzle2
        elif choice == 3:
            print("You select Depth 4")
            puzzleChoice = puzzle4
        elif choice == 4:
            print("You select Depth 8")
            puzzleChoice = puzzle8
        elif choice == 5:
            print("You select Depth 16")
            puzzleChoice = puzzle16
        elif choice == 6:
            print("You select Depth 20")
            puzzleChoice = puzzle20
        elif choice == 7:
            print("You select Depth 24")
            puzzleChoice = puzzle24
        else:
            print("Using default Depth 16")
            puzzleChoice = puzzle16
        
        printMatrix(puzzleChoice)
        
    if choice == 2:
        print("\nYou select to create your own puzzle. Please enter your puzzle, use a zero to represent the blank. Enter each row, use space between numbers. Example: 1 2 3")
        print("please enter the first row")
        firstRow = input()
        print("please enter the second row")
        secondRow = input()
        print("please enter the third row")
        thirdRow = input()
        
        puzzleChoice = numpy.array(
                    [[int(firstRow[0]),int(firstRow[2]),int(firstRow[4])],
                    [int(secondRow[0]),int(secondRow[2]),int(secondRow[4])],
                    [int(thirdRow[0]),int(thirdRow[2]),int(thirdRow[4])]])

    start = puzzle(puzzleChoice)
    
    print("\nEnter your choice of algorithm: \nType '1' for Uniform Cost Search \nType '2' for A* with the Misplaced Tile heuristic \nType '3' for A* with the Manhattan distance heuristic.")
    choice = int(input())
    print()
    
    if choice == 1:
        print("You select to use Uniform Cost Search")
        # Calculate the time to run the algorithm
        startTime = time.time()
        result = uniform_cost_search(start, goal)
        endTime = time.time()
        
        # Store the solution path to an array, then print it out with the corresponding height
        path = []
        while(result.parent != None):
            path.append((result.getMatrix(), result.height, result.expended))
            result = result.parent
        path.append((result.getMatrix(), result.height, result.expended))
        path.reverse()
        
        for p in path:
            print("Matrix: ")
            printMatrix(p[0])
            print("Height: " + str(p[1]) + "\tExpended: " + str(p[2]) + "\n")
        
    if choice == 2:
        print("You select to use A* with the Misplaced Tile heuristic")
        # Calculate the time to run the algorithm
        startTime = time.time()
        result = a_star_with_misplaced_tiles(start, goal)
        endTime = time.time()
        
        # Store the solution path to an array, then print it out with the corresponding height
        path = []
        while(result.parent != None):
            path.append((result.getMatrix(), result.height, result.expended))
            result = result.parent
        path.append((result.getMatrix(), result.height, result.expended))
        path.reverse()
        
        for p in path:
            print("Matrix: ")
            printMatrix(p[0])
            print("Height: " + str(p[1]) + "\tExpended: " + str(p[2])  + "\n")
            
    if choice == 3:
        print("You select to use A* with the Manhattan distance heuristic")
        # Calculate the time to run the algorithm
        startTime = time.time()
        result = a_star_with_manhattan_distance(start, goal)
        endTime = time.time()
        
        # Store the solution path to an array, then print it out with the corresponding height
        path = []
        while(result.parent != None):
            path.append((result.getMatrix(), result.height, result.expended))
            result = result.parent
        path.append((result.getMatrix(), result.height, result.expended))
        path.reverse()
        
        for p in path:
            print("Matrix: ")
            printMatrix(p[0])
            print("Height: " + str(p[1]) + "\tExpended: " + str(p[2])  + "\n")    
    
    print(f"Algorithm finish! Taking {endTime - startTime} seconds \n \n")
    
if __name__ == "__main__":
    main()   