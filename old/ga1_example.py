import random
import numpy as np

# Define the VRP problem
class VRP:
    def __init__(self, num_customers, num_vehicles, depot, customers, capacity):
        self.num_customers = num_customers
        self.num_vehicles = num_vehicles
        self.depot = depot
        self.customers = customers
        self.capacity = capacity

    def distance(self, customer1, customer2):
        return np.linalg.norm(np.array(customer1) - np.array(customer2))

# Define the Genetic Algorithm
class GeneticAlgorithm:
    def __init__(self, vrp, population_size, mutation_rate, generations):
        self.vrp = vrp
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = list(range(1, self.vrp.num_customers + 1))
            random.shuffle(individual)
            population.append(individual)
        return population

    def fitness(self, individual):
        total_distance = 0
        current_load = 0
        current_location = self.vrp.depot

        for customer in individual:
            customer_location = self.vrp.customers[customer - 1]
            total_distance += self.vrp.distance(current_location, customer_location)
            current_load += 1
            if current_load > self.vrp.capacity:
                total_distance += self.vrp.distance(customer_location, self.vrp.depot)
                current_location = self.vrp.depot
                current_load = 1
            current_location = customer_location

        total_distance += self.vrp.distance(current_location, self.vrp.depot)
        return total_distance

    def selection(self):
        # Roulette wheel selection
        selected = random.choices(self.population, k=2, weights=[1/self.fitness(ind) for ind in self.population])
        print(selected)
        return selected

    def crossover(self, parent1, parent2):
        size = len(parent1)
        start, end = sorted(random.sample(range(size), 2))
        child = [None] * size
        child[start:end] = parent1[start:end]
        # TODO: da un genitore passare solo posizioni relative (ordine) e non assolute 
        # TODO: capire quali parti trasmettere ai figli (non random) 
        pointer = 0
        for gene in parent2:
            if gene not in child:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = gene

        return child

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(len(individual)), 2)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    def evolve(self):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.selection()
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population

    def run(self):
        for generation in range(self.generations):
            self.evolve()
            best_individual = min(self.population, key=self.fitness)
            print(f"Generation {generation}: Best fitness = {self.fitness(best_individual)}")

# Example usage
num_customers = 10
num_vehicles = 3
depot = (0, 0)
customers = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_customers)]
capacity = 5

vrp = VRP(num_customers, num_vehicles, depot, customers, capacity)
ga = GeneticAlgorithm(vrp, population_size=50, mutation_rate=0.1, generations=100)
ga.run()