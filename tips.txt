# CarSharing_RicercaOperativa
 
Sono noti i luoghi di origine delle persone che si recano quotidianamente al Polo Scientifico Tecnologico UniFe a inizio giornata (stessa ora di arrivo). Sono noti quelli disponibili ad operare come autisti in un servizio di Car Pooling. Tutti gli altri sono interessati a viaggiare come passeggeri e prendono la propria macchina solo se nessuno li serve: in tal caso non vogliono nessun altro a bordo. Ogni auto porta fino a 5 persone (conducente incluso). 
Si determini la soluzione che minimizza il numero di km percorsi dalle auto.

# Ottimizzazione con Algoritmi di Clustering (K-Means, DBSCAN, o Agglomerative Clustering)
Idea: Prima di assegnare i driver, si raggruppano i passeggeri in cluster basati sulla distanza geografica. I cluster dovrebbero essere di massimo 5 persone (incluso il driver).
Vantaggio: Evita percorsi inefficienti dovuti a decisioni greedy locali.

Implementazione:
Si esegue K-Means con  K  uguale al numero di autisti disponibili.
Oppure si usa DBSCAN, che raggruppa i passeggeri in base alla densità delle loro posizioni.
Si assegna a ogni cluster un autista e si trova il percorso minimo per raggiungere tutti i passeggeri prima del Polo.

# Risoluzione come Problema di Minimo Albero Ricoprente (MST - Minimum Spanning Tree)
Idea:
Creare un grafo completo in cui ogni nodo è una persona e i pesi degli archi rappresentano la distanza tra loro.
Costruire un Minimum Spanning Tree (MST) usando l’algoritmo di Prim o Kruskal.
Dividere l’albero in sottogruppi (ognuno con massimo 5 persone) assegnando un driver a ciascun sottogruppo.
Vantaggio: Minimizza la somma delle distanze necessarie per raccogliere i passeggeri.

Implementazione:
Creare un grafo completo con le distanze come pesi.
Applicare Prim/Kruskal per trovare il MST.
Dividere il MST in gruppi da massimo 5 nodi con una tecnica di “potatura” e assegnare un autista per ogni gruppo.

# Algoritmo del Commesso Viaggiatore con Vincoli di Capacità (Capacitated TSP)
Idea:
Considerare ogni autista come un commesso viaggiatore che deve visitare al massimo 4 passeggeri prima di arrivare al Polo.
Risolvere un Problema del Commesso Viaggiatore con Capacità (Capacitated TSP), trovando il percorso minimo per ogni auto.
Vantaggio: Ottimizza ogni tragitto per ridurre la distanza.

Implementazione:
Utilizzare algoritmi euristici per TSP (es. Nearest Neighbor con miglioramenti come 2-opt).
Usare Gurobi o Google OR-Tools per la versione esatta.

# Simulated Annealing o Algoritmi Genetici
Idea: Si genera una soluzione casuale e si migliora iterativamente scambiando passeggeri tra le auto o modificando le rotte.
Vantaggio: Adatto a problemi complessi quando le soluzioni esatte sono troppo costose computazionalmente.

Implementazione:
Definire una funzione di costo (distanza totale percorsa).
Usare Simulated Annealing per esplorare le soluzioni vicine a quella corrente, accettando peggioramenti temporanei per evitare minimi locali.
Oppure usare Algoritmi Genetici con cromosomi che rappresentano assegnazioni di passeggeri ad auto.