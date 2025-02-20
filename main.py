from greedy.greedy1 import greedy1
from kmeans.kmeans4 import kmeans4
from vrp.vrp3 import vrp3
from ls.ls1 import ls1
from ls.ls2 import ls2
from ls.ls3 import ls3
from utils import generatore, plot_all, plot_total, funzione_obiettivo

# Scegli istanza su cui eseguire: 1 = Piccola, 2 = Media, 3 = Grande
istanza = 2

if istanza == 1:
    # Piccola istanza
    tot_users = 20
    n_drivers = 3
    map_size = 50
elif istanza == 2:
    # Media istanza
    tot_users = 50
    n_drivers = 8
    map_size = 100
elif istanza == 3:
    # Grande istanza
    tot_users = 100
    n_drivers = 10
    map_size = 200
elif istanza == 4:
    # GIGA istanza
    tot_users = 1000
    n_drivers = 150
    map_size = 500

seed = None # Seed istanza da utilizzare (None = random)

# Generazione delle istanze
users, drivers, polo = generatore(tot_users, n_drivers, map_size, seed)

# GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Greedy
tracks_greedy = greedy1(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_greedy = funzione_obiettivo(tracks_greedy)
print(f"Funzione Obiettivo Greedy: {fo_greedy}")

#K KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
#Esecuzione algoritmo K-Means
tracks_kmeans = kmeans4(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_kmeans = funzione_obiettivo(tracks_kmeans)
print(f"Funzione Obiettivo K-Means: {fo_kmeans}")

# VRP
# Copia delle istanze originali
users1 = users.copy() 
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo VRP
tracks_vrp = vrp3(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_vrp = funzione_obiettivo(tracks_vrp)
print(f"Funzione Obiettivo VRP: {fo_vrp}")

# LOCAL SEARCH 1 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls1_greedy = ls1(users1, drivers1, polo1, tracks_greedy)
# Calcolo della funzione obiettivo
fo_ls1_greedy = funzione_obiettivo(tracks_ls1_greedy)
print(f"Funzione Obiettivo Local Search 1 Greedy: {fo_ls1_greedy}")

# LOCAL SEARCH 1 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls1_kmeans = ls1(users1, drivers1, polo1, tracks_kmeans)
# Calcolo della funzione obiettivo
fo_ls1_kmeans = funzione_obiettivo(tracks_ls1_kmeans)
print(f"Funzione Obiettivo Local Search 1 K-Means: {fo_ls1_kmeans}")

# LOCAL SEARCH 2 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls2_greedy = ls2(users1, drivers1, polo1, tracks_greedy)
# Calcolo della funzione obiettivo
fo_ls2_greedy = funzione_obiettivo(tracks_ls2_greedy)
print(f"Funzione Obiettivo Local Search 2 Greedy: {fo_ls2_greedy}")

# LOCAL SEARCH 2 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls2_kmeans = ls2(users1, drivers1, polo1, tracks_kmeans)
# Calcolo della funzione obiettivo
fo_ls2_kmeans = funzione_obiettivo(tracks_ls2_kmeans)
print(f"Funzione Obiettivo Local Search 2 K-Means: {fo_ls2_kmeans}")

# LOCAL SEARCH 3 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls3_greedy = ls3(users1, drivers1, polo1, tracks_greedy)
# Calcolo della funzione obiettivo
fo_ls3_greedy = funzione_obiettivo(tracks_ls3_greedy)
print(f"Funzione Obiettivo Local Search 3 Greedy: {fo_ls3_greedy}")

# LOCAL SEARCH 3 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls3_kmeans = ls3(users1, drivers1, polo1, tracks_kmeans)
# Calcolo della funzione obiettivo
fo_ls3_kmeans = funzione_obiettivo(tracks_ls3_kmeans)
print(f"Funzione Obiettivo Local Search 3 K-Means: {fo_ls3_kmeans}")

# plot_all("Greedy", tracks1, users, drivers, polo, map_size)
# plot_all("K-Means", tracks2, users, drivers, polo, map_size)
# plot_all("VRP3", tracks3, users, drivers, polo, map_size)

"""
plot_total(users, drivers, polo, map_size, [("Greedy - FO: " + str(fo_greedy), tracks_greedy),
                                  ("K-Means - FO: " + str(fo_kmeans), tracks_kmeans),
                                  ("VRP3 - FO: " + str(fo_vrp), tracks_vrp),
                                  ("LS1 Greedy - FO: " + str(fo_ls), tracks_ls),
                                  ("LS1 K-Means - FO: " + str(fo_ls_vrp), tracks_ls_vrp)])
"""

plot_total(users, drivers, polo, map_size, [("Greedy - FO: " + str(fo_greedy), tracks_greedy),
                                  ("K-Means - FO: " + str(fo_kmeans), tracks_kmeans),
                                  ("VRP - FO: " + str(fo_vrp), tracks_vrp),
                                  ("LS1 Greedy - FO: " + str(fo_ls1_greedy), tracks_ls1_greedy),
                                  ("LS1 K-Means - FO: " + str(fo_ls1_kmeans), tracks_ls1_kmeans),])

plot_total(users, drivers, polo, map_size, [("Greedy - FO: " + str(fo_greedy), tracks_greedy),
                                  ("K-Means - FO: " + str(fo_kmeans), tracks_kmeans),
                                  ("VRP - FO: " + str(fo_vrp), tracks_vrp),
                                  ("LS2 Greedy - FO: " + str(fo_ls2_greedy), tracks_ls2_greedy),
                                  ("LS2 K-Means - FO: " + str(fo_ls2_kmeans), tracks_ls2_kmeans)])

plot_total(users, drivers, polo, map_size, [("Greedy - FO: " + str(fo_greedy), tracks_greedy),
                                  ("K-Means - FO: " + str(fo_kmeans), tracks_kmeans),
                                  ("VRP - FO: " + str(fo_vrp), tracks_vrp),
                                  ("LS3 Greedy - FO: " + str(fo_ls3_greedy), tracks_ls3_greedy),
                                  ("LS3 K-Means - FO: " + str(fo_ls3_kmeans), tracks_ls3_kmeans)])

"""
plot_all("Greedy", tracks_greedy, users, drivers, polo, map_size)
plot_all("LS1 Greedy", tracks_ls, users, drivers, polo, map_size)
plot_all("VRP", tracks_vrp, users, drivers, polo, map_size)
plot_all("LS1 VRP", tracks_ls_vrp, users, drivers, polo, map_size)
"""