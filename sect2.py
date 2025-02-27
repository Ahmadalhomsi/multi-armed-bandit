import numpy as np
import matplotlib.pyplot as plt

# Eşit Olasılıklı Zar Atımı
fair_dice_rolls = np.random.randint(1, 7, size=1000)
values, counts = np.unique(fair_dice_rolls, return_counts=True)

plt.bar(values, counts, alpha=0.7, label="Eşit Olasılıklı Zar")
plt.title("Eşit Olasılıklı Zar Atımı")
plt.xlabel("Zar Yüzleri")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Normal Dağılım ile Zar Atımı
normal_dice_rolls = np.round(np.random.normal(loc=3.5, scale=1, size=1000)).astype(int)
normal_dice_rolls = np.clip(normal_dice_rolls, 1, 6)  # Değerleri 1-6 arasında sınırla
values_normal, counts_normal = np.unique(normal_dice_rolls, return_counts=True)

plt.bar(values_normal, counts_normal, alpha=0.7, label="Normal Dağılımlı Zar")
plt.title("Normal Dağılımlı Zar Atımı")
plt.xlabel("Zar Yüzleri")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Poisson Dağılımı ile Zar Atımı
poisson_dice_rolls = np.random.poisson(lam=3, size=1000)
poisson_dice_rolls = np.clip(poisson_dice_rolls, 1, 6)  # Değerleri 1-6 arasında sınırla
values_poisson, counts_poisson = np.unique(poisson_dice_rolls, return_counts=True)

plt.bar(values_poisson, counts_poisson, alpha=0.7, label="Poisson Dağılımlı Zar")
plt.title("Poisson Dağılımlı Zar Atımı")
plt.xlabel("Zar Yüzleri")
plt.ylabel("Frequency")
plt.legend()
plt.show()