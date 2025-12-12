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
    # Robotics industry snapshot (2024 order-of-magnitude)
    - Commercial robotics revenue 2024: ~**$45B** (analyst ranges vary widely).
    - Working split (do **not** sum; definitions overlap):
      - Industrial / factory: ~$25B
      - Logistics & warehouse: ~$15–20B
      - Medical & surgical: ~$15B
      - Agriculture autonomy: ~$7B
      - Defense & security robots: ~$30B
      - Consumer / home: ~$11B
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    segment_data_robotics = [
        {"segment": "Industrial / factory", "value_billion": 25},
        {"segment": "Logistics & warehouse", "value_billion": 18},
        {"segment": "Medical & surgical", "value_billion": 15},
        {"segment": "Agriculture autonomy", "value_billion": 7},
        {"segment": "Defense & security", "value_billion": 30},
        {"segment": "Consumer / home", "value_billion": 11},
    ]

    pie_labels_robotics = [entry["segment"] for entry in segment_data_robotics]
    pie_values_robotics = [entry["value_billion"] for entry in segment_data_robotics]

    pie_fig_robotics = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_robotics,
                values=pie_values_robotics,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
            )
        ]
    )

    pie_fig_robotics.update_layout(
        title="Robotics segments (2024 directional, USD billions; overlapping scopes)",
        annotations=[
            dict(text="Direction only", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig_robotics
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the pie:**
    - Slices use mid-band values from analyst ranges; numbers overlap across sources, so treat as scale markers rather than a reconciled total.
    - Industrial remains concentrated in a few Japanese/European suppliers; logistics and defense/security are fast-growing but defined differently by each analyst.
    - Consumer/home figures are smaller than industrial in dollars but dominate unit volumes (vacuums, mops, lawn).
    """)
    return


@app.cell
def _(go):
    import json
    from pathlib import Path

    base_dir_robotics = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    robotics_nodes_path = base_dir_robotics / "data" / "robotics_nodes.json"

    if not robotics_nodes_path.exists():
        raise FileNotFoundError(f"Robotics nodes file not found at {robotics_nodes_path}")

    with robotics_nodes_path.open("r", encoding="utf-8") as robotics_nodes_file:
        robotics_nodes = json.load(robotics_nodes_file)

    icicle_labels_robotics = [node["label"] for node in robotics_nodes]
    icicle_parents_robotics = [node["parent"] for node in robotics_nodes]
    icicle_values_robotics = [node["value"] for node in robotics_nodes]
    icicle_hover_robotics = [node["hover"] for node in robotics_nodes]

    icicle_fig_robotics = go.Figure(
        go.Icicle(
            labels=icicle_labels_robotics,
            parents=icicle_parents_robotics,
            values=icicle_values_robotics,
            branchvalues="total",
            customdata=icicle_hover_robotics,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_robotics.update_layout(
        title="Robotics economy icicle — 2024 directional scale (USD billions)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    icicle_fig_robotics
    return


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**
    - Root uses a directional ~$106B sum for visualization; segments overlap across analyst definitions.
    - Company nodes show reported revenues where available; they do not reconcile to parents and are included for relative scale only.
    - Defense/security and service-robot scopes differ by source; percentages are best read within each branch, not as a global total.
    """)
    return


if __name__ == "__main__":
    app.run()





