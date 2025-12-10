import random

# Fitness function: count number of 1s in the string
def fitness(individual):
    return sum(individual)

# Random selection proportional to fitness
def random_selection(population, fitness_fn):
    total_fitness = sum(fitness_fn(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += fitness_fn(ind)
        if current >= pick:
            return ind
    return population[-1]

# Reproduce: single-point crossover
def reproduce(x, y):
    n = len(x)
    c = random.randint(1, n-1)
    return x[:c] + y[c:]

# Mutation: flip a random bit
def mutate(individual):
    n = len(individual)
    i = random.randint(0, n-1)
    individual[i] = 1 - individual[i]
    return individual

# Genetic Algorithm
def genetic_algorithm(population, fitness_fn, max_generations=100):
    for generation in range(max_generations):
        new_population = []
        for _ in range(len(population)):
            x = random_selection(population, fitness_fn)
            y = random_selection(population, fitness_fn)
            child = reproduce(x, y)
            if random.random() < 0.1:  # mutation probability
                child = mutate(child)
            new_population.append(child)
        population = new_population

        # Check if any individual is "fit enough"
        best = max(population, key=fitness_fn)
        if fitness_fn(best) == len(best):  # all 1s
            print(f"Solution found in generation {generation}: {best}")
            return best
    # Return best individual after max_generations
    best = max(population, key=fitness_fn)
    print(f"Best after {max_generations} generations: {best}")
    return best

# Example run
if __name__ == "__main__":
    # Initial population: 10 individuals, each 8 bits long
    population = [[random.randint(0,1) for _ in range(8)] for _ in range(10)]
    genetic_algorithm(population, fitness)
