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
 
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go

    return (go,)


@app.cell
def _(go):
    # Data based on the "How this hangs together" section
    segment_data = [
        {"segment": "Specialty Chemicals", "value_trillion": 0.95},
        {"segment": "Petrochemicals & Polymers", "value_trillion": 0.70},
        {"segment": "Agrochemicals", "value_trillion": 0.25},
        {"segment": "Consumer & Care Chemicals", "value_trillion": 0.125},
        {"segment": "Industrial Gases", "value_trillion": 0.11},
    ]

    pie_labels = [entry["segment"] for entry in segment_data]
    pie_values_trillion = [entry["value_trillion"] for entry in segment_data]

    # Create the pie chart
    pie_fig = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels,
                values=pie_values_trillion,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.3f}T<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}T<br><extra></extra>",
            )
        ]
    )

    pie_fig.update_layout(
        title="Global Chemicals Industry Segmentation (2024 Estimates)",
        annotations=[
            dict(text="Major<br>Segments", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    pie_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    **Note on Data:**
    The chart above visualizes the major functional segments described in the text.
    The sum of these specific segments is approximately **US$2.14T**.

    The text notes that the total global chemicals market is estimated between **US$3.5T** (narrow definition) and **US$5.8T** (broad definition including pharma). The difference is accounted for by overlapping categories, pharmaceuticals, fertilizers, and other downstream formulated products not explicitly categorized in the five main functional buckets.
    """
    )
    return


@app.cell
def _(go):
    import json
    from pathlib import Path

    data_path = Path(__file__).parent / "chemical_nodes.json"
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
        title="Chemicals Industry Icicle — 2024 market size (billions USD, rough)",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
    )

    icicle_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    **How to read the icicle:**
    - Root uses the narrower **US$3.5T** estimate to leave visual headroom; children roll up with branchvalues="total".
    - Company nodes are illustrative and use reported 2024 segment/group sales converted roughly to USD (FX approximations).
    - Logos for the highlighted companies live in `media/companies/chemical_industry/` and can be linked or layered into custom tooltips if desired.
    """
    )
    return


if __name__ == "__main__":
    app.run()
