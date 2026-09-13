# Análisis Python — eToro Finance Dashboard

Versión reproducible del parcial práctico (carga, limpieza, KPIs, gráficos y análisis ejecutivo).

```bash
cd python
pip install -r requirements.txt
python analyze_portfolio.py --csv ../data/delta_Cartera_principal_250802026_1.csv
```

Salidas en `python/reports/`:

- `analisis_ejecutivo.md`
- `kpis.json`
- `activos.csv`
- `volumen_mensual.csv`
- `figures/*.png` (tema oscuro / verde eToro)

FX por defecto (referencia 13-sep-2026): `1 USD = 3100 COP`, `1 EUR = 1.17 USD`.
