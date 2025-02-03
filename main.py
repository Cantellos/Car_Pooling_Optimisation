import matplotlib.pyplot as plt
import numpy as np

def generatore (tot_utenti, n_driver, map_size, seed=None):
  if seed is not None:
    np.random.seed(seed)

  users=[]
  drivers=[]

  limit = (int)(map_size/2)
  for i in range(tot_utenti-n_driver):
        users.append([np.random.randint(-limit,limit),np.random.randint(-limit,limit)])
        
  for i in range(n_driver):
    drivers.append([np.random.randint(-limit,limit),np.random.randint(-limit,limit)])
        
  polo = [0, 0]

  return users, drivers, polo

def plot_graph(users, drivers, polo):

    plt.figure(figsize=(8, 8))

    xu, yu = zip(*users)
    plt.scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    plt.scatter(xd, yd, color='blue', marker='o')
    
    plt.scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    plt.axhline(0, color='black', linewidth=1)  # Asse X
    plt.axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)

    # Aggiungi etichette e griglia
    plt.xlabel("Asse X")
    plt.ylabel("Asse Y")
    plt.grid(True)
    plt.title("Visualizzazione di punti nel piano cartesiano")

    # Mostra il grafico
    plt.show()

"""def plot_tracks(tracks, users, drivers, polo):
   # visualizza i segmenti percorso dai driver
  plt.figure(figsize=(8, 8))
   
  for track in tracks:
        x, y = zip(*track)
        plt.plot(x, y, marker='o')

  xu, yu = zip(*users)
  plt.scatter(xu, yu, color='green', marker='o')

  xd, yd = zip(*drivers)
  plt.scatter(xd, yd, color='blue', marker='o')

  plt.scatter(polo[0], polo[1], color='red', marker='o')

  # Aggiungi assi cartesiani centrati in (0,0)
  plt.axhline(0, color='black', linewidth=1)  # Asse X
  plt.axvline(0, color='black', linewidth=1)  # Asse Y

  # Imposta i limiti fissi per gli assi
  plt.xlim(-25, 25)
  plt.ylim(-25, 25)

  # Aggiungi etichette e griglia
  plt.xlabel("Asse X")
  plt.ylabel("Asse Y")
  plt.grid(True)
  plt.title("Visualizzazione di punti nel piano cartesiano")
  plt.legend()
  plt.show()
"""

def plot_all(tracks, users, drivers, polo):
    # due grafici affiancati
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    # grafico 1
    xu, yu = zip(*users)

    axs[0].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[0].scatter(xd, yd, color='blue', marker='o')
    
    axs[0].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[0].axhline(0, color='black', linewidth=1)  # Asse X
    axs[0].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[0].set_xlim(-25, 25)
    axs[0].set_ylim(-25, 25)
    
    # Aggiungi etichette e griglia
    axs[0].set_xlabel("Asse X")
    axs[0].set_ylabel("Asse Y")
    axs[0].grid(True)

    # grafico 2
    for track in tracks:
        x, y = zip(*track)
        plt.plot(x, y, marker='o')

    axs[1].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[1].scatter(xd, yd, color='blue', marker='o')

    axs[1].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[1].axhline(0, color='black', linewidth=1)  # Asse X
    axs[1].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[1].set_xlim(-25, 25)
    axs[1].set_ylim(-25, 25)

    # Aggiungi etichette e griglia
    axs[1].set_xlabel("Asse X")
    axs[1].set_ylabel("Asse Y")
    axs[1].grid(True)

    # Mostra il grafico
    plt.show()

def distanza(p1, p2):
    # Distanza Euclidea
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    # Distanza Manhattan
    # return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # Distanza di Chebyshev
    # return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    # Distanza di Minkowski
    # return (abs(p1[0] - p2[0]) ** 3 + abs(p1[1] - p2[1]) ** 3) ** (1/3)

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

def your_greedy(users, drivers, polo):
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

def funzione_obiettivo(tracks):
  # calcola la lunghezza totale per ogni percorso
  lunghezza_totale = 0
  for track in tracks:
      lunghezza = 0
      for i in range(1, len(track)):
          lunghezza += distanza(track[i-1], track[i])
      lunghezza_totale += lunghezza
    
  return lunghezza_totale

users, drivers, polo = generatore(20, 3, 50, 2)
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
tracks = your_greedy(users1, drivers1, polo1)
print(f"USERS: ", users1)
print(f"DRIVERS: ", drivers1)
plot_graph(users, drivers, polo)
plot_all(tracks, users, drivers, polo)
print(f"Funzione Obiettivo", funzione_obiettivo(tracks))
