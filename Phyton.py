import math
import tkinter as tk
from tkinter import messagebox
import random

# ---------------------- FUNZIONI DI CALCOLO ---------------------- #

def calcola_eoq(D, S, H):
 
    Calcolo del Lotto Economico di Ordinazione (EOQ)
    D : domanda annua
    S : costo per ordine
    H : costo di mantenimento unitario annuo
    return math.sqrt((2 * D * S) / H)
def calcola_safety_stock(sigma, lead_time):
    Calcolo della Scorta di Sicurezza (Safety Stock)
    sigma : deviazione standard della domanda giornaliera
    lead_time : tempo di approvvigionamento in giorni
    return sigma * math.sqrt(lead_time)

def calcola_reorder_level(D_giornaliera, lead_time, safety_stock):
  
    Calcolo del Livello di Riordino (Reorder Point)
    D_giornaliera : domanda media giornaliera
    lead_time : tempo di approvvigionamento in giorni
    safety_stock : scorta di sicurezza
   
    return (D_giornaliera * lead_time) + safety_stock

# ---------------------- SIMULAZIONE 3 ANNI ---------------------- #

def simulazione_3_anni(D, S, H, lead_time, sigma):
    Simula l'EOQ e il livello di riordino per 3 anni
    con variazioni casuali della domanda
  
    risultati = []
    for anno in range(1, 4):
        # Genera una variazione casuale della domanda annuale (±10%)
        D_var = D * random.uniform(0.9, 1.1)
        D_giornaliera = D_var / 365
        
        eoq = calcola_eoq(D_var, S, H)
        safety_stock = calcola_safety_stock(sigma, lead_time)
        reorder_level = calcola_reorder_level(D_giornaliera, lead_time, safety_stock)
        
        risultati.append({
            "Anno": anno,
            "Domanda_Annua": round(D_var, 2),
            "EOQ": round(eoq, 2),
            "Safety_Stock": round(safety_stock, 2),
            "Reorder_Level": round(reorder_level, 2)
        })
    return risultati

# ---------------------- INTERFACCIA GRAFICA ---------------------- #

def calcola():
    try:
        # Lettura dei dati dalla GUI
        D = float(entry_domanda.get())
        S = float(entry_costo_ordine.get())
        H = float(entry_costo_mantenimento.get())
        lead_time = float(entry_lead_time.get())
        sigma = float(entry_sigma.get())
        
        # Esecuzione della simulazione
        risultati = simulazione_3_anni(D, S, H, lead_time, sigma)
        
        # Mostra i risultati nella finestra
        text_output.delete(1.0, tk.END)
        for r in risultati:
            text_output.insert(tk.END, 
                f"Anno {r['Anno']}:\n"
                f"  Domanda annua: {r['Domanda_Annua']}\n"
                f"  EOQ: {r['EOQ']}\n"
                f"  Scorta di sicurezza: {r['Safety_Stock']}\n"
                f"  Livello di riordino: {r['Reorder_Level']}\n\n"
            )
    except ValueError:
        messagebox.showerror("Errore", "Inserire valori numerici validi.")

# ---------------------- COSTRUZIONE DELLA GUI ---------------------- #

root = tk.Tk()
root.title("EOQ e Livello di Riordino - Project Work Pegaso")
root.geometry("500x550")

# Etichette e campi di input
tk.Label(root, text="Domanda annua (D)").pack(pady=5)
entry_domanda = tk.Entry(root)
entry_domanda.pack()

tk.Label(root, text="Costo per ordine (S)").pack(pady=5)
entry_costo_ordine = tk.Entry(root)
entry_costo_ordine.pack()

tk.Label(root, text="Costo di mantenimento unitario (H)").pack(pady=5)
entry_costo_mantenimento = tk.Entry(root)
entry_costo_mantenimento.pack()

tk.Label(root, text="Lead time (giorni)").pack(pady=5)
entry_lead_time = tk.Entry(root)
entry_lead_time.pack()

tk.Label(root, text="Deviazione standard domanda giornaliera (sigma)").pack(pady=5)
entry_sigma = tk.Entry(root)
entry_sigma.pack()

# Bottone di calcolo
tk.Button(root, text="Calcola EOQ e Livello di Riordino", command=calcola).pack(pady=15)

# Area di output
text_output = tk.Text(root, height=20, width=60)
text_output.pack(pady=10)
# Avvio della GUI
root.mainloop()