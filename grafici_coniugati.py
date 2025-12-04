import numpy as np
import matplotlib.pyplot as plt

p_data = np.array([423.6, 421.6, 418.1, 414.6, 410.6, 407.1, 403.1, 399.1, 396.1, 390.6, 
                   388.1, 383.6, 380.6, 374.6, 372.1, 366.1, 363.1, 355.6, 352.1, 346.6, 
                   341.6, 333.1, 328.1, 314.6, 306.1])

q_data = np.array([228.1, 227.6, 228.6, 229.6, 231.1, 232.1, 233.6, 235.1, 235.6, 238.6, 
                   238.6, 240.6, 241.1, 244.6, 244.6, 248.1, 248.6, 253.6, 254.6, 257.6, 
                   260.1, 266.1, 268.6, 279.6, 285.6])

# Lavoro sui reciproci
x = 1 / p_data   # 1/p
y = 1 / q_data   # 1/q

# Regressione lineare: 1/q = m * (1/p) + b
m, b = np.polyfit(x, y, 1)

# Punti per la retta di fit
x_fit = np.linspace(x.min(), x.max(), 200)
y_fit = m * x_fit + b

plt.figure()

# Dati sperimentali
plt.scatter(x, y, color='red', s=30, marker='.', label='Dati')

# Retta di fit con equazione in legenda
equation = r"$y = {:.3g}\,x + {:.3g}$".format(m, b)
plt.plot(x_fit, y_fit, label=equation)

# Notazione scientifica sugli assi
plt.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))

plt.xlabel('1/p [1/mm]')
plt.ylabel('1/q [1/mm]')
plt.title("Punti Coniugati")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
