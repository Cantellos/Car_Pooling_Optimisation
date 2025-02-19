import numpy as np
from sklearn.cluster import KMeans
from utils import distanza, funzione_obiettivo
import random

# TODO: Randomizzare l'ordine dei driver nel kmeans per evitare che il primo driver abbia sempre i migliori vicini

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

def kmeans4(users, drivers, polo):
    # Randomizzo l'ordine dei driver per 10 volte e tengo il risultato migliore
    best_tracks = []
    best_fo = 1000000

    for i in range(20):
        drivers_c = drivers.copy()
        # Randomizzo l'ordine dei driver
        random.shuffle(drivers_c)
        
        # Applichiamo K-Means con n. driver clusters
        kmeans = KMeans(n_clusters=len(drivers_c), n_init=1, init=np.array(drivers_c))
        # fit di kmeans su users e drivers_c
        X = np.array(users)
        kmeans.fit(X)
        y_kmeans = kmeans.predict(X)
        
        tracks = []

        # Limitiamo il numero di elementi in ogni cluster
        max_elements_per_cluster = 4
        cluster_counts = np.bincount(y_kmeans) # Conta il numero di elementi per cluster
        for cluster in range(len(drivers_c)):            
            # Trovo gli elementi del cluster
            indices = np.where(y_kmeans == cluster)[0]
            cluster_users = [users[i] for i in indices]
            tracks.append([drivers_c[cluster]])
            
            for i in range(min(max_elements_per_cluster, len(cluster_users))):
                nn, _ = get_nn(drivers_c[cluster], cluster_users, polo)
                tracks[cluster].append(nn)
                cluster_users.remove(nn)
                drivers_c[cluster] = nn
            tracks[cluster].append(polo)

            excluded = []
                    
            # Indici di quelli da eliminare
            for cluser in cluster_users:
                excluded.append(users.index(cluser))

            # Riassegna gli elementi esclusi al prossimo cluster
            for idx in excluded:
                y_kmeans[idx] += 1

        # aggiungiamo gli users che non sono stati assegnati
        for i in range(len(X)):
            if y_kmeans[i] == len(drivers_c):
                tracks.append([X[i].tolist(), polo])
        
        if funzione_obiettivo(tracks) < best_fo:
            best_fo = funzione_obiettivo(tracks)
            best_tracks = tracks
    
    # Visualizziamo i risultati
    #plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', edgecolor='k', alpha=0.7)
    #plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
    #plt.title("Clustering con K-Means")
    #plt.show()

    return best_tracks