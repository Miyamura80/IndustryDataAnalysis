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
    # Space industry snapshot (2023–24 order-of-magnitude)
    - Global space economy 2024: ~**$613B** (all in)
    - Core satellite industry (launch + manufacturing + services + ground): ~**$293B**
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    segment_data_space = [
        {"segment": "Launch services", "value_billion": 15},
        {"segment": "Satellite manufacturing", "value_billion": 20},
        {"segment": "Satellite services", "value_billion": 108.3},
        {"segment": "Ground equipment (sat)", "value_billion": 155.3},
        {"segment": "Earth observation & analytics", "value_billion": 6.5},
        {"segment": "Space tourism & crew", "value_billion": 1.0},
    ]

    pie_labels_space = [entry["segment"] for entry in segment_data_space]
    pie_values_space = [entry["value_billion"] for entry in segment_data_space]

    pie_fig_space = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_space,
                values=pie_values_space,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
            )
        ]
    )

    pie_fig_space.update_layout(
        title="Space industry segments (order-of-magnitude 2023–24, USD billions)",
        annotations=[
            dict(text="Core + near-core", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig_space
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the pie:**
    - Uses high-level, rounded figures across multiple analyst cuts.
    - Sums the core and adjacent slices (~$306B) rather than the full ~$613B space economy to keep the chart readable.
    - Launch + manufacturing are small compared with downstream services and ground equipment.
    - GNSS-only downstream estimates ($260–301B) would enlarge the ground slice substantially if added in full.
    """)
    return


@app.cell
def _(go):
    import json
    from pathlib import Path

    base_dir = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    space_nodes_path = base_dir / "data" / "space_nodes.json"

    if not space_nodes_path.exists():
        raise FileNotFoundError(f"Space nodes file not found at {space_nodes_path}")

    with space_nodes_path.open("r", encoding="utf-8") as space_nodes_file:
        space_nodes = json.load(space_nodes_file)

    icicle_labels_space = [node["label"] for node in space_nodes]
    icicle_parents_space = [node["parent"] for node in space_nodes]
    icicle_values_space = [node["value"] for node in space_nodes]
    icicle_hover_space = [node["hover"] for node in space_nodes]

    icicle_fig_space = go.Figure(
        go.Icicle(
            labels=icicle_labels_space,
            parents=icicle_parents_space,
            values=icicle_values_space,
            branchvalues="total",
            customdata=icicle_hover_space,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_space.update_layout(
        title="Space economy icicle — 2024 revenue scale (USD billions, rough)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    icicle_fig_space
    return


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**
    - Root uses ~$613B global space economy; children mix core satellite slices with adjacent GNSS and verticals. Branchvalues="total" rolls values upward.
    - Ground equipment sector broken down into GNSS, Network, and Consumer sub-segments for granularity.
    - Company nodes are illustrative, using reported or guided revenues/backlogs converted to USD where needed. They do not sum cleanly to parents.
    - GNSS downstream (~$260–301B) sits outside the BryceTech satellite-industry total; shown separately to avoid double counting the core.
    - Figures come from 2023–24 disclosures and analyst reports; treat as directional only.
    """)
    return


if __name__ == "__main__":
    app.run()
