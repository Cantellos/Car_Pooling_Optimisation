import numpy as np
import matplotlib.pyplot as plt

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

def plot_all(title, tracks, users, drivers, polo, map_size):
    # due grafici affiancati
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    fig.suptitle(title)

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
    axs[0].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[0].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)
    
    # Aggiungi etichette e griglia
    axs[0].set_xlabel("Asse X")
    axs[0].set_ylabel("Asse Y")
    axs[0].grid(True)

    # grafico 2
    for track in tracks:
        x, y = zip(*track)
        # plot di un percorso indicato con una freccia
        axs[1].plot(x, y, marker='o')

    axs[1].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[1].scatter(xd, yd, color='blue', marker='o')

    axs[1].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[1].axhline(0, color='black', linewidth=1)  # Asse X
    axs[1].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[1].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[1].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

    # Aggiungi etichette e griglia
    axs[1].set_xlabel("Asse X")
    axs[1].set_ylabel("Asse Y")
    axs[1].grid(True)

    # Mostra il grafico
    plt.show()

def plot_total(users, drivers, polo, map_size, tracks_all):
    # numero di righe e 3 colonne pari al numero di grafici da visualizzare (tranne il primo)
    rows = (int)((len(tracks_all)+1)/3)
    cols = 3

    fig, axs = plt.subplots(rows, cols, figsize=(18, 10))

    fig.suptitle("Risultati ottenuti")

    # grafico 1
    xu, yu = zip(*users)

    axs[0][0].set_title("Istanza generata")

    axs[0][0].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[0][0].scatter(xd, yd, color='blue', marker='o')
    
    axs[0][0].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[0][0].axhline(0, color='black', linewidth=1)  # Asse X
    axs[0][0].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[0][0].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[0][0].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)
    
    # Aggiungi etichette e griglia
    axs[0][0].set_xlabel("Asse X")
    axs[0][0].set_ylabel("Asse Y")
    axs[0][0].grid(True)

    titles, tracks_list = zip(*tracks_all)

    for i, tracks in enumerate(tracks_list):
        pos_x = (int)((i+1)/cols)
        pos_y = (int)((i+1)%cols)

        axs[pos_x][pos_y].set_title(titles[i])

        for track in tracks:
            x, y = zip(*track)
            axs[pos_x][pos_y].plot(x, y, marker='o')
        axs[pos_x][pos_y].scatter(xu, yu, color='green', marker='o')

        xd, yd = zip(*drivers)
        axs[pos_x][pos_y].scatter(xd, yd, color='blue', marker='o')

        axs[pos_x][pos_y].scatter(polo[0], polo[1], color='red', marker='o')

        # Aggiungi assi cartesiani centrati in (0,0)
        axs[pos_x][pos_y].axhline(0, color='black', linewidth=1)  # Asse X
        axs[pos_x][pos_y].axvline(0, color='black', linewidth=1)  # Asse Y

        # Imposta i limiti fissi per gli assi
        axs[pos_x][pos_y].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
        axs[pos_x][pos_y].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

        # Aggiungi etichette e griglia
        axs[pos_x][pos_y].set_xlabel("Asse X")
        axs[pos_x][pos_y].set_ylabel("Asse Y")
        axs[pos_x][pos_y].grid(True)

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

def funzione_obiettivo(tracks):
  # calcola la lunghezza totale per ogni percorso
  lunghezza_totale = 0
  for track in tracks:
      lunghezza = 0
      for i in range(1, len(track)):
          lunghezza += distanza(track[i-1], track[i])
      lunghezza_totale += lunghezza
    
  return round(lunghezza_totale,1)