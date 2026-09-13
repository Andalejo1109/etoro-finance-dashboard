# Reporte analisis de portafolio de inversion

**Analista:** Andrés Alejandro Rodríguez Lozano  
**Fuente:** extracto eToro `delta_Cartera_principal_250802026_1.csv`  
**Ventana:** 2025-03-31 → 2026-08-15  
**FX usada (referencia 13-sep-2026):** 1 USD = 3100 COP; 1 EUR = 1.17 USD

## KPIs

| Indicador | Valor |
|---|---|
| Operaciones totales | 1,383 |
| Trades BUY / SELL | 1,227 / 105 |
| Ratio BUY:SELL (ops) | 11.69 |
| Depósitos / retiros | 25 / 26 |
| Volumen USD | 19,724.19 |
| Volumen EUR | 1,560.16 |
| Suma Quote amount (validación ~21k) | 21,284.35 |
| Volumen COP (aprox.) | 66,803,690 |
| Compras − ventas (USD equiv.) | 17,114.13 |
| Comisiones (suma Fee amount) | -53.1075 |
| Operaciones con apalancamiento | 4 |
| Activos distintos en trades | 18 |

## Top compras

- **SPYG** (FUND): 6,209 USD en compras (32.1%), qty neta 56.672
- **BRK-B** (STOCK): 4,144 USD en compras (21.4%), qty neta 8.476
- **SMH** (FUND): 3,143 USD en compras (16.3%), qty neta 7.785
- **IEMG** (FUND): 2,809 USD en compras (14.5%), qty neta 38.683
- **VTI** (FUND): 1,432 USD en compras (7.4%), qty neta 4.376

Concentración: HHI = 0.2045 (moderada). Top 3 = 69.8% del volumen de compra. Mix FUND/STOCK/CRYPTO = 77.3% / 22.5% / 0.2%.

## Análisis ejecutivo

**1. Diagnóstico de concentración y riesgo.**  
El volumen de compra está dominado por fondos cotizados, no por stock picking. SPYG, SMH y BRK-B concentran el núcleo de la cartera: crecimiento de large cap estadounidense, semis y un holding conglomerado. Eso reduce el riesgo específico de una sola acción, pero no elimina el riesgo de factor: hay sobrepeso a growth + tecnología (SPYG + SMH) frente a mercado total (VTI) y emergentes (IEMG). El HHI de compras es moderada y el Top 3 absorbe 69.8% del capital transado. Las acciones individuales (NU, COHR, BLK) son satélite y, en el caso de NU, un experimento apalancado 5x que se cerró el mismo día. CRYPTO (ETH) y IBIT son exposición táctica, no el motor del portafolio.

**2. Comportamiento y psicología financiera.**  
La serie temporal no es la de un trader de corto plazo. Hay 1227 compras frente a 105 ventas (ratio 11.69:1). Abril 2025 muestra pruebas de instrumentos y dos tickets apalancados; a partir de mayo el patrón es acumulación recurrente en los mismos ETFs, con ventas residuales. Eso es consistente con DCA y con una mentalidad de largo plazo: se acepta la volatilidad en vez de liquidar el core. Los depósitos y retiros en USD existen, pero no rompen la dirección neta de acumulación (17,114 USD equiv. de compras menos ventas).

**3. Plan de acción estratégico.**  
(1) Mantener el DCA mensual sobre el core (SPYG / VTI / IEMG / BRK-B) y evitar reabrir tickets 5x: el costo de ese experimento fue ruido, no ventaja. (2) Rebalancear el factor tecnológico: SMH ya cumple el rol de satélite de semis; no subir más su peso relativo frente a un índice amplio (VTI o VT) o a calidad/dividendo (SCHD). (3) Disciplina de largo plazo: no vender el core por drawdowns de sector; usar aportes constantes para promediar, revisar pesos una o dos veces al año y dejar que el tiempo —no el apalancamiento— haga el trabajo.

## Cómo reproducir

```bash
cd python
pip install -r requirements.txt
python analyze_portfolio.py --csv ../data/delta_Cartera_principal_250802026_1.csv
```
