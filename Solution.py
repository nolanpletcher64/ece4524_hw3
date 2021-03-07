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
            
            # Set rowSum fitness
            
            
            # Reset row count
            rowCount = np.zeros(9)
            
            
        # Iterate through each column in board
        for i in range(9):
            
            # Iterate through each number in column
            for j in range(9):
                
                # Increment number of occurences of the number
                colCount[self.values[j][i] - 1] += 1
                
            # Set colSum fitness
            
            
            # Reset column count
            colCount = np.zeros(9)
            
            
        # Iterate through each square in board
        for i in range(0, 9, 3):
            
            # Iterate through each number in square
            for j in range(0, 9, 3):
                
                for k in range(3):
                    
                    sqrCount[self.values[i+k][j] - 1] += 1
                    sqrCount[self.values[i+k][j+1] - 1] += 1
                    sqrCount[self.values[i+k][j+2] - 1] += 1
                    
            # Set sqrSum fitness
            
                    
            # Reset square count
            sqrCount = np.zeros(9)
        
        
        # Calculate total fitness, PERFECTSCORE = 243
        self.fitness = "Insert formula here"
        
        return
    
    