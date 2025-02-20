from utils import distanza
import numpy as np
from sklearn.cluster import KMeans
import random

def get_4nn(driver, cusers):
    # Trova i 4 vicini più vicini
    min_dist = 1000000

    nn = [None, None, None, None]
    dist = [min_dist, min_dist, min_dist, min_dist]

    for i in range(4):
        for p in cusers:
            if p not in nn:
                d = distanza(driver, p)
                if d < dist[i]:
                    dist[i] = d
                    nn[i] = p

    return nn, dist
    
def kmeans1(users, drivers, polo):

    # Randomizzo l'ordine dei drivers per aumentare la diversità delle soluzioni
    drivers_c = drivers.copy()
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
    for cluster in range(len(drivers_c)):            
        # Trovo gli elementi del cluster
        indices = np.where(y_kmeans == cluster)[0]
        cluster_users = [users[i] for i in indices]
        tracks.append([drivers_c[cluster]])

        nns, _ = get_4nn(drivers_c[cluster], cluster_users)

        for i in range(min(max_elements_per_cluster, len(cluster_users))):
            
            tracks[cluster].append(nns[i])
            cluster_users.remove(nns[i])
            drivers_c[cluster] = nns[i]
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
    
    return tracks