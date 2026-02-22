# Keamanan Aplikasi Web — Ancaman Umum dan Mitigasi

Keamanan aplikasi web melindungi data dan pengguna dari eksploitasi. Dokumen ini merangkum ancaman umum dan praktik mitigasi.

---

## Prinsip Umum

- **Defense in depth** — Beberapa lapis kontrol (validasi input, auth, encryption, logging).
- **Least privilege** — User dan proses hanya punya akses yang diperlukan.
- **Never trust input** — Validasi dan sanitasi di server; jangan percaya client.
- **Fail secure** — Saat error, sistem menolak akses; tidak membocorkan data sensitif.

---

## Injeksi (Injection)

**SQL Injection** — Input user disisipkan ke query; attacker bisa baca/ubah data atau bypass auth. **Mitigasi:** Gunakan parameterized query atau ORM; jangan konkatenasi string ke SQL. Validasi input; batasi karakter khusus. Principle of least privilege untuk user DB. NoSQL, OS command, LDAP injection: hindari menempatkan input user langsung ke interpreter; gunakan API aman dan whitelist.

---

## Autentikasi dan Session

- **Weak password** — Enforce kebijakan; hash dengan bcrypt/Argon2; jangan simpan plain text.
- **Session** — Regenerate session ID setelah login; cookie HttpOnly, Secure, SameSite; HTTPS wajib.
- **Brute force** — Rate limiting, captcha, lockout; 2FA untuk akun sensitif.
- **Credential stuffing** — Deteksi login anomali; 2FA.

---

## Sensitive Data Exposure

- **Transit** — HTTPS (TLS) untuk semua; HSTS.
- **At rest** — Enkripsi data sensitif di DB; key management aman; jangan log password/token.
- **Display** — Mask data sensitif di UI dan log; batasi akses per role.

---

## Access Control

- **Privilege escalation** — Cek otorisasi di setiap endpoint; gunakan ID dari session, bukan dari body; validasi ownership.
- **IDOR** — Gunakan UUID atau token opaque; selalu cek "apakah user ini boleh akses resource ini?"
- **Path traversal** — Whitelist path; jangan gunakan input user sebagai path file.

---

## Security Misconfiguration

- Ganti default credentials; matikan debug di production; nonaktifkan fitur tidak dipakai.
- Security headers: Content-Security-Policy, X-Content-Type-Options, X-Frame-Options. CORS ketat.

---

## XSS (Cross-Site Scripting)

Output encoding (escape) sesuai konteks (HTML, attribute, JS). Content-Security-Policy. Input validation; sanitasi jika terima HTML. HttpOnly cookie mengurangi dampak pencurian session.

---

## CSRF (Cross-Site Request Forgery)

CSRF token di form/header; validasi di server. SameSite cookie (Strict/Lax). API: Bearer token di header; CORS ketat.

---

## Dependency dan Logging

- Update dependency; npm audit, Snyk, Dependabot. Hapus dependency tidak dipakai.
- Log: login, akses sensitif, error; jangan log password/token. Monitoring dan alert anomali.

---

## Checklist

- [ ] Input divalidasi; parameterized query. Auth kuat; rate limit; 2FA jika perlu.
- [ ] HTTPS; data sensitif terenkripsi. Otorisasi di setiap endpoint.
- [ ] Output encoding anti-XSS; CSRF token. Konfigurasi aman; security headers.
- [ ] Dependency di-update; logging dan monitoring aktif.

---

*Keamanan adalah proses berkelanjutan; integrasikan ke SDLC.*
