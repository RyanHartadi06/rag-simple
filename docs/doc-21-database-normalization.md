# Normalisasi Database — Konsep dan Bentuk Normal

Normalisasi adalah proses mengorganisasi skema database untuk mengurangi redundansi dan anomali (update, insert, delete) dengan memecah tabel ke bentuk normal. Dokumen ini membahas dependensi, bentuk normal (1NF–BCNF), dan trade-off denormalisasi.

---

## Tujuan Normalisasi

- **Mengurangi redundansi** — Data yang sama tidak disimpan berulang; menghemat ruang dan memudahkan maintenance.
- **Mengurangi anomali** — Update satu tempat; insert dan delete tidak menimbulkan inkonsistensi atau data "yatim".
- **Memperjelas relasi** — Satu fakta di satu tempat; integritas referensial lewat foreign key.

---

## Konsep Dasar

### Atribut dan Key
- **Superkey** — Himpunan atribut yang nilainya unik untuk setiap baris. Bisa berisi atribut berlebih.
- **Candidate key** — Superkey minimal (tidak ada subset yang masih superkey). Dipilih satu sebagai **primary key**.
- **Prime attribute** — Atribut yang termasuk dalam suatu candidate key.
- **Non-prime attribute** — Atribut yang tidak termasuk candidate key.

### Dependensi
- **Functional dependency (FD)** — A → B: jika nilai A sama, nilai B pasti sama. A "menentukan" B.
- **Full functional dependency** — A → B dan tidak ada subset A yang menentukan B (untuk composite key).
- **Transitive dependency** — A → B dan B → C, maka A → C (transitif melalui B).
- **Partial dependency** — Non-prime tergantung pada bagian (bukan seluruh) candidate key; hanya relevan jika key komposit.

---

## Bentuk Normal

### First Normal Form (1NF)
- Setiap atribut bernilai **atomic** (tidak ada multivalue atau repeating group).
- Setiap baris **unik** (ada candidate key).
- Contoh melanggar: kolom "Telepon" berisi "081, 082" atau kolom "Hobi" berisi list. Perbaikan: pecah ke baris terpisah atau tabel terpisah.

### Second Normal Form (2NF)
- Sudah **1NF**.
- Semua non-prime attribute **fully dependent** pada primary key (tidak ada partial dependency).
- Contoh: Tabel (OrderID, ProductID, ProductName, Qty). ProductName hanya tergantung ProductID, bukan (OrderID, ProductID). Perbaikan: pisah Product ke tabel Product(ProductID, ProductName); Order detail hanya (OrderID, ProductID, Qty).

### Third Normal Form (3NF)
- Sudah **2NF**.
- Tidak ada **transitive dependency**: non-prime tidak tergantung pada non-prime lain. Setiap non-prime hanya tergantung pada candidate key.
- Contoh: (EmployeeID, DeptID, DeptName). DeptName tergantung DeptID, DeptID tergantung EmployeeID → transitive. Perbaikan: pisah Department(DeptID, DeptName); Employee(EmployeeID, DeptID).

### Boyce-Codd Normal Form (BCNF)
- Setiap **determinant** (sisi kiri FD nontrivial) adalah **candidate key**. Lebih ketat dari 3NF; menangani kasus di mana ada lebih dari satu candidate key dan FD yang melibatkan overlap.
- Jika skema sudah 3NF dan hanya ada satu candidate key, maka sudah BCNF.

### Bentuk Normal Lebih Tinggi
- **4NF** — Menangani multi-valued dependency (MVD).
- **5NF** — Menangani join dependency. Jarang didesain manual; pemahaman 1NF–BCNF cukup untuk banyak aplikasi.

---

## Proses Normalisasi (Praktis)

1. Mulai dari kebutuhan (entitas, atribut, relasi).
2. Buat tabel dalam 1NF (atomic, unique rows).
3. Cari FD; hilangkan partial dependency → 2NF.
4. Hilangkan transitive dependency → 3NF.
5. Cek determinant; pastikan setiap FD nontrivial punya determinant candidate key → BCNF jika perlu.
6. Tentukan primary key dan foreign key; nama relasi yang jelas.

---

## Denormalisasi (Trade-off)

- **Normalisasi penuh** — Minim redundansi; banyak join; bisa lambat untuk query read-heavy dan analitik.
- **Denormalisasi** — Menyimpan data yang "sudah di-join" (redundansi) untuk mempercepat read; update harus menjaga konsistensi (trigger, aplikasi, atau eventual).
- **Kapan denormalisasi** — Read sangat dominan; query kompleks yang sering; reporting/warehouse. Lakukan dengan sadar dan terdokumentasi.

---

## Ringkasan

- 1NF: atomic, unique rows.
- 2NF: 1NF + no partial dependency.
- 3NF: 2NF + no transitive dependency.
- BCNF: every determinant is candidate key.
- Normalisasi mengurangi redundansi dan anomali; denormalisasi dipakai untuk performa read dengan trade-off konsistensi dan maintenance.

---

*Pemahaman normalisasi membantu desain database yang bersih dan maintainable; untuk OLAP/warehouse, denormalisasi sering dipakai dengan sengaja.*
