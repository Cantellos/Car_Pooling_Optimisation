from utils import distanza
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_4_nn(driver, cusers):
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
    

def kmeans(users, drivers, polo):
    # Applichiamo K-Means con n. driver clusters
    kmeans = KMeans(n_clusters=len(drivers), n_init=1, init=np.array(drivers))
    # fit di kmeans su users e drivers
    X = np.array(users)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    print(f"users: ",users)
    print(f"Y_KMEANS: ",y_kmeans)

    
    # Limitiamo il numero di elementi in ogni cluster
    max_elements_per_cluster = 4
    cluster_counts = np.bincount(y_kmeans) # Conta il numero di elementi per cluster
    excluded = []
    for cluster in range(len(drivers)):
        if cluster_counts[cluster] > max_elements_per_cluster:

            indices = np.where(y_kmeans == cluster)[0]
            cluster_users = [users[i] for i in indices]

            print(f"CLUSTER USERS: ",cluster_users)
            print(f"DRIVER: ",drivers[cluster])

            nns, _ = get_4_nn(drivers[cluster], cluster_users)
            print(f"NN: ",nns)
                    
            # Indici di quelli da eliminare
            for cluser in cluster_users:
                if cluser not in nns:
                    excluded.append(users.index(cluser))

    for idx in excluded:
        y_kmeans[idx] = -1  # Assign to an invalid cluster
        
    """
    # Limit the number of elements in each cluster
    max_elements_per_cluster = 4
    cluster_counts = np.bincount(y_kmeans) # Conta il numero di elementi per cluster
    for cluster in range(len(drivers)):
        if cluster_counts[cluster] > max_elements_per_cluster:
            indices = np.where(y_kmeans == cluster)[0]
            #for i in range(cluster_counts[cluster]):
               # if y_kmeans[i] == cluster:
                 #   indices.append(X[i])
                
            print(f"Y_KMEANS = ",y_kmeans)
            print(f"CLUSTER: ",cluster)
            print(f"INDICES: ",indices)
            print(f"INDIC[0]: ",X[indices[0]])

            print(f"DRIVER: ",drivers[cluster])
            print(X)

            for indice in indices:
              print(f"NN:", get_nn(drivers[cluster], [X[indice][0], X[indice][1]] ))

            np.random.shuffle(indices)
            for idx in indices[max_elements_per_cluster:]:
                y_kmeans[idx] = -1  # Assign to an invalid cluster
    """

    # Visualizziamo i risultati
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', edgecolor='k', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X', label='Centroidi')
    plt.title("Clustering con K-Means")
    plt.legend()
    plt.show()
    
    # Creiamo le tracce
    tracks = []
    for i in range(len(drivers)):
        tracks.append([drivers[i]])
        for j in range(len(X)):
            if y_kmeans[j] == i:
                tracks[i].append(X[j].tolist())
        tracks[i].append(polo)

    # aggiungiamo gli users che non sono stati assegnati
    for i in range(len(X)):
        if y_kmeans[i] == -1:
            tracks.append([X[i].tolist(), polo])
    
    return tracks