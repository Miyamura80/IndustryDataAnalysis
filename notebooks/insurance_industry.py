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
        {"segment": "Reinsurance", "value_trillion": 0.395},
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

    - Market sizes (Life / Health / P&C) are global premium pools originally reported in **EUR** by Allianz (Global Insurance Report 2025), converted here at ~1.08 EUR/USD for visual consistency.
    - Life: €2.902T → ~$3.1T | Health: €1.682T → ~$1.8T | P&C: €2.424T → ~$2.6T
    - Reinsurance market size (~$0.4T) is 2024 global reinsurance gross written premium (~$293B non-life + ~$102B life; Atlas Magazine / AM Best reinsurer rankings).
    - Company figures use **AM Best 2024 net premiums written** (USD), which provides a clean comparable basis across sectors.
    - Reinsurer company figures are AM Best **gross premiums written** from their reinsurer ranking.
    - Total across all four sectors sums to approximately **US$8.0T**; note reinsurance (~$0.4T) is largely ceded from the primary Life/Health/P&C books, so primary premiums alone are ~$7.6T (Swiss Re sigma).
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

    - Root shows the combined global insurance market at **~US$8.0T** (sum of four sectors); children roll up with `branchvalues="total"`.
    - **Life** (~$3.1T) is the largest sector by premiums, followed by **P&C** (~$2.6T), **Health** (~$1.8T), and **Reinsurance** (~$0.4T).
    - Company nodes use AM Best 2024 net premiums written (or GPW for reinsurers) in USD for cross-sector comparability.
    - There is inherent overlap: reinsurance premiums are ceded from primary Life, Health, and P&C books, so the $8.0T total double-counts some premium flow.
    - Health sector top players (UnitedHealth, Centene, Elevance) are US-centric managed-care giants; the global pool includes many smaller national carriers.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## US P&C market sizes (last 5 years)

    The plot below uses the provided CSV (NAIC/III-derived lines of business) and shows the last 5 years with available data.

    Notes:
    - The CSV includes a 2025 column but it is blank in this extract, so the chart will typically show 2020-2024.
    - Cyber is included, but note it is reported as *direct* premiums written in the CSV, while the other lines are *net* premiums written.
    - "Commercial Property - Fire + Allied (combined)" is used (and the separate Fire / Allied rows are excluded) to avoid double counting.
    """)
    return


@app.cell
def _(go, mo):
    import csv
    import pathlib

    csv_path = pathlib.Path(
        "/Users/eito/Downloads/insurance_subsegment_market_sizes_2020_2025_partial.csv"
    )
    warning = None
    fig = None

    if not csv_path.exists():
        warning = mo.md(
            "WARNING: CSV not found at: "
            f"`{csv_path}`\n\n"
            "Update `csv_path` in this cell to point to your local file."
        )
    else:
        with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = reader.fieldnames or []
            year_cols = [c for c in fieldnames if c.isdigit()]
            years = sorted(int(c) for c in year_cols)
            rows = [
                r
                for r in reader
                if r.get("segment") == "Property & Casualty" and r.get("geo") == "US"
            ]

        year_has_data: dict[int, bool] = {y: False for y in years}
        for r in rows:
            for y in years:
                v = (r.get(str(y)) or "").strip()
                if v:
                    year_has_data[y] = True

        years_with_data = [y for y in years if year_has_data.get(y)]
        plot_years = years_with_data[-5:]

        if not plot_years:
            warning = mo.md("WARNING: No year columns with data found in the CSV.")
        else:
            exclude_subsegments = {
                "Commercial Property - Fire",
                "Commercial Property - Allied Lines",
            }

            subsegment_to_values: dict[str, list[float | None]] = {}
            direct_only_subsegments = {"Cyber"}
            for r in rows:
                metric = (r.get("metric") or "").strip()
                subsegment = (r.get("subsegment") or "").strip()
                if not subsegment or subsegment in exclude_subsegments:
                    continue

                if subsegment in direct_only_subsegments:
                    if not metric.startswith("Direct premiums written"):
                        continue
                else:
                    if not metric.startswith("Net premiums written"):
                        continue

                values: list[float | None] = []
                for y in plot_years:
                    raw = (r.get(str(y)) or "").strip()
                    values.append(float(raw) if raw else None)

                subsegment_to_values[subsegment] = values

            if not subsegment_to_values:
                warning = mo.md(
                    "WARNING: No US P&C rows with metric `Net premiums written` were found to plot."
                )
            else:
                totals_net: list[float | None] = []
                for i in range(len(plot_years)):
                    total = 0.0
                    has_any = False
                    for series in subsegment_to_values.values():
                        # Don't mix direct-written cyber into the net-written total.
                        if series is subsegment_to_values.get("Cyber"):
                            continue
                        val = series[i]
                        if val is None:
                            continue
                        total += val
                        has_any = True
                    totals_net.append(total if has_any else None)

                fig = go.Figure()
                x_years = [str(y) for y in plot_years]
                for name in sorted(subsegment_to_values.keys()):
                    fig.add_trace(
                        go.Scatter(
                            x=x_years,
                            y=subsegment_to_values[name],
                            mode="lines+markers",
                            name=name,
                            hovertemplate=(
                                "<b>%{fullData.name}</b><br>Year: %{x}<br>Premiums: $%{y:.2f}B"
                                "<extra></extra>"
                            ),
                        )
                    )

                fig.add_trace(
                    go.Scatter(
                        x=x_years,
                        y=totals_net,
                        mode="lines+markers",
                        name="Total (net-written lines only)",
                        line=dict(width=4, dash="dash"),
                        hovertemplate=(
                            "<b>%{fullData.name}</b><br>Year: %{x}<br>Premiums: $%{y:.2f}B"
                            "<extra></extra>"
                        ),
                    )
                )

                fig.update_layout(
                    title=(
                        f"US P&C insurance market sizes ({plot_years[0]}-{plot_years[-1]})"
                    ),
                    xaxis=dict(
                        title="Year",
                        type="category",
                        categoryorder="array",
                        categoryarray=x_years,
                    ),
                    yaxis_title="Premiums ($bn)",
                    legend_title="Line of business",
                    hovermode="x unified",
                    margin=dict(t=70, l=40, r=20, b=40),
                )

    output = warning if warning is not None else fig
    output
    return


@app.cell
def _(mo):
    mo.md("""
    ## Global insurance market size proxies (last 5 years, with uncertainty)

    This chart uses a proxy-estimates CSV that includes a point estimate and a low/high uncertainty band by year.
    Values are aggregated to the sector level (Life / Health / P&C / Reinsurance) by summing subsegments.
    """)
    return


@app.cell
def _(go, mo):
    import csv as _csv
    import pathlib as _pathlib

    _proxy_csv_path = _pathlib.Path(
        "/Users/eito/Downloads/insurance_subsegment_market_sizes_2020_2025_proxy_estimates.csv"
    )

    _proxy_output = None
    _proxy_fig = None

    if not _proxy_csv_path.exists():
        _proxy_output = mo.md(
            "WARNING: Proxy estimates CSV not found at: "
            f"`{_proxy_csv_path}`\n\n"
            "Update `_proxy_csv_path` in this cell to point to your local file."
        )
    else:
        with _proxy_csv_path.open("r", newline="", encoding="utf-8") as _proxy_csv_file:
            _proxy_reader = _csv.DictReader(_proxy_csv_file)
            _proxy_fieldnames = _proxy_reader.fieldnames or []
            _proxy_year_cols = [c for c in _proxy_fieldnames if c.isdigit()]
            _proxy_years = sorted(int(c) for c in _proxy_year_cols)
            _proxy_rows = [r for r in _proxy_reader]

        # Last 5 years with any data present.
        _year_has_data: dict[int, bool] = {y: False for y in _proxy_years}
        for _r in _proxy_rows:
            for _y in _proxy_years:
                if (_r.get(str(_y)) or "").strip():
                    _year_has_data[_y] = True
        _years_with_data = [y for y in _proxy_years if _year_has_data.get(y)]
        _plot_years = _years_with_data[-5:]

        if not _plot_years:
            _proxy_output = mo.md("WARNING: No year columns with data found in the proxy CSV.")
        else:
            _segment_color = {
                "Life": "#1f77b4",
                "Health": "#2ca02c",
                "Reinsurance": "#ff7f0e",
                "Property & Casualty": "#d62728",
            }

            _x_years = [str(y) for y in _plot_years]
            _proxy_fig = go.Figure()

            # Plot each subsegment as its own series.
            for _r in _proxy_rows:
                _seg = (_r.get("segment") or "").strip()
                _subseg = (_r.get("subsegment") or "").strip()
                if not _seg or not _subseg:
                    continue

                _y_vals_b: list[float | None] = []
                _err_plus_b: list[float] = []
                _err_minus_b: list[float] = []
                _has_any = False

                for _y in _plot_years:
                    _raw = (_r.get(str(_y)) or "").strip()
                    _raw_low = (_r.get(f"{_y}_low") or "").strip()
                    _raw_high = (_r.get(f"{_y}_high") or "").strip()
                    if not _raw or not _raw_low or not _raw_high:
                        _y_vals_b.append(None)
                        _err_plus_b.append(0.0)
                        _err_minus_b.append(0.0)
                        continue

                    _v = float(_raw)
                    _low = float(_raw_low)
                    _high = float(_raw_high)
                    _has_any = True

                    _y_vals_b.append(_v / 1e9)
                    _err_plus_b.append(max(0.0, (_high - _v) / 1e9))
                    _err_minus_b.append(max(0.0, (_v - _low) / 1e9))

                if not _has_any:
                    continue

                _name = f"{_seg} — {_subseg}"
                _color = _segment_color.get(_seg, "#7f7f7f")

                _proxy_fig.add_trace(
                    go.Scatter(
                        x=_x_years,
                        y=_y_vals_b,
                        mode="lines+markers",
                        name=_name,
                        legendgroup=_seg,
                        line=dict(width=2, color=_color),
                        marker=dict(size=6, color=_color),
                        error_y=dict(
                            type="data",
                            array=_err_plus_b,
                            arrayminus=_err_minus_b,
                            visible=True,
                        ),
                        hovertemplate=(
                            "<b>%{fullData.name}</b><br>Year: %{x}"
                            "<br>Premiums: $%{y:.1f}B"
                            "<extra></extra>"
                        ),
                    )
                )

            _proxy_fig.update_layout(
                title=(
                    "Global insurance market size proxies by subsegment "
                    f"({_plot_years[0]}-{_plot_years[-1]}, with uncertainty)"
                ),
                xaxis=dict(
                    title="Year",
                    type="category",
                    categoryorder="array",
                    categoryarray=_x_years,
                ),
                yaxis=dict(title="Estimated premiums ($bn, log scale)", type="log"),
                legend_title="Subsegment",
                hovermode="x unified",
                margin=dict(t=70, l=50, r=20, b=40),
            )

    _proxy_output_or_fig = _proxy_output if _proxy_output is not None else _proxy_fig
    _proxy_output_or_fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## Cyber insurance companies (treemap by premium volume)

    Treemap areas use the midpoint of the stated range (or the exact value where available). Hover shows the low/high bounds and the confidence tag.
    """)
    return


