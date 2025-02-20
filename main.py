from greedy.greedy1 import greedy1
from greedy.greedy2 import greedy2
from kmeans.kmeans1 import kmeans1
from kmeans.kmeans2 import kmeans2
from ls.ls1 import ls1
from ls.ls2 import ls2
from ls.ls3 import ls3
from ls.msls import msls
from utils import generatore, funzione_obiettivo, plot_2, plot_2_2, plot_all

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

seed = None # Seed istanza da utilizzare (None = random)

# Generazione delle istanze
users, drivers, polo = generatore(tot_users, n_drivers, map_size, seed)

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

plot_2(users, drivers, polo, map_size, "GREEDY", "Greedy 1 - FO: "+str(fo_greedy1), tracks_greedy1, "Greedy 2- FO: "+str(fo_greedy2), tracks_greedy2)

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

# LOCAL SEARCH 1 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls1_greedy = ls1(users1, drivers1, polo1, "greedy")
# Calcolo della funzione obiettivo
fo_ls1_greedy = round(funzione_obiettivo(tracks_ls1_greedy), 1)
print(f"Funzione Obiettivo Local Search 1 Greedy: {fo_ls1_greedy}")

#plot_all("Local Search 1 Greedy", tracks_ls1_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 1 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls1_kmeans = ls1(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_ls1_kmeans = round(funzione_obiettivo(tracks_ls1_kmeans), 1)
print(f"Funzione Obiettivo Local Search 1 K-Means: {fo_ls1_kmeans}")

#plot_all("Local Search 1 K-Means", tracks_ls1_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 1", 
        tracks_row=[("Greedy 2 - FO: " + str(fo_greedy2), tracks_greedy2), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("LS1 Greedy - FO: " + str(fo_ls1_greedy), tracks_ls1_greedy), ("LS1 K-Means - FO: " + str(fo_ls1_kmeans), tracks_ls1_kmeans)])

# LOCAL SEARCH 2 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls2_greedy = ls2(users1, drivers1, polo1, "greedy")
# Calcolo della funzione obiettivo
fo_ls2_greedy = round(funzione_obiettivo(tracks_ls2_greedy), 1)
print(f"Funzione Obiettivo Local Search 2 Greedy: {fo_ls2_greedy}")

#plot_all("Local Search 2 Greedy", tracks_ls2_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 2 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls2_kmeans = ls2(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_ls2_kmeans = round(funzione_obiettivo(tracks_ls2_kmeans), 1)
print(f"Funzione Obiettivo Local Search 2 K-Means: {fo_ls2_kmeans}")

#plot_all("Local Search 2 K-Means", tracks_ls2_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 2", 
        tracks_row=[("Greedy 2 - FO: " + str(fo_greedy2), tracks_greedy2), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("LS2 Greedy - FO: " + str(fo_ls2_greedy), tracks_ls2_greedy), ("LS2 K-Means - FO: " + str(fo_ls2_kmeans), tracks_ls2_kmeans)])

# LOCAL SEARCH 3 - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls3_greedy = ls3(users1, drivers1, polo1, "greedy")
# Calcolo della funzione obiettivo
fo_ls3_greedy = round(funzione_obiettivo(tracks_ls3_greedy), 1)
print(f"Funzione Obiettivo Local Search 3 Greedy: {fo_ls3_greedy}")

#plot_all("Local Search 3 Greedy", tracks_ls3_greedy, users, drivers, polo, map_size)

# LOCAL SEARCH 3 - KMEANS
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls3_kmeans = ls3(users1, drivers1, polo1, "kmeans")
# Calcolo della funzione obiettivo
fo_ls3_kmeans = round(funzione_obiettivo(tracks_ls3_kmeans), 1)
print(f"Funzione Obiettivo Local Search 3 K-Means: {fo_ls3_kmeans}")

#plot_all("Local Search 3 K-Means", tracks_ls3_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "LOCAL SEARCH 3", 
        tracks_row=[("Greedy 2 - FO: " + str(fo_greedy2), tracks_greedy2), ("K-Means 2 - FO: " + str(fo_kmeans2), tracks_kmeans2)], 
        tracks_col=[("LS3 Greedy - FO: " + str(fo_ls3_greedy), tracks_ls3_greedy), ("LS3 K-Means - FO: " + str(fo_ls3_kmeans), tracks_ls3_kmeans)])

# MULTI START LOCAL SEARCH - GREEDY
# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_msls_greedy = msls(users1, drivers1, polo1, "greedy", 10)
# Calcolo della funzione obiettivo
fo_msls_greedy = round(funzione_obiettivo(tracks_msls_greedy), 1)
print(f"Funzione Obiettivo Multi Start Local Search Greedy: {fo_msls_greedy}")

#plot_all("Multi Start Local Search - Greedy", tracks_msls_greedy, users, drivers, polo, map_size)

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

#plot_all("Multi Start Local Search - K-Means", tracks_msls_kmeans, users, drivers, polo, map_size)

plot_2_2(users, drivers, polo, map_size, "MULTI START LOCAL SEARCH", 
        tracks_row=[("LS3 Greedy - FO: " + str(fo_ls3_greedy), tracks_ls3_greedy), ("LS3 K-Means - FO: " + str(fo_ls3_kmeans), tracks_ls3_kmeans)],
        tracks_col=[("MSLS LS3 Greedy - FO: " + str(fo_msls_greedy), tracks_msls_greedy), ("MSLS LS3 Greedy - FO: " + str(fo_msls_kmeans), tracks_msls_kmeans)])