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
    # If the ocean were a country, its \$2.5 trillion economy would be one of the world's largest (OECD frames it as the world's fifth-largest economy).

    80% of all global goods travel by sea. The ocean economy has grown 2.5x since 1995, outpacing the 1.9x growth of the world economy (UNCTAD 2025). In 2024, global seaborne trade hit 12.7 billion tons -- roughly 1.6 tons for every person on Earth.

    ---

    ## Blue Economy Overview (2024)
    - Global blue economy: ~\$2.5T GVA (OECD); UNCTAD puts ocean trade (exports) at ~\$2.2T (2023).
    - Marine tourism is the single largest segment at \$725B (33% of ocean trade).
    - Maritime shipping moves 80% of global trade by volume but is only 17% of the ocean economy by value.
    - Offshore wind is the fastest-growing segment at ~16% CAGR, projected to reach \$215B by 2034.
    - Three companies (SubCom, ASN, NEC) control >60% of submarine cables carrying 99% of intercontinental internet traffic.
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    segment_data = [
        {"segment": "Marine Tourism & Recreation", "value_billion": 725},
        {"segment": "Maritime Shipping", "value_billion": 387},
        {"segment": "Fisheries & Aquaculture", "value_billion": 310},
        {"segment": "Shipbuilding & Marine Equipment", "value_billion": 240},
        {"segment": "Port Infrastructure & Services", "value_billion": 180},
        {"segment": "Offshore Oil & Gas", "value_billion": 155},
        {"segment": "Naval Defense & Maritime Security", "value_billion": 98},
        {"segment": "Offshore Wind Energy", "value_billion": 49},
        {"segment": "Desalination & Water", "value_billion": 42},
        {"segment": "Submarine Cables & Telecom", "value_billion": 32},
        {"segment": "Marine Biotechnology", "value_billion": 7.9},
        {"segment": "Deep-Sea Mining", "value_billion": 3.9},
    ]

    pie_labels = [d["segment"] for d in segment_data]
    pie_values = [d["value_billion"] for d in segment_data]

    pie_fig = go.Figure(
        data=[
            go.Pie(
                labels=pie_labels,
                values=pie_values,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.1f}B<br><extra></extra>",
            )
        ]
    )

    pie_fig.update_layout(
        title="Blue economy segments (2024, USD billions)",
        annotations=[
            dict(text="~$2.2T", x=0.5, y=0.5, font_size=16, showarrow=False)
        ],
        showlegend=True,
        height=600,
    )

    pie_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Segmentation notes:
    - Marine tourism dominates at 33% of the ocean economy -- coastal and beach tourism alone is \$591B, dwarfing the cruise industry (\$60B) despite cruise lines' outsized media presence.
    - Maritime shipping (\$387B) moves 12.7 billion tons of cargo annually, but the port infrastructure that handles it (\$180B) is a separate and substantial segment.
    - Fisheries and aquaculture (\$310B) crossed a milestone in 2022: farmed fish production surpassed wild capture for the first time (FAO).
    - Among the smaller, high-growth segments -- offshore wind (\$49B), marine biotech (\$7.9B), and deep-sea mining (\$3.9B) -- are the fastest-growing, with CAGRs of ~16%, 10.4%, and 14.5% respectively.
    - Segment sizes are revenue/market size estimates, not GVA. Some double-counting exists (e.g., shipbuilding revenue overlaps with naval defense procurement).
    - Sources: UNCTAD Global Trade Update (June 2025), OECD Ocean Economy to 2050 (March 2025), Polaris Market Research, Precedence Research, Cognitive Market Research.
    """
    )
    return


@app.cell
def _(go):
    import json
    import pathlib

    _base_dir = (
        pathlib.Path(__file__).parent
        if "__file__" in globals()
        else (
            pathlib.Path.cwd() / "notebooks"
            if (pathlib.Path.cwd() / "notebooks").exists()
            else pathlib.Path.cwd()
        )
    )
    _nodes_path = _base_dir / "data" / "ocean_nodes.json"

    if not _nodes_path.exists():
        raise FileNotFoundError(f"Ocean nodes file not found at {_nodes_path}")

    with _nodes_path.open("r", encoding="utf-8") as _f:
        _nodes = json.load(_f)

    _icicle_labels = [node["label"] for node in _nodes]
    _icicle_parents = [node["parent"] for node in _nodes]
    _icicle_values = [node["value"] for node in _nodes]
    _icicle_hover = [node["hover"] for node in _nodes]

    icicle_fig = go.Figure(
        go.Icicle(
            labels=_icicle_labels,
            parents=_icicle_parents,
            values=_icicle_values,
            branchvalues="total",
            customdata=_icicle_hover,
            hovertemplate="<b>%{label}</b><br>%{customdata}<extra></extra>",
            textinfo="label+value+percent parent",
            tiling={"orientation": "v"},
        )
    )

    icicle_fig.update_layout(
        title="Blue economy icicle map -- 2024 market size (USD billions)",
        margin=dict(t=90, l=30, r=30, b=30),
        uniformtext=dict(minsize=10, mode="hide"),
        height=800,
    )

    icicle_fig.update_traces(
        root_color="lightgrey",
        tiling=dict(orientation="v"),
        maxdepth=4,
    )

    icicle_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the icicle:
    - Root anchors to ~\$2.2T global blue economy, split into eight branches: Tourism, Transport, Food, Shipbuilding, Energy, Defense, Infrastructure, and Deep-Sea Mining.
    - Company nodes are illustrative, using reported segment revenues. They do not sum cleanly to parents -- the unnamed space represents remaining market participants.
    - Marine Tourism (\$725B) is the largest branch, but most of the value is in diffuse coastal tourism (\$591B) rather than the concentrated cruise industry (\$60B).
    - Container shipping is \$175B, but the four named carriers (Maersk, CMA CGM, COSCO, Hapag-Lloyd) represent \$106B -- the unnamed portion includes MSC (#1 by fleet size, private), Evergreen, ONE, and others.
    - Offshore Energy shows the energy transition in miniature: oil and gas (\$155B) still 3x larger than wind (\$49B), but wind is growing at ~16% CAGR vs flat/declining O&G services.
    - Submarine cables is a remarkable oligopoly: three companies (SubCom, ASN, NEC) control >60% of wet-plant manufacturing for cables carrying 99% of intercontinental internet data.
    - Sources: Company annual reports (2024), UNCTAD, OECD, Precedence Research, MarketsandMarkets, Grand View Research.
    """
    )
    return


