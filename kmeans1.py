from utils import distanza
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# PRENDE I 4 VICINI PIU' VICINI DI UN DRIVER

def get_4nn(driver, cusers):
    # trova i 4 vicini più vicini
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
    
# TODO: Randomizzare l'ordine dei driver nel kmeans per evitare che il primo driver abbia sempre i migliori vicini

def kmeans1(users, drivers, polo):
    # Applichiamo K-Means con n. driver clusters
    kmeans = KMeans(n_clusters=len(drivers), n_init=1, init=np.array(drivers))
    # fit di kmeans su users e drivers
    X = np.array(users)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    
    tracks = []

    # Limitiamo il numero di elementi in ogni cluster
    max_elements_per_cluster = 4
    cluster_counts = np.bincount(y_kmeans) # Conta il numero di elementi per cluster
    for cluster in range(len(drivers)):            
        # Trovo gli elementi del cluster
        indices = np.where(y_kmeans == cluster)[0]
        cluster_users = [users[i] for i in indices]
        tracks.append([drivers[cluster]])

        nns, _ = get_4nn(drivers[cluster], cluster_users)

        for i in range(min(max_elements_per_cluster, len(cluster_users))):
            
            tracks[cluster].append(nns[i])
            cluster_users.remove(nns[i])
            drivers[cluster] = nns[i]
        tracks[cluster].append(polo)

        excluded = []
                
        # Indici di quelli da eliminare
        for cluser in cluster_users:
            excluded.append(users.index(cluser))

        # Riassegna gli elementi esclusi al prossimo cluster
        for idx in excluded:
            y_kmeans[idx] += 1
    

    # Visualizziamo i risultati
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', edgecolor='k', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
    plt.title("Clustering con K-Means")
    plt.show()

    # aggiungiamo gli users che non sono stati assegnati
    for i in range(len(X)):
        if y_kmeans[i] == len(drivers):
            tracks.append([X[i].tolist(), polo])
    
    return tracks