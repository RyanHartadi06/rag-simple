# Pemrograman Fungsional — Dasar dan Konsep

Pemrograman fungsional (FP) adalah paradigma yang menekankan evaluasi fungsi, imutabilitas, dan menghindari side effect. Dokumen ini membahas konsep inti dan penerapan praktis dalam bahasa yang mendukung FP (misalnya JavaScript, Python, atau bahasa fungsional murni).

---

## Ciri Utamanya

- **First-class functions** — Fungsi bisa disimpan di variabel, dikirim sebagai argumen, dan dikembalikan sebagai nilai.
- **Imutabilitas** — Data tidak diubah in-place; "perubahan" menghasilkan nilai/struktur baru. Mengurangi bug terkait state bersama.
- **Mengurangi side effect** — Fungsi sebisa mungkin pure: output hanya tergantung input; tidak mengubah state global atau I/O di dalam fungsi (I/O bisa diisolasi di edge).
- **Deklaratif** — Fokus pada "apa" yang diinginkan, bukan "bagaimana" langkah demi langkah (imperatif). Contoh: map, filter, reduce alih-alih loop manual.

---

## Pure Function

- **Pure function** — Untuk input yang sama, selalu mengembalikan output yang sama; tidak ada side effect (tidak mengubah variabel global, tidak baca waktu/random, tidak I/O di dalam).
- **Manfaat** — Mudah di-test, mudah di-reason tentang, dan bisa di-cache (memoization). Komposisi fungsi pure tetap pure.

Contoh pure: `const add = (a, b) => a + b;`  
Contoh impure: fungsi yang mengubah variabel global atau memanggil `Math.random()`.

---

## Imutabilitas

- **Jangan ubah data lama** — Buat salinan atau struktur baru. Di JavaScript: spread operator, `map`/`filter` yang mengembalikan array baru; hindari `push`/`splice` pada array yang dipakai bersama.
- **Struktur persistent** — Di bahasa FP murni (Haskell, Clojure) struktur data dirancang untuk "perubahan" yang efisien tanpa menyalin seluruh data (persistent data structure). Di JS/Python, kita sering pakai salinan untuk struktur sederhana.
- **Manfaat** — Predictable; aman untuk concurrency; memudahkan time-travel debug dan undo.

---

## Higher-Order Function

- **Higher-order function** — Fungsi yang menerima fungsi sebagai argumen atau mengembalikan fungsi.
- **Contoh:** `map`, `filter`, `reduce`, `forEach`. Contoh custom: fungsi yang menerima predicate dan mengembalikan filterer.

```javascript
const filter = (predicate) => (arr) => arr.filter(predicate);
const isEven = (n) => n % 2 === 0;
const filterEven = filter(isEven);
filterEven([1, 2, 3, 4]); // [2, 4]
```

---

## Map, Filter, Reduce

- **map(f)** — Transformasi setiap elemen; panjang array sama. `arr.map(x => x * 2)`.
- **filter(predicate)** — Menyaring elemen yang memenuhi kondisi. `arr.filter(x => x > 0)`.
- **reduce(f, initial)** — Menggabungkan semua elemen menjadi satu nilai. `arr.reduce((acc, x) => acc + x, 0)`.

Banyak operasi pada koleksi bisa diekspresikan dengan kombinasi map–filter–reduce; alur data jelas dan tanpa mutasi.

---

## Komposisi Fungsi

- **Compose** — Menggabungkan fungsi: `compose(f, g)(x) === f(g(x))`. Output satu fungsi jadi input fungsi berikutnya.
- **Pipe** — Urutan kiri ke kanan: `pipe(g, f)(x) === f(g(x))`. Lebih natural dibaca untuk beberapa orang.
- **Manfaat** — Membangun perilaku kompleks dari fungsi kecil; kode deklaratif dan modular.

---

## Closure

- **Closure** — Fungsi yang "mengingat" lingkungan tempat ia dibuat (variabel di scope luar). Dipakai untuk private state, factory, partial application.
- Contoh: fungsi yang mengembalikan fungsi counter; counter menyimpan state dalam closure.

---

## Recursion

- **Recursion** — Fungsi memanggil diri sendiri; base case menghentikan. Di FP, rekursi sering dipakai alih-alih loop.
- **Tail recursion** — Pemanggilan terakhir adalah pemanggilan rekursif; compiler/runtime bisa mengoptimasi (tail-call optimization). Di JS, dukungan terbatas; di bahasa seperti Haskell rekursi adalah idiomatik.

---

## Lazy Evaluation (Konsep)

- **Lazy** — Nilai dihitung hanya saat dibutuhkan. Contoh: generator, iterator, infinite list di Haskell. Menghemat memori dan memungkinkan struktur data tak hingga.
- Di bahasa non-lazy (JS, Python), kita pakai generator/iterator untuk efek serupa.

---

## Penerapan di JavaScript/TypeScript

- **Immutability** — Spread, `map`/`filter`/`reduce`; library seperti Immer untuk nested update.
- **Avoid mutation** — Jangan ubah parameter fungsi; return nilai baru.
- **Functional style** — Compose, pipe, curry; library seperti Ramda atau Lodash/fp.
- **React** — Komponen fungsional + hooks; state update lewat setState dengan nilai baru (immutable update).

---

## Ringkasan

- FP menekankan pure function, imutabilitas, dan komposisi. Manfaat: predictability, testability, dan reasoning yang lebih mudah.
- Higher-order function, map/filter/reduce, closure, dan komposisi adalah alat inti. Bisa diterapkan bertahap dalam bahasa imperatif tanpa beralih sepenuhnya ke bahasa fungsional murni.

---

*Memahami FP memperkaya toolbox; bahkan dalam kode imperatif, pola map/filter/reduce dan imutabilitas banyak dipakai.*
