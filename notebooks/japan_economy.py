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
    # Japan economy snapshot (2024 nominal GDP basis)

    - Base used here: **Japan nominal GDP = JPY 609.3T**.
    - Sector slices are **reconstructed/approximate** value-added shares (aligned to Cabinet Office SNA industry data, normalized to 100%), not a verbatim single-table release.
    - These are **GDP-equivalent sector sizes**, not company TAM estimates.
    - Company nodes use latest annual disclosed revenue / operating revenue / net sales and are shown as **illustrative scale markers**, not as strict sector share.
    """)
    return


@app.cell
def _():
    import csv
    from pathlib import Path

    return csv, Path


@app.cell
def _():
    import plotly.graph_objects as go

    return (go,)


@app.cell
def _(go, mo):
    sector_data_japan = [
        {
            "segment": "Manufacturing",
            "share_percent": 20.6,
            "value_trillion_yen": 125.5,
        },
        {
            "segment": "Real estate",
            "share_percent": 11.0,
            "value_trillion_yen": 67.0,
        },
        {
            "segment": "Wholesale & retail trade",
            "share_percent": 12.5,
            "value_trillion_yen": 76.2,
        },
        {
            "segment": "Professional, scientific & technical",
            "share_percent": 9.2,
            "value_trillion_yen": 56.1,
        },
        {
            "segment": "Health & social work",
            "share_percent": 8.3,
            "value_trillion_yen": 50.6,
        },
        {
            "segment": "Finance & insurance",
            "share_percent": 4.8,
            "value_trillion_yen": 29.2,
        },
        {
            "segment": "Construction",
            "share_percent": 5.3,
            "value_trillion_yen": 32.3,
        },
        {
            "segment": "Transport & postal",
            "share_percent": 5.3,
            "value_trillion_yen": 32.3,
        },
        {
            "segment": "Public administration",
            "share_percent": 4.9,
            "value_trillion_yen": 29.9,
        },
        {
            "segment": "Information & communications",
            "share_percent": 4.6,
            "value_trillion_yen": 28.0,
        },
        {"segment": "Other services", "share_percent": 4.4, "value_trillion_yen": 26.8},
        {"segment": "Education", "share_percent": 3.6, "value_trillion_yen": 21.9},
        {
            "segment": "Utilities, water, waste",
            "share_percent": 2.6,
            "value_trillion_yen": 15.8,
        },
        {
            "segment": "Accommodation & food services",
            "share_percent": 1.8,
            "value_trillion_yen": 11.0,
        },
        {
            "segment": "Agriculture, forestry & fishing",
            "share_percent": 1.0,
            "value_trillion_yen": 6.1,
        },
        {"segment": "Mining", "share_percent": 0.1, "value_trillion_yen": 0.6},
    ]

    pie_labels_japan = [entry["segment"] for entry in sector_data_japan]
    pie_values_japan = [entry["value_trillion_yen"] for entry in sector_data_japan]
    pie_customdata_japan = [entry["share_percent"] for entry in sector_data_japan]

    pie_fig_japan = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels_japan,
                values=pie_values_japan,
                customdata=pie_customdata_japan,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>JPY %{value:.1f}T<br>%{percent}",
                hovertemplate=(
                    "<b>%{label}</b><br>"
                    "GDP-equivalent size: JPY %{value:.1f}T<br>"
                    "Share of economy: %{customdata:.1f}%<br><extra></extra>"
                ),
            )
        ]
    )

    pie_fig_japan.update_layout(
        title="Japan economy by sector (2024, nominal GDP basis, JPY trillions)",
        annotations=[
            dict(
                text="GDP-equivalent<br>sector mix",
                x=0.5,
                y=0.5,
                font_size=14,
                showarrow=False,
            )
        ],
        showlegend=True,
    )

    mo.ui.plotly(pie_fig_japan)
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the pie:**
    - The slices are reconstructed from Cabinet Office value-added shares multiplied by **JPY 609.3T** nominal GDP.
    - Rounded shares add to roughly 100%, so values are directional to about one decimal place.
    - This is an economy map, not an investable-market map: it mixes public, private, nonprofit, and imputed activity.
    - Manufacturing is still the largest single sector, but the combined service sectors are much larger than the factory/export narrative on their own.
    """)
    return


