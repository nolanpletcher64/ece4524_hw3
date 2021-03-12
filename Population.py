# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a collection of Solutions

import numpy as np
import random
import Solution

class Population:
    NUMGENERATIONS = 1000
    PERFECTSCORE = 243

    def __init__(self, popsize, elitism, antielitism):
        self.popsize = popsize
        self.solutions = []
        self.elitism = elitism
        self.mutateProb = .1
        self.antielitism = antielitism

    def initialize(self):
        for i in range(self.popsize):
            self.solutions.append(Solution.Solution())

    def newGeneration(self):

        # Sort solutions by fitness
        self.solutions.sort(reverse=True)

        # Build new population comprised of (elitism) number of most fit, and
        # (antielitism) number of least fit to start with
        newSolutions = self.solutions[-self.antielitism:] + self.solutions[:self.elitism]
        
        fitProbs = []
        fitSum = 0
        
        # Calculate sum of all fitnesses
        for i in range(len(self.solutions)):
            fitSum += self.solutions[i].fitness
            
        # Create array of probabilites based on fitness (SUM = 1)
        # Each element = (individual fitness) / (SUM of fitnesses)
        for i in range(len(self.solutions)):
            fitProbs.append(self.solutions[i].fitness / fitSum)
            

        for i in range(self.popsize - len(newSolutions)):            
            
            # Choose two parents randomly from population
            # Higher fitness is more likely to be chosen          
            parent1 = np.random.choice(self.solutions, p = fitProbs)
            parent2 = np.random.choice(self.solutions, p = fitProbs)
            
            # Breed chosen parents to create new child
            child = parent1.breed(parent2)
            
            # Add child to new generation
            newSolutions.append(child)

        self.solutions = sorted(newSolutions, reverse=True)
        
        # Mutate the new current population
        for solution in self.solutions: 
            
            # Mutate based on probability
            if (random.random() <= self.mutateProb):
                solution.mutate()        

        # return max fitness value
        return self.solutions[0].getFitness()

    def toString(self):
        popStr = ''

        for solution in self.solutions:
            popStr += solution.toString() + '\n\n'

        return popStr