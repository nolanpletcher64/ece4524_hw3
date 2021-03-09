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
        
        return

    def mutate(self):
        # Choose a row and switch two values randomly
        chosenRow = random.randint(0,8)
        chosen1 = random.randint(0,8)
        chosen2 = random.randint(0,8)
        
        cell1 = self.cells[chosenRow][chosen1]
        cell2 = self.cells[chosenRow][chosen2]
        
        self.cells[chosenRow][chosen1] = cell2
        self.cells[chosenRow][chosen2] = cell1
        
        # Update new fitness
        self.fitness = self.getFitness()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    