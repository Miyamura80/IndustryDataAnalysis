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
    - Reinsurance market size (~\$0.4T) is 2024 global reinsurance gross written premium (~\$293B non-life + ~\$102B life; Atlas Magazine / AM Best reinsurer rankings).
    - Company figures use **AM Best 2024 net premiums written** (USD), which provides a clean comparable basis across sectors.
    - Reinsurer company figures are AM Best **gross premiums written** from their reinsurer ranking.
    - Total across all four sectors sums to approximately **US\$8.0T**; note reinsurance (~\$0.4T) is largely ceded from the primary Life/Health/P&C books, so primary premiums alone are ~\$7.6T (Swiss Re sigma).
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

    - Root shows the combined global insurance market at **~US\$8.0T** (sum of four sectors); children roll up with `branchvalues="total"`.
    - **Life** (~$3.1T) is the largest sector by premiums, followed by **P&C** (~$2.6T), **Health** (~$1.8T), and **Reinsurance** (~$0.4T).
    - Company nodes use AM Best 2024 net premiums written (or GPW for reinsurers) in USD for cross-sector comparability.
    - There is inherent overlap: reinsurance premiums are ceded from primary Life, Health, and P&C books, so the \$8.0T total double-counts some premium flow.
    - Health sector top players (UnitedHealth, Centene, Elevance) are US-centric managed-care giants; the global pool includes many smaller national carriers.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## US P&C market sizes (last 5 years)

    US Property & Casualty net premiums written by line of business (NAIC statutory data via Triple-I / S&P Global). The dashed line sums the net-written lines only; Cyber is shown as direct premiums written (it is reported as DWP, not NPW) and is excluded from that total. The Triple-I line-of-business table is publicly archived only through 2023, so the NPW lines are blank for 2024-2025; Cyber runs to 2024.
    """)
    return


@app.cell
def _(go, mo):
    import csv as _csv
    from pathlib import Path as _Path

    _data_dir = (
        _Path(__file__).parent / "data"
        if "__file__" in globals()
        else _Path.cwd() / "notebooks" / "data"
    )
    _csv_path = _data_dir / "insurance_us_pc_market_sizes_2020_2025.csv"

    _uspc_out = None
    if not _csv_path.exists():
        _uspc_out = mo.md(f"Data file not found: `{_csv_path}`")
    else:
        with _csv_path.open("r", newline="", encoding="utf-8") as _f:
            _reader = _csv.DictReader(_f)
            _fields = _reader.fieldnames or []
            _years = sorted(int(_c) for _c in _fields if _c.isdigit())
            _rows = [
                _r
                for _r in _reader
                if _r.get("segment") == "Property & Casualty"
                and _r.get("geo") == "US"
            ]

        _exclude = {
            "Commercial Property - Fire",
            "Commercial Property - Allied Lines",
        }
        _direct_only = {"Cyber"}

        _year_has = {
            _y: any((_r.get(str(_y)) or "").strip() for _r in _rows) for _y in _years
        }
        _plot_years = [_y for _y in _years if _year_has[_y]][-5:]

        _series = {}
        for _r in _rows:
            _sub = (_r.get("subsegment") or "").strip()
            if not _sub or _sub in _exclude:
                continue
            _vals = []
            for _y in _plot_years:
                _raw = (_r.get(str(_y)) or "").strip()
                _vals.append(float(_raw) if _raw else None)
            _series[_sub] = _vals

        _totals = []
        for _i in range(len(_plot_years)):
            _t, _has = 0.0, False
            for _sub, _vals in _series.items():
                if _sub in _direct_only or _vals[_i] is None:
                    continue
                _t += _vals[_i]
                _has = True
            _totals.append(_t if _has else None)

        _x = [str(_y) for _y in _plot_years]
        _fig = go.Figure()
        for _name in sorted(_series):
            _fig.add_trace(
                go.Scatter(
                    x=_x,
                    y=_series[_name],
                    mode="lines+markers",
                    name=_name,
                    connectgaps=False,
                    hovertemplate="<b>%{fullData.name}</b><br>%{x}: $%{y:.1f}B<extra></extra>",
                )
            )
        _fig.add_trace(
            go.Scatter(
                x=_x,
                y=_totals,
                mode="lines+markers",
                name="Total (net-written lines only)",
                line=dict(width=4, dash="dash", color="#1b2330"),
                hovertemplate="<b>%{fullData.name}</b><br>%{x}: $%{y:.1f}B<extra></extra>",
            )
        )
        _fig.update_layout(
            title=f"US P&C insurance market sizes ({_plot_years[0]}-{_plot_years[-1]})",
            xaxis=dict(title="Year", type="category"),
            yaxis_title="Premiums ($bn)",
            legend_title="Line of business",
            hovermode="x unified",
            height=470,
            margin=dict(t=70, l=55, r=20, b=40),
        )
        _uspc_out = _fig

    _uspc_out
    return


@app.cell
def _(mo):
    mo.md("""
    ## Global insurance market size proxies (last 5 years, with uncertainty)

    Global premium pools by segment, with a low/high band spanning reputable estimates (Swiss Re sigma, Allianz, Munich Re, OECD). The line is the point estimate; whiskers show the band. Bands widen where sources disagree on definitions — most visibly Health in 2024, where Swiss Re allocates all accident-and-health to non-life and captures the full US private-health pool, while Allianz draws health more narrowly.
    """)
    return


@app.cell
def _(go, mo):
    import csv as _pcsv
    from pathlib import Path as _PPath

    _pdir = (
        _PPath(__file__).parent / "data"
        if "__file__" in globals()
        else _PPath.cwd() / "notebooks" / "data"
    )
    _proxy_path = _pdir / "insurance_global_market_size_proxies_2020_2025.csv"

    _proxy_out = None
    if not _proxy_path.exists():
        _proxy_out = mo.md(f"Data file not found: `{_proxy_path}`")
    else:
        with _proxy_path.open("r", newline="", encoding="utf-8") as _pf:
            _preader = _pcsv.DictReader(_pf)
            _pyears = sorted(
                int(_c) for _c in (_preader.fieldnames or []) if _c.isdigit()
            )
            _prows = list(_preader)

        _seg_color = {
            "Life": "#1f5fd6",
            "Health": "#2e8b57",
            "Property & Casualty": "#c0392b",
            "Reinsurance": "#c98f3c",
        }
        _x2 = [str(_y) for _y in _pyears]
        _pfig = go.Figure()
        for _r in _prows:
            _seg = (_r.get("segment") or "").strip()
            _sub = (_r.get("subsegment") or "").strip()
            if "total" not in _sub.lower() and "all products" not in _sub.lower():
                continue
            _yv, _ep, _em, _has = [], [], [], False
            for _y in _pyears:
                _v = (_r.get(str(_y)) or "").strip()
                _lo = (_r.get(f"{_y}_low") or "").strip()
                _hi = (_r.get(f"{_y}_high") or "").strip()
                if _v and _lo and _hi:
                    _vf, _lof, _hif = float(_v), float(_lo), float(_hi)
                    _yv.append(_vf)
                    _ep.append(max(0.0, _hif - _vf))
                    _em.append(max(0.0, _vf - _lof))
                    _has = True
                else:
                    _yv.append(None)
                    _ep.append(0.0)
                    _em.append(0.0)
            if not _has:
                continue
            _color = _seg_color.get(_seg, "#7f7f7f")
            _pfig.add_trace(
                go.Scatter(
                    x=_x2,
                    y=_yv,
                    mode="lines+markers",
                    name=_seg,
                    line=dict(width=2.5, color=_color),
                    marker=dict(size=7, color=_color),
                    error_y=dict(
                        type="data",
                        symmetric=False,
                        array=_ep,
                        arrayminus=_em,
                        color=_color,
                        thickness=1,
                        width=4,
                    ),
                    connectgaps=True,
                    hovertemplate="<b>%{fullData.name}</b><br>%{x}: $%{y:,.0f}B<extra></extra>",
                )
            )
        _pfig.update_layout(
            title="Global insurance premium pools by segment (2020-2025, with uncertainty)",
            xaxis=dict(title="Year", type="category"),
            yaxis=dict(title="Premiums ($bn, log scale)", type="log"),
            legend_title="Segment",
            hovermode="x unified",
            height=470,
            margin=dict(t=70, l=60, r=20, b=40),
        )
        _proxy_out = _pfig

    _proxy_out
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


@app.cell
def _(mo):
    mo.md(
        """
    ---

    # Insurance market structure: who bears risk, who funds it, at what multiple

    Notebook entry. Durable structural model plus the 2024-2026 evidence that supports it. Point-in-time figures are dated inline; the layer model and the multiple gradient are the parts expected to survive.

    Researched: 2026-08-18. Trigger: checking whether large dedicated cybersecurity VCs carry any cyber-insurance exposure. The answer is essentially none, which turned out to be the normal case and worth explaining.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 1. The layer model

    Insurance markets separate into three layers that look adjacent but have different economics, different capital providers, and different valuation regimes. Confusing them is the most common error when reasoning about "insurance" as a business.
    """
    )
    return


@app.cell
def _(mo):
    _svg = """
