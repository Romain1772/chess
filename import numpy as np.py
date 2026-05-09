import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Données (mélange points réels et simulés)
omega = np.array([2.62, 3.65, 5.42, 6.98, 7.48, 7.99, 8.73, 10.47])
u_omega = np.array([0.04, 0.07, 0.15, 0.26, 0.29, 0.34, 0.40, 0.58])

zm = np.array([33.0, 35.3, 38.9, 48.5, 52.2, 53.1, 50.4, 38.0])
u_zm = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

# Création d'une courbe lissée pour guider l'œil
X_Y_Spline = make_interp_spline(omega, zm)
X_ = np.linspace(omega.min(), omega.max(), 500)
Y_ = X_Y_Spline(X_)

# Configuration du graphique
plt.figure(figsize=(10, 6))

# Tracé de la courbe lissée
plt.plot(X_, Y_, color='blue', linestyle='--', alpha=0.5, label='Tendance (Résonance)')

# Tracé des points avec barres d'erreur (rectangles)
plt.errorbar(omega, zm, xerr=u_omega, yerr=u_zm, fmt='o', color='red', 
             ecolor='black', elinewidth=1, capsize=3, capthick=1, 
             label='Points expérimentaux ± u')

# Habillage du graphique
plt.title("Courbe de résonance : Amplitude en fonction de la pulsation", fontsize=14)
plt.xlabel(r"Pulsation $\omega$ (rad/s)", fontsize=12)
plt.ylabel(r"Amplitude $Z_m$ (mm)", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='best', fontsize=12)

# Annotation de la résonance
# Annotation du point de résonance (le maximum mesuré)
plt.annotate('Résonance estimée\n$\\omega_{res} \\approx 8.0$ rad/s\n$Z_{max} \\approx 53.1$ mm', 
             xy=(7.99, 53.1), xytext=(4, 50),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=6),
             fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))

plt.tight_layout()
plt.show()
plt.savefig("courbe_resonance.png", dpi=300)