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
    # 4.66 million robots are working. Almost none carry robot-specific insurance.

    The world operates ~4.66 million industrial robots (IFR, 2024), adding ~542,000 more every year, plus a fast-growing fleet of service, surgical, delivery and (soon) humanoid robots. That is several hundred billion dollars of machines that sense, decide and physically act. Yet there is no regulator-reported "robotics insurance" line: dedicated robotics / autonomous-systems premium is a directional estimate of only a few hundred million dollars. The risk is carried almost entirely inside product-liability, general-liability, workers-comp and cyber policies that were never designed for autonomous machines.

    ---

    ## Robotics Insurance Deep Dive (2025)
    - Deployed base: ~4.66M operational industrial robots (2024, +9% YoY), ~200k professional service robots sold in 2024. Robotics revenue ~\$45-90B depending on scope; GlobalData projects ~\$205B by 2030.
    - Dedicated robotics insurance premium: no clean figure exists. Syndicated reports quote \$0.19-1.4B for 2024 on undisclosed methodology; a defensible read is low hundreds of millions in genuinely robot-specific premium.
    - Sits at the intersection of the ~\$8T global insurance industry, the ~\$45-90B robotics market, and product-liability / commercial-lines books that silently absorb most robot risk today.
    - Coverage is contracting where it should expand: new ISO endorsements CG 40 47 / CG 40 48 (effective Jan 2026) let carriers strip AI-related claims from standard GL, and regulators approved >80% of the AI-exclusion filings from Berkshire Hathaway, Chubb and Travelers.
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    gap_stack = [
        {"label": "Deployed industrial-robot capital (est.)", "value_b": 375, "color": "#4e79a7"},
        {"label": "Silent robot risk inside general P&C books (est.)", "value_b": 20, "color": "#f28e2b"},
        {"label": "Dedicated robotics insurance premium (est.)", "value_b": 0.5, "color": "#e15759"},
    ]

    gap_fig = go.Figure()

    gap_fig.add_trace(
        go.Bar(
            y=[d["label"] for d in gap_stack],
            x=[d["value_b"] for d in gap_stack],
            orientation="h",
            marker_color=[d["color"] for d in gap_stack],
            text=[
                f"${d['value_b']:,.0f}B" if d["value_b"] >= 100
                else f"${d['value_b']:.0f}B" if d["value_b"] >= 5
                else f"${d['value_b']:.1f}B"
                for d in gap_stack
            ],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>$%{x:,.1f}B<extra></extra>",
        )
    )

    gap_fig.add_annotation(
        x=375, y="Dedicated robotics insurance premium (est.)",
        text="<b>Dedicated robotics premium is ~0.1% of deployed robot capital</b>",
        showarrow=True, arrowhead=2,
        ax=-120, ay=-40,
        font=dict(size=13, color="#e15759"),
    )

    gap_fig.update_layout(
        title="The robotics protection gap: deployed capital vs. what's explicitly insured (est., USD billions, log scale)",
        xaxis=dict(
            title="USD billions (log scale)",
            type="log",
            range=[-0.5, 3.0],
        ),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=320, r=80, b=50),
        height=340,
    )

    gap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Protection-gap notes (all figures directional estimates, not measured):
    - Deployed industrial-robot capital: 4.66M operational units (IFR World Robotics 2025) at a rough installed cost of \$50-100k each (robot + integration) implies ~\$300-450B of deployed industrial-robot capital alone, before service, surgical, delivery and humanoid robots. The \$375B bar is the midpoint.
    - Silent robot risk: an estimate of the robot-attributable exposure embedded inside general product-liability, CGL, workers-comp and cyber policies that were not designed for autonomous machines. Nobody measures this cleanly.
    - Dedicated robotics premium: genuinely robot-branded cover (Lloyd's-backed programs, robotics MGAs) is plausibly only a few hundred million dollars. Syndicated market reports quote \$0.19-1.4B for the "robot insurance market" on undisclosed methodology and likely conflate adjacent lines.
    - The gap is widening, not closing: standard policies increasingly exclude AI. Treat the specific dollar figures as scale markers, not precise values.
    """
    )
    return


@app.cell
def _(go):
    target_years = ["2024 (syndicated est.)", "2026 (est.)", "2030 low", "2032 high"]
    target_values = [1.2, 1.9, 5.0, 8.7]
    target_colors = ["#4e79a7", "#4e79a7", "#f28e2b", "#e15759"]
    target_sources = [
        "market.us / marketintelo (undisclosed method)",
        "QYResearch-style estimate",
        "Extrapolated ~13-25% CAGR (low)",
        "marketintelo target (~24.9% CAGR)",
    ]

    target_fig = go.Figure(
        go.Bar(
            x=target_years,
            y=target_values,
            marker_color=target_colors,
            text=[f"${v:.1f}B" for v in target_values],
            textposition="outside",
            customdata=target_sources,
            hovertemplate="<b>%{x}</b><br>$%{y:.1f}B<br>%{customdata}<extra></extra>",
        )
    )

    target_fig.update_layout(
        title="Robotics insurance market: vendor estimates disagree wildly (USD billions)",
        xaxis=dict(title="", type="category"),
        yaxis=dict(title="Robotics insurance premium (USD billions, est.)", range=[0, 10]),
        margin=dict(t=70, l=60, r=40, b=60),
        height=360,
    )

    target_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Market-projection notes:
    - Every figure here is a third-party market-research estimate with undisclosed methodology, and they disagree by more than 5x for the same year. That disagreement is itself the finding: nobody actually knows the size of the robotics insurance market.
    - Reported robotics-insurance TAMs for 2024 cluster loosely at \$1-1.4B ("Robot Insurance" \$1.2B, "Robotics Manufacturer Liability" \$1.41B), with projected CAGRs of 13-25% to the early 2030s. QYResearch quotes a far smaller ~\$187M (2026) pure-play figure.
    - The more credible signal that a real market is forming is not the TAM reports but funded specialty activity: Koop Technologies launched a robotics GL + E&O product on Lloyd's paper, AIUC raised a \$15M seed for AI underwriting (2025), and Munich Re / HSB launched AI liability cover (2026).
    - Colour distinguishes the near-term estimates (blue) from the forward projections (orange / red).
    """
    )
    return


