import os
#os.environ['OMP_NUM_THREADS'] = '4'
import matplotlib.pyplot as plt
import numpy as np
from greedy1 import greedy1
from kmeans1 import kmeans1
from kmeans2 import kmeans2
from kmeans3 import kmeans3
from kmeans4 import kmeans4
from vrp1 import vrp1
from vrp2 import vrp2
from vrp3 import vrp3
from ls1 import ls1
from utils import generatore, plot_graph, plot_all, funzione_obiettivo


# Piccola istanza
tot_users_p = 20
n_drivers_p = 3
map_size_p = 50

# Media istanza
tot_users_m = 50
n_drivers_m = 8
map_size_m = 100

# Grande istanza
tot_users_g = 100
n_drivers_g = 18
map_size_g = 200

seed = None

# Seleziona l'istanza da utilizzare
tot_users = tot_users_m
n_drivers = n_drivers_m
map_size = map_size_m

# Generazione delle istanze
#users, drivers, polo = generatore(tot_users_p, n_drivers_p, map_size_p, seed) # Piccola istanza
users, drivers, polo = generatore(tot_users, n_drivers, map_size, seed) # Media istanza
#users, drivers, polo = generatore(tot_users_g, n_drivers_g, map_size_g, seed) # Grande istanza


# Memorizzazione delle istanze originali
users3, users4, users5 = users.copy(), users.copy(), users.copy()
drivers3, drivers4, drivers5 = drivers.copy(), drivers.copy(), drivers.copy()
polo3, polo4, polo5 = polo.copy(), polo.copy(), polo.copy()

users6 = users.copy()
drivers6 = drivers.copy()
polo6 = polo.copy()

# Esecuzione degli algoritmi

# tracks_greedy = your_greedy(users1, drivers1, polo1) #FO: 269.9
tracks1 = kmeans1(users4, drivers4, polo4) # FO: 298.3
# tracks2 = kmeans2(users2, drivers2, polo2) # FO: 261.2
# tracks3 = kmeans3(users3, drivers3, polo3) # FO: 261.2
# tracks4 = kmeans4(users4, drivers4, polo4) # FO: 257.7
# tracks6 = vrp3(users5, drivers5, polo5) # FO: 254.1
tracks7 = ls1(users5, drivers5, polo5, tracks1) # FO: 254.1

#print(f"Funzione Obiettivo Kmeans 1", funzione_obiettivo(tracks))
#print(f"Funzione Obiettivo Kmeans 3", funzione_obiettivo(tracks3))
#print(f"Funzione Obiettivo Kmeans 4", funzione_obiettivo(tracks4))
print(f"Funzione Obiettivo VRP3", funzione_obiettivo(tracks1))
print(f"Funzione Obiettivo LS1", funzione_obiettivo(tracks7))

#plot_all("K-Means 3", tracks3, users, drivers, polo, map_size)
#plot_all("K-Means 4", tracks4, users, drivers, polo, map_size)
plot_all("VRP3", tracks1, users, drivers, polo, map_size)
plot_all("LS1", tracks7, users, drivers, polo, map_size)
