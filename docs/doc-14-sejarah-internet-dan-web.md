# Sejarah Internet dan Web — Ringkasan Panjang

Dokumen ini merangkum perkembangan internet dan world wide web dari awal riset sampai era modern, termasuk tokoh, protokol, dan peristiwa penting.

---

## Asal Usul: Jaringan Komputer dan ARPANET

### Konteks (1960-an)
- Perang Dingin; kebutuhan komunikasi yang tahan gangguan (misalnya jika satu node hancur).
- Riset di AS (ARPA — Advanced Research Projects Agency) dan di tempat lain tentang time-sharing dan jaringan packet-switched.
- **Packet switching** — Data dipecah menjadi paket yang bisa dikirim lewat rute berbeda dan disusun kembali di tujuan; dasar dari cara internet bekerja sampai sekarang.

### ARPANET (1969)
- Proyek ARPA yang menghubungkan beberapa universitas dan lembaga riset.
- **29 Oktober 1969** — Pesan pertama dikirim antara UCLA dan SRI (Stanford Research Institute); sistem sempat crash setelah dua karakter "LO" (seharusnya "LOGIN"), tapi ini dianggap tonggak pertama.
- Node awal: UCLA, SRI, UCSB, University of Utah. Topologi berkembang; NCP (Network Control Protocol) dipakai sebagai protokol host-to-host.
- **Email** — Ray Tomlinson (1971) mengirim email pertama dan memilih simbol @ untuk memisahkan user dan host.

### Dari NCP ke TCP/IP
- ARPANET mulanya memakai NCP. Kebutuhan interkoneksi dengan jaringan lain (misalnya packet radio, satellite) mendorong desain protokol yang lebih generik.
- **TCP/IP** — Dikembangkan oleh Vint Cerf, Bob Kahn, dan lain-lain. TCP menangani pengiriman andal; IP menangani addressing dan routing. Protokol ini menjadi fondasi "internet" (jaringan dari jaringan).
- **1 Januari 1983** — "Flag day": ARPANET beralih ke TCP/IP; ini sering dianggap sebagai kelahiran internet dalam bentuk yang kita kenal.

---

## Pertumbuhan Internet (1980-an–1990-an)

- **Domain Name System (DNS)** — 1980-an; nama domain (seperti example.com) dipetakan ke alamat IP; memudahkan manusia.
- **NSFNET** — Jaringan National Science Foundation (AS) menghubungkan banyak universitas; menjadi tulang punggung sebelum komersialisasi.
- **World Wide Web** — Ditemukan oleh **Tim Berners-Lee** di CERN (Swiss). Konsep: hypertext + internet. Komponen utama:
  - **HTML** — Bahasa markup untuk halaman.
  - **URI/URL** — Alamat unik sumber daya.
  - **HTTP** — Protokol untuk meminta dan mengirim halaman.
  - **Browser pertama** — Berners-Lee juga menulis browser/editor pertama (1990). Situs web pertama di dunia dijalankan di CERN.
- **Browser populer** — Mosaic (1993) mempopulerkan GUI dan gambar inline; kemudian Netscape Navigator mendominasi sebelum "browser wars" dengan Internet Explorer.
- **Komersialisasi** — Pertengahan 1990-an; NSFNET dibuka untuk lalu lintas komersial; ISP bermunculan; dot-com boom.

---

## Web 2.0 dan Era Sosial (2000-an)

- **Web 2.0** — Istilah untuk web yang lebih interaktif dan user-generated: blog, wiki, media sosial, AJAX, aplikasi berbasis web.
- **Google** — Didirikan 1998; pencarian berbasis PageRank dan kemudian iklan (AdWords/Ads) mengubah cara orang menemukan informasi dan cara bisnis monetisasi.
- **Media sosial** — Friendster, MySpace, lalu Facebook, Twitter, LinkedIn, YouTube; konten dan lalu lintas semakin terpusat di platform.
- **Mobile** — iPhone (2007) dan Android mendorong akses internet lewat ponsel; responsive design dan aplikasi native menjadi standar.

---

## Cloud, Skala, dan Keamanan (2010-an–Sekarang)

- **Cloud computing** — AWS, Azure, Google Cloud; infrastruktur sebagai layanan; startup dan perusahaan memindahkan beban ke cloud.
- **Skala** — Video streaming (Netflix, YouTube), konferensi (Zoom), e-commerce raksasa; CDN, microservices, container (Docker), orchestrator (Kubernetes) menjadi umum.
- **Keamanan dan privasi** — HTTPS menyebar; GDPR dan regulasi privasi; isu kebocoran data, phishing, ransomware; 2FA dan zero-trust makin lazim.
- **Decentralization & Web3** — Blockchain dan konsep "web3" muncul; masih berkembang dan kontroversial.

---

## Protokol dan Standar Penting

| Protokol/Layer | Fungsi Singkat |
|----------------|----------------|
| **IP** | Addressing dan routing paket di jaringan. IPv4 vs IPv6 (alamat lebih banyak). |
| **TCP** | Koneksi andal, ordered; dipakai HTTP, banyak aplikasi. |
| **UDP** | Tanpa koneksi; dipakai streaming, game, DNS. |
| **HTTP/HTTPS** | Request-response untuk web; HTTPS = HTTP + TLS (enkripsi). |
| **DNS** | Resolusi nama domain ke IP. |
| **TLS/SSL** | Enkripsi dan autentikasi; dasar "S" di HTTPS. |

---

## Tokoh Kunci (Ringkas)

- **Vint Cerf & Bob Kahn** — Desain TCP/IP; sering disebut "bapak internet".
- **Tim Berners-Lee** — Penemu WWW; HTML, HTTP, browser pertama; advokat untuk web terbuka dan standar.
- **Marc Andreessen** — Tim Mosaic; pendiri Netscape.
- **Larry Page & Sergey Brin** — Pendiri Google; PageRank dan pencarian.
- Banyak tokoh lain di bidang jaringan, keamanan, open source, dan bisnis digital.

---

## Dampak Sosial dan Ekonomi

- **Komunikasi** — Email, chat, video call; batas geografis berkurang.
- **Informasi** — Akses pengetahuan; juga mis/disinformasi dan filter bubble.
- **Ekonomi** — E-commerce, iklan digital, gig economy, platform; juga kekhawatiran monopoli dan pajak.
- **Politik dan privasi** — Gerakan sosial lewat media sosial; pengawasan dan regulasi konten; perlindungan data pribadi.

---

*Internet dan web terus berevolusi; memahami sejarah membantu konteks untuk keputusan teknis dan kebijakan masa depan.*
