# GraphQL vs REST — Perbandingan dan Kapan Memilih

GraphQL dan REST adalah pendekatan berbeda untuk API. Dokumen ini membandingkan konsep, kelebihan, dan skenario penggunaan.

---

## REST (Singkat)

Resource-oriented: URL = resource (noun); method HTTP = action. GET /users, GET /users/1, POST /users, PUT /users/1, DELETE /users/1. Stateless; response biasanya fixed shape per endpoint. Versioning lewat URL atau header. Caching HTTP (GET) mudah; standard status code.

---

## GraphQL (Singkat)

Satu endpoint (biasanya POST); client mengirim query yang mendefinisikan data yang diminta. Response shape mengikuti query (no over-fetching, no under-fetching). Schema strongly typed; introspection. Mutations untuk write; subscriptions untuk real-time (over WebSocket). Client-driven: frontend meminta tepat field dan nested resource yang dibutuhkan.

---

## Over-fetching dan Under-fetching

REST: endpoint mengembalikan struktur tetap. Kadang terlalu banyak data (over-fetch) atau perlu banyak request (under-fetch, e.g. user lalu orders lalu products). GraphQL: satu request dengan query nested; dapat tepat field dan depth yang diminta. Mengurangi round-trip dan ukuran response yang tidak perlu.

---

## Fleksibilitas dan Kompleksitas

GraphQL memberi fleksibilitas besar ke client; cocok ketika banyak client (mobile, web, partner) dengan kebutuhan data berbeda. Trade-off: query kompleks bisa mahal (N+1, depth); perlu batasan (max depth, query cost) dan optimasi resolver (DataLoader, batching). REST endpoint lebih predictable dan mudah di-cache per URL.

---

## Caching

REST: cache per URL; GET idempotent; CDN dan browser cache mudah. GraphQL: satu endpoint; cache tidak per-request URL; cache di client (normalized cache, e.g. Apollo) atau layer yang memahami query. HTTP cache tradisional kurang cocok untuk GraphQL murni.

---

## Versioning

REST: version di path (/v1/users) atau header; breaking change = versi baru. GraphQL: schema evolution; tambah field (non-breaking); deprecate field; hindari remove/h rename breaking. Deprecation dan tooling memudahkan transisi.

---

## Learning Curve dan Ekosistem

REST: konsep sederhana; banyak dokumentasi dan contoh. GraphQL: schema, resolver, query language; butuh pemahaman types dan best practice (N+1, auth, rate limit per query). Tooling: GraphQL punya introspection, Playground, codegen; REST punya OpenAPI, Swagger.

---

## Kapan REST

API publik sederhana; caching HTTP penting; tim dan konsumen terbiasa REST; resource jelas dan fixed. Microservice internal yang kecil dan stabil.

---

## Kapan GraphQL

Banyak client dengan kebutuhan data berbeda; ingin mengurangi over/under-fetch dan round-trip. Rapid iteration frontend tanpa menunggu endpoint baru. Relasi kompleks dan nested; client ingin kontrol penuh atas shape. Siap invest di schema design, resolver optimization, dan batasan keamanan (query complexity, depth).

---

## Hybrid

Beberapa sistem memakai REST untuk resource sederhana dan cache-heavy; GraphQL untuk dashboard atau client yang butuh fleksibilitas. BFF (Backend for Frontend) bisa mengonsumsi REST internal dan mengekspos GraphQL ke client.

---

Ringkasan: REST sederhana, cache-friendly, resource-oriented. GraphQL fleksibel, client-driven, mengurangi over/under-fetch; butuh perhatian pada performa dan keamanan query. Pilih berdasarkan kebutuhan client, caching, dan kesiapan tim.
