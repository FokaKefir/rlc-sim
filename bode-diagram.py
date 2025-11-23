from scipy import signal
import matplotlib.pyplot as plt

# Paraméterek egy alulcsillapított esethez
R = 5.0
L = 0.1
C = 0.001

# Átviteli függvény (Transfer Function) definiálása
# H(s) = (1/LC) / (s^2 + (R/L)s + (1/LC))  -> Ez a kondenzátor feszültségére vonatkozik
num = [1/(L*C)]             # Számláló
den = [1, R/L, 1/(L*C)]     # Nevező (s^2, s^1, s^0 együtthatói)

system = signal.TransferFunction(num, den)

# Bode diagram számítása
w, mag, phase = signal.bode(system)

plt.figure(figsize=(10, 8))

# Amplitúdó (Erősítés) diagram
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)    # Logaritmikus skála az X tengelyen
plt.title('Bode Diagram')
plt.ylabel('Erősítés (dB)')
plt.grid(True, which="both")

# Fázis diagram
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.ylabel('Fázis (fok)')
plt.xlabel('Frekvencia (rad/s)')
plt.grid(True, which="both")

plt.show()