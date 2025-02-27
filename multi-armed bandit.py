import numpy as np
import matplotlib.pyplot as plt

# 1000 örnek üretmek için dağılımları tanımlayalım
np.random.seed(42)  # Rastgelelik için sabit bir seed değeri

# Normal Dağılım
normal_data = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(normal_data, bins=30, alpha=0.7, label="Normal Dağılım")
print("Normal Dağılım - Ortalama:", np.mean(normal_data), "Varyans:", np.var(normal_data))

# Poisson Dağılımı
poisson_data = np.random.poisson(lam=5, size=1000)
plt.hist(poisson_data, bins=30, alpha=0.7, label="Poisson Dağılımı")
print("Poisson Dağılım - Ortalama:", np.mean(poisson_data), "Varyans:", np.var(poisson_data))

# Üstel Dağılım
exponential_data = np.random.exponential(scale=1, size=1000)
plt.hist(exponential_data, bins=30, alpha=0.7, label="Üstel Dağılım")
print("Üstel Dağılım - Ortalama:", np.mean(exponential_data), "Varyans:", np.var(exponential_data))

# Binom Dağılımı
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(binomial_data, bins=30, alpha=0.7, label="Binom Dağılımı")
print("Binom Dağılım - Ortalama:", np.mean(binomial_data), "Varyans:", np.var(binomial_data))

# Pareto Dağılımı
pareto_data = np.random.pareto(a=2, size=1000)
plt.hist(pareto_data, bins=30, alpha=0.7, label="Pareto Dağılımı")
print("Pareto Dağılım - Ortalama:", np.mean(pareto_data), "Varyans:", np.var(pareto_data))

# Histogramları gösterelim
plt.title("Olasılık Dağılımlarının Karşılaştırılması")
plt.xlabel("Değerler")
plt.ylabel("Frekans")
plt.legend()
plt.show()