@app.cell
def _(go):
    strategy_companies = [
        {"company": "Maersk", "country": "DK", "strategy": "Ocean logistics integrators", "revenue_b": 55.5,
         "hover": "Total group $55.5B. Ocean $35.2B + Logistics $12.8B + Terminals $5.5B. Integrating end-to-end."},
        {"company": "CMA CGM", "country": "FR", "strategy": "Ocean logistics integrators", "revenue_b": 55.5,
         "hover": "Total group $55.5B. Private (Saade family). Acquired CEVA Logistics. Air cargo via CMA CGM Air Cargo."},
        {"company": "COSCO Shipping", "country": "CN", "strategy": "Ocean logistics integrators", "revenue_b": 32.3,
         "hover": "$32.3B. State-owned. #4 by container fleet. Ports + shipping + logistics integration."},
        {"company": "DP World", "country": "AE", "strategy": "Ocean logistics integrators", "revenue_b": 20.0,
         "hover": "Revenue $20.0B (2024 record). 90+ terminals. Acquiring logistics companies to become end-to-end."},

        {"company": "Equinor", "country": "NO", "strategy": "Energy transition players", "revenue_b": 104.0,
         "hover": "$104B total. 67% offshore O&G, growing offshore wind (Dogger Bank, Empire Wind). Targeting 10-12 GW renewables by 2030 (cut from 12-16 GW in Feb 2025)."},
        {"company": "Ørsted", "country": "DK", "strategy": "Energy transition players", "revenue_b": 10.3,
         "hover": "$10.3B (DKK 71.0B, 2024). Former DONG Energy (Danish Oil & Natural Gas). Fully pivoted to offshore wind. 15.5 GW portfolio."},
        {"company": "Shell (offshore)", "country": "NL", "strategy": "Energy transition players", "revenue_b": 45.0,
         "hover": "Offshore-attributable ~$45B (of $284B total). Deep water Gulf of Mexico, North Sea. Sold onshore wind assets to focus offshore."},
        {"company": "Petrobras", "country": "BR", "strategy": "Energy transition players", "revenue_b": 82.0,
         "hover": "$82B. ~95% offshore production. Pre-salt deep water is core. World's leading FPSO operator."},

        {"company": "CSSC", "country": "CN", "strategy": "Shipyard conglomerates", "revenue_b": 10.0,
         "hover": "~$10B. China State Shipbuilding Corp. World's #1 by tonnage. State-owned mega-conglomerate."},
        {"company": "HD Hyundai Heavy", "country": "KR", "strategy": "Shipyard conglomerates", "revenue_b": 10.5,
         "hover": "$10.5B. World's #2. Ulsan = world's largest single shipyard. LNG carrier orderbook dominance."},
        {"company": "Samsung Heavy", "country": "KR", "strategy": "Shipyard conglomerates", "revenue_b": 7.4,
         "hover": "~$7.4B. LNG carrier and drillship specialist. Record orderbook in 2024."},
        {"company": "Fincantieri", "country": "IT", "strategy": "Shipyard conglomerates", "revenue_b": 8.8,
         "hover": "~$8.8B. World leader in cruise ship construction. Also naval vessels (Italian/US Navy). Acquired Wartsila Voyage."},

        {"company": "Carnival Corp", "country": "US", "strategy": "Cruise & marine tourism", "revenue_b": 25.0,
         "hover": "$25.0B (2024 record). 9 brands, 95 ships. World's largest cruise operator."},
        {"company": "Royal Caribbean", "country": "US", "strategy": "Cruise & marine tourism", "revenue_b": 16.5,
         "hover": "$16.5B. Icon of the Seas = world's largest cruise ship (2024). Celebrity, Silversea brands."},
        {"company": "Norwegian Cruise Line", "country": "US", "strategy": "Cruise & marine tourism", "revenue_b": 9.5,
         "hover": "$9.5B (2024 record). Premium/luxury positioning via Oceania and Regent Seven Seas brands."},

        {"company": "Mowi", "country": "NO", "strategy": "Seafood & aquaculture", "revenue_b": 5.5,
         "hover": "$5.5B. World's largest Atlantic salmon farmer. Norway, Scotland, Chile, Canada operations."},
        {"company": "Maruha Nichiro", "country": "JP", "strategy": "Seafood & aquaculture", "revenue_b": 7.5,
         "hover": "~$7.5B. Japan's #1 seafood company. Wild capture + aquaculture + processed foods."},
        {"company": "Thai Union", "country": "TH", "strategy": "Seafood & aquaculture", "revenue_b": 4.3,
         "hover": "~$4.3B. World's largest canned tuna producer. Chicken of the Sea, John West brands."},
        {"company": "Nippon Suisan", "country": "JP", "strategy": "Seafood & aquaculture", "revenue_b": 6.5,
         "hover": "~$6.5B. Japan's #2 seafood company. Aquaculture, wild capture, marine ingredients."},

        {"company": "HII", "country": "US", "strategy": "Naval & defense", "revenue_b": 11.5,
         "hover": "$11.5B. US Navy's sole carrier builder, primary submarine builder. Newport News + Ingalls yards."},
        {"company": "Naval Group", "country": "FR", "strategy": "Naval & defense", "revenue_b": 4.7,
         "hover": "~$4.7B. Nuclear subs (Barracuda-class), frigates. French state-owned. Export programs globally."},
        {"company": "BAE Systems (maritime)", "country": "UK", "strategy": "Naval & defense", "revenue_b": 8.0,
         "hover": "Maritime segment ~$8B (of $35.7B total). Type 26 frigates, Astute-class subs, Dreadnought program."},
        {"company": "Hanwha Ocean", "country": "KR", "strategy": "Naval & defense", "revenue_b": 7.9,
         "hover": "~$7.9B (KRW 10.78T, 2024). Ex-DSME. South Korean submarines and naval vessels + commercial shipbuilding dual-use."},

        {"company": "Prysmian", "country": "IT", "strategy": "Subsea specialists", "revenue_b": 18.5,
         "hover": "EUR 17B+ total ($18.5B). Subsea cables ~$5B. World leader in submarine power and telecom cables."},
        {"company": "SLB", "country": "US", "strategy": "Subsea specialists", "revenue_b": 36.0,
         "hover": "$36B total. Offshore/subsea ~$9B. World's largest oilfield services company. Subsea trees, drilling."},
        {"company": "SubCom", "country": "US", "strategy": "Subsea specialists", "revenue_b": 2.0,
         "hover": "~$2B. $4.7B backlog. One of only 3 global wet-plant submarine cable manufacturers."},
    ]

    _flag = {
        "US": "\U0001f1fa\U0001f1f8",
        "UK": "\U0001f1ec\U0001f1e7",
        "DK": "\U0001f1e9\U0001f1f0",
        "FR": "\U0001f1eb\U0001f1f7",
        "CN": "\U0001f1e8\U0001f1f3",
        "NL": "\U0001f1f3\U0001f1f1",
        "NO": "\U0001f1f3\U0001f1f4",
        "KR": "\U0001f1f0\U0001f1f7",
        "IT": "\U0001f1ee\U0001f1f9",
        "AE": "\U0001f1e6\U0001f1ea",
        "BR": "\U0001f1e7\U0001f1f7",
        "JP": "\U0001f1ef\U0001f1f5",
        "TH": "\U0001f1f9\U0001f1ed",
        "CH": "\U0001f1e8\U0001f1ed",
    }

    _root = "Blue Economy Players"
    _tm_labels = [_root]
    _tm_parents = [""]
    _tm_values = [0.0]
    _tm_customdata = [""]

    _strategies = sorted({c["strategy"] for c in strategy_companies})
    _strat_idx: dict[str, int] = {}
    for _s in _strategies:
        _strat_idx[_s] = len(_tm_labels)
        _tm_labels.append(_s)
        _tm_parents.append(_root)
        _tm_values.append(0.0)
        _tm_customdata.append(f"<b>{_s}</b>")

    _total = 0.0
    for _c in strategy_companies:
        _r = float(_c["revenue_b"])
        _total += _r
        _f = _flag.get(_c["country"], "")
        _lbl = f"{_c['company']} {_f}".strip()

        _tm_labels.append(_lbl)
        _tm_parents.append(_c["strategy"])
        _tm_values.append(_r)
        _tm_customdata.append(
            "<b>{lbl}</b>"
            "<br>Strategy: {strat}"
            "<br>Revenue: ${r:.1f}B"
            "<br>{hover}"
            "<extra></extra>".format(
                lbl=_lbl,
                strat=_c["strategy"],
                r=_r,
                hover=_c["hover"],
            )
        )
        _tm_values[_strat_idx[_c["strategy"]]] += _r

    _tm_values[0] = _total

    treemap_fig = go.Figure(
        go.Treemap(
            labels=_tm_labels,
            parents=_tm_parents,
            values=_tm_values,
            branchvalues="total",
            customdata=_tm_customdata,
            hovertemplate="%{customdata}",
            texttemplate="<b>%{label}</b><br>$%{value:.1f}B",
        )
    )

    treemap_fig.update_layout(
        title="Blue economy competitive landscape by strategic archetype (2024, total company revenue)",
        margin=dict(t=90, l=10, r=10, b=10),
    )

    treemap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Strategy archetype notes:

    Companies grouped by HOW they compete in the ocean economy, not by traditional industry verticals:

    1. Ocean logistics integrators (Maersk, CMA CGM, COSCO, DP World): These companies are converging from different starting points -- shipping lines acquiring logistics, port operators expanding inland -- all racing to become end-to-end supply chain platforms. Maersk and CMA CGM both hit \$55.5B in 2024, but with opposite strategies: Maersk divested Svitzer (towage) to double down on integrated logistics, while CMA CGM expanded into air cargo and media.
    2. Energy transition players (Equinor, Orsted, Shell, Petrobras): Companies bridging offshore oil and gas to offshore wind. Orsted is the extreme case -- formerly Danish Oil & Natural Gas, now 100% renewables. Equinor targets 10-12 GW of renewables by 2030 (cut from 12-16 GW in Feb 2025) while still producing 2M+ barrels/day offshore.
    3. Shipyard conglomerates (CSSC, HD Hyundai Heavy, Samsung Heavy, Fincantieri): China (~53%) and South Korea (~28%) together build ~81% of global shipbuilding by tonnage (~93% including Japan). Record orderbooks in 2024 driven by LNG carrier demand and container ship fleet renewal. Fincantieri is the European outlier -- dominant in cruise ship construction.
    4. Cruise and marine tourism (Carnival, Royal Caribbean, Norwegian): All three posted record revenues in 2024, fully recovered from COVID. Combined fleet of ~200+ ships. Capital-intensive: a single large cruise ship costs \$1-1.5B to build.
    5. Seafood and aquaculture (Mowi, Maruha Nichiro, Thai Union, Nippon Suisan): Japanese companies dominate by revenue but Norwegian companies lead in high-value Atlantic salmon. The industry is consolidating -- top 10 companies control ~15% of global seafood trade.
    6. Naval and defense (HII, Naval Group, BAE Maritime, Hanwha Ocean): Driven by geopolitical competition. HII has irreplaceable monopoly position as US Navy's only aircraft carrier builder. AUKUS submarine deal (Australia-UK-US) is reshaping global naval supply chains.
    7. Subsea specialists (Prysmian, SLB, SubCom): Companies operating on the ocean floor -- cables, subsea oil and gas infrastructure, and deepwater engineering. The submarine cable triopoly (SubCom, ASN, NEC) is a hidden chokepoint for global internet infrastructure.

    Revenue shown is total company revenue, not ocean-specific. For diversified companies (Shell, SLB, Prysmian), the ocean-attributable portion is noted in hover text.
    """
    )
    return


@app.cell
def _(go):
    sankey_labels = [
        "Crude Oil & Products", "Dry Bulk (ore, coal, grain)", "Containerized Goods",
        "LNG / LPG", "Vehicles & Machinery", "Other Cargo",
        "Intra-Asia", "Middle East → Asia", "Trans-Pacific",
        "Asia → Europe", "Atlantic", "Other Routes",
        "Asia-Pacific", "Europe", "Americas",
    ]

    sankey_links = {
        "source": [
            0, 0, 0, 0,
            1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3,
            4, 4, 4,
            5, 5, 5, 5,
            6, 6,
            7,
            8, 8,
            9,
            10, 10, 10,
            11, 11, 11,
        ],
        "target": [
            7, 6, 10, 11,
            6, 8, 10, 11,
            6, 8, 9, 10,
            7, 6, 11,
            8, 9, 10,
            6, 10, 11, 8,
            12, 13,
            12,
            14, 12,
            13,
            13, 14, 12,
            12, 14, 13,
        ],
        "value": [
            15, 5, 4, 3,
            18, 4, 5, 3,
            9, 6, 5, 2,
            6, 3, 1,
            3, 2, 2,
            8, 5, 4, 3,
            38, 5,
            21,
            9, 7,
            7,
            8, 7, 3,
            5, 3, 3,
        ],
    }

    _node_colors = (
        ["#4e79a7"] * 6
        + ["#f28e2b"] * 6
        + ["#59a14f"] * 3
    )

    sankey_fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                pad=20,
                thickness=25,
                line=dict(color="black", width=0.5),
                label=sankey_labels,
                color=_node_colors,
                hovertemplate="<b>%{label}</b><br>Total flow: %{value}<extra></extra>",
            ),
            link=dict(
                source=sankey_links["source"],
                target=sankey_links["target"],
                value=sankey_links["value"],
                hovertemplate="<b>%{source.label}</b> → <b>%{target.label}</b><br>Weight: %{value}<extra></extra>",
            ),
        )
    )

    sankey_fig.update_layout(
        title="Seaborne trade flows: cargo type → major route → importing region (directional, 2024)",
        margin=dict(t=70, l=30, r=30, b=30),
        height=600,
    )

    sankey_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Seaborne trade flow notes:
    - Left column (blue): Cargo categories. Dry bulk is the largest by tonnage at >5.6B tons (~44% of the 12.7B total); the narrower "main bulks" (iron ore, coal, grain) are ~3.5B tons. Containerized goods are ~17% by tonnage but carry the highest value per ton.
    - Middle column (orange): Major sea routes. Intra-Asia dominates -- 63% of global container port calls are in Asia. The Middle East to Asia corridor is the primary energy artery (crude oil + LNG to China, India, Japan, South Korea).
    - Right column (green): Importing regions. Asia-Pacific is the dominant destination, reflecting China's role as both the world's largest importer of raw materials and a major consumer market.
    - Flows are directional weights illustrating relative volume, not exact tonnage. The intent is to show the structural pattern: raw materials flow east, manufactured goods flow west, and intra-Asian trade is the largest single flow.
    - Key chokepoints not shown: Strait of Malacca (~25% of global trade), Suez Canal (~12%), Panama Canal (~5%), Strait of Hormuz (~20% of global oil).
    - Sources: UNCTAD Review of Maritime Transport 2024, Clarksons Research, Drewry Shipping Consultants.
    """
    )
    return


