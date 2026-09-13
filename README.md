# eToro Finance Dashboard

Dashboard analítico de cartera de inversiones en bolsa, construido como **parcial práctico** del curso *Bases de Datos y Analítica* (Universidad Sergio Arboleda) y publicado como base de un desarrollo abierto alrededor de eToro.

**Autor:** Andrés Alejandro Rodríguez Lozano  
**GitHub:** [Andalejo1109](https://github.com/Andalejo1109)  
**eToro:** [@Andalejo1109](https://www.etoro.com/people/andalejo1109)

Repo: https://github.com/Andalejo1109/etoro-finance-dashboard

---

## Origen

Correo del 11 sep 2026, asunto `finance dashboard etoro to github` (`andres.rodriguezlo@usa.edu.co` → `alejo1109@gmail.com`), con tres adjuntos:

1. `Parcial 1 bases de datos 20263 (1) (1).pdf` — enunciado
2. `delta_Cartera principal_250802026_1.csv` — extracto eToro
3. `parcial 1 - Valery Johanna Rubiano Castro.pbix` — entrega de ejemplo

## Qué hay ahora en el repo

| Ruta | Estado |
|---|---|
| `README.md` / `LICENSE` / `.gitignore` | Listo |
| `docs/enunciado.md` | Listo (rúbrica en Markdown) |
| `docs/Parcial_1_bases_de_datos_20263.pdf` | Pendiente de upload (binario) |
| `data/delta_Cartera_principal_250802026_1.csv` | Pendiente de upload (216 KB) |
| `examples/parcial-1-Valery-Johanna-Rubiano-Castro.pbix` | Pendiente de upload (binario) |

Los tres archivos originales están en el correo. En GitHub: **Add file → Upload files** y arrástralos a `docs/`, `data/` y `examples/`.

---

## Caso de estudio

Evaluar la capacidad de cargar, limpiar, transformar con condicionales y visualizar datos financieros para tomar decisiones sobre una cartera real (broker eToro).

El CSV completo tiene **1.383 filas** (mar 2025 – ago 2026). Suma de `Quote amount` ≈ **21.284** USD/EUR.

- Operaciones: 1.227 BUY / 105 SELL / 25 DEPOSIT / 26 WITHDRAW
- Tipos: 1.091 FUND, 213 STOCK, 28 CRYPTO, 51 FIAT
- Activos más frecuentes: SPYG, SMH, BRK-B, IEMG, VTI

---

## Rúbrica (resumen)

**Parte I — Preparación (10%)** — carga, limpieza, condicionales, columna COP.

**Parte II — Visualización (50%)**

1. KPIs: conteo, volumen USD/EUR, volumen COP
2. Línea temporal USD, BUY vs SELL
3. Tree map por activo + pie de moneda
4. Columnas por `Base type` + Top 5
5. Segmentadores: fecha, `Way`, `Base type`

**Parte III — UI y análisis (40%)**

- Identidad eToro (fondo oscuro, verde, logo)
- Análisis ejecutivo: concentración, psicología del inversor, plan (DCA, rebalanceo, largo plazo)

Título: *Reporte analisis de portafolio de inversión*. Subtítulo: *Analista: (nombre)*.

Detalle: [`docs/enunciado.md`](docs/enunciado.md).

---

## Hoja de ruta (desarrollo eToro)

- [ ] Subir PDF, CSV completo y PBIX por la UI
- [ ] Versión propia del `.pbix` (no solo la entrega de ejemplo)
- [ ] Limpieza reproducible del CSV (Python / pandas)
- [ ] KPIs alineados con SPYG, SMH, BRK.B, IEMG, VTI + DCA
- [ ] Reporte o app para copiers / comunidad LATAM
- [ ] Refresh automático del extracto de operaciones

---

## Privacidad

El repo está **público**. El CSV es historial real de operaciones y el `.pbix` lleva el nombre de una estudiante. Si prefieres privacidad, cambia el repo a private en Settings → General → Danger Zone, o pide que lo deje privado.

eToro es marca de eToro Group Ltd. Este repo no está afiliado ni respaldado por eToro.
