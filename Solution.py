# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a genome that specifies a Sudoku board layout

import numpy as np
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

    def mutate(self):
        # For now, just repopulate randomly. Change this to do something smart.
        self.populate()
        self.fitness = self.getFitness()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    