@app.cell
def _(go):
    from plotly.subplots import make_subplots

    wind_years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
    cumulative_gw = [23, 29, 35, 57, 64, 75, 83]
    annual_invest_b = [26, 31, 50, 43, 31, 77, 31]

    dual_fig = make_subplots(specs=[[{"secondary_y": True}]])

    dual_fig.add_trace(
        go.Bar(
            x=wind_years,
            y=annual_invest_b,
            name="Annual investment ($B)",
            marker_color="steelblue",
            hovertemplate="<b>Offshore Wind Investment</b><br>Year: %{x}<br>$%{y}B<extra></extra>",
        ),
        secondary_y=False,
    )

    dual_fig.add_trace(
        go.Scatter(
            x=wind_years,
            y=cumulative_gw,
            name="Cumulative installed (GW)",
            mode="lines+markers",
            line=dict(color="#59a14f", width=3),
            marker=dict(size=8),
            hovertemplate="<b>Installed Capacity</b><br>Year: %{x}<br>%{y} GW<extra></extra>",
        ),
        secondary_y=True,
    )

    dual_fig.update_layout(
        title="Offshore wind: annual investment vs. cumulative installed capacity (2018-2024)",
        xaxis=dict(title="Year", type="category"),
        hovermode="x unified",
        margin=dict(t=70, l=50, r=50, b=40),
        legend=dict(x=0.01, y=0.99),
    )
    dual_fig.update_yaxes(title_text="Annual investment (USD billions)", secondary_y=False)
    dual_fig.update_yaxes(title_text="Cumulative installed capacity (GW)", secondary_y=True)

    dual_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Offshore wind investment notes:
    - Cumulative installed offshore wind capacity reached ~83 GW by end of 2024 (GWEC), up from ~23 GW in 2018 -- a 3.6x increase in six years.
    - Annual investment fell to ~\$31B in 2024 after a record ~\$77B in 2023 (BloombergNEF); offshore-wind investment is lumpy, driven by large project-financing cycles in China (leading by installed capacity), the UK (Dogger Bank), and the US (Vineyard Wind, Empire Wind).
    - The 2022 dip reflects supply chain disruption and Siemens Gamesa turbine quality issues that delayed several European projects.
    - Floating offshore wind is <1% of installed capacity today but unlocks 80%+ of the global ocean wind resource (areas with water depth >60m). Hywind Tampen (Norway) and WindFloat Atlantic (Portugal) are early commercial demonstrators.
    - By 2034, the offshore wind market is projected to reach \$215B at ~16% CAGR (Precedence Research), making it the fastest value-growth segment in the blue economy.
    - Sources: GWEC Global Offshore Wind Report 2025, BloombergNEF, IRENA, Precedence Research.
    """
    )
    return


@app.cell
def _(go):
    growth_data = [
        {"period": "2024 (actual)", "value_t": 2.2, "color": "#4e79a7", "source": "UNCTAD"},
        {"period": "2030 (projected)", "value_t": 3.2, "color": "#f28e2b", "source": "OECD"},
        {"period": "2034 (projected)", "value_t": 5.0, "color": "#f28e2b", "source": "Polaris (~8.6% CAGR)"},
        {"period": "2050 (projected)", "value_t": 5.2, "color": "#e15759", "source": "OECD (~4x 1995)"},
    ]

    growth_fig = go.Figure(
        go.Bar(
            x=[d["period"] for d in growth_data],
            y=[d["value_t"] for d in growth_data],
            marker_color=[d["color"] for d in growth_data],
            text=[f"${d['value_t']:.1f}T" for d in growth_data],
            textposition="outside",
            customdata=[d["source"] for d in growth_data],
            hovertemplate="<b>%{x}</b><br>$%{y:.1f}T<br>Source: %{customdata}<extra></extra>",
        )
    )

    growth_fig.update_layout(
        title="Blue economy growth trajectory: 2024 to 2050 (USD trillions)",
        xaxis=dict(title="", type="category"),
        yaxis=dict(title="USD trillions", range=[0, 10.5]),
        margin=dict(t=70, l=60, r=40, b=40),
        height=400,
    )

    growth_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Growth projection notes:
    - The blue economy has grown 2.5x since 1995, outpacing the 1.9x growth of the world economy (UNCTAD 2025). It is projected to at least double again by 2050.
    - OECD projects the ocean economy will exceed \$3T GVA by 2030 and nearly 4x its 1995 level by 2050. Cumulative capex of ~\$20T is implied. (The trajectory bars blend different measures — UNCTAD ocean-trade value, a Polaris market-size estimate, and OECD GVA — so read them as directional scale, not a single consistent metric; the 2034→2050 step looks flat only because those two bars use different definitions.)
    - The structural drivers: offshore wind (~16% CAGR), aquaculture (6-8% CAGR replacing stagnant wild capture), submarine cables (surging from AI data center demand), and desalination (water scarcity in MENA, India, Australia).
    - The structural headwind: offshore oil and gas -- currently \$155B -- is projected to shrink from dominant to 25% of ocean economy capex by 2050 as the energy transition progresses (OECD). Offshore wind is projected to capture 50% of capex.
    - Deep-sea mining is the wild card: if ISA grants commercial licenses (expected 2025-2027), the segment could grow from \$3.9B to \$10-41B by 2033, but environmental opposition is fierce (30+ countries support a moratorium).
    - Sources: OECD "The Ocean Economy to 2050" (March 2025), Polaris Market Research, UNCTAD Global Trade Update (June 2025), Precedence Research.
    """
    )
    return


