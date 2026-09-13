# Examen Práctico: Bases de Datos y Analítica (Primer Corte)

**Profesor:** Andrés Alejandro Rodríguez Lozano  
**Correo:** andres.rodriguezlo@usa.edu.co  
**Caso de estudio:** Análisis y Gestión de Cartera de Inversiones en Bolsa  
**Archivo de trabajo:** `delta_Cartera principal_250802026_1.csv`

## Objetivo

Evaluar la capacidad del estudiante para cargar, limpiar, transformar mediante condicionales y visualizar datos financieros, construyendo un dashboard analítico para la toma de decisiones.

## Diccionario de datos

El CSV contiene un registro histórico de operaciones bursátiles:

- **Date:** fecha y hora exacta de la transacción.
- **Way:** sentido de la operación (`BUY`, `SELL`, y también depósitos/retiros).
- **Base amount:** unidades adquiridas o vendidas del activo.
- **Base currency (name):** ticker y nombre del activo (ej. `SMH (VanEck Semiconductor ETF)`, `NU (NU Holdings)`).
- **Base type:** categoría del instrumento (`FUND`, `STOCK`, `CRYPTO`, `FIAT`).
- **Quote amount:** monto total involucrado (volumen transado).
- **Quote currency:** moneda de cotización (`USD`, `EUR`).
- **Exchange:** bolsa o mercado (Nasdaq, NYSE, etc.).
- **Sent/Received from / Sent to:** origen o destino (transferencias / cripto).
- **Fee amount / Fee currency (name):** comisión y su moneda.
- **Broker:** intermediario (eToro).
- **Notes:** información adicional (p. ej. operaciones apalancadas).
- **Sync Base Holding:** indicador lógico de sincronización.
- **Leverage Metadata:** margen o apalancamiento de la posición.

### Conceptos de negocio

Un nulo en trading no siempre es un error de extracción. Campos vacíos en `Leverage Metadata` o `Fee amount` suelen indicar que la operación no usó margen o no tuvo comisión explícita.

## Parte II — Visualización y construcción del dashboard (50%)

### 4. Indicadores clave — tarjetas (10%)

- Total de operaciones (conteo de registros).
- Volumen total transado en USD y EUR (suma de `Quote amount` por `Quote currency`).
- Volumen total transado en pesos colombianos (columna calculada).

### 5. Tendencia temporal — líneas (10%)

Evolución del volumen en USD (`Quote amount`) en el tiempo (mes/año), diferenciando BUY y SELL.

### 6. Composición — tree map y torta (10%)

- Tree map de volumen por activo (`Base currency (name)`).
- Pie chart de peso por divisa (`Quote currency` + suma de `Quote amount`).

### 7. Distribución transaccional — barras y columnas (10%)

- Columnas agrupadas por `Base type` (STOCK, FUND, CRYPTO).
- Barras horizontales con el Top 5 de activos por dinero invertido.

### 8. Interactividad (10%)

Segmentadores: rango de fechas, tipo de operación (`Way`), tipo de activo (`Base type`).

## Parte III — Diseño UI y análisis estratégico

### 9. Diseño visual e identidad eToro (10%)

Fondos oscuros, acento verde, contrastes blanco/gris, logo de eToro en lugar de la plantilla genérica de Power BI.

### 10. Análisis directivo y estrategia (30%)

Cuadro de texto de máximo tres párrafos:

1. Diagnóstico de concentración y riesgo (tree map y barras; FUND vs STOCK).
2. Comportamiento y psicología financiera (BUY vs SELL; acumulación vs trading).
3. Plan de acción: DCA, rebalanceo estructural, principios de largo plazo.

## Notas

1. Complementar con conceptos de ETFs y acciones.
2. Título: *Reporte analisis de portafolio de inversión*. Subtítulo: *Analista: (nombre y apellido)*.
3. Configuración regional: el CSV usa punto (`.`) como separador de miles.
4. Validar que la suma de `Quote amount` esté cerca de 21 mil USD/EUR.
5. Usar las páginas necesarias para que el reporte sea autoexplicativo.
6. Títulos y etiquetas de datos en cada gráfico.
