import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Global Insurance Industry Segmentation (2024)
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    # Data: global insurance premiums by sector (2024), converted EUR→USD at ~1.08
    segment_data = [
        {"segment": "Life", "value_trillion": 3.134},
        {"segment": "Property & Casualty (P&C)", "value_trillion": 2.618},
        {"segment": "Health", "value_trillion": 1.817},
        {"segment": "Reinsurance", "value_trillion": 1.750},
    ]

    pie_labels = [entry["segment"] for entry in segment_data]
    pie_values_trillion = [entry["value_trillion"] for entry in segment_data]

    pie_fig = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels,
                values=pie_values_trillion,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.3f}T<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.3f}T<br><extra></extra>",
            )
        ]
    )

    pie_fig.update_layout(
        title="Global Insurance Industry Segmentation (2024 Premiums)",
        annotations=[
            dict(text="Major<br>Sectors", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig
    return


@app.cell
def _(mo):
    mo.md("""
    **Note on Data:**

    - Market sizes (Life / Health / P&C) are global premium pools originally reported in **EUR** by IAIS / sigma, converted here at ~1.08 EUR/USD for visual consistency.
    - Life: €2.902T → ~$3.1T | Health: €1.682T → ~$1.8T | P&C: €2.424T → ~$2.6T
    - Reinsurance market size ($1.75T) is gross reinsurance premiums from IAIS 2025 GIMAR (end-2024).
    - Company figures use **AM Best 2024 net premiums written** (USD), which provides a clean comparable basis across sectors.
    - Reinsurer company figures are AM Best **gross premiums written** from their reinsurer ranking.
    - Total across all four sectors sums to approximately **US$9.3T**, though there is some overlap (e.g. reinsurance premiums are ceded from primary insurers).
    """)
    return


@app.cell
def _(go):
    import json
    from pathlib import Path

    data_path = Path(__file__).parent / "insurance_nodes.json"
    with data_path.open("r", encoding="utf-8") as f:
        icicle_nodes = json.load(f)

    icicle_labels = [node["label"] for node in icicle_nodes]
    icicle_parents = [node["parent"] for node in icicle_nodes]
    icicle_values = [node["value"] for node in icicle_nodes]
    icicle_hover_texts = [node["hover"] for node in icicle_nodes]

    icicle_fig = go.Figure(
        go.Icicle(
            labels=icicle_labels,
            parents=icicle_parents,
            values=icicle_values,
            branchvalues="total",
            customdata=icicle_hover_texts,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig.update_layout(
        title="Insurance Industry Icicle — 2024 premiums (billions USD)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    icicle_fig
    return


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**

    - Root shows the combined global insurance market at **~US$9.3T** (sum of four sectors); children roll up with `branchvalues="total"`.
    - **Life** (~$3.1T) is the largest sector by premiums, followed by **P&C** (~$2.6T), **Health** (~$1.8T), and **Reinsurance** ($1.75T).
    - Company nodes use AM Best 2024 net premiums written (or GPW for reinsurers) in USD for cross-sector comparability.
    - There is inherent overlap: reinsurance premiums are ceded from primary Life, Health, and P&C books, so the $9.3T total double-counts some premium flow.
    - Health sector top players (UnitedHealth, Centene, Elevance) are US-centric managed-care giants; the global pool includes many smaller national carriers.
    """)
    return


if __name__ == "__main__":
    app.run()
