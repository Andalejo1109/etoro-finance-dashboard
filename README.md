# eToro Finance Dashboard

Parcial práctico de *Bases de Datos y Analítica* (Universidad Sergio Arboleda) y base de un desarrollo abierto alrededor de eToro.

**Autor:** Andrés Alejandro Rodríguez Lozano  
**Repo:** https://github.com/Andalejo1109/etoro-finance-dashboard  
**eToro:** [@Andalejo1109](https://www.etoro.com/people/andalejo1109)

## Análisis Python (listo)

Código reproducible + reporte ejecutivo:

- Script: [`python/analyze_portfolio.py`](python/analyze_portfolio.py)
- Reporte: [`python/reports/analisis_ejecutivo.md`](python/reports/analisis_ejecutivo.md)
- Tablas: [`python/reports/kpis.json`](python/reports/kpis.json) · [`python/reports/activos.csv`](python/reports/activos.csv)

```bash
cd python
pip install -r requirements.txt
python analyze_portfolio.py --csv ../data/delta_Cartera_principal_250802026_1.csv
```

Hallazgos rápidos (mar 2025 – ago 2026):

- 1.383 operaciones; suma `Quote amount` = **21.284** (validación del enunciado)
- Ratio BUY:SELL = **11.69 : 1** (acumulación, no trading)
- Compras netas ≈ **17.114 USD equiv.**
- Core: SPYG 32%, BRK-B 21%, SMH 16%, IEMG 15%, VTI 7%
- HHI de compras = 0.20 (concentración moderada); 77% FUND

## Material del parcial

| Ruta | Estado |
|---|---|
| `docs/enunciado.md` | Listo |
| `python/` | Listo |
| `data/delta_Cartera_principal_250802026_1.csv` | Subir por la UI de GitHub |
| `docs/*.pdf` y `examples/*.pbix` | Subir por la UI (binarios) |

## Hoja de ruta

- [x] Versión Python del análisis
- [ ] Subir CSV / PDF / PBIX
- [ ] Versión propia del `.pbix`
- [ ] App o reporte para copiers LATAM
- [ ] Refresh automático del extracto

El repo es público. El CSV es historial real de operaciones.
