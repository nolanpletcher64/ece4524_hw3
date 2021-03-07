# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a genome that specifies a Sudoku board layout

import numpy as np

class Solution(object):
    
    def __init_(self):
        self.values = np.zeros((9, 9), dtype=int)
        self.fitness = 0
        return
    
    def mutation():
        
        return
        
    def breeding():
        
        return
        
    def fitnessEval(self):
        
        rowCount = np.zeros(9)
        rowSum = 0
        colCount = np.zeros(9)
        colSum = 0
        sqrCount = np.zeros(9)
        sqrSum = 0
        
        # Iterate through each row in board
        for i in range(9):
            
            # Iterate through each number in the row
            for j in range(9):
                
                # Increment number of occurences of the number
                rowCount[self.values[i][j] - 1] += 1
            
            rowSum += (1.0 / (len(set(rowCount)))) / 9
            
            # Reset row count
            rowCount = np.zeros(9)
            
        # Iterate through each column in board
        for i in range(9):
            
            # Iterate through each number in column
            for j in range(9):
                
                # Increment number of occurences of the number
                colCount[self.values[j][i] - 1] += 1
                
            colSum += (1.0 / (len(set(colCount)))) / 9
            
            # Reset column count
            colCount = np.zeros(9)
            
            
        
        return
    
    