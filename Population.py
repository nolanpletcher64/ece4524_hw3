# Population Nolan Pletcher ECE5424 Mar 6 2021
# This class contains a collection of Solutions

import numpy as np
import random
import Solution

class Population:
    NUMGENERATIONS = 100
    PERFECTSCORE = 243

    def __init__(self, popsize, elitism, antielitism):
        self.popsize = popsize
        self.solutions = []
        self.elitism = elitism
        self.mutateProb = .01
        self.antielitism = antielitism

    def initialize(self):
        for i in range(self.popsize):
            self.solutions.append(Solution.Solution())

    def newGeneration(self):

        # Sort solutions by fitness
        self.solutions.sort(reverse=True)

        # Build new population comprised of (elitism) number of most fit, and
        # (antielitism) number of least fit, filling in rest with random solutions
        newSolutions = self.solutions[-self.antielitism:] + self.solutions[:self.elitism]

        for i in range(self.popsize - len(newSolutions)):
            
            # newSolutions.append(Solution.Solution())
            
            # Choose two parents randomly from half of population with higher fitness            
            chosen1 = random.randint(0, int(len(self.solutions) / 2))
            chosen2 = random.randint(0, chosen1)
            
            parent1 = self.solutions[chosen1]
            parent2 = self.solutions[chosen2]
            
            # Breed chosen parents to create new child
            child = parent1.breed(parent2)
            
            # Add child to new generation
            newSolutions.append(child)

        self.solutions = sorted(newSolutions, reverse=True)
        
        # Mutate the new current population
        for solution in self.solutions: 
            
            # Mutate based on probability
            if (random.random() >= self.mutateProb):
                solution.mutate()        

        # return max fitness value
        return self.solutions[0].getFitness()

    def toString(self):
        popStr = ''

        for solution in self.solutions:
            popStr += solution.toString() + '\n\n'

        return popStr