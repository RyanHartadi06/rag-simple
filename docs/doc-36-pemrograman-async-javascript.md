# Pemrograman Async di JavaScript

JavaScript single-threaded; operasi I/O dan timer tidak memblokir thread. Dokumen ini membahas callback, Promise, async/await, dan pola umum.

---

## Callback

Fungsi yang dipanggil setelah operasi selesai. Masalah: callback hell (nesting dalam), error handling tersebar. Convention: callback(err, result) di Node.js. Callback sekali dipanggil (success atau error).

---

## Promise

Promise merepresentasikan nilai (atau alasan penolakan) di masa depan. States: pending, fulfilled, rejected. then(onFulfilled, onRejected), catch(onRejected), finally(). Chaining: return Promise dari then untuk chain berikutnya. Promise.all(iterable): tunggu semua fulfill atau satu reject. Promise.race: selesai begitu satu settle. Promise.allSettled: tunggu semua settle (fulfill/reject). Promise constructor: new Promise((resolve, reject) => { ... }).

---

## async/await

async function selalu mengembalikan Promise. await menunda eksekusi sampai Promise settle; hanya di dalam async. await promise; nilai = nilai fulfill; throw = reject. Error handling: try/catch di sekitar await. Sequential: await satu per satu. Parallel: Promise.all([f1(), f2()]) lalu await. Jangan await di loop jika tidak perlu sequential; gunakan Promise.all untuk parallel.

---

## Error Handling

Promise: catch di chain atau try/catch dengan await. Unhandled rejection: pastikan setiap Promise punya catch atau return ke caller. Global: unhandledrejection. Propagate: throw di async function atau return Promise.reject().

---

## Pola Umum

Fetch lalu process: async () => { const res = await fetch(url); const data = await res.json(); return process(data); }. Retry: loop dengan delay; break on success. Timeout: Promise.race(fn(), new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms))). Sequential loop: for await atau for loop dengan await di dalam. Parallel: Promise.all(array.map(async item => ...)).

---

## Event Loop

Call stack; task queue (macrotask); microtask queue (Promise then/catch, queueMicrotask). Microtask dijalankan setelah current script, sebelum macrotask berikutnya. Menghindari blocking: operasi berat di chunk atau worker.

---

Ringkasan: prefer async/await atas callback; gunakan Promise.all untuk parallel; error handling dengan try/catch; pahami event loop untuk urutan eksekusi.
