from utils import distanza

def costo(track):
    c = 0
    for i in range(len(track)-1):
        c += distanza(track[i], track[i+1])
    return c

def ls1(drivers, users, polo, tracks):
    
    tracks_c = tracks.copy()
    best_tracks = tracks_c.copy()

    improved = True
    i=0
    while(improved):
        best_saving = 0
        improved = False

        # Mossa 1: Swap user di driver diversi
        for ext in range(len(tracks_c)):
            for int in range(ext+1, len(tracks_c)):
                for u_e in range(1, len(tracks_c[ext])-1):
                    for u_i in range(1, len(tracks_c[int])-1):

                        costo_track_before = costo(tracks_c[ext]) + costo(tracks_c[int])

                        #print(f"Track_ext: ", ext, ", el_ext: ", u_e, ", Track_int: ", int, ", el_int: ", u_i)
                        #print("Costo prima: ", costo_track_before)
                        
                        track1 = tracks_c[ext].copy()
                        track2 = tracks_c[int].copy()

                        track1[u_e], track2[u_i] = track2[u_i], track1[u_e]

                        costo_track_after = costo(track1) + costo(track2)

                        if costo_track_after < costo_track_before:
                            #print(f"Costo dopo: ",costo_track_after)
                            saving = costo_track_before - costo_track_after
                            #print("Saving: ", saving)

                            if saving > best_saving:
                                best_saving = saving
                                best_tracks = tracks_c.copy()
                                best_tracks.remove(tracks_c[ext])
                                best_tracks.append(track1)
                                best_tracks.remove(tracks_c[int])
                                best_tracks.append(track2)
                                #print("Best saving: ", best_saving)
                                improved = True
                                i += 1
        
        # Mossa 2: swap user liberi con user in macchina
        # Mossa 3: swap ordine user stessa macchina
        
        tracks_c = best_tracks

    print("Miglioramenti: ", i)
    return best_tracks