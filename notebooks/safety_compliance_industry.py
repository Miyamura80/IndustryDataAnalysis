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
    # Operational Safety Compliance Monitoring snapshot (2024 order-of-magnitude)
    - This map covers multiple sectors that analysts slice differently depending on software, systems, or hardware + services scope.
    - Sector market sizes sum to ~$47B but are not additive into one clean industry total because they mix software-only markets with hardware/systems-heavy markets (maritime and rail especially).
    - Top companies shown with 2024 total company revenue; segment-level safety compliance revenue is rarely disclosed cleanly.

    | Sector | 2024 Market Size | Top Companies (2024 Revenue) |
    |--------|------------------|------------------------------|
    | EHS / Workplace Safety software | $0.76B | IBM $62.8B, SAP ~$37B, Wolters Kluwer ~$6.4B |
    | Process Safety Systems (SIS/ESD/BMS/HIPPS) | $4.2B | Honeywell $38.5B, Emerson $17.5B, Siemens ~$82B |
    | Aviation SMS | $3.5B | RTX $80.8B, Airbus ~$75B, Honeywell $38.5B |
    | Maritime Safety Systems | $30.3B | Thales ~$22B, Kongsberg ~$4.5B, Saab ~$6B |
    | Railway Safety Systems | $6.5B | Siemens ~$82B, Alstom ~$20B, Hitachi ~$65B |
    | Construction Safety Management software | $1.72B | Autodesk $5.5B, Trimble $3.7B, Procore $1.15B |
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go

    return (go,)


@app.cell
def _(go):
    segment_data_safety = [
        {"segment": "EHS / Workplace Safety software", "value_billion": 0.761},
        {"segment": "Process Safety Systems", "value_billion": 4.2},
        {"segment": "Aviation SMS", "value_billion": 3.5},
        {"segment": "Maritime Safety Systems", "value_billion": 30.31},
        {"segment": "Railway Safety Systems", "value_billion": 6.5},
        {"segment": "Construction Safety Management software", "value_billion": 1.72},
    ]

    pie_labels_safety = [entry["segment"] for entry in segment_data_safety]
    pie_values_safety = [entry["value_billion"] for entry in segment_data_safety]

    pie_fig_safety = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_safety,
                values=pie_values_safety,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.2f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.2f}B<br><extra></extra>",
                textposition="outside",
            )
        ]
    )

    pie_fig_safety.update_layout(
        title="Operational Safety Compliance sectors (2024, USD billions; directional)",
        annotations=[
            dict(text="Sector cuts", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
        ),
        margin=dict(t=90, b=80, l=60, r=280),
        height=700,
        uniformtext_minsize=10,
        uniformtext_mode="hide",
    )

    pie_fig_safety.update_traces(
        textposition="outside",
        textfont_size=11,
        pull=0.01,
    )

    pie_fig_safety
    return


@app.cell
def _(mo):
    mo.md(
        """
    **Notes on the pie:**
    - Maritime Safety Systems dominates at ~$30B (65% of combined sectors), reflecting that it includes vessel hardware, communications equipment, and coastal/port infrastructure.
    - EHS/Workplace and Construction Safety are software-only markets, hence much smaller ($0.76B and $1.72B respectively).
    - Process Safety, Aviation SMS, and Railway Safety mix software with hardware/systems, sitting in the $3.5B-$6.5B range.
    - Sectors are not additive into one clean total because definitions and scope vary across analyst reports.
    """
    )
    return


@app.cell
def _(go):
    import json
    import pathlib

    safety_base_dir = (
        pathlib.Path(__file__).parent
        if "__file__" in globals()
        else (
            pathlib.Path.cwd() / "notebooks"
            if (pathlib.Path.cwd() / "notebooks").exists()
            else pathlib.Path.cwd()
        )
    )
    safety_nodes_path = safety_base_dir / "data" / "safety_compliance_nodes.json"

    if not safety_nodes_path.exists():
        raise FileNotFoundError(
            f"Safety compliance nodes file not found at {safety_nodes_path}"
        )

    with safety_nodes_path.open("r", encoding="utf-8") as safety_nodes_file:
        safety_nodes = json.load(safety_nodes_file)

    icicle_labels_safety = [node["label"] for node in safety_nodes]
    icicle_parents_safety = [node["parent"] for node in safety_nodes]
    icicle_values_safety = [node["value"] for node in safety_nodes]
    icicle_hover_safety = [node["hover"] for node in safety_nodes]

    icicle_fig_safety = go.Figure(
        go.Icicle(
            labels=icicle_labels_safety,
            parents=icicle_parents_safety,
            values=icicle_values_safety,
            branchvalues="total",
            customdata=icicle_hover_safety,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_safety.update_layout(
        title="Operational Safety Compliance icicle (2024 scale, USD billions, directional)",
        margin=dict(t=90, l=30, r=30, b=30),
        uniformtext=dict(minsize=10, mode="hide"),
        height=800,
    )

    icicle_fig_safety.update_traces(
        root_color="lightgrey",
        tiling=dict(orientation="v"),
        maxdepth=4,
    )

    icicle_fig_safety
    return


@app.cell
def _(mo):
    mo.md(
        """
    **How to read the icicle:**
    - Root sums sector slices to ~$47B; this is not a clean industry total because sectors mix software with hardware/systems markets.
    - Maritime dominates visually because it includes hardware-heavy vessel and port infrastructure systems.
    - Company nodes are illustrative; revenues shown are total company revenue since safety compliance segment revenue is rarely broken out.
    - Software-only sectors (EHS, Construction Safety) are narrower slices; hardware/systems sectors (Maritime, Railway, Process) are larger.
    - Use this for order-of-magnitude sizing and relative share thinking, not for precise market reconciliation.
    """
    )
    return


if __name__ == "__main__":
    app.run()
