import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import os

def process_files():
    # Finestra nascosta solo per usare il file dialog
    root = tk.Tk()
    root.withdraw()

    filepaths = filedialog.askopenfilenames(
        title="Seleziona i file da convertire"
    )

    if not filepaths:
        return

    count = 0
    for fp in filepaths:
        p = Path(fp)

        try:
            # Leggo tutto il file
            with p.open("r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                # File vuoto, salto
                continue

            # Tolgo la prima riga
            lines = lines[1:]

            # Sostituisco le virgole con spazi
            lines = [line.replace(",", " ") for line in lines]

            # Nuovo percorso con estensione .txt
            new_path = p.with_suffix(".txt")

            # Scrivo il nuovo file
            with new_path.open("w", encoding="utf-8", newline="\n") as f:
                f.writelines(lines)

            # Se vuoi eliminare l'originale, scommenta questa riga:
            # if p != new_path:
            #     os.remove(p)

            count += 1

        except Exception as e:
            print(f"Errore con il file {p}: {e}")

    messagebox.showinfo("Fatto", f"Hai convertito {count} file in .txt")

if __name__ == "__main__":
    process_files()