@app.cell
def _(go):
    chokepoint_data = [
        {"chokepoint": "Strait of Malacca", "pct_trade": 25, "daily_barrels_m": 23.7,
         "risk": "Piracy, congestion. 94,000+ vessels/yr. Narrowest point: 2.8 km."},
        {"chokepoint": "Strait of Hormuz", "pct_trade": 8, "daily_barrels_m": 21.0,
         "risk": "Geopolitical (Iran). 20-25% of global oil. ~20% of seaborne LNG."},
        {"chokepoint": "Suez Canal", "pct_trade": 12, "daily_barrels_m": 5.5,
         "risk": "Single point of failure. Ever Given 2021. Houthi attacks 2024 rerouted most container traffic (container tonnage -75-82%; overall Suez tonnage -51-64%)."},
        {"chokepoint": "Panama Canal", "pct_trade": 5, "daily_barrels_m": 0.9,
         "risk": "Drought (2023-24 reduced transits 36%). Water-dependent locks. US-China trade route."},
        {"chokepoint": "Danish Straits", "pct_trade": 3, "daily_barrels_m": 3.2,
         "risk": "Baltic Sea access. Russian energy exports. Shallow draft limits."},
        {"chokepoint": "Bab el-Mandeb", "pct_trade": 7, "daily_barrels_m": 6.2,
         "risk": "Yemen/Houthi attacks. Gateway to Suez. ~6.2M barrels/day oil + 8% of LNG."},
        {"chokepoint": "Cape of Good Hope", "pct_trade": 5, "daily_barrels_m": 2.0,
         "risk": "Suez alternative. +10-14 days transit. Surged in 2024 due to Red Sea diversions."},
    ]

    _labels = [d["chokepoint"] for d in chokepoint_data]
    _pct = [d["pct_trade"] for d in chokepoint_data]
    _barrels = [d["daily_barrels_m"] for d in chokepoint_data]
    _risk = [d["risk"] for d in chokepoint_data]

    choke_fig = go.Figure()

    choke_fig.add_trace(
        go.Bar(
            y=_labels,
            x=_pct,
            orientation="h",
            name="% of global seaborne trade",
            marker_color="#4e79a7",
            text=[f"{v}%" for v in _pct],
            textposition="outside",
            customdata=list(zip(_risk, _barrels)),
            hovertemplate="<b>%{y}</b><br>%{x}% of global trade · ~%{customdata[1]}M b/d oil<br>%{customdata[0]}<extra></extra>",
        )
    )

    choke_fig.update_layout(
        title="Maritime chokepoints: share of global seaborne trade (%)",
        xaxis=dict(title="% of global seaborne trade", range=[0, 32]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=160, r=80, b=40),
        height=400,
    )

    choke_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Maritime chokepoint notes:
    - These seven passages collectively handle ~65% of global seaborne trade. Disruption at any one reshapes global logistics costs.
    - The Houthi attacks on Red Sea shipping (2024-2025) demonstrated real-world impact: most container traffic rerouted via Cape of Good Hope (container tonnage down ~75-82%; overall Suez tonnage down ~51-64%), adding 10-14 days and ~\$1M per voyage in fuel costs. Container shipping rates spiked 3-4x on Asia-Europe lanes.
    - The Strait of Hormuz is the most consequential for energy: 20-25% of global oil and ~20% of seaborne LNG passes through. Iran's proximity makes it a permanent geopolitical flashpoint.
    - Panama Canal drought (2023-24) reduced daily transits from ~38 to ~24, creating months-long queues. Auction slots sold for \$4M+. Climate change makes this a recurring risk.
    - The Strait of Malacca (25% of global trade, 94,000+ vessels/year) is the world's busiest -- a single accident or blockage would dwarf the Ever Given disruption.
    - Insurance implications: war risk premiums for Red Sea transit surged from 0.07% to 1.0%+ of hull value in 2024. The maritime insurance market (hull, cargo, P&I) is ~\$35B globally.
    - Sources: US EIA, UNCTAD Review of Maritime Transport 2024, Lloyd's List, Clarksons Research.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    ## Blue Economy Market Gaps and Whitespace

    The ocean economy is large but riddled with structural gaps -- underinsured assets, missing infrastructure, regulatory vacuums, and technology that hasn't kept pace with ambition. The chart below quantifies the largest gaps by dollar value.
    """
    )
    return


@app.cell
def _(go):
    gap_data = [
        {"gap": "Shipping decarbonization investment needed", "value_b": 1000, "category": "Technology",
         "detail": "IMO 2050 net-zero requires $1T. Green fuels are <1% of energy mix today."},
        {"gap": "Climate adaptation finance gap (all sectors)", "value_b": 284, "category": "Finance",
         "detail": "Developing nations need $310-365B/yr by 2035 for all adaptation; only ~$26B/yr flows today (~12x gap; UNEP)."},
        {"gap": "Offshore wind supply chain (cables + vessels)", "value_b": 120, "category": "Infrastructure",
         "detail": "117,640 km of subsea cable needed by 2040. Only 3 HVDC cable makers. Vessels ~$400M each."},
        {"gap": "IUU fishing economic losses", "value_b": 50, "category": "Sustainability",
         "detail": "1 in 5 fish caught illegally. $26-50B/yr total impact. AI monitoring at $1.4B by 2029."},
        {"gap": "Ocean plastic damage vs cleanup spending", "value_b": 19, "category": "Sustainability",
         "detail": "11-12.7M tonnes enter ocean/yr. $19B/yr damage; only $1.9B/yr spent on cleanup (10x gap)."},
        {"gap": "Smart port digitization gap", "value_b": 5.7, "category": "Infrastructure",
         "detail": "Top ports are smart; ~4,600 ports globally are not. $1.6B to $7.3B market by 2032."},
        {"gap": "Blue carbon credit market potential", "value_b": 14.8, "category": "Sustainability",
         "detail": "Only 81 projects globally, 10 issuing credits. Potential $8.7-14.8B by 2033 at 22-25% CAGR."},
        {"gap": "Ocean-based CDR market potential", "value_b": 3.2, "category": "Technology",
         "detail": "$0.85B today. $209M invested across 56 developers. Ocean absorbs 30% of CO2 but CDR is immature."},
        {"gap": "Marine insurance coverage gaps", "value_b": 37, "category": "Finance",
         "detail": "$34-37B market but climate claims +37%, cyber risks +42%. Parametric uptake minimal."},
        {"gap": "Aquaculture insurance gap (developing world)", "value_b": 7.1, "category": "Finance",
         "detail": "Norway/Japan near-universal coverage; Asia-Pacific, Africa minimal. $7.1B market by 2032."},
        {"gap": "Seafarer officer shortage", "value_b": 4.5, "category": "Workforce",
         "detail": "89,510 officers needed by 2026. 800,000 need alt-fuel training by mid-2030s."},
        {"gap": "Offshore wind workforce gap", "value_b": 3.8, "category": "Workforce",
         "detail": "628,000 technicians needed by 2030. 38,000 unfilled in US alone."},
    ]

    _sorted = sorted(gap_data, key=lambda d: d["value_b"], reverse=True)

    _cat_colors = {
        "Technology": "#e15759",
        "Finance": "#f28e2b",
        "Infrastructure": "#4e79a7",
        "Sustainability": "#59a14f",
        "Workforce": "#b07aa1",
    }

    gap_fig = go.Figure()

    gap_fig.add_trace(
        go.Bar(
            y=[d["gap"] for d in _sorted],
            x=[d["value_b"] for d in _sorted],
            orientation="h",
            marker_color=[_cat_colors[d["category"]] for d in _sorted],
            text=[
                f"${d['value_b']:,.0f}B" if d["value_b"] >= 10
                else f"${d['value_b']:.1f}B"
                for d in _sorted
            ],
            textposition="outside",
            customdata=[f"{d['category']}: {d['detail']}" for d in _sorted],
            hovertemplate="<b>%{y}</b><br>$%{x:,.1f}B<br>%{customdata}<extra></extra>",
        )
    )

    gap_fig.update_layout(
        title="Blue economy market gaps by estimated scale (USD billions, log scale)",
        xaxis=dict(
            title="USD billions (log scale)",
            type="log",
            range=[0.3, 3.3],
        ),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=340, r=80, b=50),
        height=550,
        annotations=[
            dict(
                text="<b>Legend:</b>  "
                     "<span style='color:#e15759'>● Technology</span>  "
                     "<span style='color:#f28e2b'>● Finance</span>  "
                     "<span style='color:#4e79a7'>● Infrastructure</span>  "
                     "<span style='color:#59a14f'>● Sustainability</span>  "
                     "<span style='color:#b07aa1'>● Workforce</span>",
                xref="paper", yref="paper",
                x=0.5, y=1.08,
                showarrow=False,
                font=dict(size=11),
            )
        ],
    )

    gap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Market gap analysis -- key findings:

    The five categories of gaps cluster into two tiers by scale:

    Tier 1 -- systemic, trillion-dollar gaps:
    - Shipping decarbonization (\$1T): The IMO's Net-Zero Framework was approved in April 2025 but adoption was delayed until October 2026. Green methanol and ammonia are not cost-competitive. Zero/near-zero fuels must be 5-10% of shipping's energy mix by 2030 -- currently a rounding error. Up to 800,000 seafarers will need alternative fuel training.
    - Climate adaptation finance gap (\$284B/yr, all sectors): Developing countries need \$310-365B/year by 2035 for adaptation across all sectors; only ~\$26B/year flows today -- a ~12x gap (UNEP Adaptation Gap 2025). Coastal flood protection is among the highest adaptation costs but offers minimal financial returns, leaving public finance as the main path.

    Tier 2 -- addressable, billion-dollar opportunities:
    - Offshore wind supply chain: 117,640 km of submarine cable needed by 2040 (vs. 55,500 km installed today). Only 3 companies make HVDC cable. Installation vessels cost ~\$400M each and take 3-4 years to build. This is a capital-intensive bottleneck with a decade-long runway.
    - IUU fishing (\$26-50B/yr): 1 in 5 fish caught globally is illegal. AI-based vessel monitoring works but is inconsistently deployed, particularly in developing-nation EEZs where the problem is worst. Global Fishing Watch and OceanMind are leading.
    - Marine insurance gaps: Climate-linked claims rose 37%, cyber risks up 42%, yet parametric insurance uptake remains minimal. Aquaculture insurance barely exists outside Norway and Japan despite aquaculture being the fastest-growing food sector.
    - Blue carbon credits: Only 81 projects globally, 10 actively issuing credits. Mangroves dominate (72 of 81 projects). Seagrass is growing at 30.9% CAGR but has only 4 projects. Kelp is not yet creditable.

    Emerging whitespace:
    - Ocean-based CDR: \$0.85B today, but corporate offtake agreements (Microsoft, Frontier) signal \$50-250B total CDR market by 2030-2035. Captura (direct ocean capture) and Planetary Technologies (ocean alkalinity enhancement, \$31.3M offtake for 115K tCO2) are furthest along.
    - Seawater mineral extraction: 230 billion tons of lithium dissolved in seawater. Saudi Arabia has 2 industrial-scale brine extraction plants under construction (\$65M). Desalination co-processing is the near-term on-ramp.
    - Deep-sea mining: Clarion-Clipperton Zone holds more cobalt, nickel, and manganese than all known land deposits combined. But ISA regulatory paralysis, environmental opposition, and The Metals Company's \$320M net loss (2025) suggest this remains pre-commercial for years.

    Sources: UNCTAD, OECD, IMO MEPC 83, UNEP Adaptation Gap Report 2025, GWEC, BIMCO/ICS Seafarer Workforce Report, CDR.fyi, Nature npj Ocean Sustainability, TGS/4C Offshore Wind Analysis.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    # Appendix: Shipping Decarbonization Deep Dive

    Shipping burns 242 million tonnes of fuel per year. Only 0.7% of it is decarbonized.

    International shipping emits ~700-900 Mt CO2 annually (all shipping ~1,000 Mt, ~3% of global emissions) -- roughly comparable to the aviation industry. In 2024, container shipping alone hit a record 240.6 Mt CO2. The IMO approved a landmark Net-Zero Framework in April 2025 with carbon pricing at \$100-\$380/tCO2, but actual decarbonization in 2025 amounts to approximately 0.7% of bunker sales. Green methanol and ammonia remain 2-4x more expensive than fossil fuels, and the 1,942-ship alternative fuel orderbook is mostly LNG -- a fuel whose climate credentials are contested due to methane slip.

    Key figures:
    - Global shipping fuel consumption: ~242.4 Mt (2024), up 4.0% YoY due to Red Sea rerouting.
    - CO2 emissions: ~1,000 Mt/yr (3% of global). Container shipping alone: 240.6 Mt (record, +14% YoY).
    - Alternative fuel share of bunker sales: VLSFO 52%, HSFO 32%, MGO 13.3%, biofuels 1%, LNG 1.7%, methanol 0.02%.
    - Alternative fuel orderbook: 1,942 ships total -- LNG 1,259 (65%), methanol 385 (20%), LPG 139 (7%), ammonia 45 (2%).
    - IMO Net-Zero Framework: GHG fuel intensity standard + carbon pricing (\$100/\$380 per tCO2), entry into force 2027-2028.
    - EU ETS for shipping: phase-in 40% (2024) -> 70% (2025) -> 100% (2026). Estimated cost: USD 7.5B/yr at full scope.
    - The liner industry has already invested USD 150B in decarbonization. An additional \$1T+ is needed by 2050.
    """
    )
    return


