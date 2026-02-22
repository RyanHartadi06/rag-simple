# RAG — Retrieval-Augmented Generation

Aplikasi RAG berbasis **LangChain** dan **Ollama** yang mengindeks dokumen Markdown, lalu menjawab pertanyaan berdasarkan konten dokumen melalui API Flask.

## Fitur

- **Ingest** — Memuat semua file `.md` di folder `docs`, memecah menjadi chunk, dan menyimpan embedding ke **Chroma** (vector store).
- **RAG Chain** — Mengambil chunk relevan untuk pertanyaan, lalu menghasilkan jawaban dengan **Ollama** (LLM).
- **API** — Endpoint kesehatan, tanya-jawab, dan re-ingest via **Flask**.

## Persyaratan

- **Python 3.12+**
- **Ollama** berjalan di mesin Anda ([install Ollama](https://ollama.com))
- Model Ollama yang diunduh:
  - **LLM:** `llama3.2` (atau model lain, sesuaikan di `.env`)
  - **Embedding:** `nomic-embed-text`

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Instalasi

1. Clone atau masuk ke folder proyek:

   ```bash
   cd rag
   ```

2. Buat virtual environment dan aktifkan:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate   # macOS/Linux
   ```

3. Pasang dependensi:

   ```bash
   pip install -e .
   ```

4. Salin `.env.example` ke `.env` (atau buat `.env`) dan sesuaikan:

   ```env
   OLLAMA_BASE_URL=http://localhost:11434
   LLM_MODEL=llama3.2
   EMBED_MODEL=nomic-embed-text
   DOCS_DIR=./docs
   DB_DIR=./db
   ```

## Menjalankan Aplikasi

1. Pastikan **Ollama** sudah jalan dan model LLM + embedding sudah di-pull.

2. Jalankan server Flask:

   ```bash
   python app.py
   ```

   Server berjalan di `http://localhost:5000`. Jika folder `db` belum ada, ingest akan dijalankan otomatis saat startup.

## API

| Method | Endpoint   | Deskripsi |
|--------|------------|-----------|
| GET    | `/health` | Cek status layanan. |
| POST   | `/ask`     | Tanya jawab RAG. Body JSON: `{"question": "Pertanyaan Anda"}`. |
| POST   | `/ingest`  | Re-index ulang semua dokumen di `DOCS_DIR` (berguna setelah menambah/ubah file MD). |

### Contoh `/ask`

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Apa itu Git?\"}"
```

Contoh respons:

```json
{
  "question": "Apa itu Git?",
  "answer": "...",
  "sources": ["./docs/doc-06-tutorial-git-basics.md", ...]
}
```

## Struktur Proyek

```
rag/
├── app.py          # Flask API (health, ask, ingest)
├── rag.py          # Load docs, split, embed, Chroma, RAG chain
├── docs/           # Dokumen Markdown yang di-index
├── db/             # Penyimpanan Chroma (vector store)
├── .env            # Konfigurasi (OLLAMA_*, DOCS_DIR, DB_DIR)
├── pyproject.toml  # Dependensi Python
└── README.md
```

## Menambah Dokumen

1. Letakkan file `.md` di folder `docs/`.
2. Panggil **POST** `/ingest` untuk memperbarui index, atau restart aplikasi (jika `db` dihapus maka ingest otomatis jalan lagi).

## Variabel Lingkungan

| Variabel         | Default              | Keterangan                    |
|------------------|----------------------|-------------------------------|
| `OLLAMA_BASE_URL`| `http://localhost:11434` | URL dasar Ollama.        |
| `LLM_MODEL`      | `llama3.2`           | Model LLM untuk jawaban.      |
| `EMBED_MODEL`    | `nomic-embed-text`   | Model embedding.              |
| `DOCS_DIR`       | `./docs`             | Folder sumber dokumen `.md`.   |
| `DB_DIR`         | `./db`               | Folder persist Chroma.        |

## Menjalankan RAG dari CLI (opsional)

Untuk uji coba langsung dari terminal tanpa API:

```bash
python rag.py
```

Ini memuat vector store dan menjalankan satu pertanyaan contoh ("Apa Itu Git?"). Edit baris terakhir di `rag.py` untuk mengubah pertanyaan.