<svg viewBox="0 0 720 470" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Insurance layer model: signal/software feeds distribution, which writes on risk transfer; the revenue multiple falls down the stack from 15-30x to 1-3x" style="width:100%;max-width:720px;height:auto;font-family:'PT Sans',system-ui,-apple-system,'Segoe UI',sans-serif;">
  <defs>
    <linearGradient id="mgrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1f5fd6"/>
      <stop offset="50%" stop-color="#c98f3c"/>
      <stop offset="100%" stop-color="#b5502e"/>
    </linearGradient>
    <marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0 L10 5 L0 10 z" fill="#5b6675"/>
    </marker>
  </defs>

  <rect x="24" y="20" width="600" height="116" rx="12" fill="#eef3fc" stroke="#c7d8f4"/>
  <rect x="24" y="20" width="7" height="116" rx="3.5" fill="#1f5fd6"/>
  <text x="48" y="52" font-size="16" font-weight="700" fill="#1f5fd6">SIGNAL / SOFTWARE</text>
  <text x="48" y="78" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">OWNS</text>
  <text x="48" y="98" font-size="13.5" fill="#1b2330">data, scores, controls,</text>
  <text x="48" y="116" font-size="13.5" fill="#1b2330">evidence, telemetry</text>
  <text x="330" y="78" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">FUNDED BY</text>
  <text x="330" y="98" font-size="13.5" fill="#1b2330">generalist + sector VC</text>
  <text x="330" y="116" font-size="13.5" fill="#1b2330">(software multiples)</text>
  <text x="600" y="52" font-size="15" font-weight="700" text-anchor="end" fill="#1f5fd6">15–30x</text>

  <line x1="120" y1="140" x2="120" y2="174" stroke="#5b6675" stroke-width="1.6" marker-end="url(#arw)"/>
  <text x="132" y="162" font-size="12" font-style="italic" fill="#5b6675">feeds</text>

  <rect x="24" y="178" width="600" height="116" rx="12" fill="#fbf4e8" stroke="#ecd9b6"/>
  <rect x="24" y="178" width="7" height="116" rx="3.5" fill="#c98f3c"/>
  <text x="48" y="210" font-size="16" font-weight="700" fill="#b07d2c">DISTRIBUTION — MGA / broker</text>
  <text x="48" y="236" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">OWNS</text>
  <text x="48" y="256" font-size="13.5" fill="#1b2330">the customer, underwriting</text>
  <text x="48" y="274" font-size="13.5" fill="#1b2330">authority, commission on GWP</text>
  <text x="330" y="236" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">FUNDED BY</text>
  <text x="330" y="256" font-size="13.5" fill="#1b2330">insurance-native capital,</text>
  <text x="330" y="274" font-size="13.5" fill="#1b2330">carriers who supply the paper</text>
  <text x="600" y="210" font-size="15" font-weight="700" text-anchor="end" fill="#b07d2c">~5x</text>

  <line x1="120" y1="298" x2="120" y2="332" stroke="#5b6675" stroke-width="1.6" marker-end="url(#arw)"/>
  <text x="132" y="320" font-size="12" font-style="italic" fill="#5b6675">writes on</text>

  <rect x="24" y="336" width="600" height="116" rx="12" fill="#f8ece7" stroke="#e6c3b6"/>
  <rect x="24" y="336" width="7" height="116" rx="3.5" fill="#b5502e"/>
  <text x="48" y="368" font-size="16" font-weight="700" fill="#b5502e">RISK TRANSFER — carrier</text>
  <text x="48" y="394" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">OWNS</text>
  <text x="48" y="414" font-size="13.5" fill="#1b2330">the balance sheet, statutory</text>
  <text x="48" y="432" font-size="13.5" fill="#1b2330">capital, the loss itself</text>
  <text x="330" y="394" font-size="10.5" letter-spacing="0.07em" fill="#5b6675">FUNDED BY</text>
  <text x="330" y="414" font-size="13.5" fill="#1b2330">reinsurers, PE, strategic</text>
  <text x="330" y="432" font-size="13.5" fill="#1b2330">carriers, sovereigns</text>
  <text x="600" y="368" font-size="15" font-weight="700" text-anchor="end" fill="#b5502e">1–3x</text>

  <rect x="648" y="20" width="15" height="432" rx="7.5" fill="url(#mgrad)"/>
  <text x="695" y="236" font-size="10.5" letter-spacing="0.09em" fill="#5b6675" text-anchor="middle" transform="rotate(90 695 236)">REVENUE MULTIPLE FALLS</text>
