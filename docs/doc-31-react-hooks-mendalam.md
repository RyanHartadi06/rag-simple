# React Hooks — Panduan Mendalam

Hooks memungkinkan penggunaan state dan fitur React tanpa class.

## useState

useState(initialValue) mengembalikan [value, setter]. Setter bisa nilai atau fungsi (prev => next). Initial state bisa lazy: useState(() => compute()). deps [] = sekali; tanpa deps = setiap render.

## useEffect

useEffect(fn, deps): fn jalan setelah render. Return cleanup (opsional). Gunakan untuk fetch, subscription, DOM. Async: definisikan async function di dalam effect lalu panggil.

## useContext

useContext(MyContext) baca nilai Context. Re-render saat value berubah. Gabung dengan Provider.

## useRef

useRef(initialValue): objek { current } persist; ubah .current tidak trigger re-render. Untuk ref DOM atau nilai mutable.

## useMemo dan useCallback

useMemo(() => compute(a,b), [a,b]) cache hasil. useCallback(fn, deps) cache fungsi. Berguna untuk child yang di-memo. Dependency array wajib benar.

## Aturan Hooks

Hanya di top level; hanya dari function component atau custom Hook. Eslint-plugin-react-hooks menegakkan.

## useReducer

useReducer(reducer, initialArg) untuk state kompleks. dispatch(action) trigger update. Berguna untuk share logic update atau context.

Ringkasan: useState/useEffect/useContext/useRef/useMemo/useCallback/useReducer; ikuti aturan dan dependency array.
