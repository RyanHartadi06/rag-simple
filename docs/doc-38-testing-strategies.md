# Strategi Testing — Unit, Integration, E2E

Testing memastikan perilaku yang diharapkan dan mengurangi regresi. Dokumen ini membahas piramida testing, jenis test, dan praktik.

---

## Piramida Testing

Banyak unit test (cepat, murah, fokus); lebih sedikit integration test (beberapa komponen/DB/API); sedikit E2E test (full flow, lambat, mahal). Rasio bisa disesuaikan; prinsip: banyak feedback cepat, sedikit yang lambat dan brittle.

---

## Unit Test

Menguji satu unit (fungsi, class) dalam isolasi; dependency di-mock atau di-stub. Cepat; menjalankan ribuan dalam detik. Fokus pada perilaku publik; edge case dan error path. Assert jelas: satu konsep per test. Naming: should_expectedBehavior_whenCondition atau test("describes scenario"). Red–green–refactor: tulis test gagal, buat lulus, refactor. Coverage berguna tapi tidak cukup; kualitas assertion dan skenario penting.

---

## Integration Test

Menguji beberapa unit bersama (API + DB, service + repository). Nyata atau test double (DB in-memory, mock external API). Lebih lambat; menemukan bug di boundary dan alur. Fokus pada path penting; tidak perlu cover semua kombinasi (itu untuk unit). Setup/teardown: migrasi DB, seed data, cleanup.

---

## E2E Test

Menguji sistem dari perspektif user (browser, API client). Full stack; data dan environment mendekati production. Paling lambat dan paling rapuh (UI change, timing). Gunakan untuk critical path (login, checkout); minimalkan jumlah; stabilkan dengan selector dan wait yang robust. Flaky test: perbaiki atau hapus; jangan biarkan mengaburkan signal.

---

## Test Double

Stub: mengembalikan nilai yang ditentukan. Mock: memverifikasi pemanggilan (expect call). Spy: mencatat pemanggilan. Fake: implementasi sederhana yang "cukup benar" (in-memory repo). Gunakan secukupnya; over-mock membuat test coupled ke implementasi.

---

## TDD (Test-Driven Development)

Tulis test dulu (red); implementasi minimal untuk lulus (green); refactor. Manfaat: desain terpaksa dari sisi pemakai; coverage alami; refactor berani. Bukan dogma; berguna untuk logic rumit dan API design.

---

## Non-Functional

Performance test: load, stress, spike. Security: SAST/DAST, dependency scan. Contract test: konsumen dan produser API setuju pada kontrak (Pact, OpenAPI). Sesuaikan dengan risiko dan effort.

---

Ringkasan: piramida (banyak unit, cukup integration, sedikit E2E); unit cepat dan terisolasi; integration untuk boundary; E2E untuk critical path; test double secukupnya; TDD opsional tapi berguna; sesuaikan dengan konteks.