@app.cell
def _(go):
    reg_milestones = [
        {"milestone": "IMO 2023 GHG Strategy adopted (MEPC 80)", "year": 2023, "category": "IMO"},
        {"milestone": "EU ETS for shipping begins (40% phase-in)", "year": 2024, "category": "EU"},
        {"milestone": "CII tightening: 9% below 2019 baseline", "year": 2025, "category": "IMO"},
        {"milestone": "FuelEU Maritime enters force", "year": 2025, "category": "EU"},
        {"milestone": "EU ETS 70% phase-in", "year": 2025, "category": "EU"},
        {"milestone": "EU ETS 100% + CH4/N2O in scope", "year": 2026, "category": "EU"},
        {"milestone": "IMO Net-Zero Framework enters force", "year": 2027, "category": "IMO"},
        {"milestone": "IMO GFI standard + carbon pricing enforcement", "year": 2028, "category": "IMO"},
        {"milestone": "IMO target: 20% GHG reduction (vs 2008)", "year": 2030, "category": "IMO"},
        {"milestone": "FuelEU: -14.5% GHG intensity vs baseline", "year": 2035, "category": "EU"},
        {"milestone": "IMO target: 70% GHG reduction (strive 80%)", "year": 2040, "category": "IMO"},
        {"milestone": "IMO target: Net-zero emissions", "year": 2050, "category": "IMO"},
    ]

    _cat_colors = {"IMO": "#4e79a7", "EU": "#f28e2b"}

    reg_fig = go.Figure()

    reg_fig.add_trace(
        go.Bar(
            y=[m["milestone"] for m in reg_milestones],
            x=[m["year"] for m in reg_milestones],
            orientation="h",
            marker_color=[_cat_colors[m["category"]] for m in reg_milestones],
            text=[str(m["year"]) for m in reg_milestones],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Year: %{x}<extra></extra>",
        )
    )

    reg_fig.update_layout(
        title="Shipping decarbonization regulatory timeline (2023-2050)",
        xaxis=dict(title="Year", range=[2022, 2052]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=380, r=80, b=50),
        height=550,
        annotations=[
            dict(
                text="<span style='color:#4e79a7'>IMO (global)</span>  |  "
                "<span style='color:#f28e2b'>EU (regional)</span>",
                xref="paper", yref="paper",
                x=0.5, y=1.06,
                showarrow=False, font=dict(size=12),
            )
        ],
    )

    reg_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Regulatory landscape notes:

    IMO Net-Zero Framework (approved MEPC 83, April 2025):
    - First-ever global carbon pricing for an entire industry sector. Two-tiered system: ships exceeding the Base Target pay \$380/tCO2eq; ships exceeding the stricter Direct Compliance Target pay \$100/tCO2eq. Revenue flows to a new IMO Climate Fund.
    - GHG Fuel Intensity (GFI) targets use a 2008 reference value of 93.3 gCO2eq/MJ. The 2028 base target is 89.6 gCO2eq/MJ (4% reduction), tightening annually to 65.3 gCO2eq/MJ by 2035 (30% reduction). A 2040 target of 65% reduction was also agreed.
    - Applies to ships over 5,000 GT (85% of shipping emissions). Formal adoption was expected October 2025 but was delayed to an extraordinary MEPC session in fall 2026. Entry into force projected 2027, enforcement from 2028.

    EU ETS for shipping:
    - Phase-in: 40% of emissions (2024), 70% (2025), 100% (2026). From 2026, CH4 and N2O also in scope.
    - EU carbon allowance price: EUR 65-90/tCO2 in 2024-2025. Total cost estimated at USD 7.5B/year at full scope (Drewry).
    - Compliance cost per tonne of VLSFO: \$185/t in 2025, rising to \$319/t in 2026 (full phase-in + GHG scope expansion).

    FuelEU Maritime (effective January 1, 2025):
    - Requires -2% GHG intensity vs reference value of 91.16 gCO2eq/MJ from 2025, tightening to -6% (2030), -14.5% (2035), -31% (2040), -62% (2045), -80% (2050).
    - Penalty: EUR 2,400 per tonne VLSFO equivalent deficit. Escalating 10% multiplier for consecutive non-compliance.

    CII (Carbon Intensity Indicator):
    - Ships rated A-E. D for 3 consecutive years or E for 1 year requires corrective action plan.
    - ~42% of the global tanker, bulk carrier, and container fleet at risk of D/E ratings without operational changes.
    - D/E ratings cause 5-15% charter rate discounts, ESG-sensitive charterer exclusion, and asset value depreciation.

    Sources: IMO MEPC 83 summary, DNV, European Commission EU ETS FAQ, Drewry Maritime, Lloyd's Register FuelEU guide.
    """
    )
    return


@app.cell
def _(go):
    fuel_data = [
        {"fuel": "VLSFO (fossil baseline)", "cost_hfo_eq": 585, "trl": "9 - Mature",
         "fleet_pct": "52% of bunker sales", "co2_reduction": "0% (baseline)", "color": "#636363"},
        {"fuel": "HSFO + scrubber", "cost_hfo_eq": 520, "trl": "9 - Mature",
         "fleet_pct": "32% of bunker sales", "co2_reduction": "0% (baseline)", "color": "#969696"},
        {"fuel": "LNG (fossil)", "cost_hfo_eq": 550, "trl": "9 - Mature",
         "fleet_pct": "1.7% of bunker sales", "co2_reduction": "~20% tank-to-wake (methane slip offsets)", "color": "#4e79a7"},
        {"fuel": "Bio-LNG", "cost_hfo_eq": 1000, "trl": "8 - Qualified",
         "fleet_pct": "<0.1%", "co2_reduction": "65-85% well-to-wake", "color": "#76b7b2"},
        {"fuel": "Grey methanol", "cost_hfo_eq": 700, "trl": "9 - Mature",
         "fleet_pct": "0.02% of bunker sales", "co2_reduction": "~0% (fossil feedstock)", "color": "#f28e2b"},
        {"fuel": "Bio-methanol", "cost_hfo_eq": 1600, "trl": "7-8",
         "fleet_pct": "Pilot scale", "co2_reduction": "65-95% well-to-wake", "color": "#e15759"},
        {"fuel": "E-methanol", "cost_hfo_eq": 2400, "trl": "6-7",
         "fleet_pct": "Pre-commercial", "co2_reduction": "~95% well-to-wake", "color": "#b07aa1"},
        {"fuel": "Green ammonia", "cost_hfo_eq": 1900, "trl": "6-7",
         "fleet_pct": "Testing phase", "co2_reduction": "~95% well-to-wake (zero carbon)", "color": "#59a14f"},
        {"fuel": "Green hydrogen", "cost_hfo_eq": 5000, "trl": "4-5 (marine)",
         "fleet_pct": "R&D only", "co2_reduction": "100% (zero carbon)", "color": "#edc948"},
        {"fuel": "Biofuel blend (B30)", "cost_hfo_eq": 750, "trl": "8-9",
         "fleet_pct": "~3.2% of bunker sales", "co2_reduction": "20-25% (at B30 blend)", "color": "#ff9da7"},
    ]

    fuel_fig = go.Figure()

    fuel_fig.add_trace(
        go.Bar(
            y=[f["fuel"] for f in fuel_data],
            x=[f["cost_hfo_eq"] for f in fuel_data],
            orientation="h",
            marker_color=[f["color"] for f in fuel_data],
            text=[f"${f['cost_hfo_eq']:,}/t" for f in fuel_data],
            textposition="outside",
            customdata=[
                f"TRL: {f['trl']}<br>Fleet share: {f['fleet_pct']}<br>CO2 reduction: {f['co2_reduction']}"
                for f in fuel_data
            ],
            hovertemplate="<b>%{y}</b><br>Cost (HFO-equivalent): $%{x:,}/t<br>%{customdata}<extra></extra>",
        )
    )

    fuel_fig.add_vline(
        x=585, line_dash="dash", line_color="red",
        annotation_text="VLSFO baseline: $585/t", annotation_position="top right",
    )

    fuel_fig.update_layout(
        title="Marine fuel cost comparison (USD/tonne, HFO-energy-equivalent basis, 2025)",
        xaxis=dict(title="USD per tonne (energy-adjusted to HFO equivalent)", range=[0, 5800]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=200, r=100, b=50),
        height=550,
    )

    fuel_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Fuel cost comparison notes:

    Prices shown on an energy-equivalent basis (adjusted to HFO energy content). Methanol has roughly half the energy density of HFO, so a tonne of methanol at \$350/t costs ~\$700/t on an HFO-equivalent basis.

    Key observations:
    - VLSFO at \$585/t is the baseline. With EU ETS at full phase-in (2026), the effective cost rises to \$755-795/t for intra-EU voyages.
    - LNG is currently the cheapest alternative (~\$550/t HFO-eq), but methane slip (up 180% since 2016) erodes its GHG advantage to ~20% well-to-wake.
    - Green methanol costs 2.5-4.5x the fossil baseline depending on pathway (bio-methanol vs e-methanol).
    - Green ammonia at ~\$1,900/t HFO-eq is 3-4x the baseline. 45 ammonia-capable ships on order, but bunkering infrastructure is minimal.
    - Carbon price needed for fuel switching: green ammonia needs ~\$360/tCO2 incentive. The IMO's \$100/\$380 framework gets partway there but likely insufficient alone before 2035.
    - Biofuel blends (B30) are the easiest near-term drop-in option -- no engine modifications, 20-25% CO2 reduction.

    Sources: Ship & Bunker, S&P Global Platts, DNV, SEA-LNG, Methanol Institute, Oxford Institute for Energy Studies.
    """
    )
    return


