import matplotlib.pyplot as plt
import numpy as np
from greedy1 import your_greedy
from kmeans_ls import kmeans
from kmeans_ls2 import kmeans
from utils import generatore, plot_graph, plot_all, funzione_obiettivo


users, drivers, polo = generatore(20, 3, 50, 2)

users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()

# tracks = your_greedy(users1, drivers1, polo1) #FO: 269.9
# tracks = kmeans(users1, drivers1, polo1) # FO: 302.0
tracks = kmeans(users1, drivers1, polo1) # FO: 261.2

print(f"USERS: ", users1)
print(f"DRIVERS: ", drivers1)
plot_all(tracks, users, drivers, polo)
print(f"Funzione Obiettivo", funzione_obiettivo(tracks))
