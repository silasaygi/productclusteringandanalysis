# 📊 Ürün Kümeleme ve Analizi  

Bu proje, **Turkcell Geleceği Yazanlar platformunda Kaan Can Yılmaz eğitmeninin hazırladığı** veri analizi ve makine öğrenimi konularını içeren bir çalışmadır. Proje kapsamında rastgele oluşturulmuş **ürün fiyatları, ortalama puanlar ve menşei bilgileri** üzerinden **veri analizi, görselleştirme ve kümeleme algoritmaları** uygulanmıştır.  

Bu çalışmayla **veri görselleştirme, keşifsel veri analizi (EDA) ve makine öğrenimi algoritmaları** hakkında kapsamlı bilgi edinmek amaçlanmıştır.  

## 🛠 Kullanılan Teknolojiler  
- **Python** (Veri işleme ve modelleme)  
- **Pandas & NumPy** (Veri manipülasyonu)  
- **Seaborn & Matplotlib** (Veri görselleştirme)  
- **Scikit-learn** (Makine öğrenimi algoritmaları)  
- **t-SNE & Dendrogram** (Kümeleme analizi)  

## 📌 Proje İçeriği  

### 1️⃣ Veri Setinin Oluşturulması  
Projede, rastgele oluşturulan **100 adet ürün** için aşağıdaki değişkenler kullanılmıştır:  
- **Ürün Adı** (`urun_adi`)  
- **Fiyat** (`fiyat`)  
- **Ortalama Puan** (`ortalama_puan`)  
- **Menşei** (`mensei`)  

**📌 Amaç**:  
Farklı menşeilere sahip ürünlerin fiyat ve puan dağılımlarını analiz etmek ve benzer ürünleri kümeleyerek gruplar oluşturmak.  

### 2️⃣ Keşifsel Veri Analizi (EDA)  
Veri setinin genel yapısını anlamak için aşağıdaki analizler gerçekleştirilmiştir:  
- 📊 **Temel İstatistiksel Özet** (`data.describe()`)  
- 📊 **Veri Türlerinin ve Eksik Verilerin İncelenmesi** (`data.info()`)  

#### 🔍 Veri Dağılımını Görselleştirme  
- 📈 **Fiyat Dağılımı Histogramı**  
- 📈 **Ortalama Puan Dağılımı Histogramı**  
- 📉 **Fiyat & Ortalama Puan Arasındaki İlişki (Scatter Plot)**  

### 3️⃣ Veri Görselleştirme  
Veriyi daha iyi anlamak adına çeşitli grafikler oluşturulmuştur:  
- 📊 **Menşei bazında fiyat dağılımı (Boxplot)**  
- 📊 **Menşei bazında ortalama puan dağılımı (Boxplot)**  
- 📊 **Fiyat & Ortalama Puan Arasındaki İlişki (Scatter Plot, Hue = Menşei)**  

### 4️⃣ Makine Öğrenimi ile Kümeleme Analizi  
Verideki benzer ürünleri belirlemek için **K-Means Kümeleme Algoritması** uygulanmıştır.  
- **Özellikler (Features):** `fiyat`, `ortalama_puan`  
- **Küme Sayısı:** 4 (Deneysel olarak belirlendi)  

🚀 **t-SNE Görselleştirme** ile kümeler iki boyutta gösterildi.  
📌 **Dendrogram (Hiyerarşik Kümeleme)** kullanılarak veri noktaları arasındaki mesafeler analiz edildi.  

---

## 📂 Dosya Yapısı  
```bash
📦 urun-kumeleme-analizi  
 ├── 📜 urun_kumeleme_analizi.ipynb  # Jupyter Notebook dosyası  
 ├── 📜 README.md                    # Proje açıklamaları  
