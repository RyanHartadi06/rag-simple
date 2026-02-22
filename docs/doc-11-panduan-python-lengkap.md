# Panduan Lengkap Python untuk Pemula

Python adalah bahasa pemrograman serba guna yang populer untuk pemula karena sintaksnya yang mudah dibaca dan ekosistem perpustakaannya yang kaya. Dokumen ini mencakup dasar-dasar sampai konsep menengah.

---

## Mengapa Python?

Python dirancang dengan filosofi "readability counts". Kode Python sering terlihat seperti pseudocode: dekat dengan bahasa manusia. Keunggulan utama:

- **Mudah dipelajari** — Kurva belajar landai; cocok untuk pemula.
- **Serba guna** — Web (Django, Flask), data science (pandas, NumPy), ML (scikit-learn, TensorFlow), otomasi, scripting.
- **Komunitas besar** — Banyak tutorial, forum, dan perpustakaan open source.
- **Cross-platform** — Berjalan di Windows, macOS, Linux.

---

## Instalasi

### Windows
1. Unduh installer dari [python.org](https://www.python.org/downloads/).
2. Jalankan installer; **centang "Add Python to PATH"**.
3. Verifikasi: buka Command Prompt, ketik `python --version` dan `pip --version`.

### macOS / Linux
Banyak sistem sudah menyertakan Python 3. Cek dengan `python3 --version`. Untuk instalasi terbaru:
- macOS: `brew install python3`
- Ubuntu/Debian: `sudo apt update && sudo apt install python3 python3-pip`

### Environment (Opsional tapi Disarankan)
Gunakan virtual environment agar dependency per proyek terpisah:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install requests
```

---

## Tipe Data Dasar

### Angka
- **int** — Bilangan bulat: `42`, `-7`.
- **float** — Bilangan desimal: `3.14`, `-0.5`.

### Teks
- **str** — String: `"hello"`, `'world'`, `"""multi line"""`. Immutable.

### Boolean
- **bool** — `True` atau `False`. Perhatikan huruf kapital.

### None
- **NoneType** — Merepresentasikan “tanpa nilai”: `x = None`.

### Konversi
```python
int("42")    # 42
float("3.14") # 3.14
str(100)     # "100"
```

---

## Variabel dan Penamaan

- Nama variabel boleh huruf, angka, underscore; tidak boleh diawali angka.
- Konvensi: gunakan `snake_case` untuk variabel dan fungsi; `PascalCase` untuk kelas.
- Python bersifat dynamic typing: tipe tidak dideklarasikan, tapi tetap ada saat runtime.

```python
nama = "Budi"
umur = 25
tinggi = 1.75
```

---

## Operator

- **Aritmetika:** `+`, `-`, `*`, `/`, `//` (floor), `%` (modulo), `**` (pangkat).
- **Perbandingan:** `==`, `!=`, `<`, `>`, `<=`, `>=`. Hasilnya `bool`.
- **Logical:** `and`, `or`, `not`.
- **Keanggotaan:** `in`, `not in` — untuk cek di string/list/set/dict.

---

## String: Operasi Umum

- Penggabungan: `"Hello" + " " + "World"`.
- Repeat: `"ab" * 3` → `"ababab"`.
- Indexing: `s[0]`, `s[-1]` (karakter terakhir).
- Slicing: `s[1:4]`, `s[:3]`, `s[2:]`, `s[::-1]` (reverse).
- Method: `.lower()`, `.upper()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.startswith()`, `.endswith()`.
- Format: f-string `f"Nama: {nama}, Umur: {umur}"` atau `.format()`.

---

## Struktur Kontrol

### if / elif / else
```python
if nilai >= 80:
    grade = "A"
elif nilai >= 70:
    grade = "B"
else:
    grade = "C"
```

### for
```python
for i in range(5):
    print(i)  # 0,1,2,3,4

for item in ["a", "b", "c"]:
    print(item)

for k, v in {"a": 1, "b": 2}.items():
    print(k, v)
```

### while
```python
n = 0
while n < 5:
    print(n)
    n += 1
```

### break dan continue
- `break` — Keluar dari loop.
- `continue` — Lewat ke iterasi berikutnya.

---

## List (Daftar)

- Ordered, mutable, boleh duplikat. `lst = [1, 2, 3]`.
- Indexing dan slicing sama seperti string.
- Method: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.count()`, `.index()`.
- List comprehension: `[x**2 for x in range(5)]` → `[0,1,4,9,16]`.
- Bisa nested: `matrix = [[1,2],[3,4]]`.

---

## Tuple

- Ordered, **immutable**. `t = (1, 2, 3)` atau `t = 1, 2, 3`.
- Berguna untuk data yang tidak boleh diubah dan untuk unpacking: `a, b = (1, 2)`.
- Satu elemen: `(1,)` — perlu koma.

---

## Set (Himpunan)

- Unordered, **unique** (no duplicate), mutable. `s = {1, 2, 3}`.
- Operasi: union `|`, intersection `&`, difference `-`, symmetric difference `^`.
- Method: `.add()`, `.remove()`, `.discard()`, `.union()`, `.intersection()`.
- Berguna untuk deduplikasi dan cek keanggotaan dengan cepat.

---

## Dictionary (Dict)

- Pasangan key–value; key unik, biasanya immutable. `d = {"nama": "Budi", "umur": 25}`.
- Akses: `d["nama"]` atau `d.get("nama", default)`.
- Method: `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`, `.get()`.
- Dict comprehension: `{x: x**2 for x in range(5)}`.

---

## Fungsi

```python
def greet(nama, salam="Halo"):
    return f"{salam}, {nama}!"

greet("Budi")           # "Halo, Budi!"
greet("Budi", "Hi")     # "Hi, Budi!"
```

- **Default argument** — Nilai default hanya dievaluasi sekali; hindari mutable default (misalnya `def f(a=[])`).
- ***args** — Menerima tuple argumen posisional. **kwargs** — Menerima dict argumen keyword.
- **return** — Mengembalikan satu nilai (atau tuple untuk banyak nilai). Tanpa return → `None`.

---

## Scope dan LEGB

- **L**ocal, **E**nclosing (nonlocal), **G**lobal, **B**uilt-in.
- Baca variabel global bisa langsung; untuk **assign** perlu `global x` (atau `nonlocal x` di dalam nested function).

---

## Modul dan Import

- Satu file `.py` = satu modul.
- `import modul` — Pakai: `modul.fungsi()`.
- `from modul import fungsi` — Langsung `fungsi()`.
- `from modul import *` — Tidak disarankan (namespace polusi).
- Package = folder berisi `__init__.py` (Python 3.3+ bisa tanpa untuk namespace package).

---

## Penanganan File

```python
# Context manager (disarankan)
with open("file.txt", "r", encoding="utf-8") as f:
    isi = f.read()

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

- Mode: `"r"` (read), `"w"` (write, overwrite), `"a"` (append), `"rb"`/`"wb"` (binary).
- Selalu spesifikasi `encoding` untuk teks (misalnya `utf-8`).

---

## Exception Handling

```python
try:
    hasil = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
except (TypeError, ValueError) as e:
    print("Error lain:", e)
else:
    print("Tidak ada error")
finally:
    print("Selalu dijalankan")
```

- **raise** — Melempar exception: `raise ValueError("Pesan")`.
- Buat exception custom dengan mewarisi dari `Exception`.

---

## Kelas (OOP Dasar)

```python
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        return f"Saya {self.nama}, {self.umur} tahun."

class Mahasiswa(Orang):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
```

- **Encapsulation** — Atribut private (konvensi: `_nama` atau `__nama`).
- **Inheritance** — `super()` untuk memanggil method parent.
- **Polymorphism** — Method overriding; duck typing ("if it walks like a duck...").

---

## Lanjutan (Ringkas)

- **Decorator** — Fungsi yang membungkus fungsi lain: `@decorator` di atas definisi fungsi.
- **Generator** — Fungsi dengan `yield`; lazy iteration, hemat memori.
- **Context manager** — `with`; implement `__enter__` dan `__exit__`.
- **Type hints** — `def f(x: int) -> str:` (opsional, untuk dokumentasi dan tooling).

---

## Sumber Belajar

- Dokumentasi resmi: [docs.python.org](https://docs.python.org/3/).
- Buku: *Automate the Boring Stuff with Python* (gratis online).
- Praktek: LeetCode, HackerRank, proyek kecil (script otomasi, web scraping, API).

---

*Dengan dasar ini Anda bisa melanjutkan ke topik seperti Django/Flask, pandas, atau machine learning.*
