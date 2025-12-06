import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

def plotta_grafici():
    """
    Apre una finestra di dialogo per selezionare più file,
    legge i dati (X e Y separati da spazio) e li plotta sovrapposti.
    """
    # 1. Nasconde la finestra principale di Tkinter, dato che ci serve solo la finestra di dialogo.
    root = tk.Tk()
    root.withdraw()
    
    # 2. Apertura della finestra di dialogo per la selezione multipla dei file
    # filter ti permette di selezionare solo i file di testo o tutti i file.
    filepaths = filedialog.askopenfilenames(
        title="Seleziona i file di dati (asse X e Y separati da spazio)",
        filetypes=(("File di testo", "*.txt"), ("Tutti i file", "*.*"))
    )
    
    # Se l'utente annulla la selezione, la lista è vuota
    if not filepaths:
        print("Nessun file selezionato. Operazione annullata.")
        return

    # 3. Preparazione del grafico
    plt.figure(figsize=(10, 6))
    
    # Definiamo una lista di colori da usare per i grafici
    # Puoi espandere questa lista se prevedi di caricare molti file.
    colori = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta']
    
    # 4. Lettura e Plotting di ciascun file
    for i, filepath in enumerate(filepaths):
        try:
            # Usa np.loadtxt per leggere i dati. 
            # Ha il vantaggio di gestire facilmente separatori di spazio e multipli colonne.
            # 'unpack=True' trasforma un array di due colonne in due array separati (X e Y)
            data = np.loadtxt(filepath)
            
            # Assicurati che il file contenga almeno due colonne
            if data.ndim == 1 or data.shape[1] < 2:
                 print(f"ATTENZIONE: Il file '{filepath}' non contiene dati X e Y validi (almeno 2 colonne). Saltato.")
                 continue

            # La prima colonna è X, la seconda è Y
            X = data[:, 0]
            Y = data[:, 1]
            
            # Determina il colore e l'etichetta (label) per la legenda
            colore_corrente = colori[i % len(colori)] # Il modulo (%) ricicla i colori se superi la lista
            nome_file = filepath.split('/')[-1] # Prende solo il nome del file dal percorso
            
            # Plotta la serie
            plt.plot(X, Y, 
                     color=colore_corrente, 
                     label=f'Dati da: {nome_file}')

        except Exception as e:
            # Cattura eventuali errori durante la lettura del file
            print(f"Errore nella lettura del file '{filepath}': {e}")
            continue

    # 5. Aggiunta di titoli e legenda per chiarezza
    plt.title("Grafici Sovrapposti da File Multipli")
    plt.xlabel("Asse X")
    plt.ylabel("Asse Y")
    plt.legend() # Mostra la legenda con i nomi dei file
    plt.grid(True)
    
    # 6. Mostra il grafico
    plt.show()

# Esecuzione della funzione
if __name__ == "__main__":
    plotta_grafici()