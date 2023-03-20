from individual import Individual
import random

class Population:
    def __init__(self, popSize, mutationRate, targetGenome):
        self.popSize = popSize
        self.mutationRate = mutationRate
        self.genomeLength = len(targetGenome)
        self.targetGenome = targetGenome
        self.foundOptimalGenome = False
        self.population = []
        self.generation = 1

    def initialPop(self):
        """
        Creates the initial population as a (list) of Individuals
        """

        for _ in range(self.popSize):
            idv = Individual(self.genomeLength)

            idv.initialGenome()
            idv.fitnessCalc(self.targetGenome)
            
            self.population.append(idv)

    def generateChild(self, parA, parB):
        """
        Generates a child joining the genome of the two parents
        This function simulates the crossing over by randomly choosing a index where the genome of the parents is going to be split
        The child's genome is the result of the junction of the randomly split genome of the parents

        Parameters:
            parA & parB (Individual): the chosen parents
        """
        child = Individual(self.genomeLength)

        #crossing over
        idx = random.randrange(self.genomeLength)  
        child.genome += parA.genome[:idx]
        child.genome += parB.genome[idx:]

        child.mutation(self.mutationRate)
        child.fitnessCalc(self.targetGenome)

        #check if this the target genome
        if child.fitness == self.genomeLength ** 2:
            self.foundOptimalGenome = True

        return child
    
    def select_5(self):
        """
        Selects the 5 more adapted Individuals
        """
        pop_sorted = sorted(self.population, key=lambda Individual: Individual.fitness, reverse=True)
        return pop_sorted[:5]
        


    def newPop(self):
        """
        Generates a new pop
        For each new Individual, new parents are chosen using the selection method
        """
        self.generation += 1
        newPop = []
        top5_parents = self.select_5()

        for _ in range(self.popSize):
            newPop.append(self.generateChild(self.selection(top5_parents), self.selection(top5_parents)))

        self.population = newPop

        
    def selection(self, top_5):
        """
        Selects a parent randomly between the top 5 more adapated Individuals

        Parameters:
            top5 (list): a list contatining the top 5 more adapted Individuals
        """
        return top_5[random.randrange(5)]

    def printPop(self):
        print(*(idv.genome for idv in self.population), sep="\n")