@app.cell
def _(Path, go, mo):
    import json

    icicle_base_dir = (
        Path(__file__).resolve().parent
        if "__file__" in globals()
        else Path.cwd()
    )
    icicle_candidate_paths = [
        icicle_base_dir / "data" / "japan_economy_nodes.json",
        Path.cwd() / "notebooks" / "data" / "japan_economy_nodes.json",
    ]

    japan_nodes_path = next(
        (path for path in icicle_candidate_paths if path.exists()), None
    )
    if japan_nodes_path is None:
        icicle_tried_paths = ", ".join(str(path) for path in icicle_candidate_paths)
        raise FileNotFoundError(
            f"Japan economy nodes file not found (tried: {icicle_tried_paths})"
        )

    with japan_nodes_path.open("r", encoding="utf-8") as japan_nodes_file:
        japan_nodes = json.load(japan_nodes_file)

    icicle_labels_japan = [node["label"] for node in japan_nodes]
    icicle_parents_japan = [node["parent"] for node in japan_nodes]
    icicle_values_japan = [node["value"] for node in japan_nodes]
    icicle_hover_japan = [node["hover"] for node in japan_nodes]

    icicle_fig_japan = go.Figure(
        go.Icicle(
            labels=icicle_labels_japan,
            parents=icicle_parents_japan,
            values=icicle_values_japan,
            branchvalues="total",
            customdata=icicle_hover_japan,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig_japan.update_traces(root_color="lightgrey")
    icicle_fig_japan.update_layout(
        title="Japan economy icicle — 2024 sector scale with representative listed leaders",
        margin=dict(t=70, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode="hide"),
        height=950,
    )

    mo.ui.plotly(icicle_fig_japan)
    return


@app.cell
def _(mo):
    mo.md("""
    **How to read the icicle:**
    - Root is **JPY 609.3T**, matching the nominal GDP base used for the sector map.
    - First-level nodes are GDP-equivalent sector sizes. For large private sectors, second-level company nodes show the latest disclosed revenue scale for representative leaders.
    - The company nodes are **not sector share estimates** because company revenue and sector gross value added are different accounting concepts.
    - Public administration, education, health, and several service categories are kept mostly as remainder / fragmented nodes because listed-company ranking is much less meaningful there.
    - The telecom-heavy information & communications branch is especially important to read carefully: disclosed operator revenues are large relative to sector GVA, which is exactly why this should be treated as a structure map rather than a reconciliation.
    """)
    return


@app.cell
def _(csv, Path, go, mo):
    treemap_base_dir = (
        Path(__file__).resolve().parent
        if "__file__" in globals()
        else Path.cwd()
    )
    treemap_candidate_paths = [
        treemap_base_dir / "data" / "japan_top50_revenue_treemap_dataset.csv",
        Path.cwd()
        / "notebooks"
        / "data"
        / "japan_top50_revenue_treemap_dataset.csv",
    ]

    revenue_csv_path = next(
        (path for path in treemap_candidate_paths if path.exists()), None
    )
    if revenue_csv_path is None:
        treemap_tried_paths = ", ".join(str(path) for path in treemap_candidate_paths)
        raise FileNotFoundError(
            f"Japan revenue treemap CSV not found (tried: {treemap_tried_paths})"
        )

    with revenue_csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        revenue_rows = list(csv.DictReader(csv_file))

    color_map = {
        "Public": "#1f77b4",
        "Private": "#e4572e",
        "Mixed": "#9aa0a6",
    }

    public_total = sum(
        float(row["RevenueUsdBillions"])
        for row in revenue_rows
        if row["Type"] == "Public"
    )
    private_total = sum(
        float(row["RevenueUsdBillions"])
        for row in revenue_rows
        if row["Type"] == "Private"
    )
    mixed_total = sum(
        float(row["RevenueUsdBillions"])
        for row in revenue_rows
        if row["Type"] == "Mixed"
    )
    overall_total = public_total + private_total + mixed_total

    treemap_labels = [
        "Covered revenue universe",
        "Public companies",
        "Private companies",
    ]
    treemap_parents = ["", "Covered revenue universe", "Covered revenue universe"]
    treemap_values = [overall_total, public_total, private_total]
    treemap_text = [
        "Top-50 revenue set plus grouped remainder, USD billions.",
        "Public-company totals use the listed-company coverage universe.",
        "Private-company entries are the verified private Japanese companies that break into the top 50 by revenue.",
    ]
    treemap_colors = ["#d3d3d3", color_map["Public"], color_map["Private"]]

    if mixed_total > 0:
        treemap_labels.append("Mixed / grouped remainder")
        treemap_parents.append("Covered revenue universe")
        treemap_values.append(mixed_total)
        treemap_text.append(
            "Grouped remainder bucket. Includes the rest of the covered listed-company universe plus verified private-company revenue embedded in the remainder."
        )
        treemap_colors.append(color_map["Mixed"])

    for row in revenue_rows:
        company_type = row["Type"]
        parent_label = {
            "Public": "Public companies",
            "Private": "Private companies",
            "Mixed": "Mixed / grouped remainder",
        }[company_type]
        treemap_labels.append(row["Company"])
        treemap_parents.append(parent_label)
        treemap_values.append(float(row["RevenueUsdBillions"]))
        treemap_text.append(
            f"Rank {row['Rank']} • {company_type} • Revenue: ${float(row['RevenueUsdBillions']):.2f}B"
        )
        treemap_colors.append(color_map[company_type])

    treemap_fig = go.Figure(
        go.Treemap(
            labels=treemap_labels,
            parents=treemap_parents,
            values=treemap_values,
            branchvalues="total",
            customdata=treemap_text,
            texttemplate="<b>%{label}</b><br>$%{value:.2f}B",
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            marker=dict(colors=treemap_colors),
        )
    )

    treemap_fig.update_layout(
        title="Japanese company revenue treemap — top 50 plus covered remainder (USD billions)",
        margin=dict(t=70, l=0, r=0, b=0),
        height=950,
    )

    mo.ui.plotly(treemap_fig)
    return


@app.cell
def _(mo):
    mo.md("""
    **Notes on the treemap:**
    - Blue denotes **public companies** and orange denotes **private companies**. The grouped remainder is shown in grey because it is a mixed bucket by construction.
    - Revenues are **global consolidated revenues of Japanese-headquartered companies**, not revenue earned inside Japan.
    - The treemap uses the top-50 public-company ranking as the base, inserts the verified private firms large enough to break into that top tier, and then groups the remainder into a single covered-universe bucket.
    - This makes the chart useful for scale and ownership-structure intuition without pretending we have audited revenue coverage for the entire private-company base in Japan.
    """)
    return


if __name__ == "__main__":
    app.run()
