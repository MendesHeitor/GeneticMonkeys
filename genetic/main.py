from population import Population

def main():

    popSize = int(input("Please insert the number of individual of each population: "))
    targetPhrase = input("Now, please insert the target phrase: ")
    mutationRate = float(input("Insert a mutation rate (remember, your value must be around 0-1): "))

    Pop = Population(popSize, mutationRate, targetPhrase)
    Pop.initialPop()

    while Pop.foundOptimalGenome == False:
        Pop.newPop()

    print(f'\nThe genome "{targetPhrase}" was found in generation {Pop.generation}')


if __name__ == "__main__":
    main()
