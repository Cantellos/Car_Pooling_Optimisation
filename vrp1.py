import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from utils import distanza, funzione_obiettivo
import random

# TODO: Parallelizzare la ricerca del NN di tutti i driver

def get_nn(driver, cusers, polo):
    # trova il vicino più vicino
    min_dist = 1000000
    nn = None
    k = 11

    for p in cusers:
        dist = (k * distanza(driver, p)) / distanza(p, polo)
        if dist < min_dist:
            min_dist = dist
            nn = p
    return nn, min_dist

def vrp1(users, drivers, polo):
    # Randomizzo l'ordine dei driver per 10 volte e tengo il risultato migliore
    best_tracks = []
    best_fo = 1000000

    for i in range(200):
        users_c = users.copy()
        drivers_c = drivers.copy()
        # Randomizzo l'ordine dei driver
        random.shuffle(drivers_c)
        
        tracks = [0 for _ in range(len(drivers_c))]

        for i in range(len(drivers_c)):
            tracks[i] = [drivers_c[i]]
            
            for j in range(4): # Itero per ogni passeggero
                nn, _ = get_nn(drivers_c[i], users_c, polo)
                tracks[i].append(nn)
                users_c.remove(nn)
                drivers_c[i] = nn
            tracks[i].append(polo)

        # aggiungiamo gli users che non sono stati assegnati
        for exc in users_c:
            tracks.append([exc, polo])

        print(funzione_obiettivo(tracks))
        
        if funzione_obiettivo(tracks) < best_fo:
            best_fo = funzione_obiettivo(tracks)
            best_tracks = tracks
    
    # Visualizziamo i risultati
    #plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', edgecolor='k', alpha=0.7)
    #plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
    #plt.title("Clustering con K-Means")
    #plt.show()

    return best_tracks