@app.cell
def _(go):
    coverage_data = [
        {"segment": "Product liability + CGL", "value_pct": 40},
        {"segment": "Workers' compensation", "value_pct": 22},
        {"segment": "Equipment / machinery breakdown", "value_pct": 15},
        {"segment": "Professional liability / E&O", "value_pct": 12},
        {"segment": "Cyber / cyber-physical", "value_pct": 7},
        {"segment": "Specialty autonomous-systems lines", "value_pct": 4},
    ]

    cov_labels = [d["segment"] for d in coverage_data]
    cov_values = [d["value_pct"] for d in coverage_data]

    cov_fig = go.Figure(
        data=[
            go.Pie(
                labels=cov_labels,
                values=cov_values,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Est. share of robot risk: %{value}%<br><extra></extra>",
            )
        ]
    )

    cov_fig.update_layout(
        title="How robot risk is insured today (est. share of robotics-attributable premium)",
        annotations=[
            dict(text="By line", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    cov_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Coverage-type notes (qualitative ranking; no credible quantitative split exists, so proportions are estimates from broker/industry sources):
    - Product liability + commercial general liability is the dominant bucket: bodily-injury and property claims land on the robot maker's and integrator's books. This is where most robot risk actually sits.
    - Workers' compensation covers shop-floor cobot / AMR exposure at the end-user. Note cobots can reduce claims: one Universal Robots deployment cut injury claims ~40%, so this line is partly a cost-saver, not just an exposure.
    - Equipment / machinery breakdown insures the robot asset itself.
    - Professional liability / E&O is the fastest-growing frontier, essential for Robotics-as-a-Service operators and integrators whose uptime and performance obligations create errors-and-omissions exposure. Koop's product is explicitly GL + E&O.
    - The core structural problem: autonomous-robot losses are hybrid (defective hardware + flawed AI decision + cyber + operator error), so they do not map cleanly onto one policy, and liability is contested across OEM, AI-model vendor, integrator and operator.
    """
    )
    return


@app.cell
def _(go):
    buyer_data = [
        {"segment": "Robot manufacturers / OEMs", "value_pct": 44},
        {"segment": "End-user enterprises deploying robots", "value_pct": 30},
        {"segment": "RaaS operators (fleet owners)", "value_pct": 16},
        {"segment": "System integrators", "value_pct": 10},
    ]

    buyer_labels = [d["segment"] for d in buyer_data]
    buyer_values = [d["value_pct"] for d in buyer_data]

    buyer_fig = go.Figure(
        data=[
            go.Pie(
                labels=buyer_labels,
                values=buyer_values,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Est. share of robotics-attributable premium: %{value}%<br><extra></extra>",
            )
        ]
    )

    buyer_fig.update_layout(
        title="Robotics insurance by buyer segment (2025 est.)",
        annotations=[
            dict(text="By buyer", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    buyer_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Buyer-segmentation notes (estimates from broker sources):
    - Robot manufacturers / OEMs are the largest, most mature buyers: they carry product liability + CGL + recall, from majors (Fanuc, ABB, KUKA, Yaskawa, Intuitive Surgical) to startups. Their risk is written mostly by big product-liability carriers (AXA XL, Allianz, Chubb, AIG), not by robot-labelled policies.
    - End-user enterprises (factories, warehouses/3PLs, hospitals, farms, retailers) buy workers-comp + CGL + property, and are mostly unaware their standard policies may now exclude AI/autonomy. SMBs are the most exposed to the coverage gap because they rely on off-the-shelf BOP/CGL.
    - RaaS operators are the fastest-growing buyer type: they own the robots but deploy them at customer sites, so they need E&O + GL + property on fleets. RaaS adoption grew ~42% in 2024 (IFR).
    - System integrators are a distinct, often-overlooked buyer that stitches multi-vendor systems and inherits blame, carrying E&O + GL.
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
    _nodes_path = _base_dir / "data" / "robotics_insurance_nodes.json"

    if not _nodes_path.exists():
        raise FileNotFoundError(f"Robotics insurance nodes file not found at {_nodes_path}")

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
        title="Robotics insurance market map — 2025 dedicated premium (est., USD billions)",
        margin=dict(t=90, l=30, r=30, b=30),
        uniformtext=dict(minsize=10, mode="hide"),
        height=800,
    )

    icicle_fig.update_traces(
        root_color="lightgrey",
        tiling=dict(orientation="v"),
        maxdepth=3,
    )

    icicle_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the icicle:
    - Root anchors to a directional ~\$0.5B of DEDICATED robotics / autonomous-systems premium (2025 estimate), split into four branches: specialty and emerging-risk carriers, robotics-native MGAs / insurtechs, reinsurance / capacity, and brokers plus data enablers.
    - The node values are directional estimates only. There is no reported robotics premium by company, so these are best read as relative positioning, not precise GWP.
    - This map deliberately excludes the far larger silent robot exposure inside the product-liability books of AXA XL, Allianz, Chubb and AIG. Those carriers insure most of the world's robot makers, but not under a robotics label, so they do not appear as dedicated premium here.
    - The robotics-native insurtechs (Koop, SkyWatch, Flock, ATA, Axis, Vouch) are small by premium but define the category and sit on Lloyd's syndicates plus carrier capacity (Global Aerospace, Tokio Marine Kiln, The Hartford).
    """
    )
    return


@app.cell
def _(go):
    # focus: "specialist" = robotics/autonomy is core to the offering
    #        "diversified" = robots are one exposure inside a broad book
    strategy_companies = [
        {"company": "AXA XL", "country": "FR", "strategy": "Scale product-liability writers", "premium_b": 0.09,
         "focus": "diversified",
         "hover": "Leading product & general liability + life-sciences liability carrier. De facto insurer of many robot / surgical-robot OEMs, but written as product liability, not robotics. Est. robotics-attributable."},
        {"company": "Allianz Commercial", "country": "DE", "strategy": "Scale product-liability writers", "premium_b": 0.08,
         "focus": "diversified",
         "hover": "Global commercial carrier; major product-liability and recall writer for industrial manufacturers, robots included. Est. robotics-attributable."},
        {"company": "Chubb", "country": "US", "strategy": "Scale product-liability writers", "premium_b": 0.07,
         "focus": "diversified",
         "hover": "Large multi-line P&C writer of product liability; also filed to EXCLUDE AI-related claims from GL. Est. robotics-attributable."},
        {"company": "AIG", "country": "US", "strategy": "Scale product-liability writers", "premium_b": 0.06,
         "focus": "diversified",
         "hover": "Global commercial insurer; product-liability capacity for manufacturers deploying robots. Est. robotics-attributable."},
        {"company": "Munich Re / HSB", "country": "DE", "strategy": "Specialty & emerging-risk carriers", "premium_b": 0.06,
         "focus": "specialist",
         "hover": "HSB AI Liability Insurance (2026) pays AI-driven bodily injury / property damage GL excludes. Munich Re Tech Trend Radar names humanoids + autonomous mobility as top trends. Est."},
        {"company": "Global Aerospace", "country": "US", "strategy": "Specialty & emerging-risk carriers", "premium_b": 0.07,
         "focus": "specialist",
         "hover": "Aviation specialty carrier; underwriter behind SkyWatch.AI and a leading commercial drone / UAS writer. Est."},
        {"company": "Tokio Marine Kiln", "country": "JP", "strategy": "Specialty & emerging-risk carriers", "premium_b": 0.03,
         "focus": "specialist",
         "hover": "Backs MGA Advanced Technology Assurance; writes drone/UAS and cyber for autonomous rail, automated factories, robotics. Est."},
        {"company": "Relm Insurance", "country": "BM", "strategy": "Specialty & emerging-risk carriers", "premium_b": 0.015,
         "focus": "specialist",
         "hover": "Bermuda emerging-risk carrier; AI liability suite (2025) covering AI-driven bodily injury, property damage, professional negligence. Est."},
        {"company": "Zurich (YAS)", "country": "CH", "strategy": "Specialty & emerging-risk carriers", "premium_b": 0.02,
         "focus": "specialist",
         "hover": "Zurich HK x YAS (2026): embedded robot micro-insurance sold at the point of robot sale/service. First named APAC robot micro-insurance program. Est."},
        {"company": "Koop Technologies", "country": "US", "strategy": "Robotics-native insurtechs", "premium_b": 0.025,
         "focus": "specialist",
         "hover": "Industry-first Robotics GL + E&O (2022) with CJ Coleman + Lloyd's. API underwriting on robot telemetry; targets AVs, robots, RaaS. Est."},
        {"company": "SkyWatch.AI", "country": "US", "strategy": "Robotics-native insurtechs", "premium_b": 0.03,
         "focus": "specialist",
         "hover": "On-demand drone insurance (up to $10M from ~$10/hr), underwritten by Global Aerospace; Marsh took a minority stake (2025). Telemetry-based pricing. Est."},
        {"company": "Flock", "country": "UK", "strategy": "Robotics-native insurtechs", "premium_b": 0.045,
         "focus": "specialist",
         "hover": "UK on-demand drone insurer (~35% of UK commercial drone market); pivoted to connected / autonomous fleets. ~$38M Series B (2023). Est."},
        {"company": "Advanced Tech Assurance", "country": "UK", "strategy": "Robotics-native insurtechs", "premium_b": 0.02,
         "focus": "specialist",
         "hover": "London MGA backed by Tokio Marine Kiln; cyber + tech cover for unmanned aircraft, AVs, autonomous rail, automated factories, robotics. Est."},
        {"company": "Y-Risk (Hartford)", "country": "US", "strategy": "Robotics-native insurtechs", "premium_b": 0.015,
         "focus": "specialist",
         "hover": "MGA owned by The Hartford; usage-based, data-fed underwriting of AI + autonomous risks. Est."},
        {"company": "Axis Insurance", "country": "CA", "strategy": "Robotics-native insurtechs", "premium_b": 0.015,
         "focus": "specialist",
         "hover": "Canadian specialty broker/MGA with a dedicated robotics program: AI navigation failure, cyber-takeover damage, downtime, integrator liability. Est. (not AXIS Capital)."},
        {"company": "Munich Re (reins.)", "country": "DE", "strategy": "Reinsurance / capacity", "premium_b": 0.04,
         "focus": "diversified",
         "hover": "World's largest reinsurer; HSB is its robotics/AI front line; publishes AV and robot-liability research. Est. robotics-attributable capacity."},
        {"company": "Swiss Re", "country": "CH", "strategy": "Reinsurance / capacity", "premium_b": 0.025,
         "focus": "diversified",
         "hover": "Warns insurers to treat autonomous AI like silent cyber; partnered with SAS for AI risk intelligence. Est."},
        {"company": "Hannover Re", "country": "DE", "strategy": "Reinsurance / capacity", "premium_b": 0.015,
         "focus": "diversified",
         "hover": "Third-largest reinsurer; active in specialty / technology risk. Est."},
        {"company": "SCOR", "country": "FR", "strategy": "Reinsurance / capacity", "premium_b": 0.01,
         "focus": "diversified",
         "hover": "French reinsurer engaging autonomous / AI specialty risk. Est."},
    ]

    _flag = {
        "US": "\U0001f1fa\U0001f1f8",
        "UK": "\U0001f1ec\U0001f1e7",
        "CH": "\U0001f1e8\U0001f1ed",
        "DE": "\U0001f1e9\U0001f1ea",
        "JP": "\U0001f1ef\U0001f1f5",
        "FR": "\U0001f1eb\U0001f1f7",
        "CA": "\U0001f1e8\U0001f1e6",
        "BM": "\U0001f1e7\U0001f1f2",
    }

    _root = "Robotics insurers"
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
        _p = float(_c["premium_b"])
        _total += _p
        _f = _flag.get(_c["country"], "")
        _focus_marker = "◆" if _c["focus"] == "specialist" else "◇"
        _lbl = f"{_focus_marker} {_c['company']} {_f}".strip()
        _focus_label = (
            "Robotics / autonomy specialist" if _c["focus"] == "specialist"
            else "Diversified (robots one line among many)"
        )

        _tm_labels.append(_lbl)
        _tm_parents.append(_c["strategy"])
        _tm_values.append(_p)
        _tm_customdata.append(
            "<b>{lbl}</b>"
            "<br>{focus_label}"
            "<br>Strategy: {strat}"
            "<br>Est. robotics-attributable premium: ${p:.3f}B"
            "<br>{hover}"
            "<extra></extra>".format(
                lbl=_lbl,
                focus_label=_focus_label,
                strat=_c["strategy"],
                p=_p,
                hover=_c["hover"],
            )
        )
        _tm_values[_strat_idx[_c["strategy"]]] += _p

    _tm_values[0] = _total

    treemap_fig = go.Figure(
        go.Treemap(
            labels=_tm_labels,
            parents=_tm_parents,
            values=_tm_values,
            branchvalues="total",
            customdata=_tm_customdata,
            hovertemplate="%{customdata}",
            texttemplate="<b>%{label}</b><br>${value:.3f}B",
        )
    )

    treemap_fig.update_layout(
        title="Robotics insurer strategy archetypes (2025 est., by robotics-attributable premium)<br><sup>◆ = Robotics / autonomy specialist | ◇ = Diversified insurer (robots are one line among many) | all values directional estimates</sup>",
        margin=dict(t=90, l=10, r=10, b=10),
    )

    treemap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Strategy-archetype notes (values are directional estimates of robotics-attributable premium, not reported GWP):

    Four ways companies compete for robot risk:

    1. Scale product-liability writers (AXA XL, Allianz Commercial, Chubb, AIG): They already insure most of the world's robot makers through general product-liability and life-sciences books. Robots are a fraction of their premium, but in aggregate this is where most robot risk is actually held. Two of them (Chubb, plus peers like Travelers and Berkshire Hathaway) are simultaneously filing to exclude AI claims from GL.
    2. Specialty and emerging-risk carriers (Munich Re / HSB, Global Aerospace, Tokio Marine Kiln, Relm, Zurich x YAS): They write explicit AI, drone/UAS or autonomous programs. This is the layer building robot-specific wordings from scratch, including embedded micro-insurance sold at the point of robot sale.
    3. Robotics-native insurtechs (Koop, SkyWatch.AI, Flock, Advanced Technology Assurance, Y-Risk, Axis): The only explicitly robot-branded offerings. Small premium, but they define the category and differentiate on telematics-based underwriting (robot black-box and drone telemetry data). They sit on Lloyd's syndicates and carrier capacity.
    4. Reinsurance / capacity (Munich Re, Swiss Re, Hannover Re, SCOR): The balance sheet and emerging-risk research behind the primary programs. Robot-branded treaties are rare; capacity flows through general specialty and technology lines.

    Where are the robot makers themselves? RaaS providers (Starship, Serve Robotics, Nuro, and AMR / humanoid vendors) retain ownership and bundle maintenance, software updates and SLA uptime guarantees (often 99-99.9%+), which shifts liability toward the manufacturer/operator rather than reselling a named third-party policy. That structure is exactly why robot risk concentrates in OEM and operator product-liability books instead of a robotics insurance line.
    """
    )
    return


@app.cell
def _(go):
    years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
    operational_stock_m = [2.44, 2.72, 3.02, 3.48, 3.90, 4.28, 4.66]
    annual_installs_k = [422, 373, 394, 517, 553, 541, 542]

    from plotly.subplots import make_subplots

    dual_fig = make_subplots(specs=[[{"secondary_y": True}]])

    dual_fig.add_trace(
        go.Bar(
            x=years,
            y=operational_stock_m,
            name="Operational stock (M units)",
            marker_color="steelblue",
            hovertemplate="<b>Operational stock</b><br>Year: %{x}<br>%{y:.2f}M robots<extra></extra>",
        ),
        secondary_y=False,
    )

    dual_fig.add_trace(
        go.Scatter(
            x=years,
            y=annual_installs_k,
            name="Annual installations (k units)",
            mode="lines+markers",
            line=dict(color="crimson", width=3),
            marker=dict(size=8),
            hovertemplate="<b>Annual installations</b><br>Year: %{x}<br>%{y}k robots<extra></extra>",
        ),
        secondary_y=True,
    )

    dual_fig.update_layout(
        title="The exposure base keeps compounding: industrial robot stock vs. annual installs (IFR, 2018-2024)",
        xaxis=dict(title="Year", type="category"),
        hovermode="x unified",
        margin=dict(t=70, l=50, r=50, b=40),
        legend=dict(x=0.01, y=0.99),
    )
    dual_fig.update_yaxes(title_text="Operational stock (million units)", secondary_y=False)
    dual_fig.update_yaxes(title_text="Annual installations (thousand units)", secondary_y=True)

    dual_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Exposure-base notes (source: IFR World Robotics 2025, reported data):
    - The operational stock of industrial robots nearly doubled from 2.44M (2018) to 4.66M (2024), a compounding liability base that grows every year regardless of how much of it is insured.
    - Annual installations have held above 500k for four straight years (2021-2024), so the stock keeps climbing even as yearly additions plateau.
    - These are industrial robots only. Professional service robots (~200k sold in 2024), medical/surgical robots (+91% to ~16,700 units in 2024), and the nascent humanoid class sit on top of this.
    - Unlike cyber, where the exposure is data and downtime, robotics exposure is physical: every one of these machines can cause bodily injury or property damage, which is why the underlying liability sits in product-liability and workers-comp lines.
    """
    )
    return


@app.cell
def _(go):
    sankey_labels = [
        "Human error / entry into robot envelope", "Control & software error",
        "AI / perception / navigation failure", "Mechanical / hardware failure",
        "Cyber compromise (remote takeover)", "Integration / third-party component",
        "Bodily injury (worker / bystander)", "Property damage",
        "Business interruption (line stoppage)", "Product recall (fleet OTA)",
        "Workers' compensation", "Product liability + CGL",
        "Professional liability / E&O", "Cyber / cyber-physical",
        "Business interruption cover",
    ]

    sankey_links = {
        "source": [
            0, 0, 0,
            1, 1, 1,
            2, 2, 2,
            3, 3,
            4, 4, 4,
            5, 5, 5,
            6, 6,
            7, 7,
            8, 8,
            9, 9,
        ],
        "target": [
            6, 7, 8,
            6, 8, 9,
            6, 7, 9,
            7, 8,
            6, 7, 13,
            7, 8, 9,
            10, 11,
            11, 12,
            14, 11,
            11, 12,
        ],
        "value": [
            14, 5, 4,
            6, 6, 4,
            8, 5, 5,
            6, 5,
            3, 3, 6,
            5, 4, 4,
            18, 9,
            12, 6,
            10, 6,
            5, 5,
        ],
    }

    _node_colors = (
        ["#4e79a7"] * 6 +
        ["#f28e2b"] * 4 +
        ["#59a14f"] * 5
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
        title="Failure vector → incident type → insurance line (directional flows)",
        margin=dict(t=70, l=30, r=30, b=30),
        height=600,
    )

    sankey_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Failure-to-claim flow notes:
    - Left column (blue): failure vectors, from the NIOSH / OSHA robot-hazard taxonomy. The dominant cause of serious industrial injury is a human entering the robot's envelope during maintenance or setup while the machine is energised, often compounded by lockout-tagout lapses, rather than a spontaneous hardware fault.
    - Middle column (orange): incident types. Bodily injury is the best-quantified outcome; business interruption (a software or sensor fault idling a fleet with no physical damage) and fleet-wide product recall (a software over-the-air push) are the emerging large-loss channels.
    - Right column (green): insurance lines. A single robot incident commonly triggers claims against three parties at once (hardware maker, software developer, operator), so a single event can hit workers-comp, product liability and E&O simultaneously, and causation/allocation is slow and expensive.
    - Flows are directional weights illustrating relative frequency of each path, not dollar values. Sources: OSHA STD 01-12-002, NIOSH, insurer/broker framing (Allianz, IMA, Founder Shield, Koop).
    """
    )
    return


@app.cell
def _(go):
    claim_timeline = [
        {"era": "Simple bodily-injury claim (settles early)", "avg_years": 1.0, "label": "~1 year"},
        {"era": "Typical robot product-liability suit", "avg_years": 2.9, "label": "~2.9 years"},
        {"era": "Complex multi-defendant robot / AI case", "avg_years": 4.5, "label": "4-5 years"},
    ]

    _eras = [d["era"] for d in claim_timeline]
    _years_val = [d["avg_years"] for d in claim_timeline]
    _bar_labels = [d["label"] for d in claim_timeline]

    claim_fig = go.Figure(
        go.Bar(
            y=_eras,
            x=_years_val,
            orientation="h",
            marker_color=["#59a14f", "#f28e2b", "#e15759"],
            text=_bar_labels,
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Avg resolution: %{x:.1f} years<extra></extra>",
        )
    )

    claim_fig.update_layout(
        title="Robot liability claims are long-tail: time to resolution (years)",
        xaxis=dict(title="Years to resolution", range=[0, 6]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=280, r=80, b=40),
        height=320,
    )

    claim_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Claim-timeline notes:
    - Product-liability trials have the longest processing time of all US tort trials, ~35.1 months (~2.9 years) on average (US DOJ / BJS civil-trial data), and only ~3% of tort cases reach a verdict, so most settle earlier.
    - Robot cases fit the complex profile: they need engineering and software experts, and liability is contested across multiple defendants. Discovery alone runs 6 months to 2 years.
    - Realised cases show the tail: the Wanda Holbrook fatality ran from a 2015 incident to a mid-trial settlement two years later; da Vinci mass-tort claims spanned 2012-2016+.
    - Practical consequence for reserving: robot bodily-injury and product-liability claims are commonly 2-5 years from incident to resolution, with heavy expert-cost loading, so today's thin pricing will only show its true loss picture years from now.
    """
    )
    return


