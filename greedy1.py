from utils import distanza

def get_nn(driver, users):
    # trova il vicino più vicino
    min_dist = 1000000
    nn = None

    for p in users:
        dist = distanza(driver, p)
        if dist < min_dist:
            min_dist = dist
            nn = p
    return nn, min_dist

# TODO: implementare la funzione Neighbour con diverse strategie
# 1 - Distanza Neighbour + Distanza Polo-Neighbour
# 2 - Distanza Polo-Neighbour
# 3 - Distanza Neighbour + Distanza Polo-Neighbour + Distanza Polo

def greedy1(users, drivers, polo):
  # matrice di 5 colonne e n righe, dove n è il numero di driver
  tracks = [[[0,0] for i in range(6)] for j in range(len(drivers))]
  
  for j in range(5):
    for i in range(len(drivers)):
      tracks[i][j] = drivers[i]
      if j != 4: 
        nn, _ = get_nn(drivers[i], users)
        drivers[i] = nn
        users.remove(nn)
  
  for user in users:
    tracks.extend([[user, polo]])

  return tracks