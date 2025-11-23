import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 1. Paraméterek definiálása
L = 0.1      # Henry
C = 0.001    # Farad
# Az R-et változtatni fogjuk a 3 esethez!

# 2. A differenciálegyenlet rendszer definiálása
# y = [Q, I] -> Q a töltés, I az áram (dQ/dt)
def rlc_circuit(y, t, R, L, C, E):
    Q, I = y
    dQdt = I
    dIdt = (E - R * I - Q / C) / L
    return [dQdt, dIdt]

t = np.linspace(0, 0.3, 500) # Időskála: 0-tól 0.3 másodpercig
E = 10.0 # Bemenő feszültség (Step input: 10V)

# 3. A három eset vizsgálata különböző ellenállásokkal
# Számoljuk ki a kritikus ellenállást: R_crit = 2 * sqrt(L/C)
R_crit = 2 * np.sqrt(L/C) 
resistance_values = {
    'Alulcsillapított (R kicsi)': R_crit * 0.2,
    'Kritikusan csillapított': R_crit,
    'Túlcsillapított (R nagy)': R_crit * 5
}

plt.figure(figsize=(10, 6))

for label, R in resistance_values.items():
    y0 = [0, 0] # Kezdeti feltételek: Q=0, I=0
    solution = odeint(rlc_circuit, y0, t, args=(R, L, C, E))
    
    # A kondenzátor feszültsége: Vc = Q / C
    Vc = solution[:, 0] / C
    
    plt.plot(t, Vc, label=f"{label} (R={R:.1f} ohm)")

plt.title('RLC Kör Átmeneti Válasza (Step Response)')
plt.xlabel('Idő (s)')
plt.ylabel('Kondenzátor feszültsége (V)')
plt.axhline(y=E, color='r', linestyle='--', alpha=0.5, label='Bemenő feszültség')
plt.grid(True)
plt.legend()
plt.show()