@app.cell
def _(go):
    orderbook_data = [
        {"fuel": "LNG", "ships": 1259, "color": "#4e79a7"},
        {"fuel": "Methanol", "ships": 385, "color": "#f28e2b"},
        {"fuel": "LPG", "ships": 139, "color": "#76b7b2"},
        {"fuel": "Ethane", "ships": 55, "color": "#edc948"},
        {"fuel": "Hydrogen", "ships": 33, "color": "#59a14f"},
        {"fuel": "Ammonia", "ships": 45, "color": "#e15759"},
        {"fuel": "Biofuel", "ships": 22, "color": "#ff9da7"},
        {"fuel": "Nuclear", "ships": 4, "color": "#b07aa1"},
    ]

    orderbook_fig = go.Figure(
        data=[
            go.Pie(
                labels=[d["fuel"] for d in orderbook_data],
                values=[d["ships"] for d in orderbook_data],
                hole=0.4,
                marker=dict(colors=[d["color"] for d in orderbook_data]),
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>%{value} ships<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Ships on order: %{value}<br>Share: %{percent}<extra></extra>",
            )
        ]
    )

    orderbook_fig.update_layout(
        title="Alternative fuel vessel orderbook by fuel type (H1 2025, total: 1,942 ships)",
        annotations=[
            dict(text="1,942<br>ships", x=0.5, y=0.5, font_size=16, showarrow=False)
        ],
        showlegend=True,
        height=550,
    )

    orderbook_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Orderbook analysis notes:

    LNG dominance (1,259 ships, 65%):
    - LNG led H1 2025 with 87 new orders (14.2M GT), dominating the container segment.
    - LNG bunkering available at 222 ports globally, with 62 bunkering vessels in operation.
    - But methane slip is the elephant in the room: CH4 emissions from LNG ships rose 180% since 2016. From 2026, CH4 falls under EU ETS scope.

    Methanol momentum stalls (385 ships, 20%):
    - Methanol orders fell to 61 in H1 2025 from 149 in all of 2024 -- a sharp deceleration.
    - Only 48 ports have methanol bunkering available or planned (vs 222 for LNG).
    - Green methanol supply crisis: ~500,000 t/yr produced today vs potential demand of 13M t/yr by 2030 if all dual-fuel vessels operate at capacity.

    Ammonia lags (45 ships, 2%):
    - Only 3 ammonia-fuelled orders placed in H1 2025. Engine technology advancing: Japan Engine Corporation completed the world's first full-scale commercial ammonia-fueled engine in August 2025.
    - Safety and toxicity remain primary barriers -- IMO issued interim safety guidelines in March 2025.

    Nuclear emerging (4 ships):
    - DNV awarded Approval in Principle for HD Korea Shipbuilding's 15,000 TEU SMR-powered container vessel design.
    - Could eliminate \$68M/yr in operating fuel costs per large container ship.

    Sources: DNV Alternative Fuel Insight, Clarksons Green Technology Tracker, Lloyd's Register.
    """
    )
    return


@app.cell
def _(go):
    carrier_strategies = [
        {"company": "Maersk", "country": "DK", "strategy": "Methanol-first", "alt_fuel_vessels": 25, "revenue_b": 55.5,
         "hover": "19 methanol vessels deployed by end-2025. 25 total on order. Net-zero target 2040 (decade ahead of IMO)."},
        {"company": "CMA CGM", "country": "FR", "strategy": "LNG + methanol pivot", "alt_fuel_vessels": 77, "revenue_b": 55.5,
         "hover": "77 LNG dual-fuel vessels ordered/delivered. JV with TotalEnergies for LNG bunkering. Also completed inaugural green methanol bunkering in Shanghai."},
        {"company": "MSC", "country": "CH", "strategy": "LNG pragmatist", "alt_fuel_vessels": 150, "revenue_b": 40.0,
         "hover": "~40 dual-fuel vessels added in 2025. 150+ ships expected dual-fuel capable. Pragmatic, incremental approach."},
        {"company": "Hapag-Lloyd", "country": "DE", "strategy": "LNG + methanol", "alt_fuel_vessels": 45, "revenue_b": 20.0,
         "hover": "37 LNG dual-fuel ships in service/on order. 8 new methanol ships ordered (>USD 500M). Bio-LNG supply deal with Shell."},
        {"company": "Evergreen", "country": "TW", "strategy": "LNG-led, hedging methanol", "alt_fuel_vessels": 41, "revenue_b": 15.0,
         "hover": "11 x 24,000 TEU LNG dual-fuel ships (~USD 3.25B). ~30 methanol vessels on order. Chose LNG as primary in Jan 2025."},
        {"company": "ONE", "country": "JP", "strategy": "Methanol bet", "alt_fuel_vessels": 12, "revenue_b": 14.0,
         "hover": "12 methanol dual-fuel containerships announced. First deliveries by 2030. Currently using sustainable biofuels."},
        {"company": "COSCO", "country": "CN", "strategy": "Multi-fuel hedger", "alt_fuel_vessels": 16, "revenue_b": 32.3,
         "hover": "4 large container vessels retrofitted to methanol dual-fuel. 12 x 18,000 TEU LNG dual-fuel ships ordered. Exploring methanol, ammonia, LNG."},
    ]

    _flag_decarb = {
        "DK": "\U0001f1e9\U0001f1f0", "FR": "\U0001f1eb\U0001f1f7", "CH": "\U0001f1e8\U0001f1ed",
        "DE": "\U0001f1e9\U0001f1ea", "TW": "\U0001f1f9\U0001f1fc", "JP": "\U0001f1ef\U0001f1f5",
        "CN": "\U0001f1e8\U0001f1f3",
    }

    _root_d = "Shipping Line Strategies"
    _tm_labels_d = [_root_d]
    _tm_parents_d = [""]
    _tm_values_d = [0.0]
    _tm_customdata_d = [""]

    _strategies_d = sorted({c["strategy"] for c in carrier_strategies})
    _strat_idx_d: dict[str, int] = {}
    for _s in _strategies_d:
        _strat_idx_d[_s] = len(_tm_labels_d)
        _tm_labels_d.append(_s)
        _tm_parents_d.append(_root_d)
        _tm_values_d.append(0.0)
        _tm_customdata_d.append(f"<b>{_s}</b>")

    _total_d = 0.0
    for _c in carrier_strategies:
        _r = float(_c["alt_fuel_vessels"])
        _total_d += _r
        _f = _flag_decarb.get(_c["country"], "")
        _lbl = f"{_c['company']} {_f}".strip()

        _tm_labels_d.append(_lbl)
        _tm_parents_d.append(_c["strategy"])
        _tm_values_d.append(_r)
        _tm_customdata_d.append(
            "<b>{lbl}</b>"
            "<br>Strategy: {strat}"
            "<br>Alt-fuel vessels: {v}"
            "<br>Revenue: ${r:.1f}B"
            "<br>{hover}"
            "<extra></extra>".format(
                lbl=_lbl, strat=_c["strategy"], v=int(_r), r=_c["revenue_b"], hover=_c["hover"],
            )
        )
        _tm_values_d[_strat_idx_d[_c["strategy"]]] += _r

    _tm_values_d[0] = _total_d

    carrier_fig = go.Figure(
        go.Treemap(
            labels=_tm_labels_d,
            parents=_tm_parents_d,
            values=_tm_values_d,
            branchvalues="total",
            customdata=_tm_customdata_d,
            hovertemplate="%{customdata}",
            texttemplate="<b>%{label}</b><br>%{value} vessels",
        )
    )

    carrier_fig.update_layout(
        title="Major shipping lines: decarbonization strategies by alt-fuel vessel count",
        margin=dict(t=90, l=10, r=10, b=10),
        height=500,
    )

    carrier_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Carrier strategy analysis:

    The industry has split into three camps:

    1. Methanol-first (Maersk, ONE): Maersk is the undisputed leader, deploying 19 methanol vessels by end-2025. Net-zero target is 2040, a decade ahead of IMO. The bet: methanol's compatibility with existing port infrastructure and potential for bio/e-methanol blending outweighs the 2-4x cost premium.

    2. LNG pragmatists (CMA CGM, MSC, Evergreen): These carriers chose the fuel with the best available infrastructure (222 ports) and lowest cost premium. MSC alone expects 150+ dual-fuel capable ships. The risk: methane slip and CH4 entering EU ETS scope from 2026.

    3. Multi-fuel hedgers (Hapag-Lloyd, COSCO): Diversifying across LNG and methanol to avoid a single-fuel bet. Hapag-Lloyd has 37 LNG ships plus 8 new methanol orders (\$500M+). Most capital-intensive but least risky approach.

    The customer dimension: ZEMBA (Zero Emission Maritime Buyers Alliance) -- 45+ members including Amazon, IKEA, Nike, Meta -- is creating demand-side pull. Hapag-Lloyd won ZEMBA's first and second tenders for e-fuel deployment.

    Sources: Maersk press releases, gCaptain, Hapag-Lloyd IR, CMA CGM sustainability reports, ZEMBA.
    """
    )
    return


