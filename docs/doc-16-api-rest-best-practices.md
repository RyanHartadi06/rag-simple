# Dokumentasi API REST — Best Practices

API REST (Representational State Transfer) adalah gaya arsitektur untuk API berbasis HTTP. Dokumen ini merangkum praktik umum untuk desain URL, metode HTTP, status code, versioning, keamanan, dan dokumentasi.

---

## Prinsip REST (Singkat)

- **Resource-oriented** — URL merepresentasikan sumber daya (noun), bukan aksi (verb). Aksi dinyatakan dengan metode HTTP.
- **Stateless** — Setiap request mandiri; server tidak menyimpan state session (state ada di klien atau token).
- **HTTP methods** — GET (baca), POST (buat), PUT/PATCH (update), DELETE (hapus).
- **Representation** — Sumber daya dipertukarkan dalam format (biasanya JSON); klien dan server setuju lewat header (Content-Type, Accept).

---

## Desain URL

### Gunakan kata benda (resources), bukan kata kerja
- **Baik:** `GET /users`, `GET /users/123`, `POST /users`, `PUT /users/123`, `DELETE /users/123`.
- **Hindari:** `GET /getUsers`, `POST /createUser`. Kata kerja sudah diwakili oleh method HTTP.

### Hierarki dan relasi
- **Nested resource** — Jika logis: `GET /users/123/orders`, `GET /users/123/orders/456`. Jangan nest terlalu dalam (misalnya `/a/b/c/d/e`).
- **Flat dengan query** — Alternatif: `GET /orders?userId=123`. Cocok ketika relasi kompleks atau banyak filter.

### Plural vs singular
- Konvensi umum: **plural** untuk koleksi — `/users`, `/orders`. Konsisten di seluruh API.

### Huruf kecil dan hyphen
- **Lowercase** — `/user-profiles`, bukan `/UserProfiles`. Hyphen lebih readable daripada camelCase di URL.

### Hindari verb di URL
- Aksi: pakai method HTTP atau resource yang jelas. Contoh: `POST /orders` (create order), bukan `POST /orders/create`.

---

## Metode HTTP

| Method | Semantik | Idempotent | Safe |
|--------|----------|------------|------|
| **GET** | Ambil resource | Ya | Ya |
| **POST** | Buat resource (atau aksi yang tidak cocok ke method lain) | Tidak | Tidak |
| **PUT** | Replace resource (full update) | Ya | Tidak |
| **PATCH** | Partial update | Idealnya ya* | Tidak |
| **DELETE** | Hapus resource | Ya | Tidak |

*Idempotent: memanggil beberapa kali efeknya sama dengan sekali. Safe: tidak mengubah state server.*

- **GET** — Tidak boleh mengubah data; bisa di-cache. Gunakan query string untuk filter: `GET /users?status=active&limit=10`.
- **POST** — Untuk create; juga untuk aksi yang tidak cocok (misalnya "submit form", "send email"). Body berisi payload.
- **PUT** — Replace keseluruhan resource; klien mengirim representasi lengkap.
- **PATCH** — Partial update; kirim hanya field yang berubah. Hindari PATCH yang mengubah hal di luar resource (side effect berat).
- **DELETE** — Hapus resource. 204 No Content atau 200 + body; konsisten.

---

## Status Code HTTP

Gunakan kode yang tepat agar klien bisa menangani dengan benar.

- **2xx Success**
  - **200 OK** — GET/PUT/PATCH berhasil; body berisi data.
  - **201 Created** — POST berhasil; resource dibuat. Sertakan header `Location` (URL resource baru) dan body (opsional).
  - **204 No Content** — Sukses tanpa body (umum untuk DELETE).
- **3xx Redirection**
  - **301/302** — Redirect; 301 permanent, 302 temporary.
  - **304 Not Modified** — Cache masih valid (conditional GET).
