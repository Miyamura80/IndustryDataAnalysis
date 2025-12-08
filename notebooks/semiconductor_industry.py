import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Semiconductor industry snapshot (2024 order-of-magnitude)
    - WSTS Autumn 2024 total semiconductor market: **$626.9B**
    - Broader 2024 “stack” (chips + equipment + OSAT + EDA/ESD): **~$805B** (rough, overlapping spend)
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    segment_data_semi = [
        {"segment": "Logic IC", "value_billion": 208.7},
        {"segment": "Memory IC", "value_billion": 167.1},
        {"segment": "Analog IC", "value_billion": 79.4},
        {"segment": "Micro IC (CPU/MCU/DSP)", "value_billion": 79.3},
        {"segment": "Optoelectronics", "value_billion": 42.1},
        {"segment": "Discrete semiconductors", "value_billion": 31.5},
        {"segment": "Sensors (non-opto)", "value_billion": 18.7},
    ]

    pie_labels_semi = [entry["segment"] for entry in segment_data_semi]
    pie_values_semi = [entry["value_billion"] for entry in segment_data_semi]

    pie_fig_semi = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_semi,
                values=pie_values_semi,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
            )
        ]
    )

    pie_fig_semi.update_layout(
        title="Semiconductor product mix (WSTS 2024, USD billions)",
        annotations=[
            dict(text="Core chips", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig_semi
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the pie:**
    - Source: WSTS Autumn 2024 forecast (full-year 2024) totaling $626.9B.
    - Shares: logic 33.3%, memory 26.6%, analog 12.7%, micro 12.6%, opto 6.7%, discrete 5.0%, sensors 3.0%.
    - Rounded values; category sums equal the WSTS total but do not map cleanly to company segment reporting.
    """)
    return


@app.cell
def _(go, mo):
    import json
    from pathlib import Path

    base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
    candidate_paths = [
        base_dir / "data" / "semiconductor_nodes.json",
        Path.cwd() / "notebooks" / "data" / "semiconductor_nodes.json",
    ]

    semiconductor_nodes_path = next((path for path in candidate_paths if path.exists()), None)
    if semiconductor_nodes_path is None:
        tried = ", ".join(str(path) for path in candidate_paths)
        raise FileNotFoundError(f"Semiconductor nodes file not found (tried: {tried})")

    with semiconductor_nodes_path.open("r", encoding="utf-8") as semiconductor_nodes_file:
        semiconductor_nodes = json.load(semiconductor_nodes_file)

    icicle_labels_semi = [node["label"] for node in semiconductor_nodes]
    icicle_parents_semi = [node["parent"] for node in semiconductor_nodes]
    icicle_values_semi = [node["value"] for node in semiconductor_nodes]
    icicle_hover_semi = [node["hover"] for node in semiconductor_nodes]

    icicle_fig_semi = go.Figure(
        go.Icicle(
            labels=icicle_labels_semi,
            parents=icicle_parents_semi,
            values=icicle_values_semi,
            branchvalues="remainder",
            customdata=icicle_hover_semi,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_semi.update_traces(root_color="lightgrey")
    icicle_fig_semi.update_layout(
        title="Semiconductor stack icicle — 2024 revenue scale (USD billions, rough)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
        height=850,
    )

    return mo.ui.plotly(icicle_fig_semi)


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**
    - Root sums chips ($626.9B) plus equipment (~$117B), OSAT (~$44B), and EDA/ESD (~$17B) to sketch an ~$805B 2024 “stack.”
    - Company nodes are illustrative revenues mapped to the nearest bucket; they do not sum to the parent and often span multiple WSTS categories.
    - Values are rounded from 2024 disclosures or widely cited market estimates; treat as directional and overlapping (capex vs merchant spend, internal vs external services).
    """)
    return


if __name__ == "__main__":
    app.run()