@app.cell
def _(go):
    gfi_years = [2025, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2040]
    gfi_base = [93.3, 89.6, 87.7, 85.8, 81.7, 77.6, 73.5, 69.4, 65.3, 32.7]
    gfi_direct = [93.3, 77.4, 75.5, 73.6, 69.5, 65.4, 61.3, 57.2, 53.2, None]

    fuel_gfi = {
        "VLSFO (fossil)": 91.2,
        "LNG (fossil)": 77.0,
        "Bio-methanol": 20.0,
        "E-ammonia": 19.0,
        "Green hydrogen": 0.0,
    }

    gfi_fig = go.Figure()

    gfi_fig.add_trace(
        go.Scatter(
            x=gfi_years, y=gfi_base,
            name="Base Target (Tier 2: $380/tCO2 penalty)",
            mode="lines+markers", line=dict(color="#e15759", width=3), marker=dict(size=8),
            hovertemplate="<b>Base Target</b><br>Year: %{x}<br>GFI: %{y:.1f} gCO2eq/MJ<extra></extra>",
        )
    )

    gfi_fig.add_trace(
        go.Scatter(
            x=[y for y, v in zip(gfi_years, gfi_direct) if v is not None],
            y=[v for v in gfi_direct if v is not None],
            name="Direct Compliance Target (Tier 1: $100/tCO2 levy)",
            mode="lines+markers", line=dict(color="#59a14f", width=3, dash="dash"), marker=dict(size=8),
            hovertemplate="<b>Direct Target</b><br>Year: %{x}<br>GFI: %{y:.1f} gCO2eq/MJ<extra></extra>",
        )
    )

    _fuel_colors_gfi = {
        "VLSFO (fossil)": "#636363", "LNG (fossil)": "#4e79a7",
        "Bio-methanol": "#f28e2b", "E-ammonia": "#b07aa1", "Green hydrogen": "#edc948",
    }

    for _fname, _fval in fuel_gfi.items():
        gfi_fig.add_hline(
            y=_fval, line_dash="dot", line_color=_fuel_colors_gfi[_fname],
            annotation_text=f"{_fname}: {_fval} gCO2eq/MJ", annotation_position="right",
        )

    gfi_fig.update_layout(
        title="IMO GHG Fuel Intensity (GFI) reduction pathway vs fuel options (gCO2eq/MJ)",
        xaxis=dict(title="Year", dtick=2),
        yaxis=dict(title="GFI (gCO2eq/MJ, well-to-wake)", range=[-5, 100]),
        margin=dict(t=80, l=60, r=200, b=50),
        height=500,
        legend=dict(x=0.01, y=0.99),
    )

    gfi_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    GFI pathway analysis:

    This chart reveals the fundamental challenge: regulatory targets tighten faster than the fuel transition can deliver.

    - VLSFO at ~91.2 gCO2eq/MJ exceeds the 2028 base target (89.6). Ships running on pure VLSFO will pay the \$380/tCO2 penalty from day one.
    - Fossil LNG at ~77 gCO2eq/MJ sits below the base target until 2033 but above the direct compliance target from 2029 (when it drops to 75.5 gCO2eq/MJ).
    - By 2033, the base target hits 73.5 gCO2eq/MJ -- below fossil LNG. At this point, no fossil fuel is compliant without blending.
    - Only bio-methanol (~20), e-ammonia (~19), and green hydrogen (0) are comfortably below both targets throughout.
    - The economics: a 15,000 TEU container vessel consuming ~200 t/day on VLSFO in 2028 faces approximately \$12,000-15,000/day in carbon penalties.

    Carriers must begin blending green fuels by 2028-2030 or face escalating financial penalties. The Base Target at \$380/tCO2 is designed to be punitive enough to drive behavior change.

    Sources: BIMCO IMO Net-Zero Framework update, ICCT analysis, DNV.
    """
    )
    return


@app.cell
def _(go):
    from plotly.subplots import make_subplots as _make_subplots

    supply_years = ["2024", "2025", "2026", "2028", "2030"]
    methanol_supply_kt = [50, 500, 1500, 5000, 15000]
    methanol_demand_kt = [200, 800, 2000, 6000, 13000]

    supply_fig = _make_subplots(specs=[[{"secondary_y": True}]])

    supply_fig.add_trace(
        go.Bar(
            x=supply_years, y=methanol_supply_kt,
            name="Green methanol supply — realistic est. (kt/yr)", marker_color="#59a14f",
            hovertemplate="<b>Supply</b><br>Year: %{x}<br>%{y:,} kt/yr<extra></extra>",
        ),
        secondary_y=False,
    )

    supply_fig.add_trace(
        go.Scatter(
            x=supply_years, y=methanol_demand_kt,
            name="Projected demand from dual-fuel fleet (kt/yr)",
            mode="lines+markers", line=dict(color="#e15759", width=3), marker=dict(size=10),
            hovertemplate="<b>Demand</b><br>Year: %{x}<br>%{y:,} kt/yr<extra></extra>",
        ),
        secondary_y=False,
    )

    supply_fig.update_layout(
        title="Green methanol: supply vs demand from shipping (thousand tonnes/yr)",
        xaxis=dict(title="Year", type="category"),
        hovermode="x unified",
        margin=dict(t=80, l=60, r=60, b=50),
        legend=dict(x=0.01, y=0.99),
        height=450,
    )
    supply_fig.update_yaxes(title_text="Thousand tonnes per year", secondary_y=False)

    supply_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Green methanol supply-demand gap:

    The gap between rhetoric and reality:
    - 2024: ~50,000 tonnes of green methanol actually available for shipping vs ~200,000 tonnes needed by the deployed fleet.
    - 2025: Pipeline expanded to 252 renewable methanol projects with 35.7 Mt of announced capacity by 2030 (e-methanol 19.4 Mt + bio-methanol 16.3 Mt, Methanol Institute). But <5% of announced projects have reached final investment decision. Risk-adjusted supply (chart above) is ~15 Mt/yr by 2030 — roughly 42% of announced capacity.
    - 2030 projection: If all 500+ methanol-capable vessels operate at capacity, shipping could absorb 13 Mt/yr of green methanol. The 35.7 Mt announced pipeline looks adequate on paper but far from reality.

    The chicken-and-egg problem: Carriers won't commit to green methanol volumes without guaranteed supply at predictable prices. Fuel producers won't build plants without long-term offtake agreements. ZEMBA's collective tender model (locking in ~70,000t of e-methanol + 25,000t of e-ammonia for 2027 delivery) is an attempt to break this deadlock.

    Green ammonia faces an even wider gap: only 45 ammonia-capable ships on order vs 385 for methanol. Ammonia's path is 3-5 years behind methanol.

    Sources: Methanol Institute, Global Maritime Forum, ZEMBA press releases.
    """
    )
    return


