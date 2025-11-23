import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# RLC paraméterek (Soros RLC kör, kimenet az R-en -> Sávszűrő)
R = 10.0    # Ohm
L = 10e-3   # Henry (10 mH)
C = 1e-6    # Farad (1 uF)

# Átviteli függvény: H(s) = (R/L * s) / (s^2 + R/L * s + 1/LC)
num = [R/L, 0]
den = [1, R/L, 1/(L*C)]
system = signal.TransferFunction(num, den)

# Frekvenciatartomány (100 Hz - 10 kHz)
w, mag, phase = signal.bode(system, n=500)
freq_hz = w / (2 * np.pi) # Konvertálás rad/s -> Hz-be

# Rezonancia frekvencia számolása
f0 = 1 / (2 * np.pi * np.sqrt(L*C))

plt.figure(figsize=(10, 8))

# 1. Amplitúdó diagram (Magnitude)
plt.subplot(2, 1, 1)
plt.semilogx(freq_hz, mag, color='blue', linewidth=2)
plt.title(f'Bode-diagram: Soros RLC kör (Sávszűrő)\nRezonancia frekvencia: {f0:.0f} Hz', fontsize=12)
plt.ylabel('Amplitúdó [dB]', fontsize=10)
plt.grid(True, which="both", ls="-", alpha=0.6)
plt.axvline(f0, color='red', linestyle='--', label=r'$f_0$ (Rezonancia)')
# -3 dB vonal
plt.axhline(-3, color='green', linestyle=':', label='-3 dB határ (Sávszélesség)')
plt.legend(loc='lower right')

# 2. Fázis diagram (Phase)
plt.subplot(2, 1, 2)
plt.semilogx(freq_hz, phase, color='orange', linewidth=2)
plt.ylabel('Fázis [fok]', fontsize=10)
plt.xlabel('Frekvencia [Hz]', fontsize=10)
plt.grid(True, which="both", ls="-", alpha=0.6)
plt.axvline(f0, color='red', linestyle='--')
plt.yticks([-90, -45, 0, 45, 90])

plt.tight_layout()
plt.savefig('bode_plot_rlc.png', dpi=300)