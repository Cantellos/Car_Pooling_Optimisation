import numpy as np
import matplotlib.pyplot as plt

# Generatore di istanze casuali
def generatore (tot_utenti, n_driver, map_size, seed=None):
    if seed is not None:
        np.random.seed(seed)

    users=[]
    drivers=[]
    polo = [0, 0]

    limit = (int)(map_size/2)
    for i in range(tot_utenti-n_driver):
            users.append([np.random.randint(-limit,limit),np.random.randint(-limit,limit)])
            
    for i in range(n_driver):
        drivers.append([np.random.randint(-limit,limit),np.random.randint(-limit,limit)])

    return users, drivers, polo


# Distanza Euclidea
def distanza(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


# Funzione obiettivo = somma lunghezza totale di ogni percorso
def funzione_obiettivo(tracks):
    lunghezza_totale = 0
    for track in tracks:
        lunghezza = 0
        for i in range(1, len(track)):
            lunghezza += distanza(track[i-1], track[i])
        lunghezza_totale += lunghezza

    return lunghezza_totale


def plot_graph(users, drivers, polo):
    plt.figure(figsize=(8, 8))

    xu, yu = zip(*users)
    plt.scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    plt.scatter(xd, yd, color='blue', marker='o')
    
    plt.scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    plt.axhline(0, color='black', linewidth=1)  # Asse X
    plt.axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)

    # Aggiungi etichette e griglia
    plt.xlabel("Asse X")
    plt.ylabel("Asse Y")
    plt.grid(True)
    plt.title("Visualizzazione di punti nel piano cartesiano")

    # Mostra il grafico
    plt.show()


def plot_all(title, tracks, users, drivers, polo, map_size):
    # due grafici affiancati
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    fig.suptitle(title)

    # grafico 1
    xu, yu = zip(*users)

    axs[0].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[0].scatter(xd, yd, color='blue', marker='o')
    
    axs[0].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[0].axhline(0, color='black', linewidth=1)  # Asse X
    axs[0].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[0].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[0].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)
    
    # Aggiungi etichette e griglia
    axs[0].set_xlabel("Asse X")
    axs[0].set_ylabel("Asse Y")
    axs[0].grid(True)

    # grafico 2
    for track in tracks:
        x, y = zip(*track)
        # plot di un percorso indicato con una freccia
        axs[1].plot(x, y, marker='o')

    axs[1].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[1].scatter(xd, yd, color='blue', marker='o')

    axs[1].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[1].axhline(0, color='black', linewidth=1)  # Asse X
    axs[1].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[1].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[1].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

    # Aggiungi etichette e griglia
    axs[1].set_xlabel("Asse X")
    axs[1].set_ylabel("Asse Y")
    axs[1].grid(True)

    # Mostra il grafico
    plt.show()


def plot_total(users, drivers, polo, map_size, tracks_all):
    # Numero di righe e 3 colonne pari al numero di grafici da visualizzare (tranne il primo)
    rows = (int)((len(tracks_all)+1)/3)
    cols = 3

    fig, axs = plt.subplots(rows, cols, figsize=(18, 10))

    fig.suptitle("Risultati ottenuti")

    # Grafico 1
    xu, yu = zip(*users)

    axs[0][0].set_title("Istanza generata")

    axs[0][0].scatter(xu, yu, color='green', marker='o')

    xd, yd = zip(*drivers)
    axs[0][0].scatter(xd, yd, color='blue', marker='o')
    
    axs[0][0].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[0][0].axhline(0, color='black', linewidth=1)  # Asse X
    axs[0][0].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[0][0].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[0][0].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)
    
    # Aggiungi etichette e griglia
    axs[0][0].set_xlabel("Asse X")
    axs[0][0].set_ylabel("Asse Y")
    axs[0][0].grid(True)

    titles, tracks_list = zip(*tracks_all)

    for i, tracks in enumerate(tracks_list):
        pos_x = (int)((i+1)/cols)
        pos_y = (int)((i+1)%cols)

        axs[pos_x][pos_y].set_title(titles[i])

        for track in tracks:
            x, y = zip(*track)
            axs[pos_x][pos_y].plot(x, y, marker='o')
        axs[pos_x][pos_y].scatter(xu, yu, color='green', marker='o')

        xd, yd = zip(*drivers)
        axs[pos_x][pos_y].scatter(xd, yd, color='blue', marker='o')

        axs[pos_x][pos_y].scatter(polo[0], polo[1], color='red', marker='o')

        # Aggiungi assi cartesiani centrati in (0,0)
        axs[pos_x][pos_y].axhline(0, color='black', linewidth=1)  # Asse X
        axs[pos_x][pos_y].axvline(0, color='black', linewidth=1)  # Asse Y

        # Imposta i limiti fissi per gli assi
        axs[pos_x][pos_y].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
        axs[pos_x][pos_y].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

        # Aggiungi etichette e griglia
        axs[pos_x][pos_y].set_xlabel("Asse X")
        axs[pos_x][pos_y].set_ylabel("Asse Y")
        axs[pos_x][pos_y].grid(True)

    # Mostra il grafico
    plt.show()

