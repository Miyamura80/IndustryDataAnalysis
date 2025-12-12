import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
    # Construction industry snapshot (2024 order-of-magnitude)
    - Global construction market 2024: ~$11–12T (different cuts; treat as directional).
    - Representative segment slices (from separate analyst sources, so they do not sum cleanly):
      - Residential buildings: ~$4.3T
      - Non-residential total: ~$9.3T
      - Within non-residential, infrastructure / civil engineering: ~$3.0T
      - Other non-residential buildings (commercial/industrial/institutional): ~$6.3T
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go

    return (go,)


@app.cell
def _(go):
    segment_data_construction = [
        {"segment": "Residential buildings", "value_billion": 4300},
        {"segment": "Infrastructure / civil", "value_billion": 3000},
        {"segment": "Other non-res buildings", "value_billion": 6300},
    ]

    pie_labels_construction = [entry["segment"] for entry in segment_data_construction]
    pie_values_construction = [
        entry["value_billion"] for entry in segment_data_construction
    ]

    pie_fig_construction = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_construction,
                values=pie_values_construction,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.0f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
            )
        ]
    )

    pie_fig_construction.update_layout(
        title="Construction segments (2024, USD billions; slices from different sources)",
        annotations=[
            dict(text="Segment cuts", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig_construction
    return


@app.cell
def _(mo):
    mo.md(
        """
    **Notes on the pie:**
    - Residential ($4.3T), infrastructure ($3.0T), and other non-residential buildings ($6.3T) come from separate market reports; they overlap, so the pie is for share intuition rather than a strict total.
    - Using billions keeps the chart readable; the implied sum (~$13.6T) sits slightly above the ~$11–12T global guides because of definitional differences.
    - Infrastructure sits inside non-residential; here it is shown separately to illustrate mix.
    - Percentages reflect the slice proportions of these three cuts, not a reconciled market total.
    """
    )
    return


@app.cell
def _(go):
    import json
    import pathlib

    base_dir = (
        pathlib.Path(__file__).parent if "__file__" in globals() else pathlib.Path.cwd()
    )
    construction_nodes_path = base_dir / "data" / "construction_nodes.json"

    if not construction_nodes_path.exists():
        raise FileNotFoundError(
            f"Construction nodes file not found at {construction_nodes_path}"
        )

    with construction_nodes_path.open("r", encoding="utf-8") as construction_nodes_file:
        construction_nodes = json.load(construction_nodes_file)

    icicle_labels_construction = [node["label"] for node in construction_nodes]
    icicle_parents_construction = [node["parent"] for node in construction_nodes]
    icicle_values_construction = [node["value"] for node in construction_nodes]
    icicle_hover_construction = [node["hover"] for node in construction_nodes]

    icicle_fig_construction = go.Figure(
        go.Icicle(
            labels=icicle_labels_construction,
            parents=icicle_parents_construction,
            values=icicle_values_construction,
            branchvalues="total",
            customdata=icicle_hover_construction,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_construction.update_layout(
        title="Construction icicle — 2024 scale (USD billions, directional)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    icicle_fig_construction
    return


@app.cell
def _(mo):
    mo.md(
        """
    **How to read the icicle:**
    - Root uses the summed segment figures (~$13.6T) to keep percentages internally consistent; this sits above the ~$11–12T global guide because sources overlap.
    - Non-residential contains infrastructure; shown separately to convey mix. Branchvalues="total" rolls values up the tree.
    - Company nodes are illustrative; revenues do not sum to parents and include diversified portfolios.
    - Use this for order-of-magnitude sizing and share thinking, not for precise reconciliation.
    """
    )
    return


if __name__ == "__main__":
    app.run()
