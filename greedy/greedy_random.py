import random

def get_random(driver, users, polo):
    # Trova un user random
    nn = random.choice(users)
    return nn, 0

def greedy_random(users, drivers, polo):

    # Randomizzo l'ordine dei drivers per aumentare la diversità delle soluzioni
    drivers_c = drivers.copy()
    random.shuffle(drivers_c)

    # Matrice di 5 colonne e n righe inizializzata a zero, dove n è il numero di driver
    tracks = [[[0,0] for i in range(6)] for j in range(len(drivers_c))]
    
    for j in range(5):
        for i in range(len(drivers_c)):
            tracks[i][j] = drivers_c[i]
            if j != 4: 
                nn, _ = get_random(drivers_c[i], users, polo)
                drivers_c[i] = nn
                users.remove(nn)

    for user in users:
        tracks.extend([[user, polo]])

    return tracks