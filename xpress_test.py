import xpress as xp

# === DATI DI INPUT ===
# Esempio di distanze in km tra i punti di origine e la destinazione (Polo Scientifico)
distanze = {
    ("A", "UniFe"): 10,  
    ("B", "UniFe"): 15,
    ("C", "UniFe"): 8,
    ("D", "UniFe"): 12,
    ("E", "UniFe"): 20,
}

# Persone disponibili e la loro posizione
persone = ["A", "B", "C", "D", "E"]
autisti = ["A", "B"]  # Questi due possono guidare
passeggeri = ["C", "D", "E"]  # Questi viaggiano come passeggeri

# Capacità massima di un'auto (compreso autista)
capienza_auto = 5

# === VARIABILI ===
# x[i] = 1 se la persona i guida, 0 altrimenti
x = {i: xp.var(name=f"x_{i}", binary=True) for i in persone}

# y[i,j] = 1 se la persona i viaggia con l'autista j
y = {(i, j): xp.var(name=f"y_{i}_{j}", binary=True) for i in passeggeri for j in autisti}

# === MODELLO DI OTTIMIZZAZIONE ===
model = xp.problem()

# Aggiunge variabili
model.addVariable(list(x.values()) + list(y.values()))

# Obiettivo: minimizzare i km percorsi
model.setObjective(
    xp.Sum(distanze[(i, "UniFe")] * x[i] for i in autisti) +
    xp.Sum(distanze[(j, "UniFe")] * y[i, j] for i in passeggeri for j in autisti),
    sense=xp.minimize
)

# Vincolo: Ogni passeggero deve viaggiare con un autista o guidare da solo
for i in passeggeri:
    model.addConstraint(x[i] + xp.Sum(y[i, j] for j in autisti) == 1, name=f"Passeggero_servito_{i}")

# Vincolo: Un autista può trasportare al massimo capienza_auto - 1 passeggeri
for j in autisti:
    model.addConstraint(xp.Sum(y[i, j] for i in passeggeri) <= (capienza_auto - 1) * x[j], name=f"Capienza_{j}")

# Risolvi il problema
model.solve()

# === RISULTATI ===
print("\n=== SOLUZIONE OTTIMA ===")
for i in persone:
    print(f"{i} guida? {'Sì' if x[i].sol > 0.5 else 'No'}")

for i in passeggeri:
    for j in autisti:
        if y[i, j].sol > 0.5:
            print(f"{i} viaggia con {j}")