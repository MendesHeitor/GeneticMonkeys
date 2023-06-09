# Genetic Monkeys
## Genetic Algorithm for the Infinite Monkey Theorem

### What's the problem?

There's a theorem called the Infinite Monkey Theorem which states that a monkey hitting a certain amount of keys on a typewriter would eventually end up typing any text, such as the entire Shakespeare's work.

As I don't have infinity to keep testing out this random approach, I have decided to face this problem using a Genetic Algorithm which mimics the evolution of a natural system.

### How is It done?

To mimic the evolution of a natural system, the genetic algorithm in question follows a sequence of steps:
    
- Generation of the initial Population: the first population is generated by picking characters randomly and using them to compose each individuals genome (The individual is represented by its genome and its fitness score: how similar to the target phrase its genome is).

-  Generate next Population: from the current population we are going to generate the next one, so we must complete the following steps:
    1. Selection: There are many ways to select the parents of the child, in this application a parent is being chosen randomly between the top 5 most adapted individuals.
    2. Reproduction/Crossing Over: After the two parents have been chosen, we will choose a random point in the string where the parents genome should be joined.
    3. Evaluation: Check if a perfect individual was generated, this step is being done at every child's generation.  

- The system will keep generating new Populations untill the perfectly adapted individual is found.

### Give it a try
This project is very simple to test, to do so you must follow the steps below:

1. Clone the Repository
2. Inside the "genetic" folder, type in the following command:
```bash
#average command (macOS, Windows, some linux distros)
python main.py

#for some linux distros the command is
python3 main.py
```
3. Input the requested variables.
4. See it working.

Try to see how the amount of individuals, the mutation rate and the length of the phrase alters the speed and efficiency of the Genetic Algorithm.

### Here is a demonstration

![GeneticMonkey](https://user-images.githubusercontent.com/93098315/226491735-e0c37fc3-5451-42ee-84b1-176e3c581f93.gif)

<sub>This video was slowed down for better visualization<sub>
    
### Next Steps 
The Genetic Algorithm efficiency relies on a diverse number of variables and functions, such as the fitness function, the selection mechanism, the crossing over mechanism, the mutation rate, the amount of individuals. In the future, I plan to document and display visually how do those variables and functions affect the efficiency of the Algorithm.
