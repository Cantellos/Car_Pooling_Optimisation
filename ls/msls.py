from utils import funzione_obiettivo
from ls.ls3 import ls3

def msls(users, drivers, polo, base, n):

    best_msls_tracks = []
    best_msls_fo = 100000
    
    # Multi-start della Local Search n volte
    for i in range(n):

        # Scegli da quale euristica costruttiva iniziare
        if base == "greedy":
            tracks = ls3(users.copy(), drivers.copy(), polo.copy(), "greedy")
        elif base == "kmeans":
            tracks = ls3(users.copy(), drivers.copy(), polo.copy(), "kmeans")
        
        # Se la soluzione trovata è migliore, aggiorna la migliore soluzione trovata finora
        if funzione_obiettivo(tracks) <= best_msls_fo:
            best_msls_fo = funzione_obiettivo(tracks)
            best_msls_tracks = tracks.copy()

    return best_msls_tracks