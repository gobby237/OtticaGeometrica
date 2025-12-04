import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# ---------------------------------------------------------
# 1. I TUOI DATI
# ---------------------------------------------------------
p_data = np.array([423.6, 421.6, 418.1, 414.6, 410.6, 407.1, 403.1, 399.1, 396.1, 390.6, 
                   388.1, 383.6, 380.6, 374.6, 372.1, 366.1, 363.1, 355.6, 352.1, 346.6, 
                   341.6, 333.1, 328.1, 314.6, 306.1])

q_data = np.array([228.1, 227.6, 228.6, 229.6, 231.1, 232.1, 233.6, 235.1, 235.6, 238.6, 
                   238.6, 240.6, 241.1, 244.6, 244.6, 248.1, 248.6, 253.6, 254.6, 257.6, 
                   260.1, 266.1, 268.6, 279.6, 285.6])

# ---------------------------------------------------------
# 2. DEFINIAMO LA FUNZIONE FISICA
# ---------------------------------------------------------
def calcola_errore(A):
    """
    Questa funzione prende una focale A, calcola dove dovrebbero essere 
    i punti q (q_teorico) e restituisce la somma degli errori al quadrato.
    """
    # Formula della lente: q = (p * f) / (p - f)
    
    q_teorico = (p_data * A) / (p_data - A)
    
    # Calcolo la differenza tra dati veri e teorici, al quadrato
    differenza = q_data - q_teorico
    somma_quadrati = np.sum(differenza**2)
    
    return somma_quadrati

# ---------------------------------------------------------
# 3. TROVIAMO IL VALORE MIGLIORE (MINIMO)
# ---------------------------------------------------------
# Cerchiamo la focale migliore tra 100mm e 200mm
risultato = minimize_scalar(calcola_errore, bounds=(100, 200), method='bounded')

A_migliore = risultato.x
Errore_minimo = risultato.fun

print(f"La focale migliore è: {A_migliore:.4f} mm")
print(f"L'errore minimo è:    {Errore_minimo:.4f}")

# ---------------------------------------------------------
# 4. PREPARIAMO I DATI PER IL GRAFICO (METODO SEMPLICE)
# ---------------------------------------------------------
# Creiamo 500 valori di prova per A, vicini al risultato trovato (zoom +/- 2mm)
lista_A = np.linspace(A_migliore - 2, A_migliore + 2, 500)

# Creiamo una lista vuota dove salveremo gli errori
lista_errori = []

# CICLO FOR: Molto più facile da capire del broadcasting!
for A_prova in lista_A:
    # Per ogni A nella lista, calcoliamo l'errore usando la funzione fatta sopra
    errore = calcola_errore(A_prova)
    lista_errori.append(errore)

# ---------------------------------------------------------
# 5. DISEGNAMO IL GRAFICO
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

# Disegna la curva
plt.plot(lista_A, lista_errori, label='Errore S(A)', color='blue')

# Disegna le linee tratteggiate
plt.axvline(x=A_migliore, color='green', linestyle='--', label=f'Minimo: {A_migliore:.2f} mm')
plt.axhline(y=Errore_minimo, color='red', linestyle='--', label='Fondo della parabola')

plt.title("Ricerca della Focale (Minimi Quadrati)")
plt.xlabel("Valore di Focale A (mm)")
plt.ylabel("Errore Totale S(A)")
plt.legend()
plt.grid(True)
plt.show()