</svg>
"""
    mo.Html(_svg)
    return


@app.cell
def _(mo):
    mo.md(
        """
    The layer determines almost everything else about the business. An MGA holds underwriting authority without holding the risk, so it lives or dies on whether a reinsurer keeps granting capacity. A carrier holds the risk and therefore holds regulatory capital, which is the constraint that governs its growth rate.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 2. The multiple gradient

    The gradient across those layers is steep, and it is the single fact that explains most investor behaviour. Software-layer businesses clear 10-30x revenue; brokers sit around 5x; capital-intensive carriers earn just 1-3x.
    """
    )
    return


@app.cell
def _(go):
    _mg_layers = [
        "AI-native / B2B insurance infra",
        "Insurance software (historic)",
        "Insurtech blended avg (2024)",
        "Broker",
        "Capital-intensive carrier",
    ]
    _mg_mid = [22.5, 10.0, 9.7, 5.0, 2.0]
    _mg_err_plus = [7.5, 0.0, 0.0, 0.0, 1.0]
    _mg_err_minus = [7.5, 0.0, 0.0, 0.0, 1.0]
    _mg_disp = ["15x to 30x", "~10x", "9.7x", "5x+", "1x to 3x"]
    _mg_margin = ["software", "software", "mixed", "20-30%", "5-10%"]
    _mg_colors = ["#1f5fd6", "#4f83e0", "#7aa3e8", "#c98f3c", "#b5502e"]

    _mg_fig = go.Figure(
        go.Bar(
            y=_mg_layers,
            x=_mg_mid,
            orientation="h",
            marker_color=_mg_colors,
            error_x=dict(
                type="data",
                symmetric=False,
                array=_mg_err_plus,
                arrayminus=_mg_err_minus,
                color="#7a8496",
                thickness=1.4,
                width=6,
            ),
            customdata=list(zip(_mg_disp, _mg_margin)),
            text=_mg_disp,
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "<b>%{y}</b><br>Revenue multiple: %{customdata[0]}"
                "<br>Margin profile: %{customdata[1]}<extra></extra>"
            ),
        )
    )
    _mg_fig.update_layout(
        title="The multiple gradient: EV/revenue by layer (bar = midpoint, whisker = range)",
        xaxis=dict(title="EV / revenue multiple (x)", range=[0, 36]),
        yaxis=dict(autorange="reversed"),
        height=340,
        margin=dict(t=70, l=210, r=60, b=50),
    )
    _mg_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    At a 5x revenue multiple, 30% margins imply roughly a 16.6x P/E. At 1x revenue, 7% margins imply roughly 14.3x. The equity story converges even though the revenue multiple differs by 5x, which is why the revenue multiple alone misleads across layers.

    Valuation basis has also tightened. Gross Written Premium is no longer treated as a credible basis in most deals. The market moved to net revenue, net commission for MGAs, or earned premium minus reinsurance and claims for carriers. Investors now pay for retained economics and unit durability.

    ### Why venture capital concentrates at the top layer

    Money put into a carrier funds reserves and statutory surplus. It does not fund growth. That is the worst possible use of venture dollars: the capital is absorbed by regulatory requirement, converts at an insurance multiple, and is exposed to loss volatility the fund cannot model. An MGA is better but carries a capacity dependency underneath it that no growth-equity fund wants sitting under a large position.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 3. The whole VC-backed insurance universe sorts the same way

    The layer model is not a cyber-only pattern. Take the roughly thirty most category-defining venture-backed insurance companies since 2010 — full-stack carriers, MGAs, embedded players, core-systems software — and their outcomes sort cleanly by layer. The companies that carried balance-sheet risk absorbed the worst repricings; the capital-light distribution and software layers held up; the cyber MGAs, which pair asset-light economics with a proprietary security signal, did best of the risk-adjacent group.
    """
    )
    return


