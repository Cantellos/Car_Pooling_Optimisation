from utils import funzione_obiettivo
from local_search.vlsn import vlsn

def msls(users, drivers, polo, base, n):

    best_msls_tracks = []
    best_msls_fo = 100000
    
    # Multi-start della Local Search n volte
    for i in range(n):

        # Scegli da quale euristica costruttiva iniziare
        if base == "greedy1":
            tracks = vlsn(users.copy(), drivers.copy(), polo.copy(), "greedy1")
        elif base == "greedy2":
            tracks = vlsn(users.copy(), drivers.copy(), polo.copy(), "greedy2")
        elif base == "kmeans":
            tracks = vlsn(users.copy(), drivers.copy(), polo.copy(), "kmeans")
        elif base == "random":
            tracks = vlsn(users.copy(), drivers.copy(), polo.copy(), "random")
            
        # Se la soluzione trovata è migliore, aggiorna la migliore soluzione trovata finora
        if funzione_obiettivo(tracks) <= best_msls_fo:
            best_msls_fo = funzione_obiettivo(tracks)
            best_msls_tracks = tracks.copy()

    return best_msls_tracks