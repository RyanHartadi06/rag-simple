# Spesifikasi Produk: Aplikasi Catatan (NoteFlow)

Dokumen ini mendeskripsikan produk aplikasi catatan dengan sinkronisasi cloud, target pengguna, fitur utama, batasan, dan target rilis.

---

## Nama & Positioning Produk

**Nama produk:** NoteFlow  
**Tagline (konsep):** Catatan dengan sinkronisasi cloud — tulis di mana saja, akses di mana saja.

**Positioning:** Aplikasi catatan untuk pengguna individu dan tim kecil yang menginginkan editor nyaman, organisasi dengan folder/tag, dan sinkronisasi lintas perangkat tanpa kompleksitas berlebihan. Bukan pengganti Notion/Confluence untuk wiki besar; fokus pada catatan pribadi dan tim kecil.

---

## Target Pengguna

- **Primary:** Mahasiswa dan profesional yang butuh mencatat meeting, ide, dan to-do dengan format rich text dan akses dari ponsel/laptop.
- **Secondary:** Tim kecil (5–15 orang) yang berbagi catatan proyek atau knowledge base sederhana.

---

## User Stories (Prioritas Tinggi)

### Manajemen catatan
- Sebagai **user**, saya ingin **membuat, mengedit, dan menghapus catatan** agar saya bisa mencatat ide dan informasi dengan fleksibel.
- Sebagai **user**, saya ingin **memformat teks** (bold, italic, underline, list berurut/tidak, heading) agar catatan saya terbaca dan terstruktur.
- Sebagai **user**, saya ingin **mencari catatan** berdasarkan kata kunci (judul dan isi) agar saya cepat menemukan informasi lama.

### Organisasi
- Sebagai **user**, saya ingin **mengelompokkan catatan ke dalam folder** agar saya bisa memisahkan topik (kerja, pribadi, proyek).
- Sebagai **user**, saya ingin **memberi tag pada catatan** agar satu catatan bisa masuk ke beberapa “kategori” tanpa duplikasi folder.
- Sebagai **user**, saya ingin **menyimpan catatan favorit/pin** di bagian atas daftar agar akses cepat ke catatan yang sering dipakai.

### Sinkronisasi & multi-perangkat
- Sebagai **user**, saya ingin **catatan saya tersinkronisasi** antar perangkat (web, Android, iOS) agar saya bisa baca dan edit di mana saja.
- Sebagai **user**, saya ingin **bekerja offline** dan perubahan tersinkron saat online agar saya tidak terganggu saat tidak ada jaringan.

### Kolaborasi (Fase lanjutan)
- Sebagai **user**, saya ingin **berbagi catatan** dengan orang lain (read-only atau edit) agar tim bisa mengakses dokumen bersama.
- Sebagai **user**, saya ingin **melihat riwayat versi** catatan agar saya bisa mengembalikan versi sebelumnya jika salah edit.

---

## Wireframe (Konsep Tingkat Tinggi)

```
+------------------+------------------------------------------+
|  Sidebar         |  Area editor utama                        |
|  - Logo NoteFlow |  - [Judul catatan]                        |
|  - [+ Catatan]   |  - [Toolbar: B I U list link]             |
|  - Cari          |  - [Isi catatan — rich text]              |
|  - Folder 1      |                                          |
|  - Folder 2      |  - Auto-save / terakhir disimpan: ...     |
|  - Tag           |                                          |
+------------------+------------------------------------------+
```

- **Sidebar:** Daftar catatan (bisa dikelompokkan folder/tag), tombol catatan baru, pencarian global.
- **Area utama:** Satu catatan aktif; toolbar format; isi editor WYSIWYG atau Markdown (tergantung keputusan teknis).
- **Responsif:** Di mobile, daftar dan editor bisa toggle (list view vs editor view).

---

## Batasan & Kebijakan

| Aspek | Batasan | Catatan |
|--------|---------|---------|
| Jumlah catatan per akun | Maks. 10.000 | Bisa dinaikkan untuk tier berbayar. |
| Ukuran per catatan | Maks. 1 MB teks | Lampiran dihitung terpisah. |
| Lampiran per catatan | Maks. 5 MB total per catatan | Format: gambar, PDF; batas jumlah per catatan TBD. |
| Penyimpanan total per akun | TBD (mis. 1 GB gratis) | Untuk free tier; upgrade untuk lebih. |

Batasan ini bisa berubah setelah riset kapasitas dan biaya infrastruktur.

---

## Non-Functional (Target)

- **Kecepatan:** Editor harus terasa responsif (input tanpa lag signifikan).
- **Offline:** Dukungan dasar: baca & edit terakhir yang tersinkron; konflik diselesaikan (last-write-wins atau prompt user).
- **Keamanan:** Data di-enkripsi in transit (TLS); opsi enkripsi at rest untuk tier berbayar (roadmap).
- **Ketersediaan:** Target uptime 99,5% untuk layanan core (catatan & sync).

---

## Versi & Timeline Target

- **v1.0 (MVP):** CRUD catatan, rich text, folder & tag, pencarian, sinkronisasi, akun & login. **Target: Q2 2025.**
- **v1.1:** Lampiran gambar/PDF, favorit/pin, peningkatan UX mobile.
- **v2.0:** Berbagi catatan, kolaborasi dasar, riwayat versi.

---

## Dokumen Terkait

- **Technical Design Document** (arsitektur, stack, API).
- **User Research Summary** (hasil wawancara/ survei calon user).
- **Competitor Comparison** (vs Notion, Google Keep, OneNote, dll.).

---

*Spesifikasi ini hidup dan dapat direvisi berdasarkan feedback stakeholder dan hasil riset.*
