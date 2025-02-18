from greedy1 import greedy1
from kmeans4 import kmeans4
from vrp3 import vrp3
from ls1 import ls1
from utils import generatore, plot_all, plot_total, funzione_obiettivo

# Scegli istanza su cui eseguire: 1 = Piccola, 2 = Media, 3 = Grande
istanza = 1

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
    n_drivers = 18
    map_size = 200

seed = 2 # Seed istanza da utilizzare (None = random)

# Generazione delle istanze
users, drivers, polo = generatore(tot_users, n_drivers, map_size, seed)

# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Greedy
tracks_greedy = greedy1(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_greedy = round(funzione_obiettivo(tracks_greedy),1)
print(f"Funzione Obiettivo Greedy: {fo_greedy}")

# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
#Esecuzione algoritmo K-Means
tracks_kmeans = kmeans4(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_kmeans = round(funzione_obiettivo(tracks_kmeans),1)
print(f"Funzione Obiettivo K-Means: {fo_kmeans}")

# Copia delle istanze originali
users1 = users.copy() 
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo VRP
tracks_vrp = vrp3(users1, drivers1, polo1)
# Calcolo della funzione obiettivo
fo_vrp = round(funzione_obiettivo(tracks_vrp),1)
print(f"Funzione Obiettivo VRP: {fo_vrp}")

# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con Greedy
tracks_ls = ls1(users1, drivers1, polo1, tracks_greedy)
# Calcolo della funzione obiettivo
fo_ls = round(funzione_obiettivo(tracks_ls),1)
print(f"Funzione Obiettivo Local Search: {fo_ls}")

# Copia delle istanze originali
users1 = users.copy()
drivers1 = drivers.copy()
polo1 = polo.copy()
# Esecuzione algoritmo Local Search con VRP
tracks_ls_vrp = ls1(users1, drivers1, polo1, tracks_vrp)
# Calcolo della funzione obiettivo
fo_ls_vrp = round(funzione_obiettivo(tracks_ls_vrp),1)
print(f"Funzione Obiettivo Local Search VRP: {fo_ls_vrp}")

# plot_all("Greedy", tracks1, users, drivers, polo, map_size)
# plot_all("K-Means", tracks2, users, drivers, polo, map_size)
# plot_all("VRP3", tracks3, users, drivers, polo, map_size)
# plot_all("LS1", tracks4, users, drivers, polo, map_size)

plot_total(users, drivers, polo, map_size, [("Greedy - FO: " + str(fo_greedy), tracks_greedy),
                                  ("K-Means - FO: " + str(fo_kmeans), tracks_kmeans),
                                  ("VRP3 - FO: " + str(fo_vrp), tracks_vrp),
                                  ("LS1 - FO: " + str(fo_ls), tracks_ls),
                                  ("LS1 VRP - FO: " + str(fo_ls_vrp), tracks_ls_vrp)])
