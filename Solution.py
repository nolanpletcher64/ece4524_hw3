# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a genome that specifies a Sudoku board layout

import numpy as np
import random
import SudokuBoard

class Solution(SudokuBoard.SudokuBoard):
    def __init__(self):
        super( ).__init__( )

        self.fitness = 0
        self.populate()

    def populate(self):
        for row in range( self.SZ ):
            self.cells[row] = list(range(1, self.SZ + 1))
            np.random.shuffle(self.cells[row])

        self.fitness = self.getFitness()
        
    def breed(self, other):
        
        child = Solution()
        
        # Iterate through rows
        for i in range(0,9):
            
            # Iterate through cells in row
            for j in range(0,9):
                
                # Randomly choose parent
                chosenParent = bool(random.getrandbits(1))
                
                # Set child's cell to parent's cell
                if chosenParent:
                    child.cells[i][j] = self.cells[i][j]
                else:
                    child.cells[i][j] = other.cells[i][j]
        
        # Update fitness
        child.fitness = child.getFitness()
        
        return child
    
    def crossover(self, other):
        
        child = Solution()
        
        # Iterate through rows
        for row in range(0,9):
            
            # Randomly choose parent
            chosenParent = bool(random.getrandbits(1))
            
            # Set child's row to parents row
            if chosenParent:
                child.cells[row] = self.cells[row]
            else:
                child.cells[row] = other.cells[row]
        
        # Update fitness
        child.fitness = child.getFitness()
        
        return child    

    def colDup(self, row, value):
        
        # Check for duplicate values in a column, used for mutate
        for col in range(0,9):
            if (self.cells[row][col] == value):
                return True
        
        return False
    
    def blockDup(self, row, col, value):
        
        i = 3 * int(row / 3)
        j = 3 * int(col / 3)
        
        # Check for duplicate values in a block, used for mutate
        for k in range(0, 3):
            if ((self.cells[i + k][j] == value) or (self.cells[i + k][j + 1] == value) or (self.cells[i + k][j + 2] == value)):
                return True
    
        return False
    
    def mutate(self):
        row = random.randint(0,8)

        col1 = random.randint(0,8)
        col2 = col1

        while col1 == col2:
            col2 = random.randint(0,8)

        # Swap these cells values
        temp = self.cells[row][col1]
        self.cells[row][col1] = self.cells[row][col2]
        self.cells[row][col2] = temp

        # Update new fitness
        self.fitness = self.getFitness()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    