def plot_2(users, drivers, polo, map_size, title, title1, tracks1, title2, tracks2):
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))

    fig.suptitle(title)

    for track in tracks1:
        x, y = zip(*track)
        # plot di un percorso
        axs[0].plot(x, y, marker='o')

    axs[0].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[0].axhline(0, color='black', linewidth=1)  # Asse X
    axs[0].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[0].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[0].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

    # Aggiungi titolo, etichette e griglia
    axs[0].set_title(title1)
    axs[0].set_xlabel("Asse X")
    axs[0].set_ylabel("Asse Y")
    axs[0].grid(True)


    for track in tracks2:
        x, y = zip(*track)
        # plot di un percorso
        axs[1].plot(x, y, marker='o')

    axs[1].scatter(polo[0], polo[1], color='red', marker='o')

    # Aggiungi assi cartesiani centrati in (0,0)
    axs[1].axhline(0, color='black', linewidth=1)  # Asse X
    axs[1].axvline(0, color='black', linewidth=1)  # Asse Y

    # Imposta i limiti fissi per gli assi
    axs[1].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
    axs[1].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

    # Aggiungi etichette e griglia
    axs[1].set_xlabel("Asse X")
    axs[1].set_ylabel("Asse Y")
    axs[1].set_title(title2)
    axs[1].grid(True)

    # Mostra il grafico
    plt.show()

def plot_2_2(users, drivers, polo, map_size, title, tracks_row, tracks_col):
    fig, axs = plt.subplots(2, 2, figsize=(16, 14))

    fig.suptitle(title)

    titlesR, tracksR = zip(*tracks_row)

    for i, tracksR in enumerate(tracksR):
        axs[0][i].set_title(titlesR[i])

        for track in tracksR:
            x, y = zip(*track)
            axs[0][i].plot(x, y, marker='o')

        xd, yd = zip(*drivers)
        axs[0][i].scatter(xd, yd, color='blue', marker='o')

        axs[0][i].scatter(polo[0], polo[1], color='red', marker='o')

        # Aggiungi assi cartesiani centrati in (0,0)
        axs[0][i].axhline(0, color='black', linewidth=1)  # Asse X
        axs[0][i].axvline(0, color='black', linewidth=1)  # Asse Y

        # Imposta i limiti fissi per gli assi
        axs[0][i].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
        axs[0][i].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

        # Aggiungi etichette e griglia
        axs[0][i].set_xlabel("Asse X")
        axs[0][i].set_ylabel("Asse Y")
        axs[0][i].set_title(titlesR[i])
        axs[0][i].grid(True)
    
    titlesC, tracksC = zip(*tracks_col)

    for i, tracksC in enumerate(tracksC):
        axs[1][i].set_title(titlesC[i])

        for track in tracksC:
            x, y = zip(*track)
            axs[1][i].plot(x, y, marker='o')

        xd, yd = zip(*drivers)
        axs[1][i].scatter(xd, yd, color='blue', marker='o')

        axs[1][i].scatter(polo[0], polo[1], color='red', marker='o')

        # Aggiungi assi cartesiani centrati in (0,0)
        axs[1][i].axhline(0, color='black', linewidth=1)  # Asse X
        axs[1][i].axvline(0, color='black', linewidth=1)  # Asse Y

        # Imposta i limiti fissi per gli assi
        axs[1][i].set_xlim(-map_size/2 - map_size*0.1, map_size/2 + map_size*0.1)
        axs[1][i].set_ylim(-map_size/2 - map_size*0.1, map_size/2+ map_size*0.1)

        # Aggiungi etichette e griglia
        axs[1][i].set_xlabel("Asse X")
        axs[1][i].set_ylabel("Asse Y")
        axs[1][i].set_title(titlesC[i])
        axs[1][i].grid(True)
    
    plt.show()