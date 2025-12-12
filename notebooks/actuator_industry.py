# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
    # Actuator industry snapshot (2024)

    - Global actuators market: **~$60–70B** depending on scope and source.
    - Growth: **~6–8% CAGR** into the early 2030s.
    - Cuts overlap (industrial vs. valves, robotics vs. factory automation, automotive vs. EV systems), so avoid summing the vertical TAMs.
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go

    return (go,)


@app.cell
def _(go):
    segment_data_actuator = [
        {"segment": "Industrial / process", "value_billion": 43.2},
        {"segment": "Robotics & factory automation", "value_billion": 15.2},
        {"segment": "Automotive", "value_billion": 24.7},
        {"segment": "Aerospace & defence", "value_billion": 11.0},
        {"segment": "HVAC & building automation", "value_billion": 14.81},
    ]

    pie_labels_actuator = [entry["segment"] for entry in segment_data_actuator]
    pie_values_actuator = [entry["value_billion"] for entry in segment_data_actuator]

    pie_fig_actuator = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_actuator,
                values=pie_values_actuator,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.2f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value}B<br><extra></extra>",
            )
        ]
    )

    pie_fig_actuator.update_layout(
        title="Actuator market slices (2024, overlapping cuts, USD billions)",
        annotations=[
            dict(
                text="Vertical cuts\n(do not sum)",
                x=0.5,
                y=0.5,
                font_size=14,
                showarrow=False,
            )
        ],
        showlegend=True,
    )

    pie_fig_actuator
    return


@app.cell
def _(mo):
    mo.md(
        """
    **Notes on the pie and margins:**
    - Values reflect widely cited 2024 estimates; verticals overlap, so the pie is for relative scale only.
    - Margin snapshot (company-level operating margin, actuator exposure varies): SMC ~25%, Rotork ~24%, Parker ~21%, Honeywell ~18–19%, Curtiss-Wright ~17%, ABB ~18%, Emerson ~12%, Flowserve ~10%, Siemens low-teens, Moog ~11–12%, JCI ~6–7%, BorgWarner/Denso/Aisin ~3–7%.
    """
    )
    return


@app.cell
def _(go):
    import json
    from pathlib import Path

    base_dir = (
        Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
    )
    candidate_paths = [
        base_dir / "data" / "actuator_nodes.json",
        Path.cwd() / "notebooks" / "data" / "actuator_nodes.json",
    ]

    actuator_nodes_path = next(
        (path for path in candidate_paths if path.exists()), None
    )
    if actuator_nodes_path is None:
        tried_paths = ", ".join(str(path) for path in candidate_paths)
        raise FileNotFoundError(f"Actuator nodes file not found (tried: {tried_paths})")

    with actuator_nodes_path.open("r", encoding="utf-8") as actuator_nodes_file:
        actuator_nodes = json.load(actuator_nodes_file)

    icicle_labels_actuator = [node["label"] for node in actuator_nodes]
    icicle_parents_actuator = [node["parent"] for node in actuator_nodes]
    icicle_values_actuator = [node["value"] for node in actuator_nodes]
    icicle_hover_actuator = [node["hover"] for node in actuator_nodes]

    icicle_fig_actuator = go.Figure(
        go.Icicle(
            labels=icicle_labels_actuator,
            parents=icicle_parents_actuator,
            values=icicle_values_actuator,
            branchvalues="total",
            customdata=icicle_hover_actuator,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_actuator.update_traces(root_color="lightgrey")
    icicle_fig_actuator.update_layout(
        title="Actuator landscape icicle — 2024 TAM cuts with margin snapshots",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
        height=900,
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    **How to read the icicle:**
    - Root sums the segment cuts (~$109B) to let the icicle render; these cuts overlap (e.g., valves vs. automation vs. automotive mechatronics), so treat as directional.
    - Segment nodes show the approximate 2024 TAM for that slice.
    - Company nodes are sized nominally (value = 1) to surface their operating margins in the hover text without implying share; “remainder / overlap” balances the parent.
    - Margins are company-level operating margins because actuator-only margin disclosure is rare.
    """
    )
    return


if __name__ == "__main__":
    app.run()