@app.cell
def _(go):
    _co_layers = [
        "Software / infrastructure",
        "Cyber MGA (signal + distribution)",
        "Distribution — MGA / embedded",
        "Full-stack carrier (risk transfer)",
    ]
    # Counts aligned to _co_layers, ordered high-multiple (top) to low (bottom).
    _co_outcomes = [
        (
            "Breakout",
            "#2e8b57",
            [2, 1, 4, 1],
            [
                "Guidewire, Akur8",
                "Coalition",
                "Next, Bold Penguin, bolttech, Cover Genius",
                "Alan",
            ],
        ),
        (
            "Mixed",
            "#c98f3c",
            [4, 4, 5, 4],
            [
                "Duck Creek, Shift, Tractable, Ledger",
                "At-Bay, Cowbell, Corvus, Resilience",
                "Pie, Openly, Kin, Vouch, Sure",
                "Lemonade, Hippo, Oscar, ZhongAn",
            ],
        ),
        (
            "Cautionary",
            "#b5502e",
            [0, 0, 2, 4],
            [
                "—",
                "—",
                "Branch, Trov",
                "Root, Metromile, Clover, wefox",
            ],
        ),
    ]

    _co_fig = go.Figure()
    for _co_name, _co_color, _co_vals, _co_examples in _co_outcomes:
        _co_fig.add_trace(
            go.Bar(
                y=_co_layers,
                x=_co_vals,
                name=_co_name,
                orientation="h",
                marker_color=_co_color,
                customdata=_co_examples,
                hovertemplate=(
                    "<b>%{y}</b><br>"
                    + _co_name
                    + ": %{x} companies<br>%{customdata}<extra></extra>"
                ),
            )
        )
    _co_fig.update_layout(
        barmode="stack",
        title="Where the outcomes landed: category-defining insurtechs by layer and result",
        xaxis=dict(title="Number of companies"),
        yaxis=dict(autorange="reversed"),
        legend=dict(title="Outcome", orientation="h", y=-0.24),
        height=360,
        margin=dict(t=70, l=220, r=30, b=80),
    )
    _co_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Read the bars top to bottom, high multiple to low. Every software, infrastructure and cyber-MGA company lands in breakout or mixed — none cautionary. The full-stack carriers invert it: one breakout (Alan, in Europe), the rest mixed or cautionary. The mechanism is the balance sheet. A carrier is judged on loss and combined ratios, holds regulatory capital, and carries catastrophe and reserve risk, so growth consumes capital instead of compounding it. When public markets stopped granting these companies software multiples and re-anchored them to insurance economics, the drawdowns ran 80-90% (Root is off ~87% from its IPO; Metromile was sold for less than the cash on its own balance sheet).

    ### Signal, software and infrastructure — the durable layer

    | Company | Founded | Raised (approx) | Status | Outcome |
    |---|---|---|---|---|
    | Guidewire 🇺🇸 | 2001 | \$40M total pre-IPO | IPO 2012 (GWRE), ~\$10B at 6.9x revenue | Breakout |
    | Akur8 🇫🇷 | 2018 | ~\$180-195M | Private; \$120M Series C (2024); Guidewire-backed | Breakout |
    | Duck Creek 🇺🇸 | 2000 | PE / corporate-backed | Vista take-private \$2.6B (2023) | Mixed |
    | Shift Technology 🇫🇷 | 2014 | ~\$320M | Private, unicorn (2021) | Mixed |
    | Tractable 🇬🇧 | 2014 | ~\$185M | Private, \$1B (2021); first CV unicorn | Mixed |
    | Ledger Investing 🇺🇸 | 2016 | ~\$90-185M (disputed) | Private; casualty ILS rails | Mixed |

    ### Cyber MGA — signal plus distribution

    | Company | Founded | Raised (approx) | Status | Outcome |
    |---|---|---|---|---|
    | Coalition 🇺🇸 | 2017 | ~\$800-860M | Private, \$5B (2022); ~\$1B revenue, no S-1 | Breakout |
    | At-Bay 🇺🇸 | 2016 | ~\$292M | Private, \$1.35B (2021) | Mixed |
    | Cowbell 🇺🇸 | 2019 | ~\$202-209M | Private; Zurich-led Series C (2024) | Mixed |
    | Corvus 🇺🇸 | 2017 | ~\$150M | Acquired by Travelers ~\$435M (2024) | Mixed |
    | Resilience 🇺🇸 | 2016 | ~\$325M | Private; Series D (2023) | Mixed |

    ### Distribution — MGA and embedded

    | Company | Founded | Raised (approx) | Status | Outcome |
    |---|---|---|---|---|
    | Next Insurance 🇺🇸 | 2016 | ~\$1.1-1.2B | Acquired by Munich Re / ERGO \$2.6B (2025) | Breakout |
    | Bold Penguin 🇺🇸 | 2016 | ~\$50M | Acquired by American Family (2021) | Breakout |
    | bolttech 🇸🇬 | 2020 | ~\$640-690M | Private, \$2.1B (2025) | Breakout |
    | Cover Genius 🇦🇺 | 2014 | ~\$350M+ equity | Private, \$1.9B (2026) | Breakout |
    | Pie Insurance 🇺🇸 | 2017 | ~\$620M | Private; \$315M Series D (2022) | Mixed |
    | Openly 🇺🇸 | 2017 | ~\$293M+ | Private; \$193M growth round (2025) | Mixed |
    | Kin 🇺🇸 | 2016 | ~\$265M equity | Private, unicorn (2023); reciprocal exchange | Mixed |
    | Vouch 🇺🇸 | 2018 | ~\$185M+ | Private; startup-focused MGA | Mixed |
    | Sure 🇺🇸 | 2015 | ~\$123M | Private; embedded-insurance API | Mixed |
    | Branch 🇺🇸 | 2018 | ~\$197M | Private; \$1.05B mark (2022), now stale | Cautionary |
    | Trov 🇺🇸 | 2012 | ~\$85-100M | Tech assets to Travelers (2022) | Cautionary |

    ### Full-stack carriers — risk transfer, the repriced layer

    | Company | Founded | Raised (approx) | Status | Outcome |
    |---|---|---|---|---|
    | Alan 🇫🇷 | 2016 | ~\$1.1B+ | Private, €5.5B (2026); profitable in France | Breakout |
    | Lemonade 🇺🇸 | 2015 | ~\$480M pre-IPO | IPO 2020 (LMND), ~\$5.6B mcap; still ~7x revenue | Mixed |
    | Hippo 🇺🇸 | 2015 | ~\$1.2B incl. SPAC | SPAC 2021 (HIPO); 5 profitable quarters after pivot | Mixed |
    | Oscar Health 🇺🇸 | 2012 | ~\$1.6B | IPO 2021 (OSCR); \$15.3B revenue, 0.53x sales | Mixed |
    | ZhongAn 🇨🇳 | 2013 | \$1.5B at IPO | IPO 2017 (6060.HK) at \$11B; >20% China online P&C | Mixed |
    | Root 🇺🇸 | 2015 | ~\$523M pre-IPO | IPO 2020 (ROOT), −87% vs IPO; profitable 2025 | Cautionary |
    | Metromile 🇺🇸 | 2011 | ~\$300M+ | Sold to Lemonade ~\$145M (2022), below its cash | Cautionary |
    | Clover Health 🇺🇸 | 2014 | ~\$925M | SPAC 2021 (CLOV); ~1.1x sales, loss-making | Cautionary |
    | wefox 🇩🇪 | 2014 | ~\$1.9B | Peak \$4.5B (2022) → near-insolvency, restructured | Cautionary |

    The single cleanest comparison in the set is Guidewire against Metromile. Guidewire raised \$40M in its entire pre-IPO life and is worth roughly \$10B; Metromile raised ~\$300M, SPAC'd at \$1.3B, and sold three years later for less than the cash on its own balance sheet. Both were "insurance technology." The difference is that one of them promised to pay claims. Premium revenue is a capital call, not free revenue: growing a carrier's book 50% demands ~50% more surplus, so top-line growth consumes equity instead of throwing off cash — the inverse of the software model those 2020-21 multiples were priced on. The most telling evidence is not the failures but how the survivors survived: they changed layer. Hippo pivoted from concentrated cat-exposed homeowners into an MGA and fronting platform and has now posted five straight profitable quarters; wefox sold its carrier and re-emerged asset-light. The fix for a struggling full-stack model was to stop being full-stack.

    The cyber MGAs are the instructive hybrid. Structurally they are MGAs, but they own a proprietary signal — continuous attack-surface scanning — that genuinely predicts loss, on a short tail the insurer can intervene to prevent. That let them capture underwriting alpha without the balance-sheet drag, which is why strategic reinsurers funded the whole cohort and Coalition now stands at a \$5B private mark on ~\$1B of revenue. The cautionary read within cyber is the Corvus price: Travelers paid ~\$435M for a \$200M+ book, roughly 2x premium — a distribution-and-capability price, not a software multiple. The gap between that and Coalition's \$5B mark is the most important unresolved number here, and a Coalition S-1 would settle it.

    ### The multiple falls monotonically down the stack

    | Layer | Typical multiple | Public / deal reference points |
    |---|---|---|
    | Software / infrastructure | 6-15x revenue | Guidewire 6.9x revenue, 30x EBITDA; Duck Creek \$2.6B take-private |
    | MGA / fee-based | 3-8x net revenue | MGA M&A 10-22x EBITDA; Cover Genius \$1.9B, bolttech \$2.1B |
    | Fronting | ~9-10x revenue | Accelerant IPO implied ~9-10x on \$178M Q1 2025 revenue |
    | Full-stack carrier | 1.5-4x revenue | Oscar 0.53x sales; Root ~0.6x; Clover ~1.1x |

    Two refinements matter. The definitional shift did most of the damage: the market stopped accepting gross written premium as a valuation base and moved to net revenue (MGAs) or earned premium net of reinsurance and claims (carriers), so a company priced on a GWP-derived top line at a software multiple, then repriced on net revenue at an insurance multiple, lost an order of magnitude without anything changing operationally. And Lemonade is the live outlier: at ~\$5.6B on ~\$800M of revenue it still trades near 7x, a software multiple on a balance-sheet business. Whether that converges up (it earns the multiple by hitting profitability) or down (toward Root and Oscar) is the cleanest open test of the whole thesis, and it should resolve within about eighteen months.

    Figures are approximate: private "raised" totals are aggregator estimates (Crunchbase / PitchBook / Tracxn) and occasionally blend debt with equity — Ledger Investing's own figure (>\$90M) and ZoomInfo's (\$185M) genuinely conflict. Deal prices, IPO proceeds and public multiples are from filings and trade press and are firmer. Valuations are last known marks, not current.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 4. Cyber insurance conditions, 2024-2026

    Underwriting quality and growth trajectory have diverged sharply, and both facts need holding at once. Underwriting is healthy: the surplus-lines loss ratio is ~56% (2025, and surplus lines is now nearly two-thirds of all cyber premium), the admitted-carrier loss ratio is ~50.2%, and Allianz Commercial reports average claim severity down 50% with large-loss frequency down 30%. Growth, meanwhile, has stalled — Q1 2026 was the eighth consecutive quarter of US pricing cuts. The chart tracks where the market is heading.
    """
    )
    return


@app.cell
def _(go):
    _cc_labels = [
        "US cyber premium (2024)",
        "Cyber reinsurance (Jan 2026 renewals)",
        "Global premium (2025->2026, proj.)",
        "S&P premium growth (2026, proj.)",
        "Third-party claims (trend)",
    ]
    _cc_vals = [-7.0, -32.0, 5.1, 17.5, 30.0]
    _cc_proj = [False, False, True, True, False]
    _cc_detail = [
        "First annual decline on record; US DWP fell to $9.14bn",
        "Risk-adjusted, aggregate excess of loss; driven by excess capacity",
        "$15.6bn (2025) -> $16.4bn (2026), projected",
        "S&P Global Ratings; 15-20% range, contested vs. 8 quarters of softening",
        "Rising; the main forward uncertainty",
    ]
    _cc_colors = ["#c0392b" if _v < 0 else "#2e8b57" for _v in _cc_vals]
    _cc_pattern = ["/" if _p else "" for _p in _cc_proj]

    _cc_fig = go.Figure(
        go.Bar(
            y=_cc_labels,
            x=_cc_vals,
            orientation="h",
            marker=dict(
                color=_cc_colors,
                pattern=dict(shape=_cc_pattern, solidity=0.72),
            ),
            customdata=_cc_detail,
            text=[f"{_v:+.0f}%" for _v in _cc_vals],
            textposition="outside",
            cliponaxis=False,
            hovertemplate="<b>%{y}</b><br>Change: %{x:+.1f}%<br>%{customdata}<extra></extra>",
        )
    )
    _cc_fig.add_vline(x=0, line_width=1, line_color="#9aa4b2")
    _cc_fig.update_layout(
        title="Cyber market 2024-26: pricing down, claims and forecasts up (hatched = projected)",
        xaxis=dict(title="Change (%)", range=[-42, 44], zeroline=False),
        yaxis=dict(autorange="reversed"),
        height=340,
        margin=dict(t=70, l=240, r=50, b=50),
    )
    _cc_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    The takeaway: a well-run cyber carrier is profitable and growing slowly. That combination is fine for insurance capital and unworkable for venture capital. Category quality and venture suitability are separate questions.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 5. Exit evidence

    The category's benchmark exit was a down-round: Corvus sold to Travelers for \$435M (announced Nov 2023, closed Jan 2024), against a \$750M valuation in its 2021 round — a 42% markdown. Coalition's \$175M round (Index Ventures, March 2021) set a \$1.75bn mark at the peak.
    """
    )
    return


