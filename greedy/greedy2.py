from utils import distanza
import random

def get_nn(driver, cusers, polo):
    # trova il vicino più vicino
    min_dist = 1000000
    nn = None
    k = 11 # peso associato alla distanza tra driver e utente (stimato empiricamente)

    for p in cusers:
        dist = (k * distanza(driver, p)) / distanza(p, polo)
        if dist < min_dist:
            min_dist = dist
            nn = p
    return nn, min_dist

def greedy2(users, drivers, polo):
  
  drivers_c = drivers.copy()

  # matrice di 5 colonne e n righe inizializzata a zero, dove n è il numero di driver
  tracks = [[[0,0] for i in range(6)] for j in range(len(drivers_c))]
  
  for j in range(5):
    for i in range(len(drivers_c)):
      tracks[i][j] = drivers_c[i]
      if j != 4: 
        nn, _ = get_nn(drivers_c[i], users, polo)
        drivers_c[i] = nn
        users.remove(nn)
  
  for user in users:
    tracks.extend([[user, polo]])

  return tracks