@app.cell
def _(go):
    tech_data_decarb = [
        {"technology": "Wind-assisted propulsion\n(Flettner rotors, rigid sails, kites)",
         "fuel_savings_pct": 15, "capex_m": 3, "vessels_deployed": 50, "market_2034_b": 40, "trl": "8-9",
         "detail": "75% of installations are retrofits. Up to 25% fuel savings in optimal wind. World's first WAPS-fitted newbuild tanker (114k DWT) delivered June 2025."},
        {"technology": "Battery-electric\n(short-sea, ferries)",
         "fuel_savings_pct": 100, "capex_m": 50, "vessels_deployed": 300, "market_2034_b": 18, "trl": "8-9",
         "detail": "Market $4.85B (2025) -> $18.4B (2032) at 21% CAGR. World's largest electric ferry: 130m, 40 MWh (Incat, May 2025)."},
        {"technology": "Air lubrication systems",
         "fuel_savings_pct": 8, "capex_m": 2, "vessels_deployed": 40, "market_2034_b": 2, "trl": "7-8",
         "detail": "Micro-bubbles reduce hull friction 5-10%. Silverstream, Samsung. Armada Technologies raised $3.2M seed (2025)."},
        {"technology": "Nuclear SMR propulsion",
         "fuel_savings_pct": 100, "capex_m": 500, "vessels_deployed": 0, "market_2034_b": 5, "trl": "3-4 (marine)",
         "detail": "HD Korea: AiP for 15,000 TEU SMR design. ABB/Blykalla MoU. Could eliminate $68M/yr in fuel costs per ship."},
    ]

    tech_fig_d = go.Figure()
    _colors_d = ["#4e79a7", "#59a14f", "#f28e2b", "#b07aa1"]

    tech_fig_d.add_trace(
        go.Bar(
            y=[t["technology"] for t in tech_data_decarb],
            x=[t["fuel_savings_pct"] for t in tech_data_decarb],
            orientation="h",
            marker_color=_colors_d,
            text=[f"{t['fuel_savings_pct']}% fuel saving" for t in tech_data_decarb],
            textposition="outside",
            customdata=[
                f"TRL: {t['trl']}<br>Vessels deployed: {t['vessels_deployed']}<br>"
                f"Capex: ~${t['capex_m']}M per vessel<br>Market by 2034: ~${t['market_2034_b']}B<br>{t['detail']}"
                for t in tech_data_decarb
            ],
            hovertemplate="<b>%{y}</b><br>Fuel savings: %{x}%<br>%{customdata}<extra></extra>",
        )
    )

    tech_fig_d.update_layout(
        title="Emerging decarbonization technologies: fuel savings potential (%)",
        xaxis=dict(title="Fuel savings (%)", range=[0, 120]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=280, r=80, b=50),
        height=400,
    )

    tech_fig_d
    return


@app.cell
def _(mo):
    mo.md(
        """
    Emerging technology notes:

    Wind-assisted propulsion (WAPS):
    - Market projected to reach \$40B by 2034. Over 50 large vessels deployed, doubling every year. 75% are retrofits.
    - Best-case 25% fuel savings, typical 8-15%. Performance varies with wind direction and route.

    Battery-electric ships:
    - Viable only for short-sea, ferries, and harbor craft. Not viable for transoceanic routes (batteries ~100x heavier than diesel for equivalent energy).
    - Market growing at 21% CAGR. World's largest electric ferry: 130m, 40 MWh battery (Incat, May 2025).

    Nuclear SMR propulsion:
    - Zero operational emissions. Could eliminate \$68M/year in fuel costs per large container ship.
    - HD Korea received DNV AiP for 15,000 TEU SMR-powered design. US DOT Maritime Administration launched SMR-for-shipping initiative.
    - Barriers: regulatory framework doesn't exist, port access restrictions, public acceptance, 10-15 year payback.

    Sources: NaviStrat Analytics, IDTechEx, MarketsandMarkets, Maritime Executive, DNV.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    Challenges, barriers, and the path to 2050:

    Six structural barriers:

    1. Green fuel availability crisis: Green methanol production is ~500kt/yr vs potential demand of 13Mt/yr by 2030. <5% of the 252 announced projects have reached final investment decision.

    2. Bunkering infrastructure gaps: LNG at 222 ports, methanol at 48 ports, ammonia essentially non-existent for commercial use.

    3. Safety and handling: Ammonia is acutely toxic. Methanol has a low flashpoint. Each fuel introduces distinct safety regimes -- 800,000 seafarers need alternative fuel training by the mid-2030s.

    4. First-mover disadvantage: Carriers using green fuels face a 2-4x cost premium. The IMO's \$380/tCO2 penalty helps but likely insufficient before 2035.

    5. LNG stranded asset risk: 1,259 LNG dual-fuel ships represent billions in capital. Methane slip has risen 180% since 2016. The "transition fuel" narrative requires a bio/e-methane supply chain that barely exists.

    6. Scrapping rate mismatch: Global fleet average age is 12.7 years. The new alt-fuel orderbook (1,942 ships) is <2% of the 109,000-ship total fleet.

    Timeline to 2050:
    - 2025-2027: FuelEU Maritime and EU ETS create European compliance pressure. Biofuel blends are the path of least resistance.
    - 2028-2030: IMO GFI standard and carbon pricing kick in. VLSFO becomes non-compliant. Green methanol supply ramps if investment decisions materialize.
    - 2031-2035: Base target drops below fossil LNG. Large-scale blending of green fuels becomes mandatory. Ammonia infrastructure buildout accelerates.
    - 2036-2040: IMO 65% reduction target. Ammonia and e-methanol become primary fuels for newbuilds. Fossil-only vessels face severe commercial penalties.
    - 2041-2050: Path to net-zero. Fleet turnover accelerates. Zero-emission transoceanic voyages become routine.

    Expert consensus (AGU Earth's Future, 2025): 30-40% carbon intensity reduction by 2030 is achievable, but only 40-75% GHG reduction by 2050 -- falling short of net-zero.

    Sources: DNV Maritime Forecast to 2050, Global Maritime Forum, UNCTAD, AGU Earth's Future (Laskar et al. 2025), BIMCO.
    """
    )
    return


if __name__ == "__main__":
    app.run()