@app.cell
def _(go):
    _ex_labels = [
        "Corvus - 2021 round",
        "Corvus - 2024 exit (Travelers)",
        "Coalition - 2021 round",
    ]
    _ex_vals = [750, 435, 1750]
    _ex_text = ["$750M", "$435M", "$1.75bn"]
    _ex_colors = ["#7aa3e8", "#b5502e", "#9aa4b2"]
    _ex_note = [
        "Funding-round valuation (2021 peak)",
        "Acquisition price; a 42% down-round vs. the 2021 mark",
        "Index Ventures round; benchmark scale insurtech",
    ]

    _ex_fig = go.Figure(
        go.Bar(
            y=_ex_labels,
            x=_ex_vals,
            orientation="h",
            marker_color=_ex_colors,
            customdata=_ex_note,
            text=_ex_text,
            textposition="outside",
            cliponaxis=False,
            hovertemplate="<b>%{y}</b><br>Valuation: $%{x:,.0f}M<br>%{customdata}<extra></extra>",
        )
    )
    _ex_fig.add_annotation(
        x=435,
        y="Corvus - 2024 exit (Travelers)",
        text="-42% vs. 2021",
        showarrow=True,
        arrowhead=2,
        ax=80,
        ay=-26,
        font=dict(size=10, color="#b5502e"),
    )
    _ex_fig.update_layout(
        title="Insurtech exits: the Corvus down-round (USD millions)",
        xaxis=dict(title="Valuation / price (USD millions)", range=[0, 2050]),
        yaxis=dict(autorange="reversed"),
        height=280,
        margin=dict(t=70, l=210, r=70, b=50),
    )
    _ex_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    - Insurtech funding fell ~50% in 2023 with valuations off more than 60% — the period the sector calls "the death of Insurtech 1.0".
    - Insurance CVC participation hit a 9-year low: only four insurance CVCs invested in insurtechs in Q1 2026 (American Family Ventures, Intact Ventures, Optum Ventures, Sancor Seguros Ventures).
    - Reinsurer scrutiny and capital constraint is the recurring friction cited against MGA models.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 6. Who actually funds cyber insurance

    The cap tables sort exactly along the layer model. Strategic insurance capital dominates risk transfer and distribution.

    | Company | Backers | Note |
    |---|---|---|
    | Corvus 🇺🇸 | Aquiline, FinTLV, .406 Ventures, SiriusPoint, Travelers | acquired by Travelers |
    | At-Bay 🇺🇸 | Munich Re | reinsurer-backed |
    | Cowbell 🇺🇸 | Zurich | carrier-backed |
    | Coalition 🇺🇸 | Index Ventures | fintech thesis rather than a cyber thesis |

    The structural logic: the natural investor in an MGA is a carrier that can also supply the paper. They are buying distribution and underwriting data, and the capacity arrives bundled with the cheque. A software fund brings money and nothing else the business needs.

    ### Cyber-specialist VCs do sometimes cross over

    Worth recording because it falsifies the simpler story that cyber funds avoid insurance on principle.

    - Forgepoint Capital 🇺🇸 led Converge Insurance 🇺🇸 (\$15M Series A, August 2023, an SMB cyber MGA), with two managing directors taking board seats. It was Forgepoint's second move into the space after incubating Surefire Cyber 🇺🇸, which sells incident response to insurers, brokers, and law firms.

    Note the shape: small, early-stage, sometimes incubated in-house. That is a fund buying optionality on a category thesis. It is a different instrument from a \$20-150M growth cheque, and it does not generalise to growth-stage funds.

    ### The AI-liability MGAs confirm the split

    The emerging AI-specific carriers are funded by insurance capital and generalists, with no cyber fund among them.

    - Armilla AI 🇨🇦: Lloyd's coverholder, Chaucer-backed, up to \$25M per organisation. Also sells a performance warranty that pays out against missed contractual KPIs such as accuracy or bias thresholds.
    - Testudo 🇺🇸: Apollo-backed, Lloyd's paper, up to \$10M, all 50 states.
    - AIUC 🇺🇸: MGA that secured Beazley paper for its liability product (May 2026). \$15M seed led by NFDG (Nat Friedman), with Emergence, Terrain, and Ben Mann among angels.
    - Munich Re aiSure 🇩🇪: incumbent reinsurer product.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 7. Where cybersecurity VCs actually sit

    Look at a large dedicated cybersecurity / AI-software fund — the kind running a ~\$1bn vehicle, writing \$20-150M cheques into 50-plus portfolio companies — and the pattern is consistent: zero risk-bearing exposure. No carrier, no MGA, no insurtech, no warranty product anywhere in the portfolio. What these funds own instead sits one layer up, in underwriting inputs. Representative signal-layer vendors:

    - SecurityScorecard: dedicated insurance business (insurance.securityscorecard.com). Partnerships with Great American Insurance Group, Willis, and Measured Analytics (first premium discount tied to a security rating). Scores correlate with claims frequency per the Marsh McLennan Cyber Risk Intelligence Center. Insurers use it for risk selection, application review, subjectivity management, and pricing.
    - Panaseer: continuous controls monitoring marketed explicitly for answering cyber insurance application questionnaires with evidence, improving terms.
    - Quantexa: decision intelligence for carriers across underwriting and claims, though general commercial lines rather than cyber.

    The AI-security startups these funds favour (data-security and agent-security companies) typically have no insurance partnership, premium programme, warranty, or payout guarantee at all.

    Caveat on interpretation: the mandate-and-multiple explanation is sufficient on its own. Do not read this absence as evidence that agentic AI risk is unpriceable. That is a separate argument requiring separate evidence, and conflating the two weakens both.

    Second caveat: these funds' LP bases often include insurance companies. That is capital flowing from insurers into software funds. It does not indicate a strategy aimed at insurers, though it does mean carriers watch these portfolios.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 8. Implication for a signal-layer vendor

    A one-way door. If a software vendor ever bears risk (warranty, payout guarantee, MGA arm), it moves from the 15-30x column to the 1-3x column, and its natural investor base shifts from software funds to carriers and reinsurers.

    Staying at the signal layer keeps software economics while still selling into the insurance channel. SecurityScorecard is the proof of shape: insurers use it for risk selection and pricing, Marsh McLennan validated its claims correlation, and it remained a software company throughout. That is a fundable shape for a generalist or sector software fund. Risk-bearing is not.

    One white space still holds: no AI-runtime or agent-security vendor has yet claimed either an insurer partnership or an insurance-backed offering. The layer model says the reachable version of that white space is the signal layer, sold to carriers, rather than capacity.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Sources

    Portfolio and investor structure:

    - https://forgepointcap.com/perspectives/converge-insurance-announces-15-million-series-a-funding-from-forgepoint-capital/
    - https://www.securityweek.com/forgepoint-capital-places-15m-series-a-bet-on-converge-insurance/
    - https://securityscorecard.com/company/press/securityscorecard-joins-forces-with-measured-analytics-and-insurance-to-deliver-industry-first-cyber-insurance-discounts-for-top-security-ratings/
    - https://www.financialcontent.com/article/bizwire-2025-4-2-securityscorecard-announces-strategic-partnership-with-willis
    - https://panaseer.com/resources/reports/support-your-cyber-insurance-application-process-with-continuous-controls-monitoring
    - https://www.quantexa.com/industries/insurance/

    Market conditions and valuation:

    - https://www.insurancejournal.com/magazines/mag-features/2026/07/27/878813.htm
    - https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/historic-softening-in-cyber-reinsurance-pricing-as-rates-plunge-32--gallagher-re-563874.aspx
    - https://windsordrake.com/insurtech-valuation/
    - https://www.cbinsights.com/research/report/insurtech-trends-q1-2026/
    - https://www.gunder.com/en/news-insights/client-news/corvus-insurance-acquired-by-travelers-companies-for-435m
    - https://research.astorya.io/post/corvus-insurance-acquired-the-story-of-a-us-cyber-insurtech-benchmark

    AI liability capacity:

    - https://www.theinsurer.com/ti/news/exclusive-ai-insurance-mga-aiuc-secures-beazley-paper-for-liability-product-2026-05-15/
    - https://www.armilla.ai/ai-insurance

    Category-defining companies and multiples (section 3):

    - https://www.ergo.com/en/newsroom/media-information/2025/20250701-ergo-acquisition-next-insurance
    - https://investor.travelers.com/newsroom/press-releases/news-details/2023/Travelers-to-Acquire-Corvus-Insurance/default.aspx
    - https://www.vistaequitypartners.com/news/vista-equity-partners-completes-acquisition-of-duck-creek-technologies/
    - https://www.coalitioninc.com/announcements/coalition-closes-250-million-in-series-f-funding
    - https://multiples.vc/public-comps/guidewire-valuation-multiples
    - https://windsordrake.com/insurtech-valuation/
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Caveats

    - Web research only, point-in-time. Some fund portfolio pages were unreachable from the research environment (proxy policy blocked the domain), so portfolios were reconstructed from funding announcements and press coverage. Announced deals are covered; unannounced or quiet positions are not.
    - Loss ratios, rate movements, and premium totals move every quarter. Re-verify anything in section 4 before using it in a pitch.
    - The S&P 15-20% growth projection for 2026 contradicts the observed softening. Both are recorded deliberately. Do not cite either without the other.
    """
    )
    return


if __name__ == "__main__":
    app.run()
