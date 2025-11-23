import numpy as np
import matplotlib.pyplot as plt

# Frekvencia tartomány (omega / omega0 arányban)
w_ratio = np.linspace(0.1, 3.0, 500)

# Amplitúdó függvény (Magnification factor)
# A = 1 / sqrt( (1 - w^2)^2 + (2*zeta*w)^2 )
# Ahol zeta = alpha / w0 (csillapítási arány)

def resonance_curve(w, zeta):
    return 1.0 / np.sqrt((1 - w**2)**2 + (2 * zeta * w)**2)

# Különböző csillapítások
zetas = [0.1, 0.25, 0.707] # Kicsi, Közepes, Nagy (Butterworth)
colors = ['blue', 'green', 'red']
labels = [r'Kicsi csillapítás ($\zeta=0.1$) - Éles rezonancia',
          r'Közepes csillapítás ($\zeta=0.25$)',
          r'Nagy csillapítás ($\zeta=0.7$) - Nincs csúcs']

plt.figure(figsize=(10, 6))

for z, c, l in zip(zetas, colors, labels):
    amp = resonance_curve(w_ratio, z)
    plt.plot(w_ratio, amp, color=c, linewidth=2.5, label=l)

# Rezonancia pont jelölése
plt.axvline(1.0, color='black', linestyle='--', alpha=0.5)
plt.text(1.05, 4.5, r'Rezonancia ($\omega = \omega_0$)', fontsize=12)

plt.title('Rezonancia Görbék (Frekvenciaválasz)', fontsize=14)
plt.xlabel(r'Frekvencia arány ($\omega / \omega_0$)', fontsize=12)
plt.ylabel('Relatív Amplitúdó (Erősítés)', fontsize=12)
plt.grid(True, which='both', alpha=0.3)
plt.legend(fontsize=10)
plt.xlim(0, 3)
plt.ylim(0, 5.5)

# Mentés
plt.savefig('resonance_curve.png', dpi=300)