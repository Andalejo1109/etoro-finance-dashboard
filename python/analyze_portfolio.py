#!/usr/bin/env python3
"""Análisis reproducible del extracto eToro del parcial práctico.

Uso:
    python analyze_portfolio.py
    python analyze_portfolio.py --csv ruta/al/archivo.csv --fx-usd-cop 3100
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
DEFAULT_CANDIDATES = [
    REPO_ROOT / "data" / "delta_Cartera_principal_250802026_1.csv",
    Path("/home/workdir/artifacts/etoro-dashboard/delta_Cartera_principal_250802026_1.csv"),
    HERE / "data" / "delta_Cartera_principal_250802026_1.csv",
]
DEFAULT_USD_COP = 3100.0
DEFAULT_EUR_USD = 1.17
ETORO_BG, ETORO_PANEL = "#121212", "#1c1c1c"
ETORO_GREEN, ETORO_RED = "#13C446", "#E74C3C"
ETORO_TEXT, ETORO_MUTED, ETORO_GRID = "#F2F2F2", "#9AA0A6", "#2A2A2A"
PALETTE = [ETORO_GREEN, "#4ECDC4", "#F7B733", "#5B8DEF", "#C084FC", "#FF8A65", "#81C784"]


def find_csv(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"No existe el CSV: {path}")
        return path
    for candidate in DEFAULT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No encontré el CSV. Pásalo con --csv o ponlo en data/")


def ticker_from_name(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        return "UNKNOWN"
    return name.split()[0]


def load_and_transform(csv_path: Path, usd_cop: float, eur_usd: float) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    expected = {"Date", "Way", "Base amount", "Base currency (name)", "Base type",
                "Quote amount", "Quote currency", "Fee amount", "Notes", "Leverage Metadata"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Columnas faltantes: {sorted(missing)}")
    df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")
    df = df.dropna(subset=["Date"]).copy()
    df["ticker"] = df["Base currency (name)"].map(ticker_from_name)
    local = df["Date"].dt.tz_convert("America/Bogota")
    df["year_month"] = local.dt.strftime("%Y-%m")
    df["is_trade"] = df["Way"].isin(["BUY", "SELL"])
    df["is_cash"] = df["Way"].isin(["DEPOSIT", "WITHDRAW"])
    df["is_leveraged"] = df["Leverage Metadata"].notna() | df["Notes"].fillna("").str.contains("leveraged", case=False)
    df["Fee amount"] = df["Fee amount"].fillna(0.0)
    df["Quote amount"] = df["Quote amount"].fillna(0.0)
    df["quote_usd_equiv"] = np.where(df["Quote currency"] == "EUR", df["Quote amount"] * eur_usd, df["Quote amount"])
    df["quote_cop"] = np.where(
        df["Quote currency"] == "EUR",
        df["Quote amount"] * usd_cop * eur_usd,
        np.where(df["Quote currency"] == "USD", df["Quote amount"] * usd_cop, 0.0),
    )
    return df


def kpis(df: pd.DataFrame, usd_cop: float, eur_usd: float) -> dict:
    trades = df[df["is_trade"]]
    cash = df[df["is_cash"]]
    buy, sell = trades[trades["Way"] == "BUY"], trades[trades["Way"] == "SELL"]
    buy_n, sell_n = len(buy), len(sell)
    return {
        "n_rows": int(len(df)), "n_ops": int(len(df)), "n_trades": int(len(trades)),
        "n_buy": int(buy_n), "n_sell": int(sell_n),
        "n_deposit": int((df["Way"] == "DEPOSIT").sum()),
        "n_withdraw": int((df["Way"] == "WITHDRAW").sum()),
        "buy_sell_ratio_ops": round(buy_n / sell_n, 2) if sell_n else None,
        "vol_usd": round(float(trades.loc[trades["Quote currency"] == "USD", "Quote amount"].sum()), 2),
        "vol_eur": round(float(trades.loc[trades["Quote currency"] == "EUR", "Quote amount"].sum()), 2),
        "vol_quote_sum": round(float(df["Quote amount"].sum()), 2),
        "vol_cop": round(float(trades["quote_cop"].sum()), 0),
        "vol_usd_equiv": round(float(trades["quote_usd_equiv"].sum()), 2),
        "buy_usd_equiv": round(float(buy["quote_usd_equiv"].sum()), 2),
        "sell_usd_equiv": round(float(sell["quote_usd_equiv"].sum()), 2),
        "net_flow_usd_equiv": round(float(buy["quote_usd_equiv"].sum() - sell["quote_usd_equiv"].sum()), 2),
        "fees_sum": round(float(df["Fee amount"].sum()), 4),
        "n_leveraged": int(df["is_leveraged"].sum()),
        "n_assets": int(df.loc[df["is_trade"], "ticker"].nunique()),
        "date_min": str(df["Date"].min().date()), "date_max": str(df["Date"].max().date()),
        "fx_usd_cop": usd_cop, "fx_eur_usd": eur_usd,
        "deposit_usd": round(float(cash.loc[cash["Way"] == "DEPOSIT", "Base amount"].sum()), 2),
        "withdraw_usd": round(float(cash.loc[cash["Way"] == "WITHDRAW", "Base amount"].sum()), 2),
    }


def asset_table(df: pd.DataFrame) -> pd.DataFrame:
    trades = df[df["is_trade"]].copy()
    rows = []
    for (ticker, name, typ), g in trades.groupby(["ticker", "Base currency (name)", "Base type"]):
        buy, sell = g[g["Way"] == "BUY"], g[g["Way"] == "SELL"]
        buy_usd, sell_usd = buy["quote_usd_equiv"].sum(), sell["quote_usd_equiv"].sum()
        rows.append({
            "ticker": ticker, "nombre": name, "tipo": typ,
            "ops": int(len(g)), "ops_buy": int(len(buy)), "ops_sell": int(len(sell)),
            "qty_buy": buy["Base amount"].sum(), "qty_sell": sell["Base amount"].sum(),
            "qty_neta": buy["Base amount"].sum() - sell["Base amount"].sum(),
            "vol_buy_usd": buy_usd, "vol_sell_usd": sell_usd, "vol_neto_usd": buy_usd - sell_usd,
        })
    out = pd.DataFrame(rows).sort_values("vol_buy_usd", ascending=False)
    total = out["vol_buy_usd"].sum()
    out["peso_buy_pct"] = (out["vol_buy_usd"] / total * 100) if total else 0.0
    return out


def concentration(asset: pd.DataFrame) -> dict:
    w = asset["vol_buy_usd"] / asset["vol_buy_usd"].sum()
    hhi = float((w ** 2).sum())
    funds = float(asset.loc[asset["tipo"] == "FUND", "vol_buy_usd"].sum())
    stocks = float(asset.loc[asset["tipo"] == "STOCK", "vol_buy_usd"].sum())
    crypto = float(asset.loc[asset["tipo"] == "CRYPTO", "vol_buy_usd"].sum())
    total = funds + stocks + crypto
    return {
        "hhi": round(hhi, 4),
        "hhi_label": "baja" if hhi < 0.15 else "moderada" if hhi < 0.25 else "alta",
        "top3_share": round(float(w.head(3).sum()) * 100, 1),
        "fund_share": round(funds / total * 100, 1) if total else 0.0,
        "stock_share": round(stocks / total * 100, 1) if total else 0.0,
        "crypto_share": round(crypto / total * 100, 1) if total else 0.0,
    }


def style_axes(ax, title: str, ylabel: str | None = None):
    ax.set_facecolor(ETORO_PANEL)
    ax.set_title(title, color=ETORO_TEXT, fontsize=13, pad=12, loc="left")
    ax.tick_params(colors=ETORO_MUTED)
    ax.yaxis.label.set_color(ETORO_MUTED)
    ax.xaxis.label.set_color(ETORO_MUTED)
    for spine in ax.spines.values():
        spine.set_color(ETORO_GRID)
    ax.grid(axis="y", color=ETORO_GRID, linewidth=0.6)
    if ylabel:
        ax.set_ylabel(ylabel, color=ETORO_MUTED)
    ax.set_axisbelow(True)


def save_fig(fig, path: Path):
    fig.patch.set_facecolor(ETORO_BG)
    fig.tight_layout()
    fig.savefig(path, dpi=160, facecolor=ETORO_BG, bbox_inches="tight")
    plt.close(fig)


def plot_all(df: pd.DataFrame, asset: pd.DataFrame, outdir: Path) -> list[Path]:
    outdir.mkdir(parents=True, exist_ok=True)
    sns.set_style("darkgrid")
    paths: list[Path] = []
    trades = df[df["is_trade"]].copy()
    monthly = (trades.groupby(["year_month", "Way"])["quote_usd_equiv"].sum()
               .unstack(fill_value=0).reindex(columns=["BUY", "SELL"], fill_value=0).sort_index())
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(monthly.index, monthly["BUY"], color=ETORO_GREEN, marker="o", linewidth=2, label="BUY")
    ax.plot(monthly.index, monthly["SELL"], color=ETORO_RED, marker="o", linewidth=2, label="SELL")
    ax.fill_between(monthly.index, monthly["BUY"], color=ETORO_GREEN, alpha=0.12)
    style_axes(ax, "Volumen mensual (USD equiv.) — BUY vs SELL", "USD")
    ax.legend(facecolor=ETORO_PANEL, edgecolor=ETORO_GRID, labelcolor=ETORO_TEXT)
    ax.tick_params(axis="x", rotation=45)
    p = outdir / "01_tendencia_mensual.png"; save_fig(fig, p); paths.append(p)

    by_type = trades.groupby("Base type")["quote_usd_equiv"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.bar(by_type.index, by_type.values, color=PALETTE[: len(by_type)])
    style_axes(ax, "Volumen por tipo de activo", "USD equiv.")
    p = outdir / "02_volumen_por_tipo.png"; save_fig(fig, p); paths.append(p)

    top5 = asset.head(5)
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    ax.barh(top5["ticker"][::-1], top5["vol_buy_usd"][::-1], color=ETORO_GREEN)
    style_axes(ax, "Top 5 activos por volumen de compra", "USD equiv.")
    p = outdir / "03_top5_activos.png"; save_fig(fig, p); paths.append(p)

    ccy = trades.groupby("Quote currency")["Quote amount"].sum()
    fig, ax = plt.subplots(figsize=(6.2, 6.2))
    _, _, autotexts = ax.pie(ccy.values, labels=ccy.index, autopct="%1.1f%%",
                             colors=[ETORO_GREEN, "#5B8DEF"], startangle=90,
                             textprops={"color": ETORO_TEXT})
    for t in autotexts:
        t.set_color(ETORO_BG); t.set_fontweight("bold")
    ax.set_title("Peso por moneda de cotización", color=ETORO_TEXT, loc="left")
    p = outdir / "04_moneda.png"; save_fig(fig, p); paths.append(p)

    fig, ax = plt.subplots(figsize=(9, 6.5))
    ranked = asset.sort_values("vol_buy_usd", ascending=True)
    ax.barh(ranked["ticker"], ranked["vol_buy_usd"], color=ETORO_GREEN, alpha=0.9)
    style_axes(ax, "Concentración de compras por activo (proxy tree map)", "USD equiv.")
    p = outdir / "05_concentracion.png"; save_fig(fig, p); paths.append(p)

    way_counts = df["Way"].value_counts()
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    colors = [ETORO_GREEN if i == "BUY" else ETORO_RED if i == "SELL" else "#5B8DEF" for i in way_counts.index]
    ax.bar(way_counts.index, way_counts.values, color=colors)
    style_axes(ax, "Conteo de operaciones por sentido", "Operaciones")
    p = outdir / "06_conteo_way.png"; save_fig(fig, p); paths.append(p)
    return paths


def executive_markdown(metrics: dict, asset: pd.DataFrame, conc: dict) -> str:
    top = asset.head(5)
    top_lines = "\n".join(
        f"- **{r.ticker}** ({r.tipo}): {r.vol_buy_usd:,.0f} USD en compras "
        f"({r.peso_buy_pct:.1f}%), qty neta {r.qty_neta:.3f}"
        for r in top.itertuples()
    )
    return (
        "# Reporte analisis de portafolio de inversion\n\n"
        f"**Analista:** Andrés Alejandro Rodríguez Lozano\n\n"
        f"Ventana: {metrics['date_min']} → {metrics['date_max']}\n\n"
        f"Ver `python/reports/analisis_ejecutivo.md` generado al correr el script.\n\n"
        f"Top compras:\n{top_lines}\n\n"
        f"HHI={conc['hhi']} ({conc['hhi_label']}), top3={conc['top3_share']}%\n"
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Análisis Python del dashboard eToro")
    p.add_argument("--csv")
    p.add_argument("--fx-usd-cop", type=float, default=DEFAULT_USD_COP)
    p.add_argument("--fx-eur-usd", type=float, default=DEFAULT_EUR_USD)
    p.add_argument("--outdir", default=str(HERE / "reports"))
    args = p.parse_args()
    csv_path = find_csv(args.csv)
    outdir = Path(args.outdir)
    figdir = outdir / "figures"
    outdir.mkdir(parents=True, exist_ok=True)
    df = load_and_transform(csv_path, args.fx_usd_cop, args.fx_eur_usd)
    metrics = kpis(df, args.fx_usd_cop, args.fx_eur_usd)
    asset = asset_table(df)
    conc = concentration(asset)
    paths = plot_all(df, asset, figdir)
    (outdir / "kpis.json").write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    asset.round(4).to_csv(outdir / "activos.csv", index=False)
    (df[df["is_trade"]].groupby(["year_month", "Way"])["quote_usd_equiv"].sum()
     .unstack(fill_value=0).reset_index().to_csv(outdir / "volumen_mensual.csv", index=False))
    # El texto ejecutivo largo ya está versionado en reports/analisis_ejecutivo.md
    print("CSV:", csv_path)
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(asset.head(8).to_string(index=False))
    print("Concentración:", conc)
    for path in paths:
        print("figura", path)


if __name__ == "__main__":
    main()
