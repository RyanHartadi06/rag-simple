# Project Overview: Sistem Manajemen Inventori

Dokumen ini menjelaskan ringkasan proyek, tujuan bisnis, teknologi, fitur utama, dan timeline pengembangan sistem manajemen inventori untuk penggunaan internal atau klien skala kecil-menengah.

---

## Ringkasan & Tujuan Bisnis

Aplikasi web ini dirancang untuk mengelola **stok barang**, **transaksi masuk/keluar**, dan **laporan inventori** dalam satu tempat. Tujuannya adalah:

- Mengurangi kesalahan pencatatan manual dan duplikasi data.
- Memberikan visibilitas real-time terhadap stok dan nilai inventori.
- Memudahkan audit dan rekonsiliasi dengan laporan yang bisa diekspor.
- Mendukung pengambilan keputusan lewat dashboard dan grafik.

Target pengguna: tim gudang, admin toko, dan manajer operasi yang membutuhkan kontrol stok tanpa kompleksitas ERP besar.

---

## Tech Stack

| Lapisan | Teknologi | Alasan Singkat |
|---------|-----------|------------------|
| **Frontend** | React + TypeScript | Komponen reusable, type safety, ekosistem kuat. |
| **State management** | (Contoh: Context API / Redux) | Manajemen state global untuk user, notifikasi, dan data inventori. |
| **Styling** | CSS Modules / Tailwind | Konsistensi UI dan kemudahan maintenance. |
| **Backend** | Node.js (Express) | Satu bahasa (JavaScript/TypeScript) untuk full-stack; cocok untuk API REST. |
| **Database** | PostgreSQL | Relasional, ACID, mendukung transaksi dan laporan kompleks. |
| **Auth** | JWT / OAuth2 (opsional) | Otentikasi dan otorisasi untuk multi-user. |
| **Deployment** | (Contoh: Docker, cloud provider) | Kontainerisasi dan skalabilitas. |

Detail versi dan dependency tercatat di `package.json` dan dokumen arsitektur terpisah.

---

## Fitur Utama

### 1. CRUD Barang
- **Create:** Tambah barang baru (kode, nama, satuan, kategori, stok minimum, dll.).
- **Read:** Daftar barang dengan filter, sort, dan pencarian; detail per barang.
- **Update:** Edit informasi barang; riwayat perubahan bisa dicatat (audit trail) jika diperlukan.
- **Delete:** Soft delete atau hard delete sesuai kebijakan; pastikan tidak ada transaksi tergantung.

### 2. Transaksi Masuk/Keluar
- Pencatatan **barang masuk** (pembelian, retur, transfer masuk) dan **barang keluar** (penjualan, retur keluar, pemakaian, rusak).
- Setiap transaksi mengupdate stok dan (opsional) nilai rata-rata atau FIFO.
- Validasi: tidak boleh keluar melebihi stok tersedia; notifikasi untuk stok di bawah minimum.

### 3. Dashboard & Grafik
- **Dashboard:** Ringkasan total barang, total nilai inventori, alert stok minimum, transaksi terakhir.
- **Grafik:** Tren stok per barang atau per kategori, perbandingan masuk vs keluar per periode (hari/minggu/bulan).
- Filter periode (tanggal mulai–akhir) untuk semua tampilan.

### 4. Export Excel/PDF
- **Excel:** Daftar barang, daftar transaksi, atau laporan ringkas per periode (bisa custom kolom).
- **PDF:** Laporan formal untuk audit atau print (misalnya kartu stok, summary bulanan).

---

## Arsitektur Singkat

- **Frontend:** SPA (Single Page Application) yang berkomunikasi dengan backend hanya lewat API REST (JSON).
- **Backend:** Layer route → controller → service → repository; validasi input dan penanganan error terpusat.
- **Database:** Tabel utama: `products`, `categories`, `transactions` (atau `stock_movements`), `users`; relasi dan indeks didesain untuk query laporan dan filter.

Detail diagram dan penamaan tabel ada di dokumen **Arsitektur & Database Schema**.

---

## Timeline (Estimasi)

| Fase | Scope | Durasi (estimasi) |
|------|--------|-------------------|
| **Fase 1 — MVP** | Auth, CRUD barang, transaksi masuk/keluar, tampilan stok, dashboard dasar | 8 minggu |
| **Fase 2 — Laporan** | Grafik, filter periode, export Excel/PDF, notifikasi stok minimum | 4 minggu |
| **Fase 3 — Integrasi** | Integrasi dengan sistem lain (e.g. kasir, akuntansi), optimasi performa, deployment production | 2 minggu |

Total estimasi **±14 minggu** dari kick-off sampai production; bisa disesuaikan dengan prioritas dan sumber daya.

---

## Risiko & Asumsi

- **Asumsi:** Pengguna memiliki pemahaman dasar inventori (stok, satuan, kategori); kebutuhan laporan tidak berubah drastis di tengah jalan.
- **Risiko:** Perubahan regulasi atau proses bisnis yang mempengaruhi format laporan; mitigasi dengan desain laporan yang konfigurasi (filter, kolom) sebanyak mungkin.

---

## Dokumen Terkait

- **Arsitektur & Database Schema**
- **API Specification (OpenAPI)**
- **User Guide** (setelah rilis)
- **Runbook Deployment**

---

*Dokumen ini hidup (living document) dan akan diperbarui seiring perkembangan proyek.*