@app.cell
def _(go):
    # Cyber premium volumes are hard to source consistently at the company level.
    # The values below follow the user-provided list, with ranges where noted.
    cyber_company_premiums = [
        {
            "company": "Coalition",
            "country": "US",
            "status": "Est.",
            "category": "MGA / Insurtech",
            "low_b": 0.9,
            "high_b": 1.1,
        },
        {
            "company": "At-Bay",
            "country": "US",
            "status": "Est.",
            "category": "MGA / Insurtech",
            "low_b": 0.6,
            "high_b": 0.8,
        },
        {
            "company": "Cowbell",
            "country": "US",
            "status": "Est.",
            "category": "MGA / Insurtech",
            "low_b": 0.25,
            "high_b": 0.35,
        },
        {
            "company": "CFC",
            "country": "UK",
            "status": "Est.",
            "category": "MGA / Insurtech",
            "low_b": 0.9,
            "high_b": 1.2,
        },
        {
            "company": "Beazley",
            "country": "UK",
            "status": "Exact",
            "category": "Carrier",
            "low_b": 1.276,
            "high_b": 1.276,
        },
        {
            "company": "Chubb",
            "country": "CH",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.56,
            "high_b": 0.80,
        },
        {
            "company": "AIG",
            "country": "US",
            "status": "Range",
            "category": "Carrier",
            "low_b": 0.25,
            "high_b": 0.30,
        },
        {
            "company": "Travelers",
            "country": "US",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.4,
            "high_b": 0.5,
        },
        {
            "company": "AXA XL",
            "country": "FR",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.6,
            "high_b": 0.8,
        },
        {
            "company": "Zurich",
            "country": "CH",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.5,
            "high_b": 0.7,
        },
        {
            "company": "Munich Re",
            "country": "DE",
            "status": "Range",
            "category": "Reinsurer",
            "low_b": 1.5,
            "high_b": 2.0,
        },
        {
            "company": "Swiss Re",
            "country": "CH",
            "status": "Est.",
            "category": "Reinsurer",
            "low_b": 1.3,
            "high_b": 1.8,
        },
        {
            "company": "Hiscox",
            "country": "UK",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.3,
            "high_b": 0.45,
        },
        {
            "company": "QBE",
            "country": "AU",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.25,
            "high_b": 0.35,
        },
        {
            "company": "Aviva",
            "country": "UK",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.15,
            "high_b": 0.25,
        },
        {
            "company": "Brit",
            "country": "UK",
            "status": "Est.",
            "category": "Carrier",
            "low_b": 0.2,
            "high_b": 0.3,
        },
    ]

    _flag_by_country = {
        "US": "🇺🇸",
        "UK": "🇬🇧",
        "CH": "🇨🇭",
        "FR": "🇫🇷",
        "DE": "🇩🇪",
        "AU": "🇦🇺",
    }

    root = "Cyber insurance"

    _labels = [root]
    _parents = [""]
    _values = [0.0]
    _customdata = [""]

    categories = sorted({str(c["category"]) for c in cyber_company_premiums})
    category_to_idx: dict[str, int] = {}
    for cat in categories:
        category_to_idx[cat] = len(_labels)
        _labels.append(cat)
        _parents.append(root)
        _values.append(0.0)
        _customdata.append(f"<b>{cat}</b><br>Group: {cat}<extra></extra>")

    total_mid_b = 0.0
    for c in cyber_company_premiums:
        low_b = float(c["low_b"])
        high_b = float(c["high_b"])
        mid_b = (low_b + high_b) / 2.0
        total_mid_b += mid_b

        flag = _flag_by_country.get(c["country"], "")
        company_label = f"{c['company']} {flag}".strip()

        _labels.append(company_label)
        _parents.append(c["category"])
        _values.append(mid_b)
        _customdata.append(
            "<b>{company}</b>"
            "<br>Category: {category}"
            "<br>Country: {flag} {country}"
            "<br>Status: {status}"
            "<br>Premium midpoint: ${mid:.2f}B"
            "<br>Range: ${low:.2f}B - ${high:.2f}B"
            "<extra></extra>".format(
                company=company_label,
                category=c["category"],
                country=c["country"],
                flag=flag,
                status=c["status"],
                mid=mid_b,
                low=low_b,
                high=high_b,
            )
        )

        # Accumulate into the category node so branchvalues="total" works.
        _values[category_to_idx[str(c["category"])]] += mid_b

    _values[0] = total_mid_b

    treemap_fig = go.Figure(
        go.Treemap(
            labels=_labels,
            parents=_parents,
            values=_values,
            branchvalues="total",
            customdata=_customdata,
            hovertemplate="%{customdata}",
            texttemplate="<b>%{label}</b><br>$%{value:.2f}B",
        )
    )

    treemap_fig.update_layout(
        title="Cyber insurance companies by premium volume (midpoints, USD billions)",
        margin=dict(t=70, l=10, r=10, b=10),
    )

    treemap_fig
    return


if __name__ == "__main__":
    app.run()
