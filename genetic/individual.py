import random

ALL_GENES = "aàáâãäbcçdeéêfghiíjklmnoóôõöpqrstuúüvwxyzAÀÁÂÃÄBCÇDEÉÊFGHIÍJKLMNOÓÔÕÖPQRSTUÚÜVWXYZ0123456789!@#$%&*()-_=+[]{};:'\"<>,.?/\| "

class Individual:
    def __init__ (self, genomeLenght):
        self.genomeLength = genomeLenght
        self.genome = ""
        self.fitness = 0


    def initialGenome(self):
        """
        Creates the initial Genome for the initial pop
        Chooses random genes and creates a string with the same size of the target phrase  
        """

        all_length = len(ALL_GENES)
        for _ in range(self.genomeLength):
            self.genome += ALL_GENES[random.randrange(all_length)]
    
    def fitnessCalc(self, target):
        """
        Calculates the fitness of the genome
        The fitness of the individual is to the power of 2, so that tiny differences in genome makes a individual more likely to be chosen to become a parent

        Parameters:
            target(string): the target genome for comparison
            
        """
        for i in range(self.genomeLength):
            if self.genome[i] == target[i]:
                self.fitness += 1
        self.fitness **= 2


    def mutation(self, mutationRate):
        """
        Decides wheter or not each gene from the genome will mutate
        Chooses a random character to replace the current if the mutation is aproved

        Parameters:
            mutationRate(float):represents the chance of a mutation occur 
        """
        all_length = len(ALL_GENES)
        for i in range(self.genomeLength):
            if(random.uniform(0, 1) < mutationRate):
                self.genome = self.genome[:i] + ALL_GENES[random.randrange(all_length)] + self.genome[i+1:]

