# Telekomünikasyon Sektöründe Müşteri Kaybı (Churn) Tahmini

Bu proje, telekomünikasyon sektöründe müşteri kaybını (churn) önceden tahmin etmeyi amaçlayan
bir makine öğrenmesi çalışmasıdır. Projede IBM Telco Customer Churn veri seti kullanılarak,
müşteri davranışları analiz edilmiş ve churn eğilimi yüksek müşteriler tespit edilmiştir.

---

## Proje Amacı

Müşteri kaybını reaktif bir problem olmaktan çıkararak, proaktif sadakat yönetimi için
kullanılabilecek bir tahmin modeli geliştirmektir.

---

## Veri Seti

- Kaynak: IBM Telco Customer Churn Dataset
- Toplam müşteri sayısı: 7.043
- Toplam değişken sayısı: 33
- Hedef değişken: Churn Label (Yes / No)

Veri seti, müşterilerin demografik bilgileri, hizmet kullanım detayları,
sözleşme türleri ve faturalandırma bilgilerini içermektedir.

---

## Kullanılan Yöntemler

- Keşifsel Veri Analizi (EDA)
- Veri Ön İşleme ve Feature Engineering
- Logistic Regression (ikili sınıflandırma)
- Pipeline yapısı
- One-Hot Encoding
- Model değerlendirme:
  - Confusion Matrix
  - ROC-AUC
  - Precision, Recall, F1-score

---

## Karşılaşılan Problemler

- Karışık veri tipleri (özellikle Total Charges)
- Data leakage (Churn Score, Churn Reason vb.)
- OneHotEncoder ve pipeline hataları
- Sınıf dengesizliği problemi

Bu problemler analiz edilerek düzeltilmiş ve model gerçekçi sonuçlar verecek şekilde
yeniden yapılandırılmıştır.

---

## Kullanılan Teknolojiler

- Python 3.10+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- Jupyter Notebook

---

## Proje Yapısı

telco-churn-project/
│
├── data/
│ └── raw/
├── 01_eda.ipynb
├── 02_preprocessing_model.ipynb
├── requirements.txt
└── README.md

## Run Prediction Script

```bash
venv\Scripts\activate
python predict.py
