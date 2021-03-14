# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a collection of Solutions

import numpy as np
import random
import Solution

class Population:
    NUMGENERATIONS = 10000
    PERFECTSCORE = 243
    
    # Variable for choosing method (breeding or crossover)
    METHOD = "crossover"

    def __init__(self, popsize, elitism, antielitism):
        self.popsize = popsize
        self.solutions = []
        self.elitism = elitism
        self.mutateProb = .02
        self.antielitism = antielitism

    def initialize(self):
        for i in range(self.popsize):
            self.solutions.append(Solution.Solution())

    def newGeneration(self):

        # Build new population comprised of (elitism) number of most fit, and
        # (antielitism) number of least fit to start with
        newParents = self.solutions[-self.antielitism:] + self.solutions[:self.elitism]
        
        fitProbs = []
        fitSum = 0
        
        # Calculate sum of all fitnesses
        for i in range(len(newParents)):
            fitSum += newParents[i].fitness
            
        # Create array of probabilites based on fitness (SUM = 1)
        # Each element = (individual fitness) / (SUM of fitnesses)
        for i in range(len(newParents)):
            fitProbs.append(newParents[i].fitness / fitSum)
            
        newSolutions = []
        
        for i in range(self.popsize):            
            
            # Choose two parents randomly from population
            # Higher fitness is more likely to be chosen          
            parent1 = np.random.choice(newParents, p = fitProbs)
            parent2 = parent1
            
            while (parent1 == parent2):
                parent2 = np.random.choice(newParents, p = fitProbs)
            
            # Breed chosen parents to create new child
            if (self.METHOD == "crossover"):
                child = parent1.crossover(parent2)                
            else:
                child = parent1.breed(parent2)
            
            # Add child to new generation
            newSolutions.append(child)

        self.solutions = newSolutions
        
        # Mutate the new current population
        for solution in self.solutions: 
            
            # Mutate based on probability
            if (random.random() <= self.mutateProb):
                solution.mutate()
                solution.mutate()
                
        # Sort solutions by fitness
        self.solutions.sort(reverse=True)

        # return max fitness value
        return self.solutions[0].getFitness()

    def toString(self):
        popStr = ''

        for solution in self.solutions:
            popStr += solution.toString() + '\n\n'

        return popStr