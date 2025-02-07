import os
os.environ['OMP_NUM_THREADS'] = '4'
import matplotlib.pyplot as plt
import numpy as np
from greedy1 import your_greedy
from kmeans_ls import kmeans
from kmeans_ls2 import kmeans2
from utils import generatore, plot_graph, plot_all, funzione_obiettivo


users, drivers, polo = generatore(20, 3, 50, i)

users1, users2 = users.copy(), users.copy()
drivers1, drivers2 = drivers.copy(), drivers.copy()
polo1, polo2 = polo.copy(), polo.copy()

# tracks = your_greedy(users1, drivers1, polo1) #FO: 269.9
tracks = kmeans(users1, drivers1, polo1) # FO: 298.3
tracks2 = kmeans2(users2, drivers2, polo2) # FO: 261.2

#print(f"USERS: ", users1)
#print(f"DRIVERS: ", drivers1)

plot_all(tracks, users, drivers, polo)
plot_all(tracks2, users, drivers, polo)

print(f"Funzione Obiettivo Kmeans 1", funzione_obiettivo(tracks))
print(f"Funzione Obiettivo Kmeans 2", funzione_obiettivo(tracks2))
