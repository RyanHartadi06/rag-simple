# Docker dan Container — Dasar hingga Workflow

Container memungkinkan aplikasi berjalan dalam lingkungan yang konsisten dan terisolasi. Docker adalah platform populer untuk membangun, mendistribusikan, dan menjalankan container. Dokumen ini membahas konsep, perintah dasar, Dockerfile, dan workflow singkat.

---

## Mengapa Container?

- **Konsistensi** — "Runs on my machine" → "runs in this image". Dev, CI, dan production memakai image yang sama; mengurangi masalah environment.
- **Isolasi** — Proses dalam container terisolasi dari host dan container lain (namespace, cgroups). Satu host bisa menjalankan banyak container.
- **Efisiensi** — Container berbagi kernel host; lebih ringan daripada VM. Startup cepat.
- **Portabilitas** — Image bisa didorong ke registry (Docker Hub, ECR, GCR) dan di-pull di mana saja.

---

## Konsep Dasar

- **Image** — Template read-only: filesystem + metadata. Dibangun dari Dockerfile atau dari image dasar (base image).
- **Container** — Instance yang berjalan dari image; layer writable di atas image. Saat container dihapus, layer writable hilang (kecuali pakai volume).
- **Registry** — Penyimpanan image. Docker Hub publik; perusahaan pakai registry privat (ECR, GCR, Harbor).
- **Dockerfile** — Skrip untuk membangun image: FROM, RUN, COPY, ENTRYPOINT, dll.

---

## Instalasi

- **Windows/macOS** — Docker Desktop (GUI + CLI). WSL2 dipakai di Windows.
- **Linux** — `curl -fsSL https://get.docker.com | sh` atau pakai paket distro. Tambah user ke grup `docker` agar tidak perlu sudo.
- Cek: `docker --version`, `docker run hello-world`.

---

## Perintah Dasar

### Image
- `docker images` — Daftar image lokal.
- `docker pull <image>` — Unduh dari registry (default Docker Hub). Contoh: `docker pull nginx:alpine`.
- `docker rmi <image>` — Hapus image lokal.
- `docker build -t nama:tag .` — Build image dari Dockerfile di direktori saat ini; tag nama:tag.

### Container
- `docker run [options] <image>` — Buat dan jalankan container. Contoh: `docker run -d -p 8080:80 --name web nginx:alpine` (detached, map port 8080→80, nama "web").
- `docker ps` — Container yang sedang berjalan. `docker ps -a` — Semua termasuk yang berhenti.
- `docker stop <container>` — Hentikan (SIGTERM lalu SIGKILL). `docker start <container>` — Jalankan lagi.
- `docker rm <container>` — Hapus container (harus stop dulu, atau `docker rm -f`).
- `docker logs <container>` — Lihat log. `docker exec -it <container> sh` — Masuk ke shell di dalam container.

### Options umum run
- `-d` — Detached (background).
- `-p host:container` — Port mapping.
- `--name` — Nama container.
- `-e VAR=value` — Environment variable.
- `-v host_path:container_path` — Bind mount (persisten). `--mount` untuk opsi lebih rinci.
- `--rm` — Hapus container saat keluar (berguna untuk one-off).

---

## Dockerfile

Contoh untuk aplikasi Node:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

- **FROM** — Base image. Pilih yang ringan (alpine) jika memungkinkan.
- **WORKDIR** — Direktori kerja di dalam image.
- **COPY** — Salin file dari build context. Gunakan .dockerignore untuk mengecualikan node_modules, .git, dll.
- **RUN** — Perintah saat build (install paket, compile). Gabungkan RUN untuk mengurangi layer (kecuali untuk cache).
- **EXPOSE** — Dokumentasi port; tidak mempublikasikan port. Publikasi lewat `-p` saat run.
- **CMD** — Perintah default saat container dijalankan. Bentuk JSON array (exec form) disarankan.
- **ENTRYPOINT** — Mirip CMD; sulit di-override. CMD sering dipakai sebagai argumen untuk ENTRYPOINT.

Best practice: urutan dari yang jarang berubah ke yang sering (COPY dependency dulu, COPY kode terakhir); multi-stage build untuk mengurangi ukuran image (build di satu stage, hanya runtime di stage akhir).

---

## Volume dan Data Persisten

- **Volume** — Dikelola Docker; nama volume. `docker volume create nama`; `docker run -v nama:/path ...`.
- **Bind mount** — Map direktori host ke container. `-v /host/path:/container/path`. Berguna untuk development (live reload).
- Data di filesystem container bersifat sementara; untuk DB atau file penting, pakai volume atau bind mount.

---

## Jaringan

- **Default network** — Setiap container bisa resolve nama container lain di network yang sama (DNS otomatis).
- `docker network create nama` — Buat network. `docker run --network nama ...` — Masuk ke network.
- Bridge (default), host, none; untuk multi-container (app + DB) pakai custom network agar bisa saling resolve nama.

---

## Docker Compose

- **Compose** — Mendefinisikan multi-container dalam satu file YAML (`docker-compose.yml`). Satu perintah untuk build, run, stop.
- Contoh minimal: service `web` (image atau build), `db` (image postgres), environment, port, volume, network. `docker compose up -d`; `docker compose down`.
- Berguna untuk dev lokal dan testing integrasi; production sering pakai orchestrator (Kubernetes) atau layanan managed.

---

## Keamanan Singkat

- Jangan run container as root jika tidak perlu; gunakan USER di Dockerfile.
- Image dari sumber tepercaya; scan vulnerability (docker scan, Trivy).
- Jangan simpan rahasia di image; pakai secret (Docker secret, env dari orchestrator) atau volume.
- Batas resource: `--memory`, `--cpus` saat run.

---

## Ringkasan

- Image = template; container = instance. Build dengan Dockerfile; simpan di registry; run dengan volume untuk data persisten.
- Perintah dasar: build, run, ps, logs, exec, stop, rm. Compose untuk multi-container.
- Praktik: Dockerfile efisien (layer, multi-stage), .dockerignore, tidak root, tidak rahasia di image.

---

*Docker adalah fondasi untuk CI/CD dan deployment modern; kuasai dasar lalu lanjut ke orchestration jika perlu.*