@app.cell
def _(go):
    systemic_events = [
        {
            "event": "da Vinci surgical-robot litigation (2012-16)",
            "modeled_loss_b": 0.10,
            "note": ">3,000 claims; Intuitive reserved ~$67M (2014). FDA MAUDE 2000-13: 144 deaths, 1,391 injuries, 8,061 malfunctions.",
            "kind": "realised",
        },
        {
            "event": "Cruise pedestrian dragging (2023)",
            "modeled_loss_b": 0.05,
            "note": "$0.5M DOJ + $1.5M NHTSA fines + confidential settlement; robotaxi unit wound down. Software mis-classified the crash.",
            "kind": "realised",
        },
        {
            "event": "Amazon robotic-FC worker injuries (2021)",
            "modeled_loss_b": 0.30,
            "note": "Serious-injury rate 7.9 / 100 workers at robotic facilities (~54% above non-robotic). >34,000 serious injuries (2021). Flows into workers' comp.",
            "kind": "realised",
        },
        {
            "event": "Robotaxi fleet OTA recall (Waymo/Zoox 2024-26)",
            "modeled_loss_b": 0.15,
            "note": "Software recalls of 1,212 / 3,871 (Waymo) and 258 (Zoox) identical vehicles at once. Precedent for fleet-wide correlated action.",
            "kind": "realised",
        },
        {
            "event": "Hypothetical: shared AI-model or OTA flaw\nacross a humanoid / AMR fleet",
            "modeled_loss_b": 5.0,
            "note": "One defective model, update or component simultaneously drives unsafe behaviour across thousands of identical robots. Modeled, no public dollar scenario exists.",
            "kind": "modeled",
        },
    ]

    _events = [e["event"] for e in systemic_events]
    _loss = [e["modeled_loss_b"] for e in systemic_events]
    _colors = ["#4e79a7" if e["kind"] == "realised" else "#e15759" for e in systemic_events]
    _hovers = [
        f"<b>{e['event']}</b><br>{e['note']}<br>Illustrative loss scale: ${e['modeled_loss_b']:.2f}B"
        for e in systemic_events
    ]

    systemic_fig = go.Figure(
        go.Bar(
            y=_events,
            x=_loss,
            orientation="h",
            marker_color=_colors,
            customdata=_hovers,
            hovertemplate="%{customdata}<extra></extra>",
            text=[f"${v:.2f}B" for v in _loss],
            textposition="outside",
        )
    )

    systemic_fig.add_shape(
        type="line", x0=0.5, x1=0.5, y0=-0.5, y1=4.5,
        line=dict(color="black", width=2, dash="dash"),
    )
    systemic_fig.add_annotation(
        x=0.5, y=4.5,
        text="← Est. total annual dedicated<br>    robotics premium (~$0.5B)",
        showarrow=False,
        font=dict(size=11),
        xanchor="left",
    )

    systemic_fig.update_layout(
        title="Robotics loss events: realised (blue) vs. modeled fleet-wide tail (red), illustrative USD billions",
        xaxis=dict(title="Illustrative loss scale (USD billions)", range=[0, 6]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=300, r=60, b=50),
        height=460,
    )

    systemic_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Systemic-risk notes (realised events carry reported figures; the fleet-wide scenario is modeled, not booked):
    - The realised events are drawn from reported data: Intuitive's ~\$67M da Vinci litigation reserve, Cruise's ~\$2M in fines plus a confidential settlement, Amazon's robotic-facility injury rate of 7.9 per 100 workers, and the robotaxi software recalls of 1,212 / 3,871 / 258 identical vehicles.
    - The robotaxi recalls are the key precedent: a single software version with a single defect produced simultaneous fleet-wide action. That is the robotics version of correlated loss.
    - The hypothetical fleet event is the robotics analogue of a cyber hurricane: one AI model, over-the-air update or shared component defect drives unsafe behaviour across thousands of identical robots at once, defeating the law of large numbers that ordinary insurance relies on. EY (2026) argues physical AI may disrupt insurers more than generative AI for exactly this reason.
    - No public dollar-denominated accumulation scenario specific to a robot fleet exists yet, which is itself a warning: the tail is unmodeled. The dashed line marks estimated total annual dedicated robotics premium (~\$0.5B) for scale; a single correlated fleet event would dwarf it.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Structural observations

    1. The market is silent, not absent. Most robot risk is real and insured, just not under a robotics label. It sits inside the product-liability, CGL, workers-comp and cyber books of AXA XL, Allianz, Chubb and AIG. That makes the true size unmeasurable and the pricing untested against robot-specific loss experience.

    2. Coverage is contracting as exposure grows. New ISO endorsements (CG 40 47 / CG 40 48, effective Jan 2026) let carriers strip AI-related claims from standard GL, and regulators approved >80% of the AI-exclusion filings from Berkshire Hathaway, Chubb and Travelers. Just as robots proliferate, the standard policies that silently covered them are carving out the autonomy.

    3. Hybrid losses defeat clean underwriting. A single robot incident can combine a defective component, a flawed AI decision, a cyber takeover and operator error, and can trigger claims against the hardware maker, the software developer and the operator at once. Liability allocation is slow, expensive and legally unsettled.

    4. The insurtechs define the category but not the premium. Koop, SkyWatch, Flock, ATA, Axis and Y-Risk are the only explicitly robot-branded writers, differentiating on telematics-based underwriting, but their combined premium is a rounding error next to the silent exposure in general commercial lines.

    5. Long-tail reserving problem. Robot bodily-injury and product-liability claims run 2-5 years to resolution with heavy expert costs. Any pricing set today on thin data will only reveal its true loss picture years later, exactly the dynamic that burned early cyber writers.

    6. Systemic fleet risk is unmodeled. Identical robots running identical software are correlated by construction. The robotaxi OTA recalls already demonstrate simultaneous fleet-wide action, yet no public accumulation scenario in dollars exists for a robot-fleet catastrophe. The capacity to absorb it does not visibly exist either.

    7. RaaS concentrates the risk. Because Robotics-as-a-Service providers retain ownership and bundle uptime guarantees, liability flows to a small number of operators and manufacturers rather than being diffused across end users, concentrating both the exposure and the eventual claims.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    # Appendix
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## A. Why robotics insurance is mostly invisible

    Cyber insurance became a distinct, expert-priced peril class because a single regulator (Lloyd's, 2019-2021) forced every participant to affirm or exclude cyber, dragging silent risk into the open. Robotics is moving in the opposite direction. There is no mandate to affirmatively price robot risk, and the standard-lines machinery is actively carving autonomy out rather than in.

    The mechanics of the invisibility:

    - No reported line. No regulator or rating bureau breaks out a robotics premium, so the risk cannot be measured, only inferred from product-liability, workers-comp and cyber books.
    - Silent by default, excluded by design. Robot risk rode inside general policies for years. Now the ISO AI-exclusion endorsements (CG 40 47 / CG 40 48, Jan 2026) and carrier filings (Berkshire Hathaway, Chubb, Travelers, >80% approved) are removing it, leaving a widening gap that specialty carriers have only begun to fill.
    - Hybrid, multi-defendant losses. A robot incident does not respect policy boundaries: it can be at once a product defect, an AI error, a cyber event and a workplace injury, contested across OEM, integrator and operator.
    - Emerging, fragmented supply. The genuinely robot-branded market is a handful of insurtechs (Koop, SkyWatch, Flock, ATA, Axis, Y-Risk) sitting on Lloyd's and specialty-carrier capacity (Global Aerospace, Tokio Marine Kiln, The Hartford), plus new AI-liability products from Munich Re / HSB and Relm.

    The uncomfortable implication: the fastest-growing physical-capital and physical-liability base in the economy is being insured by policies that were written before autonomous machines existed, and those policies are now being amended to exclude exactly the autonomy that makes robots risky.
    """
    )
    return


@app.cell
def _(go, mo):
    from plotly.subplots import make_subplots as _make_subplots_gaps

    _gap_categories = [
        "Humanoid robots",
        "Fleet-wide systemic / correlated risk",
        "Cyber-physical (robot takeover → harm)",
        "Autonomous AI decision (E&O)",
        "Delivery robots / drones",
        "RaaS operator liability",
        "Surgical / medical robots",
        "Industrial robots (product liab.)",
    ]

    # Directional estimates of exposure vs. explicitly-insured, USD billions
    _total_exposure = [40, 80, 30, 50, 3, 20, 30, 375]
    _currently_covered = [0.02, 0.0, 0.05, 0.1, 0.6, 0.3, 2.0, 15.0]

    _coverage_pct = [
        round(c / t * 100, 2) if t > 0 else 0
        for c, t in zip(_currently_covered, _total_exposure)
    ]

    _gap_fig = _make_subplots_gaps(
        rows=1,
        cols=2,
        column_widths=[0.55, 0.45],
        subplot_titles=(
            "Exposure vs. explicitly insured (est., USD billions, log scale)",
            "Coverage ratio (% of exposure explicitly insured)",
        ),
        horizontal_spacing=0.15,
    )

    _gap_fig.add_trace(
        go.Bar(
            y=_gap_categories,
            x=_total_exposure,
            orientation="h",
            name="Total exposure / addressable (est.)",
            marker_color="#d62728",
            opacity=0.7,
            hovertemplate="<b>%{y}</b><br>Exposure: $%{x:,.0f}B<extra></extra>",
        ),
        row=1,
        col=1,
    )
    _gap_fig.add_trace(
        go.Bar(
            y=_gap_categories,
            x=[max(c, 0.01) for c in _currently_covered],
            orientation="h",
            name="Explicitly insured (est.)",
            marker_color="#2ca02c",
            hovertemplate="<b>%{y}</b><br>Explicitly insured: $%{x:,.2f}B<extra></extra>",
        ),
        row=1,
        col=1,
    )

    _bar_colors = [
        "#d62728" if p < 2 else "#ff7f0e" if p < 8 else "#2ca02c"
        for p in _coverage_pct
    ]
    _gap_fig.add_trace(
        go.Bar(
            y=_gap_categories,
            x=_coverage_pct,
            orientation="h",
            name="Coverage ratio",
            marker_color=_bar_colors,
            text=[f"{p:.2f}%" if p < 1 else f"{p:.1f}%" for p in _coverage_pct],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Coverage ratio: %{x:.2f}%<extra></extra>",
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    _gap_fig.update_xaxes(type="log", title_text="USD billions (log scale)", row=1, col=1)
    _gap_fig.update_xaxes(title_text="% explicitly insured", range=[0, 12], row=1, col=2)
    _gap_fig.update_yaxes(autorange="reversed", row=1, col=1)
    _gap_fig.update_yaxes(autorange="reversed", row=1, col=2)

    _gap_fig.update_layout(
        title="Robotics coverage gaps: exposure vs. explicit cover by segment (directional estimates)",
        barmode="overlay",
        height=560,
        margin=dict(t=90, l=250, r=40, b=50),
        legend=dict(x=0.0, y=-0.15, orientation="h"),
    )

    mo.ui.plotly(_gap_fig)
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## B. Where are the market gaps?

    The chart above maps eight robotics coverage gaps. Left panel shows estimated total exposure (red) vs. amount explicitly insured (green) on a log scale; right panel shows the explicit-coverage ratio. Every figure is a directional estimate, since no measured robotics coverage data exists.

    Key gaps:

    1. Industrial robots (~\$375B deployed capital, most covered only as silent product liability). The largest exposure by far, but almost none of it is insured under a robotics label. The product-liability books carrying it were not priced against robot-specific loss experience.

    2. Fleet-wide systemic / correlated risk (~\$80B modeled, ~\$0 explicitly covered). Identical robots on identical software are correlated by construction. There is no cyber-cat-bond equivalent for robotics and no public accumulation model, so the tail is effectively uninsured.

    3. Cyber-physical (robot takeover leading to physical harm, ~\$30B exposure, thinly covered). Standard cyber policies are data-focused and generally exclude physical harm; standard property/liability excludes cyber causation. Robot takeover falls in the seam between them.

    4. Autonomous AI decision / E&O (~\$50B emerging exposure, minimal cover). When an autonomous system makes a bad decision, is it a product defect or a professional error? The ISO AI exclusions are removing this from GL faster than specialty E&O is picking it up.

    5. Surgical / medical robots (~\$30B, partly covered). The best-quantified harm data (FDA MAUDE) sits here, and life-sciences liability carriers write the OEMs, but per-procedure adverse events scale with volume as robotic surgery grows.

    6. RaaS operator liability (~\$20B, thinly covered). Fast-growing and concentrated: operators own fleets deployed at customer sites and need E&O plus GL plus property, exactly the cover the new insurtechs target but at small scale.

    7. Delivery robots / drones (~\$3B, relatively best-covered small segment). The one place with mature specialty supply (SkyWatch, Flock, Global Aerospace) and on-demand telematics-priced products, precisely because aviation/UAS regulation forced explicit cover.

    8. Humanoid robots (~\$40B projected exposure, ~\$0 explicit cover). Goldman Sachs projects a ~\$38B humanoid market by 2035. General-purpose robots operating in human spaces are the largest coming exposure and the least covered, with only early products (HSB AI liability, Koop's autonomy brand) in sight.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    Sources and caveats: IFR World Robotics 2025 (robot stock and installations, reported); Goldman Sachs (humanoid forecast); OSHA STD 01-12-002 and NIOSH (robot-hazard taxonomy and industrial injury/fatality counts); ScienceDirect / Applied Ergonomics 2024 (77 OSHA robot accidents, 2015-2022); FDA MAUDE and Journal of Robotic Surgery (da Vinci adverse events); NHTSA (Cruise, Waymo, Zoox recalls and penalties); US DOJ / BJS (product-liability trial durations); Strategic Organizing Center (Amazon injury rates); EY, PYMNTS, Coalition, IMA and Founder Shield (physical-AI and robotics underwriting commentary); Koop Technologies, SkyWatch.AI, Flock, Advanced Technology Assurance, Munich Re / HSB, Relm and Zurich / YAS (company releases). Market-size figures from market.us, marketintelo, growthmarketreports, dataintelo and QYResearch are third-party syndicated estimates with undisclosed methodology and are presented as ranges, not facts. All premium, exposure and coverage-ratio figures for robotics are directional estimates: there is no regulator-reported robotics insurance line, so numbers should be read as scale markers rather than measured values.
    """
    )
    return


if __name__ == "__main__":
    app.run()
