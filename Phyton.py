import math
import tkinter as tk
from tkinter import messagebox
import random

# ---------------------- FUNZIONI DI CALCOLO ---------------------- #

def calcola_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

def calcola_safety_stock(sigma, lead_time):
    return sigma * math.sqrt(lead_time)

def calcola_reorder_level(D_giornaliera, lead_time, safety_stock):
    return (D_giornaliera * lead_time) + safety_stock

# ---------------------- SIMULAZIONE 3 ANNI ---------------------- #

def simulazione_3_anni(D, S, H, lead_time, sigma):
    risultati = []

    for anno in range(1, 4):
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