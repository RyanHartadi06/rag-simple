# Tutorial Dasar Git — Dari Nol sampai Kolaborasi

Tutorial ini mengasumsikan Anda belum atau baru sedikit menggunakan Git. Setelah selesai, Anda diharapkan bisa menginisialisasi repo, commit, membuat branch, dan sinkronisasi dengan remote (misalnya GitHub/GitLab).

---

## Apa Itu Git?

Git adalah **sistem kontrol versi terdistribusi** (Distributed Version Control System). Fungsinya antara lain:

- Menyimpan riwayat perubahan kode (siapa, kapan, apa yang berubah).
- Memungkinkan kerja paralel lewat branch dan merge.
- Memudahkan kolaborasi lewat push/pull ke server (remote).

Bukan satu-satunya VCS, tapi paling banyak dipakai di industri.

---

## Instalasi

- **Windows:** Unduh dari [git-scm.com](https://git-scm.com) atau pakai package manager (e.g. winget, Chocolatey).
- **macOS:** `brew install git` atau Xcode Command Line Tools.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) atau `sudo dnf install git` (Fedora).

Cek instalasi: `git --version`.

---

## Konfigurasi Awal (Sekali Saja)

```bash
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
```

Nama dan email ini akan tercantum di setiap commit. Untuk cek: `git config --list`.

---

## Inisialisasi Repo & Commit Pertama

### Buat repo baru di folder saat ini

```bash
git init
```

Ini membuat folder `.git` (tersembunyi) yang menyimpan seluruh riwayat.

### Tambahkan file ke staging

```bash
git add nama_file.txt
git add folder/
git add .                    # semua file yang berubah
```

### Commit (simpan snapshot)

```bash
git commit -m "Initial commit"
git commit -m "Fix: perbaikan typo di README"
```

Pesan commit sebaiknya **jelas dan ringkas**: apa yang berubah dan mengapa (jika perlu). Hindari pesan generik seperti "update" atau "fix".

### Cek status

```bash
git status
git log --oneline            # riwayat commit singkat
```

---

## Branch: Bekerja di Cabang

Branch memungkinkan Anda mengembangkan fitur atau perbaikan tanpa mengacaukan `main`/`master`.

### Buat dan pindah branch

```bash
git branch feature-x         # buat branch bernama feature-x
git checkout feature-x       # pindah ke branch feature-x
```

Atau satu perintah:

```bash
git checkout -b feature-x
```

Di Git versi baru:

```bash
git switch -c feature-x
```

### Gabungkan branch ke branch saat ini (merge)

Misalnya Anda ada di `main` dan ingin menggabungkan `feature-x`:

```bash
git checkout main
git merge feature-x
```

Jika tidak ada konflik, merge selesai. Jika ada konflik, Git akan meminta Anda menyelesaikan di file yang bertabrakan, lalu `git add` dan `git commit`.

### Hapus branch (setelah di-merge)

```bash
git branch -d feature-x
```

---

## Remote: Sinkronisasi dengan Server

### Tambah remote

```bash
git remote add origin https://github.com/username/repo-name.git
```

`origin` adalah nama standar untuk remote utama. Cek: `git remote -v`.

### Push (kirim commit ke server)

```bash
git push -u origin main
```

`-u` men-set upstream agar ke depannya cukup `git push`. Ganti `main` jika branch default Anda lain (misalnya `master`).

### Pull (ambil perubahan dari server)

```bash
git pull origin main
```

Ini biasanya sama dengan `git fetch origin` lalu `git merge origin/main`. Selalu pull sebelum mulai kerja atau sebelum push jika ada orang lain yang push.

### Clone (unduh repo yang sudah ada)

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

Ini sekaligus menambah remote `origin` dan checkout branch default.

---

## .gitignore

Agar file tertentu **tidak** ikut di-track (binary, env, cache, dependency):

1. Buat file `.gitignore` di root repo.
2. Tulis pola per baris, contoh:

```gitignore
node_modules/
.env
*.log
dist/
.DS_Store
```

Setelah itu, `git add .` tidak akan memasukkan file yang match. File yang sudah pernah di-add harus di-untrack dulu: `git rm --cached nama_file`.

---

## Tips Singkat

- **Commit sering, pesan jelas** — Commit yang kecil dan fokus memudahkan rollback dan review.
- **Pull sebelum push** — Kurangi konflik dan merge yang rumit.
- **Gunakan branch untuk fitur/fix** — Jangan langsung commit di `main` jika tim punya aturan.
- **Jangan commit rahasia** — Gunakan `.env` dan `.gitignore`; jangan masukkan password/API key ke repo.
- **Baca output Git** — Pesan error dan status sering menjelaskan langkah berikutnya.

---

## Perintah Cepat (Cheat Sheet)

| Tujuan | Perintah |
|--------|----------|
| Status | `git status` |
| Riwayat | `git log --oneline` |
| Add semua | `git add .` |
| Commit | `git commit -m "Pesan"` |
| Branch baru | `git checkout -b nama-branch` |
| Pindah branch | `git checkout nama-branch` |
| Merge | `git merge nama-branch` |
| Push | `git push origin main` |
| Pull | `git pull origin main` |

---

*Untuk topik lanjutan (rebase, stash, tag, conflict resolution) bisa dilanjutkan di tutorial terpisah.*
