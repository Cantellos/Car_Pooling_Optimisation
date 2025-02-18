from greedy1 import greedy1
from kmeans4 import kmeans4
from vrp3 import vrp3
from ls1 import ls1
from utils import generatore, plot_all, funzione_obiettivo

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
k = 6 # Numero di algoritmi da eseguire
users_list = [users.copy() for _ in range(k)]
drivers_list = [drivers.copy() for _ in range(k)]
polo_list = [polo.copy() for _ in range(k)]

# Salvataggio nelle variabili utilizzate dagli algoritmi
users1, users2, users3, users4, users5, users6 = users_list
drivers1, drivers2, drivers3, drivers4, drivers5, drivers6 = drivers_list
polo1, polo2, polo3, polo4, polo5, polo6 = polo_list

# Esecuzione degli algoritmi (FO: = Funzione Obiettivo relativa a istanza con seed=2)
# Greedy
# tracks1 = greedy1(users1, drivers1, polo1) #FO: 269.9
# K-Means
# tracks2 = kmeans4(users2, drivers2, polo2) # FO: 257.7
# VRP
tracks3 = vrp3(users3, drivers3, polo3) # FO: 254.1
# Local Search
tracks4 = ls1(users4, drivers4, polo4, tracks3) # FO: 244.7

# print(f"Funzione Obiettivo Greedy ", funzione_obiettivo(tracks1))
# print(f"Funzione Obiettivo Kmeans ", funzione_obiettivo(tracks2))
print(f"Funzione Obiettivo VRP3", funzione_obiettivo(tracks3))
print(f"Funzione Obiettivo LS1", funzione_obiettivo(tracks4))

# plot_all("Greedy", tracks1, users, drivers, polo, map_size)
# plot_all("K-Means", tracks2, users, drivers, polo, map_size)
plot_all("VRP3", tracks3, users, drivers, polo, map_size)
plot_all("LS1", tracks4, users, drivers, polo, map_size)
