import numpy as np
import matplotlib.pyplot as plt

# Időtartomány
t = np.linspace(0, 20, 1000)

# Paraméterek
w_drive = 3.0       # Gerjesztő frekvencia (pl. generátor)
w0 = 5.0            # Sajátfrekvencia
alpha = 0.4         # Csillapítás

# 1. Állandósult válasz (Steady State) - Partikuláris megoldás
# Ez egy tiszta szinuszos rezgés a gerjesztő frekvenciával
# Az amplitúdót és fázist a fizikai képletek határozzák meg, de itt szemléltetéshez rögzítjük
steady_amp = 0.6
phase_shift = -0.5
y_steady = steady_amp * np.sin(w_drive * t + phase_shift)

# 2. Tranziens válasz (Transient) - Homogén megoldás
# Ez a csillapított sajátrezgés (lecseng)
w_d = np.sqrt(w0**2 - alpha**2) # Csillapított frekvencia
# A kezdeti feltételek miatt a tranziensnek "ki kell oltania" az állandósultat t=0-ban (ha y(0)=0)
transient_amp = -steady_amp / np.sin(0 + 0.1) # Közelítő illesztés a vizualizációhoz
y_transient = 0.8 * np.exp(-alpha * t) * np.cos(w_d * t)

# 3. Teljes válasz (Total) = Tranziens + Állandósult
y_total = y_steady + y_transient

# Plotolás
plt.figure(figsize=(10, 6))

# A komponensek (halványabban)
plt.plot(t, y_steady, label='Állandósult összetevő (Generátor)', color='red', linestyle='--', alpha=0.6, linewidth=1.5)
plt.plot(t, y_transient, label='Tranziens összetevő (Lecsengés)', color='green', linestyle=':', alpha=0.6, linewidth=1.5)

# A teljes eredő jel (vastagon)
plt.plot(t, y_total, label='Teljes mért válasz Q(t)', color='blue', linewidth=2.5)

# Jelölések
plt.title('Kényszerrezgés Időbeli Lefolyása\n(Tranziens + Állandósult)', fontsize=14)
plt.xlabel('Idő (t)', fontsize=12)
plt.ylabel('Amplitúdó', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)

# Szöveges magyarázat a ábrán
plt.text(2, 0.9, 'Tranziens szakasz\n(Kaotikus)', fontsize=10, color='blue',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
plt.text(12, 0.9, 'Állandósult szakasz\n(Tiszta szinusz)', fontsize=10, color='red',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

plt.grid(True, alpha=0.3)
plt.legend(loc='lower right', fontsize=10)
plt.xlim(0, 20)

# Mentés
plt.savefig('forced_response_diagram.png', dpi=300)