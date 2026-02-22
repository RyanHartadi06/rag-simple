# Arsitektur Microservices — Konsep, Kelebihan, dan Tantangan

Arsitektur microservices memecah aplikasi menjadi sekumpulan layanan kecil yang independen, masing-masing berjalan dalam proses sendiri dan berkomunikasi lewat API (biasanya HTTP/REST atau message queue). Dokumen ini membahas konsep, manfaat, trade-off, dan praktik umum.

---

## Monolith vs Microservices

### Monolith
- Satu codebase, satu deployment unit. Semua modul (UI, bisnis logic, akses data) dalam satu aplikasi.
- **Kelebihan:** Sederhana untuk dikembangkan dan di-deploy; transaksi dan debugging lebih mudah; cocok untuk tim kecil dan produk awal.
- **Kekurangan:** Skala terbatas (harus scale seluruh aplikasi); satu bug bisa menjatuhkan semua; teknologi terikat satu stack; deployment dan release sering “all or nothing”.

### Microservices
- Aplikasi dipecah menjadi banyak layanan (service). Setiap layanan punya tanggung jawab bisnis yang jelas (misalnya: layanan user, layanan order, layanan notifikasi).
- **Kelebihan:** Skala per layanan; tim bisa bekerja paralel dan memilih teknologi berbeda per layanan; kegagalan satu layanan tidak harus menjatuhkan seluruh sistem; deployment independen.
- **Kekurangan:** Kompleksitas operasional (deployment, monitoring, jaringan); konsistensi data dan transaksi lintas layanan lebih sulit; debugging dan tracing lebih rumit.

---

## Prinsip Dasar Microservices

1. **Single Responsibility** — Satu layanan fokus pada satu domain/bisnis (misalnya hanya mengelola “order”).
2. **Decentralized Data** — Setiap layanan punya datastore sendiri; hindari satu database raksasa yang dipakai semua layanan (shared database antipattern).
3. **Independence** — Layanan bisa di-deploy, di-scale, dan di-ganti teknologi secara independen.
4. **Communication via API** — Layanan berkomunikasi lewat API yang terdefinisi (REST, gRPC) atau message (event-driven).
5. **Failure Isolation** — Desain agar kegagalan satu layanan tidak merambat (circuit breaker, timeout, fallback).

---

## Komunikasi Antar Layanan

### Synchronous (Request–Response)
- **REST over HTTP** — Paling umum; stateless, mudah di-debug. Kekurangan: coupling temporal (pemanggil harus menunggu).
- **gRPC** — Berbasis HTTP/2, binary; cocok untuk performa tinggi dan streaming. Perlu definisi protobuf.

Synchronous cocok ketika pemanggil benar-benar butuh respons segera (misalnya “dapatkan detail user”).

### Asynchronous (Event / Message)
- **Message queue** (RabbitMQ, Kafka, AWS SQS) — Layanan mempublikasikan event; layanan lain subscribe. Pemanggil tidak menunggu.
- **Event-driven** — Layanan bereaksi pada event (misalnya “OrderCreated”); mengurangi coupling dan memungkinkan skalabilitas yang lebih fleksibel.

Asynchronous cocok untuk notifikasi, audit log, atau alur yang boleh eventual consistency.

### Pilihan
- Hindari chatty communication (banyak panggilan kecil); pertimbangkan API yang lebih “chunky”.
- Gunakan idempotency dan retry dengan backoff untuk menghadapi kegagalan jaringan.

---

## Data dan Konsistensi

- **Database per service** — Setiap layanan punya DB sendiri; tidak ada akses langsung ke DB layanan lain. Ini memaksa boundary yang jelas dan menghindari coupling lewat schema.
- **Saga pattern** — Untuk transaksi bisnis yang melibatkan beberapa layanan: urutan langkah (local transaction + kompensasi jika gagal) atau choreography (masing-masing layanan bereaksi event dan memicu langkah berikutnya).
- **Eventual consistency** — Sistem menerima bahwa data bisa tidak konsisten sesaat; konsistensi dicapai setelah event diproses. Perlu desain yang eksplisit dan idempotent consumer.

---

## Service Discovery & Load Balancing

- Layanan perlu menemukan satu sama lain (nama/host/port). **Service discovery** bisa:
  - **Client-side** — Klien bertanya ke registry (e.g. Consul, Eureka) lalu memilih instance.
  - **Server-side** — Load balancer atau mesh (e.g. Kubernetes Service, Istio) yang mengarahkan lalu lintas ke instance yang sehat.
- Health check: registry atau orchestrator memantau liveness/readiness dan hanya mengarahkan lalu lintas ke instance yang sehat.

---

## API Gateway

- Satu titik masuk untuk klien (web, mobile). Gateway menangani:
  - **Routing** ke layanan backend.
  - **Auth** (validasi token, API key).
  - **Rate limiting**, caching, logging.
  - **Aggregation** (opsional): menggabungkan beberapa panggilan ke layanan menjadi satu respons untuk klien.
- Contoh: Kong, AWS API Gateway, Azure API Management, atau custom di Kubernetes (Ingress + auth).

---

## Observability

- **Logging** — Terstruktur (JSON), dengan correlation ID yang sama untuk satu request di semua layanan.
- **Metrics** — Latency, throughput, error rate per layanan/endpoint; biasanya di Prometheus + Grafana atau solusi cloud.
- **Tracing** — Distributed tracing (e.g. Jaeger, Zipkin) untuk mengikuti satu request melewati banyak layanan; membantu debug dan analisis latency.
- **Health endpoint** — Setiap layanan menyediakan `/health` atau serupa untuk liveness/readiness.

---

## Deployment & Orchestration

- **Container (Docker)** — Standar untuk paket layanan; konsisten antara dev dan prod.
- **Orchestration (Kubernetes, ECS)** — Deployment, scaling, healing, rolling update. Kubernetes juga menyediakan Service, Ingress, ConfigMap, Secret.
- **CI/CD** — Pipeline per layanan: build → test → push image → deploy. Setiap layanan bisa punya release cycle sendiri.

---

## Kapan Memilih Microservices?

- **Cocok:** Tim besar, domain jelas terpisah, kebutuhan scale berbeda per bagian, kebutuhan release independen tinggi.
- **Tidak terburu:** Mulai dengan monolith yang modular; pecah menjadi microservices ketika ada pain (scale, deployment, ownership tim) yang jelas. “Microservices first” tanpa kebutuhan yang jelas sering menambah kompleksitas tanpa manfaat proporsional.

---

## Ringkasan Praktik

- Satu layanan = satu domain/bounded context.
- Komunikasi lewat API yang stabil; versioning API.
- Data per layanan; transaksi lintas layanan lewat saga atau eventual consistency.
- Observability dari hari pertama: log, metric, trace.
- Otomasi deployment dan testing; failure injection (chaos engineering) untuk validasi resilience.

---

*Microservices adalah pilihan arsitektur yang powerful tapi mahal; pilih ketika manfaat operasional dan organisasional benar-benar terasa.*
