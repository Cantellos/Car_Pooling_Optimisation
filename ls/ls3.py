from utils import distanza, funzione_obiettivo
from greedy.greedy2 import greedy2
from kmeans.kmeans2 import kmeans2

def costo(track):
    c = 0
    for i in range(len(track)-1):
        c += distanza(track[i], track[i+1])
    return c

def ls3(users, drivers, polo, base):

    # Scegli da quale euristica costruttiva iniziare
    if base == "greedy":
        tracks = greedy2(users.copy(), drivers.copy(), polo.copy())
    elif base == "kmeans":
        tracks = kmeans2(users.copy(), drivers.copy(), polo.copy())

    tracks_c = tracks.copy()

    improved = True
    upgrades1=0

    excluded = []
    best_excluded = excluded.copy()

    for i in range(len(tracks_c)):
        if tracks_c[i][0] not in drivers and len(tracks_c[i])==2:
            excluded.append(tracks_c[i])

    while(improved):
        best_saving = 0
        improved = False

        # Mossa 1: swap user liberi con user in macchina
        best_tracks = tracks_c.copy()
        best_tracks1 = tracks_c.copy()
        upgrades1=0

        for t in range(len(tracks_c)):
            for elt in range(1, len(tracks_c[t])-1):

                exc = 0
                while(exc < len(excluded)):
                    
                    costo_track_before = costo(tracks_c[t]) + costo(excluded[exc])
                    
                    track1 = tracks_c[t].copy()
                    track2 = excluded[exc].copy()

                    track1[elt], track2[0] = track2[0], track1[elt]

                    costo_track_after = costo(track1) + costo(track2)
                    
                    if costo_track_after < costo_track_before:
                            saving = costo_track_before - costo_track_after

                            if saving > best_saving:
                                best_saving = saving
                                best_tracks = tracks_c.copy()
                                best_excluded = excluded.copy()

                                best_tracks.remove(tracks_c[t])
                                best_tracks.append(track1)
  
                                best_tracks.remove(excluded[exc])
                                best_tracks.append(track2)

                                best_excluded.remove(excluded[exc])
                                best_excluded.append(track2)

                                improved = True
                                upgrades1 += 1
                    
                    exc += 1

        best_tracks1 = best_tracks.copy()

        # Mossa 2: Swap user di driver diversi
        best_tracks = tracks_c.copy()
        best_tracks2 = tracks_c.copy()
        upgrades2 = 0

        for ext in range(len(tracks_c)):
            for ins in range(ext+1, len(tracks_c)):
                for u_e in range(1, len(tracks_c[ext])-1):
                    for u_i in range(1, len(tracks_c[ins])-1):

                        costo_track_before = costo(tracks_c[ext]) + costo(tracks_c[ins])
                        
                        track1 = tracks_c[ext].copy()
                        track2 = tracks_c[ins].copy()

                        track1[u_e], track2[u_i] = track2[u_i], track1[u_e]

                        costo_track_after = costo(track1) + costo(track2)

                        if costo_track_after < costo_track_before:

                            saving = costo_track_before - costo_track_after

                            if saving > best_saving:
                                best_saving = saving
                                best_tracks = tracks_c.copy()
                                best_tracks.remove(tracks_c[ext])
                                best_tracks.append(track1)
                                best_tracks.remove(tracks_c[ins])
                                best_tracks.append(track2)

                                improved = True
                                upgrades2 += 1

        best_tracks2 = best_tracks.copy()

        # Mossa 3: swap ordine user stessa macchina
        best_tracks = tracks_c.copy()
        best_tracks3 = tracks_c.copy()
        upgrades3 = 0

        for t in range(len(tracks_c)):
            for u1 in range(1, len(tracks_c[t])-1):
                for u2 in range(u1+1, len(tracks_c[t])-1):

                    costo_track_before = costo(tracks_c[t])

                    track1 = tracks_c[t].copy()

                    track1[u1], track1[u2] = track1[u2], track1[u1]

                    costo_track_after = costo(track1)

                    if costo_track_after < costo_track_before:
                        saving = costo_track_before - costo_track_after

                        if saving > best_saving:
                            best_saving = saving
                            best_tracks = tracks_c.copy()
                            best_tracks.remove(tracks_c[t])
                            best_tracks.append(track1)

                            improved = True
                            upgrades3 += 1

        best_tracks3 = best_tracks.copy()

        if funzione_obiettivo(best_tracks1) <= funzione_obiettivo(best_tracks2) and funzione_obiettivo(best_tracks1) <= funzione_obiettivo(best_tracks3):
            excluded = best_excluded.copy()
            tracks_c = best_tracks1
        elif funzione_obiettivo(best_tracks2) <= funzione_obiettivo(best_tracks1) and funzione_obiettivo(best_tracks2) <= funzione_obiettivo(best_tracks3):
            tracks_c = best_tracks2
        else:
            tracks_c = best_tracks3
          
    return tracks_c