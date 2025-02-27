import numpy as np
import matplotlib.pyplot as plt

# Ağırlıklı Seçim (numpy.random.choice ile)
weights = [1, 1, 1, 1, 1, 5]  # 6'nın gelme olasılığını artır
weighted_dice_rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=1000, p=np.array(weights) / sum(weights))
values_weighted, counts_weighted = np.unique(weighted_dice_rolls, return_counts=True)

plt.bar(values_weighted, counts_weighted, alpha=0.7, label="Ağırlıklı Zar")
plt.title("Ağırlıklı Zar Atımı Sonuçları")
plt.xlabel("Zar Yüzleri")
plt.ylabel("Frekans")
plt.legend()
plt.show()

# Hileli Zar Oluşturma (Özel Fonksiyon)
def biased_dice_roll(prob_6=0.5):
    roll = np.random.rand()
    if roll < prob_6:
        return 6
    else:
        return np.random.randint(1, 6)

biased_dice_rolls = [biased_dice_roll(prob_6=0.5) for _ in range(1000)]
values_biased, counts_biased = np.unique(biased_dice_rolls, return_counts=True)

plt.bar(values_biased, counts_biased, alpha=0.7, label="Hileli Zar")
plt.title("Hileli Zar Atımı Sonuçları")
plt.xlabel("Zar Yüzleri")
plt.ylabel("Frekans")
plt.legend()
plt.show()