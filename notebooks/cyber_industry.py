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
    # Cybersecurity industry snapshot (2024 order-of-magnitude)
    - Global cyber / information security spend estimates (2024): Gartner $183.9B, Fortune $193.7B, Grand View $245.6B. This map anchors sectors to ~$210–220B.
    - Sectors shown: network/perimeter + OT, endpoint, cloud, identity, application/API, data security, security analytics/operations, managed security services, and GRC/compliance.
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    segment_data_cyber = [
        {"segment": "Network & perimeter + OT", "value_billion": 50},
        {"segment": "Endpoint security", "value_billion": 15},
        {"segment": "Cloud security", "value_billion": 36},
        {"segment": "Identity security (IAM/PAM/IGA)", "value_billion": 23},
        {"segment": "Application & API security", "value_billion": 10},
        {"segment": "Data security (DLP/DSPM)", "value_billion": 13},
        {"segment": "Security analytics & operations", "value_billion": 10},
        {"segment": "Managed security services (MSS/MDR)", "value_billion": 37},
        {"segment": "GRC / security-driven risk & compliance", "value_billion": 18},
    ]

    pie_labels_cyber = [entry["segment"] for entry in segment_data_cyber]
    pie_values_cyber = [entry["value_billion"] for entry in segment_data_cyber]

    pie_fig_cyber = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_cyber,
                values=pie_values_cyber,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.0f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
                textposition="outside",
            )
        ]
    )

    pie_fig_cyber.update_layout(
        title="Cybersecurity segments (2024, USD billions; directional)",
        annotations=[
            dict(text="Segment cuts", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
        ),
        margin=dict(t=90, b=80, l=60, r=260),
        height=800,
        uniformtext_minsize=10,
        uniformtext_mode="hide",
    )

    pie_fig_cyber.update_traces(
        textposition="outside",
        textfont_size=12,
        pull=0.01,
    )

    pie_fig_cyber
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the pie:**
    - Sector anchors sum to ~$212B, sitting inside the broader $184–246B global cyber guides.
    - Sources vary widely (e.g., endpoint ranges $15–26B); values here lean conservative for sizing clarity.
    - Network/perimeter remains the largest single bucket; managed services, cloud, and identity are also large growth wedges.
    """)
    return


@app.cell
def _(go):
    import json
    import pathlib

    # Resolve data path robustly for notebook and script runs
    cyber_base_dir = (
        pathlib.Path(__file__).parent
        if "__file__" in globals()
        else (
            pathlib.Path.cwd() / "notebooks"
            if (pathlib.Path.cwd() / "notebooks").exists()
            else pathlib.Path.cwd()
        )
    )
    cyber_nodes_path = cyber_base_dir / "data" / "cyber_nodes.json"

    if not cyber_nodes_path.exists():
        raise FileNotFoundError(f"Cyber nodes file not found at {cyber_nodes_path}")

    with cyber_nodes_path.open("r", encoding="utf-8") as cyber_nodes_file:
        cyber_nodes = json.load(cyber_nodes_file)

    icicle_labels_cyber = [node["label"] for node in cyber_nodes]
    icicle_parents_cyber = [node["parent"] for node in cyber_nodes]
    icicle_values_cyber = [node["value"] for node in cyber_nodes]
    icicle_hover_cyber = [node["hover"] for node in cyber_nodes]

    icicle_fig_cyber = go.Figure(
        go.Icicle(
            labels=icicle_labels_cyber,
            parents=icicle_parents_cyber,
            values=icicle_values_cyber,
            branchvalues="total",
            customdata=icicle_hover_cyber,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_cyber.update_layout(
        title="Cybersecurity icicle — 2024 scale (USD billions, directional)",
        margin=dict(t=90, l=30, r=30, b=30),
        uniformtext=dict(minsize=10, mode="hide"),
        height=800,
    )

    icicle_fig_cyber.update_traces(
        root_color="lightgrey",
        tiling=dict(orientation="v"),
        maxdepth=4,
    )

    icicle_fig_cyber
    return


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**
    - Root anchors to ~$212B to stay inside the major analyst ranges ($184–246B); sector branches reflect directional slices.
    - Company nodes are illustrative and do not sum to their sectors; values reference FY24 revenue or ARR where available.
    - OT and SASE sit inside the network/perimeter branch; SIEM/SOAR/XDR roll into security operations.
    - Managed services includes MSSP + MDR; GRC slice focuses on security-driven risk/compliance tooling and advisory.
    """)
    return


if __name__ == "__main__":
    app.run()

