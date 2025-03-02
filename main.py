from greedy.greedy1 import greedy1
from greedy.greedy2 import greedy2
from greedy.greedy_random import greedy_random
from kmeans.kmeans1 import kmeans1
from kmeans.kmeans2 import kmeans2
from ls.ls import ls
from ls.vnd import vnd
from ls.vlsn import vlsn
from ls.msls import msls
from ga.ga1 import ga1
from utils import generatore, funzione_obiettivo, plot_2, plot_2_2, plot_all, plot_of, plot_2_2_base

# Scegli istanza su cui eseguire: 1 = Piccola, 2 = Media, 3 = Grande
istanza = 2

if istanza == 1:
    # Piccola istanza
    tot_users = 20
    n_drivers = 3
    map_size = 50
elif istanza == 2:
    # Media istanza
    tot_users = 60
    n_drivers = 9
    map_size = 200
elif istanza == 3:
    # Grande istanza
    tot_users = 300
    n_drivers = 50
    map_size = 500

seed = 4 # Seed istanza da utilizzare (None = random)

# Generazione delle istanze
users, drivers, polo = generatore(tot_users, n_drivers, map_size, seed)

# ------------------------- GREEDY ------------------------- 

# GREEDY RANDOM
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Greedy
tracks_greedy_random = greedy_random(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_greedy_random = round(funzione_obiettivo(tracks_greedy_random), 1)
print(f"Funzione Obiettivo Greedy 1: {fo_greedy_random}")

#plot_all("Greedy Random - FO: "+str(fo_greedy_random), tracks_greedy_random, users, drivers, polo, map_size)

# GREEDY 1
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Greedy
tracks_greedy1 = greedy1(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_greedy1 = round(funzione_obiettivo(tracks_greedy1), 1)
print(f"Funzione Obiettivo Greedy 1: {fo_greedy1}")

#plot_all("Greedy 1", tracks_greedy1, users, drivers, polo, map_size)

# GREEDY 2
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Greedy
tracks_greedy2 = greedy2(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_greedy2 = round(funzione_obiettivo(tracks_greedy2), 1)
print(f"Funzione Obiettivo Greedy 2: {fo_greedy2}")

#plot_all("Greedy 2", tracks_greedy2, users, drivers, polo, map_size)

#plot_2_2(users, drivers, polo, map_size, "GREEDY", "Greedy 1 - FO: "+str(fo_greedy1), tracks_greedy1, "Greedy 2- FO: "+str(fo_greedy2), tracks_greedy2)

plot_2_2_base(users, drivers, polo, map_size, "GREEDY", 
        tracks_row=[("Greedy Random - FO: " + str(fo_greedy_random), tracks_greedy_random)],
        tracks_col=[("Greedy 1 - FO: " + str(fo_greedy1), tracks_greedy1), ("Greedy 2 - FO: " + str(fo_greedy2), tracks_greedy2)])

# ------------------------- K-MEANS ------------------------- 

# K-MEANS 1
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
#Esecuzione algoritmo K-Means
tracks_kmeans1 = kmeans1(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_kmeans1 = round(funzione_obiettivo(tracks_kmeans1), 1)
print(f"Funzione Obiettivo K-Means 1: {fo_kmeans1}")

#plot_all("K-Means 1", tracks_kmeans1, users, drivers, polo, map_size)

# K-MEANS 2
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
#Esecuzione algoritmo K-Means
tracks_kmeans2 = kmeans2(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_kmeans2 = round(funzione_obiettivo(tracks_kmeans2), 1)
print(f"Funzione Obiettivo K-Means 2: {fo_kmeans2}")

#plot_all("K-Means 2", tracks_kmeans2, users, drivers, polo, map_size)

plot_2(users, drivers, polo, map_size, "K-MEANS", "K-Means 1 - FO: "+str(fo_kmeans1), tracks_kmeans1, "K-Means 2- FO: "+str(fo_kmeans2), tracks_kmeans2)

# ------------------------- LOCAL SEARCH 1 ------------------------- 

# LOCAL SEARCH 1 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls_greedy = ls(users1, drivers1, polo1, "greedy1")
# Calcolo della funzione obiettivo
fo_ls_greedy = round(funzione_obiettivo(tracks_ls_greedy), 1)
print(f"Funzione Obiettivo Local Search Greedy: {fo_ls_greedy}")

#plot_all("Local Search 1 Greedy", tracks_ls_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 1 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls_kmeans = ls(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_ls_kmeans = round(funzione_obiettivo(tracks_ls_kmeans), 1)
print(f"Funzione Obiettivo Local Search K-Means: {fo_ls_kmeans}")

#plot_all("Local Search 1 K-Means", tracks_ls_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 1", 
        tracks_row=[("Greedy 1 - FO: " + str(fo_greedy1), tracks_greedy1), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("LS Greedy 1 - FO: " + str(fo_ls_greedy), tracks_ls_greedy), ("LS K-Means 2 - FO: " + str(fo_ls_kmeans), tracks_ls_kmeans)])

# ------------------------- LOCAL SEARCH 2 ------------------------- 

# LOCAL SEARCH 2 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_vnd_greedy = vnd(users1, drivers1, polo1, "greedy1")
# Calcolo della funzione obiettivo
fo_vnd_greedy = round(funzione_obiettivo(tracks_vnd_greedy), 1)
print(f"Funzione Obiettivo Variable Neighborhood Descent Greedy: {fo_vnd_greedy}")

#plot_all("Local Search 2 Greedy", tracks_vnd_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 2 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_vnd_kmeans = vnd(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_vnd_kmeans = round(funzione_obiettivo(tracks_vnd_kmeans), 1)
print(f"Funzione Obiettivo Variable Neighborhood Descent K-Means: {fo_vnd_kmeans}")

#plot_all("Local Search 2 K-Means", tracks_vnd_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 2", 
        tracks_row=[("Greedy 1 - FO: " + str(fo_greedy1), tracks_greedy1), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("VND Greedy - FO: " + str(fo_vnd_greedy), tracks_vnd_greedy), ("VND K-Means - FO: " + str(fo_vnd_kmeans), tracks_vnd_kmeans)])

# ------------------------- LOCAL SEARCH 3 ------------------------- 

# LOCAL SEARCH 3 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_vlsn_greedy = vlsn(users1, drivers1, polo1, "greedy1")
# Calcolo della funzione obiettivo
fo_vlsn_greedy = round(funzione_obiettivo(tracks_vlsn_greedy), 1)
print(f"Funzione Obiettivo Very Large Size Neighborhood Search Greedy: {fo_vlsn_greedy}")

#plot_all("Local Search 3 Greedy", tracks_vlsn_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 3 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_vlsn_kmeans = vlsn(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_vlsn_kmeans = round(funzione_obiettivo(tracks_vlsn_kmeans), 1)
print(f"Funzione Obiettivo Very Large Size Neighborhood Search K-Means: {fo_vlsn_kmeans}")

#plot_all("Local Search 3 K-Means", tracks_vlsn_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 3", 
        tracks_row=[("Greedy 1 - FO: " + str(fo_greedy1), tracks_greedy1), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("VLSN Greedy - FO: " + str(fo_vlsn_greedy), tracks_vlsn_greedy), ("VLSN K-Means - FO: " + str(fo_vlsn_kmeans), tracks_vlsn_kmeans)])

# ------------------------- MULTI START LOCAL SEARCH ------------------------- 

# MULTI START LOCAL SEARCH - GREEDY RANDOM
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_msls_greedy_random = msls(users1, drivers1, polo1, "random", 10)
# Calcolo della funzione obiettivo
fo_msls_greedy_random = round(funzione_obiettivo(tracks_msls_greedy_random), 1)
print(f"Funzione Obiettivo Multi Start Local Search Greedy Random: {fo_msls_greedy_random}")

# MULTI START LOCAL SEARCH - GREEDY 1
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_msls_greedy1 = msls(users1, drivers1, polo1, "greedy1", 10)
# Calcolo della funzione obiettivo
fo_msls_greedy1 = round(funzione_obiettivo(tracks_msls_greedy1), 1)
print(f"Funzione Obiettivo Multi Start Local Search Greedy 1: {fo_msls_greedy1}")

# MULTI START LOCAL SEARCH - GREEDY 2
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_msls_greedy2 = msls(users1, drivers1, polo1, "greedy2", 10)
# Calcolo della funzione obiettivo
fo_msls_greedy2 = round(funzione_obiettivo(tracks_msls_greedy2), 1)
print(f"Funzione Obiettivo Multi Start Local Search Greedy 2: {fo_msls_greedy2}")

# MULTI START LOCAL SEARCH - K-MEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_msls_kmeans = msls(users1, drivers1, polo1, "kmeans", 10)
# Calcolo della funzione obiettivo
fo_msls_kmeans = round(funzione_obiettivo(tracks_msls_kmeans), 1)
print(f"Funzione Obiettivo Multi Start Local Search K-Means: {fo_msls_kmeans}")

plot_2_2(users, drivers, polo, map_size, "MULTI START LOCAL SEARCH", 
        tracks_row=[("MSLS VLSN Greedy Random - FO: " + str(fo_msls_greedy_random), tracks_msls_greedy_random), ("MSLS VLSN Greedy 1 - FO: " + str(fo_msls_greedy1), tracks_msls_greedy1)],
        tracks_col=[("MSLS VLSN Greedy 2 - FO: " + str(fo_msls_greedy2), tracks_msls_greedy2), ("MSLS VLSN K-Means - FO: " + str(fo_msls_kmeans), tracks_msls_kmeans)])

# ------------------------- GENETIC ALGORITHM ------------------------- 

# GENETIC ALGORITHM - GREEDY RANDOM
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ga1_greedyrandom = ga1(users1, drivers1, polo1, "random")
# Calcolo della funzione obiettivo
fo_ga1_greedyrandom = round(funzione_obiettivo(tracks_ga1_greedyrandom), 1)
print(f"Funzione Obiettivo Genetic Algorithm Greedy Random: {fo_ga1_greedyrandom}")

# GENETIC ALGORITHM - GREEDY 1
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ga1_greedy1 = ga1(users1, drivers1, polo1, "greedy1")
# Calcolo della funzione obiettivo
fo_ga1_greedy1 = round(funzione_obiettivo(tracks_ga1_greedy1), 1)
print(f"Funzione Obiettivo Genetic Algorithm Greedy 1: {fo_ga1_greedy1}")

# GENETIC ALGORITHM - GREEDY 2
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ga1_greedy2 = ga1(users1, drivers1, polo1, "greedy2")
# Calcolo della funzione obiettivo
fo_ga1_greedy2 = round(funzione_obiettivo(tracks_ga1_greedy2), 1)
print(f"Funzione Obiettivo Genetic Algorithm Greedy 2: {fo_ga1_greedy2}")

# GENETIC ALGORITHM - K-MEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ga1_kmeans = ga1(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_ga1_kmeans = round(funzione_obiettivo(tracks_ga1_kmeans), 1)
print(f"Funzione Obiettivo Genetic Algorithm K-Means: {fo_ga1_kmeans}")

plot_2_2(users, drivers, polo, map_size, "GENETIC ALGORITHM", 
        tracks_row=[("Genetic Algorithm Greedy Random - FO: " + str(fo_ga1_greedyrandom), tracks_ga1_greedyrandom), ("Genetic Algorithm Greedy 1 - FO: " + str(fo_ga1_greedy1), tracks_ga1_greedy1)],
        tracks_col=[("Genetic Algorithm Greedy 2 - FO: " + str(fo_ga1_greedy2), tracks_ga1_kmeans), ("Genetic Algorithm K-Means - FO: " + str(fo_ga1_kmeans), tracks_ga1_kmeans)])

# ------------------------- FINAL RESULTS -------------------------

plot_of([("Greedy Random", fo_greedy_random), ("Greedy 1", fo_greedy1), ("Greedy 2", fo_greedy2), ("K-Means 1", fo_kmeans1), ("K-Means 2", fo_kmeans2),
        ("LS Greedy", fo_ls_greedy), ("LS K-Means", fo_ls_kmeans), ("VND Greedy", fo_vnd_greedy), ("VND K-Means", fo_vnd_kmeans),
        ("VLSN Greedy", fo_vlsn_greedy), ("VLSN K-Means", fo_vlsn_kmeans), ("MSLS Greedy", fo_msls_greedy1), ("MSLS K-Means", fo_msls_kmeans),
        ("GA Greedy Random", fo_ga1_greedyrandom), ("GA Greedy 1", fo_ga1_greedy1), ("GA Greedy 2", fo_ga1_greedy2), ("GA K-Means", fo_ga1_kmeans)])
