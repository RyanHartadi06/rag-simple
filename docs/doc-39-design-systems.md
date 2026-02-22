# Design Systems — Komponen, Token, dan Dokumentasi

Design system adalah kumpulan standar (komponen, token, pola) dan dokumentasi untuk konsistensi UI dan percepatan pengembangan.

---

## Tujuan

Konsistensi visual dan perilaku di seluruh produk. Efisiensi: komponen reusable; desainer dan developer pakai sumber kebenaran yang sama. Skalabilitas: onboarding tim baru lebih mudah; perubahan desain terpusat (token, tema).

---

## Token (Design Tokens)

Variabel untuk nilai desain: warna, typography (font, size, weight), spacing, radius, shadow, breakpoint. Nama semantik: primary-500, text-heading, spacing-md. Implementasi: CSS variables, JSON, atau integrasi ke code (Theme provider). Token memungkinkan tema (light/dark, brand) tanpa mengubah komponen satu per satu.

---

## Komponen

Komponen UI yang terdokumentasi dan bisa dipakai ulang: Button, Input, Card, Modal, dll. Variants: primary/secondary, size, state (disabled, loading). Props API yang jelas; accessibility built-in (focus, ARIA). Implementasi: React, Vue, Web Components; storybook untuk isolasi dan dokumentasi.

---

## Pola dan Prinsip

Pola: layout (grid, stack), navigasi (tabs, breadcrumb), feedback (toast, alert). Prinsip: aksesibilitas (kontras, keyboard, screen reader), mobile-first, responsif. Pola didokumentasikan dengan contoh dan kapan memakai.

---

## Dokumentasi

Situs atau wiki: overview, token, daftar komponen dengan props dan contoh, pola, guideline (copy, icon, accessibility). Contoh kode dan Figma/Sketch link. Changelog untuk rilis komponen. Living documentation: update seiring code.

---

## Proses

Desainer dan developer berkolaborasi; design token disepakati; komponen diimplementasikan dan di-version. Konsumsi: package npm atau monorepo; import komponen dan token. Feedback dari konsumen (tim produk); iterasi berdasarkan penggunaan nyata.

---

## Skala dan Governance

Mulai kecil: token + beberapa komponen inti; expand bertahap. Governance: siapa yang bisa menambah/ubah; review process; backward compatibility. Kontribusi: kontributor dari berbagai tim; dokumentasi kontribusi.

---

Ringkasan: design system = token + komponen + pola + dokumentasi. Token untuk tema dan konsistensi; komponen reusable dan aksesibel; dokumentasi hidup; kolaborasi desain–dev dan governance.