- **4xx Client Error**
  - **400 Bad Request** — Request tidak valid (format, validasi). Body berisi detail error.
  - **401 Unauthorized** — Belum login atau token tidak valid.
  - **403 Forbidden** — Tidak punya hak akses ke resource.
  - **404 Not Found** — Resource tidak ada.
  - **409 Conflict** — Konflik (misalnya duplikat, versi lama).
  - **422 Unprocessable Entity** — Validasi bisnis gagal; server paham request tapi tidak bisa memproses.
- **5xx Server Error**
  - **500 Internal Server Error** — Error tak terduga di server.
  - **503 Service Unavailable** — Overload atau maintenance.

Hindari mengembalikan 200 untuk error dengan body `{ "error": "..." }`; gunakan status code yang sesuai.

---

## Request & Response Body

### Format
- **JSON** — Standar de facto. Header: `Content-Type: application/json`, `Accept: application/json`.
- **Encoding** — UTF-8. Spesifikasi di header jika perlu.

### Naming
- Konsisten: **camelCase** (umum di JSON) atau **snake_case**; pilih satu untuk seluruh API. Dokumenkan.
- Field naming yang jelas: `createdAt`, `userId`, bukan singkatan yang ambigu.

### Pagination
- **Query:** `?page=2&limit=20` atau `?offset=20&limit=20`. Untuk cursor-based: `?cursor=abc123&limit=20`.
- **Response:** Sertakan metadata: `total`, `page`, `limit`, atau `nextCursor` agar klien bisa navigasi.

### Filtering & Sorting
- **Filter:** `?status=active&role=admin`.
- **Sort:** `?sort=createdAt&order=desc`. Konsisten penamaan dan arah.

### Error response body
Format seragam, misalnya:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      { "field": "email", "message": "Must be a valid email" }
    ]
  }
}
```
Sertakan `code` (machine-readable) dan `message` (human-readable); `details` untuk validasi per field.

---

## Versioning

- **URL path** — `/v1/users`, `/v2/users`. Paling eksplisit; caching mudah.
- **Header** — `Accept-Version: v1` atau custom header. URL tetap bersih.
- **Query** — `?version=1`. Kurang disarankan untuk versioning utama.

Pilih satu strategi; dokumentasikan. Saat breaking change, naikkan versi (v2) dan rencanakan deprecation v1.

---

## Keamanan

- **HTTPS** — Wajib di production; jangan kirim token/sensitive data lewat HTTP.
- **Authentication** — Token (JWT, OAuth2) di header: `Authorization: Bearer <token>`. Jangan taruh token di query string.
- **Authorization** — Cek hak akses per resource; 403 jika tidak boleh.
- **Rate limiting** — Batasi request per client/IP untuk mencegah abuse; header `X-RateLimit-*` atau `Retry-After`.
- **Input validation** — Validasi dan sanitasi di server; jangan percaya client. Batasi ukuran body.
- **CORS** — Set header CORS dengan benar; jangan `Access-Control-Allow-Origin: *` untuk credential.

---

## Dokumentasi

- **OpenAPI (Swagger)** — Spesifikasi standar; editor interaktif (Swagger UI), generate client/server. Maintain up-to-date dengan kode.
- **Contoh request/response** — Untuk setiap endpoint; status code sukses dan error.
- **Authentication** — Jelaskan cara dapat token dan cara mengirim (header).
- **Rate limit** — Dokumentasikan limit dan perilaku (header, 429).
- **Changelog** — Daftar perubahan dan deprecation per versi.

---

## Ringkasan Checklist

- [ ] URL resource-oriented, plural, lowercase; nested wajar.
- [ ] Method HTTP sesuai semantik; GET safe & idempotent.
- [ ] Status code tepat; error body konsisten.
- [ ] Pagination, filter, sort terdokumentasi dan konsisten.
- [ ] Versioning jelas; breaking change = versi baru.
- [ ] HTTPS, auth, rate limit, validasi input.
- [ ] Dokumentasi (OpenAPI) dan contoh selalu diperbarui.

---

*API yang konsisten dan terdokumentasi dengan baik memudahkan integrasi dan maintenance jangka panjang.*
