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
            self.cells[row] = list(range(self.SZ))
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

    def colDup(self, row, value):
        
        # Check for duplicate values in a column, used for mutate
        for col in range(0,9):
            if (self.cells[row, col] == value):
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
        # Choose a row and get two random values
        chosenRow = random.randint(0,8)
        chosen1 = random.randint(0,8)
        chosen2 = random.randint(0,8)
        
        cell1 = self.cells[chosenRow][chosen1]
        cell2 = self.cells[chosenRow][chosen2]
        
        # Ensure switching will not cause a duplicate in the columns or blocks
        if ((not self.colDup(chosenRow, cell1)) and (not self.colDup(chosenRow, cell2)) and (not self.blockDup(chosenRow, chosen1, cell2)) and (not self.blockDup(chosenRow, chosen2, cell1))):
            
            # Switch values
            self.cells[chosenRow][chosen1] = cell2
            self.cells[chosenRow][chosen2] = cell1
        
            # Update new fitness
            self.fitness = self.getFitness()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    