# TypeScript — Dasar dan Fitur Penting

TypeScript adalah superset JavaScript yang menambah static typing. Dokumen ini membahas tipe dasar, interface, generic, dan praktik singkat.

---

## Mengapa TypeScript?

Catch error lebih awal di compile time; dokumentasi hidup (tipe = kontrak); refactor lebih aman; skalabilitas di codebase besar.

---

## Setup

`npm i -D typescript`; `npx tsc --init`. Konfigurasi: target, module, strict (disarankan true), outDir. Compile: `tsc` atau `tsc -w`.

---

## Tipe Dasar

- **Primitives** — string, number, boolean, null, undefined. symbol, bigint.
- **Annotasi** — `let x: number = 5` atau inferensi `let x = 5`.
- **Array** — `number[]` atau `Array<number>`. Tuple: `[string, number]`.
- **any** — Opt-out; minimalkan. **unknown** — Lebih aman; harus narrow sebelum pakai.
- **Union** — `string | number`. Narrowing dengan typeof, in, type guard.
- **Optional** — `x?: number` berarti `number | undefined`.

---

## Interface dan Type

**interface** — Bentuk objek; bisa extend.
```typescript
interface User { id: number; name: string; email?: string; }
```
**type** — Alias; union, intersection. `type ID = string | number;` `type UserWithRole = User & { role: string };`
Interface untuk objek; type untuk union/tuple/complex.

---

## Function

Parameter dan return: `function add(a: number, b: number): number { return a + b; }`. Optional/default: `x?: number`, `x: number = 0`. Generic: `function first<T>(arr: T[]): T | undefined { return arr[0]; }`.

---

## Class

Property dan constructor: `class Point { constructor(public x: number, public y: number) {} }`. public/private/protected; readonly. implements interface; abstract class.

---

## Generic

`interface Box<T> { value: T }`. Constraints: `T extends { length: number }`. Default: `interface A<T = string>`. Reusable component dan API response type.

---

## Utility Types

Partial, Required, Readonly, Record, Pick, Omit, Exclude, Extract, ReturnType, Parameters, NonNullable. Gunakan untuk transformasi tipe tanpa definisi manual.

---

## Best Practice

strict: true. Hindari any; gunakan unknown + type guard. Consistent naming (PascalCase). Infer when clear; annotate when needed.

---

*TypeScript mengurangi bug dan meningkatkan maintainability; investasi belajar terbayar di codebase menengah-besar.*
