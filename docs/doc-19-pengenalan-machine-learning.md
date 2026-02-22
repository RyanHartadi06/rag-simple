# Pengenalan Machine Learning — Konsep dan Alur

Machine learning (ML) adalah cabang ilmu di mana sistem belajar dari data tanpa diprogram secara eksplisit untuk setiap skenario. Dokumen ini membahas konsep dasar, jenis belajar, alur kerja, dan contoh aplikasi.

---

## Apa Itu Machine Learning?

- **Definisi informal** — Program yang "belajar" dari contoh (data): menemukan pola, membuat prediksi, atau mengambil keputusan. Performa membaik seiring data dan pengalaman (training).
- **Berbeda dari pemrograman klasik** — Di pemrograman klasik, aturan ditulis manual. Di ML, aturan (model) didapat dari data melalui algoritma belajar.
- **Contoh** — Klasifikasi spam email, rekomendasi produk, deteksi wajah, prediksi harga rumah, terjemahan mesin, asisten suara.

---

## Jenis Pembelajaran

### Supervised Learning (Belajar Terawasi)
- **Input:** Dataset berisi pasangan (fitur, label). Contoh: (email teks → spam/bukan), (gambar → kelas objek).
- **Tujuan:** Belajar fungsi dari fitur ke label; prediksi label untuk data baru.
- **Klasifikasi** — Label diskrit (spam/bukan, jenis penyakit). Metrik: akurasi, precision, recall, F1.
- **Regresi** — Label kontinu (harga, suhu). Metrik: MSE, MAE, R².
- **Algoritma umum:** Linear/Logistic Regression, Decision Tree, Random Forest, SVM, Neural Network, Gradient Boosting (XGBoost, LightGBM).

### Unsupervised Learning (Belajar Tanpa Awalan)
- **Input:** Data tanpa label; hanya fitur.
- **Tujuan:** Menemukan struktur: pengelompokan (clustering), reduksi dimensi, deteksi anomali.
- **Clustering** — Mengelompokkan data yang mirip (K-Means, Hierarchical, DBSCAN).
- **Dimensionality reduction** — PCA, t-SNE; memampatkan atau memvisualisasi data.
- **Algoritma lain:** Association rules (market basket), anomaly detection.

### Reinforcement Learning (Belajar Penguatan)
- **Setting:** Agent berinteraksi dengan environment; dapat reward/penalty; tujuan memaksimalkan reward jangka panjang.
- **Contoh:** Game, robotika, otonom. Algoritma: Q-learning, Policy Gradient, Deep RL (DQN, A3C).
- Kurang dibahas detail di sini; fokus pada supervised dan unsupervised.

---

## Alur Kerja Umum (Supervised)

1. **Definisi masalah** — Prediksi apa? Klasifikasi atau regresi? Metrik sukses apa?
2. **Pengumpulan data** — Data historis, labeling jika supervised; kualitas dan kuantitas penting.
3. **Exploratory Data Analysis (EDA)** — Statistik deskriptif, visualisasi, missing value, outlier, distribusi, korelasi.
4. **Preprocessing** — Pembersihan (missing, outlier), transformasi (normalisasi, encoding kategorikal), feature engineering (fitur baru dari fitur lama).
5. **Split data** — Train (misalnya 70–80%), validation (untuk tuning), test (untuk evaluasi akhir). Hindari kebocoran data (informasi test masuk ke training).
6. **Pemilihan model** — Mulai sederhana (linear model); naik ke model kompleks (tree, neural net) jika perlu. Pertimbangkan bias–variance trade-off.
7. **Training** — Fit model pada data latih; hyperparameter tuning di validation set.
8. **Evaluasi** — Ukur di test set (akurasi, precision, recall, F1, MSE, dll.). Cross-validation untuk estimasi stabil.
9. **Deployment** — Model di-serve sebagai API, terintegrasi ke aplikasi; monitor performa dan data drift.
10. **Maintenance** — Retrain jika data berubah atau performa turun.

---

## Overfitting dan Underfitting

- **Overfitting** — Model terlalu "hapal" data latih; bagus di train, jelek di data baru. Solusi: lebih banyak data, regularisasi, simplifikasi model, dropout (untuk neural net), early stopping.
- **Underfitting** — Model terlalu sederhana; tidak menangkap pola. Solusi: model lebih kompleks, fitur lebih baik, training lebih lama.
- **Bias–variance** — Model sederhana cenderung high bias (underfit); model kompleks high variance (overfit). Tujuan: keseimbangan.

---

## Feature Engineering

- **Kualitas fitur** sering menentukan performa. Domain knowledge penting.
- **Contoh:** Dari tanggal lahir → umur; dari teks → TF-IDF, embedding; dari kategori → one-hot atau target encoding; kombinasi fitur (interaksi).
- **Scaling** — Normalisasi (0–1) atau standardisasi (mean 0, std 1) untuk algoritma yang sensitif skala (SVM, neural net, K-Means).

---

## Validasi dan Metrik

- **Train/validation/test split** — Validation untuk memilih model dan hyperparameter; test hanya untuk estimasi akhir (sekali).
- **Cross-validation** — K-fold: data dibagi K bagian; rotasi train/validation; rata-rata metrik. Mengurangi varians estimasi.
- **Metrik klasifikasi** — Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix. Pilih sesuai masalah (misalnya recall tinggi untuk deteksi penyakit).
- **Metrik regresi** — MSE, RMSE, MAE, MAPE, R².

---

## Perpustakaan dan Tools

- **Python:** scikit-learn (algoritma klasik), pandas (data), NumPy (numerik), Matplotlib/Seaborn (visualisasi). Untuk deep learning: TensorFlow, PyTorch.
- **Langkah awal:** Tutorial scikit-learn; dataset dari UCI, Kaggle; ikuti pipeline: load → preprocess → split → train → evaluate.

---

## Etika dan Batasan

- **Bias data** — Data yang bias menghasilkan model yang bias (diskriminasi). Perhatikan representasi dan fairness.
- **Interpretability** — Model kompleks (deep learning) sulit dijelaskan; di domain sensitif (kesehatan, hukum) interpretability atau explainability penting.
- **Privasi** — Data pribadi harus dilindungi; anonymisasi, regulasi (GDPR, dll.).
- **Harapan realistis** — ML bukan sihir; butuh data berkualitas, definisi masalah jelas, dan iterasi.

---

*Dengan dasar ini Anda bisa melanjutkan ke kursus atau buku ML (misalnya hands-on dengan scikit-learn dan TensorFlow/PyTorch) untuk praktek lebih dalam.*
