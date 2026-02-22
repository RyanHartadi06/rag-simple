# Optimasi Query SQL

Index mempercepat WHERE, JOIN, ORDER BY. Buat index pada kolom yang sering di predicate. EXPLAIN menunjukkan cara eksekusi; perhatikan seq scan vs index scan. Hindari function pada kolom di WHERE; hindari LIKE '%x'. Kolom JOIN ter-index. OFFSET besar mahal; pertimbangkan keyset pagination. Connection pooling; slow query log; VACUUM dan statistics. Ringkasan: index tepat, EXPLAIN, predicate ramah index, monitoring.
