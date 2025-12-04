import numpy as np
import tkinter as tk
from tkinter import filedialog

def diameter_range(x, y, perc=50.0):
    """
    Calcola il diametro per una soglia data in percentuale del range.
    perc = 50.0 -> soglia a metà tra ymin e ymax
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    # Ordiniamo in base a x per sicurezza
    idx = np.argsort(x)
    x = x[idx]
    y = y[idx]

    y_min = y.min()
    y_max = y.max()

    alpha = perc / 100.0
    level = y_min + alpha * (y_max - y_min)   # soglia percentuale

    # Maschera dei punti sopra soglia
    mask = y >= level

    if np.sum(mask) < 2:
        # Non ha senso un diametro se ho meno di 2 punti sopra soglia
        return np.nan, level

    x_in = x[mask]
    diametro = x_in.max() - x_in.min()

    return diametro, level


# --- chiedi la percentuale di soglia una volta sola ---
try:
    perc_input = input("Inserisci la soglia in percentuale (0–100, default 50): ").strip()
    if perc_input == "":
        perc = 50.0
    else:
        perc = float(perc_input)
except:
    perc = 50.0

print(f"Userò una soglia al {perc:.1f}% del range di intensità.\n")

# --- selezione file da GUI ---
root = tk.Tk()
root.withdraw()

file_names = filedialog.askopenfilenames(
    title="Seleziona i file dei profili",
    filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
)
file_names = list(file_names)

if not file_names:
    print("Nessun file selezionato.")
else:
    diametri = []

    for i, fname in enumerate(file_names, start=1):
        data = np.loadtxt(fname)
        x = data[:, 0]
        y = data[:, 1]

        diametro, level = diameter_range(x, y, perc=perc)
        diametri.append(diametro)
        print(f"Profilo {i}: diametro = {diametro:.3f} (unità x), soglia_y = {level:.3f}")

    # --- calcolo statistiche sui diametri ---
    diametri = np.asarray(diametri, dtype=float)
    # escludo eventuali NaN (profili problematici)
    valid = diametri[np.isfinite(diametri)]
    n = len(valid)

    if n == 0:
        print("\nNessun diametro valido per il calcolo delle statistiche.")
    else:
        media = np.mean(valid)
        if n > 1:
            stdev_camp = np.std(valid, ddof=1)     # deviazione standard campionaria
            stderr = stdev_camp / np.sqrt(n)       # stdev / sqrt(n)
        else:
            stdev_camp = np.nan
            stderr = np.nan

        print("\n--- Statistiche sui diametri ---")
        print(f"n = {n}")
        print(f"media diametri = {media:.3f} (unità x)")
        print(f"stdev campionaria = {stdev_camp:.3f} (unità x)")
        print(f"errore sulla media (stdev/sqrt(n)) = {stderr:.3f} (unità x)")
