import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# Rastgele veri oluşturma
np.random.seed(42)
num_samples = 100
fiyat = np.random.uniform(10, 100, num_samples)
ortalama_puan = np.random.uniform(1, 5, num_samples)
mensei = np.random.choice(["Ulke_A", "Ulke_B", "Ulke_C", "Ulke_D"], num_samples)
urun_adi = [f"Urun_{i}" for i in range(num_samples)]

data = pd.DataFrame({
    "urun_adi": urun_adi,
    "fiyat": fiyat,
    "ortalama_puan": ortalama_puan,
    "mensei": mensei  
})

# Temel veri analizi
data.describe().T
print(data.info())

# Fiyat ve Ortalama Puan Dağılımı
plt.figure(figsize=(12,6))
sns.histplot(data.fiyat, bins=20, kde=True)
plt.title("Fiyat Dağılımı")
plt.xlabel("Fiyat")
plt.ylabel("Frekans")
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(data.ortalama_puan, bins=20, kde=False)
plt.title("Ortalama Puan Dağılımı")
plt.xlabel("Ortalama Puan")
plt.ylabel("Frekans")
plt.show()

# Fiyat ve Ortalama Puan İlişkisi
plt.figure(figsize=(10,8))
sns.scatterplot(x="fiyat", y="ortalama_puan", data=data, hue="mensei", style="mensei", s=100)
plt.title("Fiyat vs Ortalama Puan")
plt.xlabel("Fiyat")
plt.ylabel("Ortalama Puan")
plt.legend(title="Mensei", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Boxplot ile fiyatların menşeiye göre dağılımı
plt.figure(figsize=(10,6))
sns.boxplot(x="mensei", y="fiyat", data=data, hue="mensei", palette="Set2")
plt.title("Fiyatların Menşeiye Göre Dağılımı")
plt.xlabel("Menşei")
plt.ylabel("Fiyat")
plt.legend(title="Mensei", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# K-Means Kümeleme
X = data[["fiyat", "ortalama_puan"]].values
kmeans = KMeans(n_clusters=4, random_state=42)
data["kume"] = kmeans.fit_predict(X)

# t-SNE ile Kümeleme Görselleştirme
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)
plt.figure(figsize=(10,6))
plt.scatter(X_tsne[:,0], X_tsne[:,1], c=data["kume"], cmap="viridis", marker="o", edgecolor="black", s=50)
plt.title("t-SNE ile Kümeleme Görselleştirme")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.colorbar(label="Küme")
plt.show()

# Dendrogram ile Hiyerarşik Kümeleme
linkage_matrix = linkage(X, method="ward")
plt.figure(figsize=(10,6))
dendrogram(linkage_matrix)
plt.title("Dendrogram")
plt.xlabel("Veri Noktaları")
plt.ylabel("Uzaklık")
plt.show()
