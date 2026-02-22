# Cloud Computing — Overview Model dan Layanan

Cloud computing adalah penyediaan sumber daya komputasi (server, storage, network, aplikasi) sebagai layanan melalui internet, dengan model bayar-pakai dan skalabilitas on-demand. Dokumen ini membahas model layanan (IaaS, PaaS, SaaS), model deployment, dan contoh penyedia.

---

## Manfaat Cloud

- **Elastisitas** — Scale up/down sesuai beban; tidak perlu beli hardware untuk puncak sementara.
- **Bayar sesuai pemakaian** — Mengurangi capex; biaya operasional lebih predictable (meski perlu monitoring agar tidak membengkak).
- **Kecepatan** — Provision resource dalam menit; deployment dan iterasi lebih cepat.
- **Global reach** — Data center di banyak region; latency rendah dan compliance (data residency).
- **Managed services** — Database, queue, ML, analytics sebagai layanan; mengurangi operasi "undifferentiated heavy lifting".

---

## Model Layanan

### IaaS (Infrastructure as a Service)
- **Apa** — Virtual machine, storage, network; Anda mengelola OS, middleware, dan aplikasi. Penyedia mengelola fisik dan virtualisasi.
- **Contoh** — AWS EC2, Azure VMs, Google Compute Engine, DigitalOcean Droplets.
- **Kontrol** — Tinggi; tanggung jawab konfigurasi dan keamanan OS ke atas. Cocok ketika butuh kontrol penuh atau migrasi lift-and-shift.

### PaaS (Platform as a Service)
- **Apa** — Platform untuk develop, run, dan manage aplikasi; runtime, database, queue sering disediakan. Anda fokus kode; penyedia mengelola OS, patch, scaling.
- **Contoh** — AWS Elastic Beanstalk, Azure App Service, Google App Engine, Heroku.
- **Kontrol** — Sedang; kurang fleksibel untuk konfigurasi low-level; cocok untuk aplikasi standar (web app, API) yang ingin cepat deploy.

### SaaS (Software as a Service)
- **Apa** — Aplikasi siap pakai; diakses lewat browser atau API. Penyedia mengelola semuanya.
- **Contoh** — Gmail, Slack, Salesforce, Notion, Zoom.
- **Kontrol** — Hanya konfigurasi dalam aplikasi; cocok untuk produktivitas dan bisnis process tanpa maintain software.

### FaaS (Function as a Service) / Serverless
- **Apa** — Jalankan fungsi (kode) tanpa manage server; trigger by event (HTTP, queue, schedule). Scale to zero; bayar per eksekusi.
- **Contoh** — AWS Lambda, Azure Functions, Google Cloud Functions.
- **Kontrol** — Hanya kode dan konfigurasi fungsi; cocok untuk event-driven, backend API ringan, dan workload sporadis.

---

## Model Deployment

- **Public cloud** — Resource shared; multi-tenant; penyedia (AWS, Azure, GCP, dll.). Paling elastis dan hemat; compliance dan security di tangan penyedia + konfigurasi Anda.
- **Private cloud** — Dedicated untuk satu organisasi; on-premise atau hosted. Kontrol dan compliance maksimal; biaya dan operasi lebih besar.
- **Hybrid** — Gabungan public dan private; misalnya data sensitif on-premise, burst atau front-end di public cloud. **Multi-cloud** — Lebih dari satu penyedia public; hindari vendor lock-in; tambah kompleksitas operasi.

---

## Layanan Umum (Contoh AWS-centric)

- **Compute** — EC2 (VM), Lambda (serverless), ECS/EKS (container).
- **Storage** — S3 (object), EBS (block untuk EC2), Glacier (archive).
- **Database** — RDS (relasional managed), DynamoDB (NoSQL), Aurora.
- **Network** — VPC, Load Balancer, CloudFront (CDN), Route 53 (DNS).
- **Security & Identity** — IAM, KMS, WAF, Shield.
- **Analytics & ML** — Redshift, Athena, SageMaker. Di GCP/Azure: setara dengan nama berbeda.

---

## Keamanan dan Tanggung Jawab

- **Shared responsibility** — Penyedia mengamankan cloud (infrastruktur, fisik, hypervisor); Anda mengamankan *in* cloud (data, konfigurasi, IAM, aplikasi). Model bervariasi per layanan (IaaS vs SaaS).
- **Best practice** — Principle of least privilege (IAM); enkripsi in transit dan at rest; network segmentation (VPC, security group); logging dan monitoring; patch dan hardening.

---

## Biaya

- **Pricing model** — Per jam/detik (compute), per GB (storage), per request (Lambda, API Gateway). Data transfer keluar sering berbayar.
- **Optimasi** — Right-sizing instance; reserved instance/savings plan untuk workload stabil; spot/preemptible untuk fault-tolerant; matikan resource tidak dipakai; monitor tag dan billing alert.

---

## Ringkasan

- Cloud = elastisitas, pay-as-you-go, managed services. IaaS (control), PaaS (platform), SaaS (aplikasi), FaaS (serverless).
- Public, private, hybrid, multi-cloud. Pilih sesuai kontrol, compliance, dan biaya.
- Shared responsibility; amankan konfigurasi dan data. Monitor biaya dan right-size resource.

---

*Cloud memungkinkan tim kecil membangun dan scale tanpa investasi hardware besar; pilih model dan layanan sesuai kebutuhan dan keterampilan operasional.*
