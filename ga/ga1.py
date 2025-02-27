from utils import funzione_obiettivo as fitness
import random
from utils import distanza

from greedy.greedy_random import greedy_random as initGR, get_random as get_nextGR
from greedy.greedy1 import greedy1 as initG1, get_nn as get_nextG1
from greedy.greedy2 import greedy2 as initG2, get_nn as get_nextG2
from kmeans.kmeans2 import kmeans2 as initKM, get_nn as get_nextKM

def initialize_population(users, drivers, polo, base):
    population = []
    for _ in range(100):
        users_c = users.copy()
        drivers_c = drivers.copy()

        if base == "random":
            individual = initGR(users_c, drivers_c, polo)
        elif base == "greedy1":
            individual = initG1(users_c, drivers_c, polo)
        elif base == "greedy2":
            individual = initG2(users_c, drivers_c, polo)
        elif base == "kmeans":
            individual = initKM(users_c, drivers_c, polo)
        
        population.append(individual)

    return population
    
def selection(population):
    #print("Selection")
    selected = random.choices(population, k=2, weights=[1/fitness(individual) for individual in population])
    return selected

# Controlla se il gene è già presente nel figlio
def check_gene(gene, child):
    for i in range(len(gene)):
        for j in range(len(child)):
            if gene[i] in child[j]:
                return False
    return True

def crossover(parent1, parent2, n_drivers):
    child = []
    
    parent1_d = []  # lista di parent1 con più di 2 elementi
    for p1 in parent1:
        if len(p1) > 2:
            parent1_d.append(p1)  
    size_p1 = len(parent1_d)

    for n in range(random.randint(1, (int)(size_p1/2)+1)):
        size_p1 = len(parent1_d)
        index = random.randint(0, size_p1-1)
        child.append(parent1_d[index])
        parent1_d.pop(index)

    for gene in parent2:
        if len(gene) != 2 and check_gene(gene, child) and len(child) < n_drivers-1:
            child.append(gene)

    return child

def get_remaining(users, drivers, child):
    users_c = []
    drivers_c = []

    for driver in drivers:
        for track in child:
            if driver not in track and driver not in drivers_c:
                drivers_c.append(driver)
    
    for user in users:
        for track in child:
            if user not in track and user not in users_c:
                users_c.append(user)

    return users_c, drivers_c

def greedy_driver(driver, users_c, polo, base):
    track = [driver]
    for _ in range(4):
        if base == "random":
            nn, _ = get_nextGR(driver, users_c, polo)
        elif base == "greedy1":
            nn, _ = get_nextG1(driver, users_c, polo)
        elif base == "greedy2":
            nn, _ = get_nextG2(driver, users_c, polo)
        elif base == "kmeans":
            nn, _ = get_nextKM(driver, users_c, polo)

        track.append(nn)
        driver = nn
        users_c.remove(nn)
    track.append(polo)
    return track

def costo(track):
    c = 0
    for i in range(len(track)-1):
        c += distanza(track[i], track[i+1])
    return c

def try_swap(child, excluded, polo):
    best_saving = 0
    best_tracks = child.copy()
    best_excluded = excluded.copy()
    
    for t in range(len(child)):
        for elt in range(1, len(child[t])-1):
            exc = 0
            while(exc < len(excluded)):
                excluded_track = [excluded[exc], polo]
                costo_track_before = costo(child[t]) + costo(excluded_track)
                track1 = child[t].copy()
                track2 = excluded_track.copy()
                track1[elt], track2[0] = track2[0], track1[elt]
                costo_track_after = costo(track1) + costo(track2)
                if costo_track_after < costo_track_before:
                    saving = costo_track_before - costo_track_after
                    if saving > best_saving:
                        best_saving = saving
                        best_tracks = child.copy()
                        best_excluded = excluded.copy()
                        best_tracks.remove(child[t])
                        best_tracks.append(track1)
                        best_excluded.remove(excluded[exc])
                        best_excluded.append(track2[0])
                        #improved = True TODO: aggiungi il while
                exc += 1

    return best_tracks, best_excluded

def mutate(child, users, drivers, polo, base):
    users_c, drivers_c = get_remaining(users, drivers, child)

    for driver in drivers_c:
        child.append(greedy_driver(driver, users_c, polo, base))
    
    if random.random() < 0.2:
        child, users_c = try_swap(child, users_c, polo)
        
    for user in users_c:
        track = [user]
        track.append(polo)
        child.append(track)

    return child
    
def evolve(population, users, drivers, polo, base):
    new_population = []
    
    for _ in range(len(population)):
        parent1, parent2 = selection(population)
        child = crossover(parent1, parent2, len(drivers))
        child = mutate(child, users, drivers, polo, base)
        new_population.append(child)
    
    return new_population
        
def ga1(user, drivers, polo, base):
    population = initialize_population(user, drivers, polo, base)

    best_individual = population[0]

    for i in range(100):
        #print("Generation ", i)
        population = evolve(population, user, drivers, polo, base)

        for individual in population:
            if fitness(individual) < fitness(best_individual):
                best_individual = individual
            
    return best_individual