# Notulen Rapat Tim — 22 Februari 2025

**Peserta:** Andi (Tech Lead), Budi (Backend), Citra (Frontend), Dina (PM)  
**Durasi:** 1 jam (10:00–11:00 WIB)  
**Topik:** Persiapan rilis v2.0 dan prioritas sprint ini  
**Notulen:** Dina

---

## Ringkasan Eksekutif

Rapat membahas progress menuju rilis v2.0, pembagian tugas QA, dokumentasi API, dan perbaikan bug kritis di aplikasi mobile. Semua action item diberi deadline dan pemilik yang jelas.

---

## Pembukaan & Agenda

- Andi membuka rapat dan mengingatkan target rilis: **akhir minggu pertama Maret 2025**.
- Agenda: (1) Status fitur, (2) Bug & risiko, (3) Dokumentasi & QA, (4) Action items.

---

## Status Fitur & Keputusan

### Fitur yang Sudah Final
- **Export PDF** — Sudah selesai dan di-merge ke branch `release/v2`. Tim setuju dianggap final dan tidak ada perubahan scope lagi untuk rilis ini.

### Yang Masih Berjalan
- **Integrasi notifikasi push** — Backend (Budi) selesai; Frontend (Citra) masih menunggu testing di device fisik. Target: selesai Kamis 27 Feb.
- **Perbaikan performa dashboard** — Andi akan review kode dan optimasi query; tidak blocking rilis selama tidak ada regresi.

### Keputusan Resmi
1. **Finalisasi fitur export PDF** — Disetujui dan ditutup.
2. **QA** — Harus selesai paling lambat **Jumat, 28 Februari 2025**. Semua critical & high priority bug harus fixed atau didokumentasikan sebagai known issue untuk rilis.
3. **Dokumentasi API** — Harus diperbarui oleh **Budi** sesuai endpoint terbaru (termasuk notifikasi dan export); format mengikuti standar OpenAPI yang sudah dipakai tim. Deadline: **27 Februari 2025**.

---

## Bug & Risiko

### Bug Kritis yang Dibahas
- **Login di aplikasi mobile (iOS & Android)** — Kadang gagal setelah update terakhir; error terkait token refresh. **Citra** akan investigasi dan target fix **24 Februari**. Andi menawarkan bantuan jika perlu debug bersama backend.

### Risiko
- Jika fix login molor, ada kemungkinan rilis v2.0 diundur 3–5 hari. Dina akan siapkan komunikasi ke stakeholder jika terjadi.

---

## Action Items

| No | Pemilik | Tugas | Deadline | Catatan |
|----|---------|--------|----------|---------|
| 1 | Citra | Fix bug login mobile (token refresh) | 24 Feb 2025 | Prioritas tertinggi |
| 2 | Dina | Update changelog & release notes draft | 25 Feb 2025 | Siap untuk review tim |
| 3 | Budi | Update dokumentasi API (OpenAPI) | 27 Feb 2025 | Include notifikasi & export |
| 4 | Semua | Selesaikan QA critical/high | 28 Feb 2025 | Bug list di Jira |

---

## Dokumentasi & Proses

- **Changelog:** Dina akan mengumpulkan daftar fitur dan perbaikan dari Jira dan Git; format mengikuti template perusahaan.
- **Release notes:** Akan disiapkan dalam dua versi: teknis (untuk internal dan partner API) dan user-facing (untuk blog/email).

---

## Rapat Berikutnya

- **Hari/tanggal:** Senin, 24 Februari 2025  
- **Waktu:** 10:00 WIB  
- **Agenda:** Konfirmasi fix login, status QA, dan final checklist rilis.

---

## Lampiran (Referensi)

- Link board sprint: [internal]
- Dokumen standar OpenAPI tim: [internal]
- Daftar known issues saat ini: [Jira filter]

---

*Notulen ini disimpan di drive tim dan di-share ke semua peserta. Jika ada koreksi, kirim ke Dina sebelum akhir hari kerja.*
