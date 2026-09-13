# eToro Finance Dashboard

Dashboard analítico de cartera de inversiones en bolsa, construido como **parcial práctico** del curso *Bases de Datos y Analítica* (Universidad Sergio Arboleda) y publicado como base de un desarrollo abierto alrededor de eToro.

**Autor:** Andrés Alejandro Rodríguez Lozano  
**GitHub:** [Andalejo1109](https://github.com/Andalejo1109)  
**eToro:** [@Andalejo1109](https://www.etoro.com/people/andalejo1109)

---

## Qué hay en este repo

| Ruta | Descripción |
|---|---|
| `docs/Parcial_1_bases_de_datos_20263.pdf` | Enunciado del examen práctico (primer corte). |
| `docs/enunciado.md` | Enunciado en Markdown (misma rúbrica). |
| `data/delta_Cartera_principal_250802026_1.csv` | Export de operaciones de eToro usado en el caso de estudio. |
| `examples/parcial-1-Valery-Johanna-Rubiano-Castro.pbix` | Entrega de ejemplo en Power BI Desktop (estudiante). |

El CSV es un extracto histórico de operaciones (broker eToro) con ~1.383 filas entre marzo 2025 y agosto 2026. La suma de `Quote amount` es ~USD/EUR 21.284, alineada con la validación pedida en el enunciado (~21 mil).

---

## Caso de estudio

Evaluar la capacidad de cargar, limpiar, transformar con condicionales y visualizar datos financieros para **tomar decisiones** sobre una cartera real.

Columnas principales del CSV:

- `Date` — fecha/hora de la transacción (ISO 8601)
- `Way` — BUY, SELL, DEPOSIT, WITHDRAW
- `Base amount` — unidades del activo
- `Base currency (name)` — ticker + nombre (SMH, SPYG, BRK-B, IEMG, VTI, ETH, etc.)
- `Base type` — FUND, STOCK, CRYPTO, FIAT
- `Quote amount` / `Quote currency` — monto y moneda (USD, EUR)
- `Exchange`, `Fee amount`, `Broker`, `Notes`, `Leverage Metadata`

Distribución rápida del extracto:

- Operaciones: 1.227 BUY / 105 SELL / 25 DEPOSIT / 26 WITHDRAW
- Tipos: 1.091 FUND, 213 STOCK, 28 CRYPTO, 51 FIAT
- Activos más frecuentes: SPYG, SMH, BRK-B, IEMG, VTI

---

## Rúbrica del parcial (resumen)

**Parte I — Preparación y transformación (10%)**  
Carga del CSV, limpieza, tipos de dato, condicionales y columnas calculadas (incluye conversión aproximada a COP).

**Parte II — Visualización (50%)**

1. KPIs en tarjetas: conteo de operaciones, volumen USD/EUR, volumen COP  
2. Línea temporal de volumen USD por mes, diferenciando BUY vs SELL  
3. Tree map por activo + pie de moneda  
4. Columnas por `Base type` + barras Top 5  
5. Segmentadores: fechas, tipo de operación, tipo de activo  

**Parte III — UI y análisis (40%)**

- Identidad visual eToro (fondo oscuro, acento verde, logo)  
- Análisis ejecutivo (máx. 3 párrafos): concentración/riesgo, psicología del inversor, plan de acción (DCA, rebalanceo, largo plazo)

Título del reporte: *Reporte analisis de portafolio de inversión*.  
Subtítulo: *Analista: (nombre y apellido)*.

---

## Cómo abrir el dashboard

1. Instalar [Power BI Desktop](https://www.microsoft.com/power-bi).
2. Abrir `examples/parcial-1-Valery-Johanna-Rubiano-Castro.pbix`.
3. Si pide la fuente, apuntar a `data/delta_Cartera_principal_250802026_1.csv`.
4. Nota regional: el CSV usa **punto (.) como separador de miles** en algunos contextos; validar tipos al cargar.

---

## Hoja de ruta (desarrollo eToro)

Este repositorio empieza como material académico. La idea es evolucionar el mismo caso hacia un desarrollo reutilizable:

- [ ] Versión propia del `.pbix` (no solo la entrega de ejemplo)
- [ ] Limpieza reproducible del CSV (Python / pandas)
- [ ] KPIs alineados con la estrategia real (SPYG, SMH, BRK.B, IEMG, VTI + DCA)
- [ ] Publicación de un reporte o app para copiers / comunidad LATAM
- [ ] Automatizar refresh del extracto de operaciones

---

## Privacidad y uso

- El CSV es un extracto de operaciones de eToro usado con fines **educativos**.
- El archivo `.pbix` de ejemplo es una entrega de estudiante; se publica como referencia pedagógica, no como producto oficial de eToro ni de la universidad.
- eToro es marca de eToro Group Ltd. Este repo no está afiliado ni respaldado por eToro.

## Licencia

Material académico + datos de ejemplo. Ver `LICENSE`.
