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
    # Only 0.17% of cyber economic losses are insured.

    Cybercrime costs the global economy ~\$9.5 trillion per year. The entire cyber insurance industry collects \$16.5 billion in premiums and pays out ~\$8.3 billion in claims. That is 0.09% of the damage it is meant to cover.

    ---

    ## Cyber Insurance Industry Deep Dive (2025)
    - Global cyber insurance market: ~\$16.5B GWP (2025). Consensus: Munich Re \$16.3B, Swiss Re \$15.6B, Gallagher Re \$16.9B.
    - US market: ~\$12.4B DWP (+11% YoY rebound after two years of decline).
    - Sits at the intersection of the ~\$9.3T global insurance industry and ~\$212B cybersecurity spend.
    - Market in deep soft cycle: 10 consecutive quarters of rate decline, reinsurance down -32% at Jan 1, 2026 renewals.
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    cost_stack = [
        {"label": "Cybercrime economic cost", "value_b": 9500, "color": "#e15759"},
        {"label": "Cybersecurity spend (prevention)", "value_b": 212, "color": "#4e79a7"},
        {"label": "Cyber insurance premiums", "value_b": 16.5, "color": "#f28e2b"},
        {"label": "Insurance claims actually paid", "value_b": 8.3, "color": "#59a14f"},
    ]

    gap_fig = go.Figure()

    gap_fig.add_trace(
        go.Bar(
            y=[d["label"] for d in cost_stack],
            x=[d["value_b"] for d in cost_stack],
            orientation="h",
            marker_color=[d["color"] for d in cost_stack],
            text=[
                f"${d['value_b']:,.0f}B" if d["value_b"] >= 100
                else f"${d['value_b']:.1f}B"
                for d in cost_stack
            ],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>$%{x:,.1f}B<extra></extra>",
        )
    )

    gap_fig.add_annotation(
        x=9500, y="Cyber insurance premiums",
        text="<b>Only 0.17% of cyber economic losses are insured</b>",
        showarrow=True, arrowhead=2,
        ax=-120, ay=-40,
        font=dict(size=13, color="#e15759"),
    )

    gap_fig.update_layout(
        title="The cyber protection gap: economic cost vs. what's insured (2025, USD billions, log scale)",
        xaxis=dict(
            title="USD billions (log scale)",
            type="log",
            range=[0.5, 4.2],
        ),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=280, r=80, b=50),
        height=350,
    )

    gap_fig
    return


@app.cell
def _(go):
    target_years = ["2024", "2025", "2030 low", "2030 high"]
    target_values = [15.3, 16.5, 30, 50]
    target_colors = ["#4e79a7", "#4e79a7", "#f28e2b", "#e15759"]
    target_sources = [
        "Munich Re (actual)",
        "Consensus estimate",
        "Gallagher Re target",
        "Howden / Munich Re target",
    ]

    target_fig = go.Figure(
        go.Bar(
            x=target_years,
            y=target_values,
            marker_color=target_colors,
            text=[f"${v:.0f}B" if v >= 30 else f"${v:.1f}B" for v in target_values],
            textposition="outside",
            customdata=target_sources,
            hovertemplate="<b>%{x}</b><br>$%{y:.1f}B<br>%{customdata}<extra></extra>",
        )
    )

    target_fig.update_layout(
        title="Cyber insurance market: where it is vs. where it needs to be",
        xaxis=dict(title="", type="category"),
        yaxis=dict(title="Global GWP (USD billions)", range=[0, 58]),
        margin=dict(t=70, l=60, r=40, b=40),
        height=350,
    )

    target_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Protection gap notes:
    - Global cybercrime economic cost is estimated at \$9.5T in 2025 (Cybersecurity Ventures), encompassing direct losses, business disruption, stolen IP, reputational damage, and recovery costs.
    - The \$212B cybersecurity spend is the prevention layer — what companies pay to stop attacks.
    - Cyber insurance premiums (\$16.5B) are only 0.17% of the economic cost they're meant to cover. Actual claims paid (~\$8.3B, implied by ~50% loss ratio) represent 0.09%.
    - Munich Re, Swiss Re, and Howden project the market needs to reach \$30-50B by 2030 to begin closing the gap. Even at \$50B, the insured fraction would be <0.5% of projected cybercrime costs.
    - The protection gap is widest for SMEs (10-20% penetration) and emerging markets (APAC = ~10% of global cyber premium).
    """
    )
    return


@app.cell
def _(go):
    coverage_data = [
        {"segment": "Standalone cyber", "value_billion": 9.0},
        {"segment": "Cyber endorsements / packaged", "value_billion": 4.5},
        {"segment": "Tech E&O + cyber blended", "value_billion": 3.0},
    ]

    cov_labels = [d["segment"] for d in coverage_data]
    cov_values = [d["value_billion"] for d in coverage_data]

    cov_fig = go.Figure(
        data=[
            go.Pie(
                labels=cov_labels,
                values=cov_values,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.1f}B<br><extra></extra>",
            )
        ]
    )

    cov_fig.update_layout(
        title="Cyber insurance by coverage type (2025, USD billions)",
        annotations=[
            dict(text="~$16.5B", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
    )

    cov_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Coverage type notes:
    - Standalone cyber is 54-59% of the total market and growing as Lloyd's mandated affirmative-only cyber since Jan 1, 2025.
    - Tech E&O + cyber blended is the largest claim area by value — errors and omissions disputes drag on for years.
    - Endorsements (cyber bolted onto a BOP or GL policy) have a remarkably low ~10% loss ratio vs ~49% for primary standalone, because endorsement sub-limits are small and rarely triggered.
    """
    )
    return


@app.cell
def _(go):
    buyer_data = [
        {"segment": "Large enterprise (>$1B rev)", "value_billion": 8.9},
        {"segment": "Mid-market ($100M-$1B)", "value_billion": 4.3},
        {"segment": "SME ($10M-$100M)", "value_billion": 2.5},
        {"segment": "Micro / small (<$10M)", "value_billion": 0.8},
    ]

    buyer_labels = [d["segment"] for d in buyer_data]
    buyer_values = [d["value_billion"] for d in buyer_data]

    buyer_fig = go.Figure(
        data=[
            go.Pie(
                labels=buyer_labels,
                values=buyer_values,
                hole=0.4,
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>Market Size: $%{value:.1f}B<br><extra></extra>",
            )
        ]
    )

    buyer_fig.update_layout(
        title="Cyber insurance by buyer segment (2025 est., USD billions)",
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
    Buyer segmentation notes:
    - Large enterprise penetration is estimated at 60-80% — most Fortune 500 companies buy cyber cover.
    - SME penetration is only 10-20% but growing at 29%+ CAGR. This is where insurtechs like Coalition and Cowbell compete with automated underwriting and free security scanning tools.
    - Enterprise segment is where Trium Cyber, Beazley, and traditional carriers dominate with bespoke manuscript policies and high attachment points.
    - The micro/small segment (<\$10M revenue) is largely untouched — policies are too small for manual underwriting economics, creating an opening for fully automated platforms.
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
    _nodes_path = _base_dir / "data" / "cyber_insurance_nodes.json"

    if not _nodes_path.exists():
        raise FileNotFoundError(f"Cyber insurance nodes file not found at {_nodes_path}")

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
        title="Cyber insurance market map — 2025 GWP (USD billions)",
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
    - Root anchors to ~\$16.5B global cyber insurance GWP (2025), split into four branches: Carriers, MGAs/Insurtechs, Reinsurers, and Brokers & adjacent services.
    - MGAs originate an estimated ~33% of total cyber GWP (including premium written on carrier paper via delegated authority), though the icicle shows only MGA-retained GWP at \$3.2B (19%). They are the innovation layer.
    - Trium Cyber stands out: zero claims across 375 policies over 3 years. Hyper-selective underwriting targeting \$100M-\$1B+ revenue companies with strong security postures.
    - Beazley is among the largest cyber insurers by absolute GWP (~\$1.2B, ~15,000 policies), though cyber is 21% of its total book — Property and Specialty are each larger segments. AIG writes a comparable or larger cyber book (\$1.2-1.6B range). Zurich agreed to acquire Beazley in early 2026; deal pending regulatory approval.
    - Brokers & adjacent services include pre-breach scanning (SecurityScorecard, BitSight), incident response panels (CrowdStrike, Mandiant), and claims management.
    """
    )
    return


@app.cell
def _(go):
    # focus: "specialist" = cyber is core/majority of business
    #        "diversified" = cyber is one line among many
    strategy_companies = [
        {"company": "Beazley", "country": "UK", "strategy": "Scale / mass writers", "premium_b": 1.20,
         "focus": "diversified", "cyber_pct": 21,
         "hover": "~15,000 policies. Buying SOC companies. Going for volume over selectivity. Cyber is 21% of total GWP — Property and Specialty are each larger segments."},
        {"company": "Chubb", "country": "CH", "strategy": "Scale / mass writers", "premium_b": 1.05,
         "focus": "diversified", "cyber_pct": 2.5,
         "hover": "~6% global cyber market share. Cyber is ~2.5% of total P&C premiums (~$42B). Massive multi-line group."},
        {"company": "AIG", "country": "US", "strategy": "Scale / mass writers", "premium_b": 1.40,
         "focus": "diversified", "cyber_pct": 5.6,
         "hover": "$1.2-1.6B range. Cyber is ~5.6% of ~$25B net premiums. Global commercial/personal/life insurer."},
        {"company": "Travelers", "country": "US", "strategy": "Scale / mass writers", "premium_b": 0.90,
         "focus": "diversified", "cyber_pct": 2.2,
         "hover": "US DWP $467M (+43.5%). Acquired Corvus for $435M. Cyber is ~2.2% of ~$41B total premiums."},
        {"company": "Trium Cyber", "country": "UK", "strategy": "Technical underwriters", "premium_b": 0.10,
         "focus": "specialist", "cyber_pct": 100,
         "hover": "First Lloyd's-approved mono-line cyber syndicate (1322). 100% cyber. £73M premium, 375 policies, ZERO claims in 3 years."},
        {"company": "Hiscox", "country": "UK", "strategy": "Technical underwriters", "premium_b": 0.38,
         "focus": "diversified", "cyber_pct": 7.5,
         "hover": "Cyber is ~7-8% of ~$5B GWP. Specialty Lloyd's carrier also writing property, casualty, marine, D&O, K&R. Actively managing down cyber as rates fall."},
        {"company": "QBE", "country": "AU", "strategy": "Technical underwriters", "premium_b": 0.30,
         "focus": "diversified", "cyber_pct": 1.5,
         "hover": "Cyber is ~1.5% of ~$20B GWP. Global multi-line insurer covering property, motor, marine, crop, liability."},
        {"company": "Brit", "country": "UK", "strategy": "Technical underwriters", "premium_b": 0.25,
         "focus": "diversified", "cyber_pct": 7,
         "hover": "Cyber is ~7% of ~$3.5B GWP. Lloyd's syndicate also writing property, energy, marine, aviation, casualty."},
        {"company": "Coalition", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.85,
         "focus": "specialist", "cyber_pct": 85,
         "hover": "~80-85% cyber. Also writes Tech E&O and Executive Risks as cyber-adjacent add-ons. Free scanning/monitoring for policyholders."},
        {"company": "At-Bay", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.35,
         "focus": "specialist", "cyber_pct": 95,
         "hover": "~95%+ cyber. US DWP $281M (+345% YoY!). Purpose-built cyber MGA with integrated MDR platform. Exited admitted cyber in 2025."},
        {"company": "Cowbell", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.20,
         "focus": "specialist", "cyber_pct": 90,
         "hover": "~90%+ cyber. Founded cyber-only; began adding D&O/EPL via Zurich partnership mid-2025. SMB-focused continuous underwriting."},
        {"company": "Resilience", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.25,
         "focus": "specialist", "cyber_pct": 95,
         "hover": "~95%+ cyber. Founded by ex-US intelligence/military. 48% European GWP growth. MGA of the Year 2025. Recently added Tech E&O in UK."},
        {"company": "Elpha Secure", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.10,
         "focus": "specialist", "cyber_pct": 100,
         "hover": "100% cyber. Early stage MGA bundling proprietary cybersecurity software with every policy. SentinelOne partnership."},
        {"company": "Stoik", "country": "FR", "strategy": "Insurtech + bundled security", "premium_b": 0.055,
         "focus": "specialist", "cyber_pct": 100,
         "hover": "100% cyber. Europe's first dedicated cyber MGA for SMEs. ~EUR 50M GWP, 200%+ YoY growth, 10K+ businesses. Bundled MDR with every policy."},
        {"company": "Measured Analytics", "country": "US", "strategy": "Insurtech + bundled security", "premium_b": 0.07,
         "focus": "specialist", "cyber_pct": 100,
         "hover": "100% cyber. AI-powered MGA using SecurityScorecard + Tenable data. SCOR/Canopius capacity. US SME focus."},
        {"company": "Mosaic", "country": "UK", "strategy": "Technical underwriters", "premium_b": 0.15,
         "focus": "diversified", "cyber_pct": 25,
         "hover": "Cyber is ~20-30% of book. London-based specialty MGA (Syndicate 1609) writing 7 lines: cyber, transactional liability, political risk, political violence, environmental, FI, professional liability."},
        {"company": "Munich Re", "country": "DE", "strategy": "Reinsurance / capacity", "premium_b": 1.75,
         "focus": "diversified", "cyber_pct": 5.4,
         "hover": "Largest cyber reinsurer globally. Cyber is ~5.4% of ~$32.6B total reinsurance premiums."},
        {"company": "Swiss Re", "country": "CH", "strategy": "Reinsurance / capacity", "premium_b": 1.30,
         "focus": "diversified", "cyber_pct": 3.6,
         "hover": "Cyber is ~3.6% of ~$36.2B total reinsurance premiums."},
        {"company": "Hannover Re", "country": "DE", "strategy": "Reinsurance / capacity", "premium_b": 0.45,
         "focus": "diversified", "cyber_pct": 1.6,
         "hover": "Cyber is ~1.6% of ~$27.5B total reinsurance. Created dedicated cyber unit April 2024. Issued cyber cat bond renewal 2025."},
    ]

    _flag = {
        "US": "\U0001f1fa\U0001f1f8",
        "UK": "\U0001f1ec\U0001f1e7",
        "CH": "\U0001f1e8\U0001f1ed",
        "DE": "\U0001f1e9\U0001f1ea",
        "AU": "\U0001f1e6\U0001f1fa",
        "FR": "\U0001f1eb\U0001f1f7",
    }

    _root = "Cyber insurers"
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
        _focus_label = "Cyber specialist" if _c["focus"] == "specialist" else "Diversified insurer"

        _tm_labels.append(_lbl)
        _tm_parents.append(_c["strategy"])
        _tm_values.append(_p)
        _tm_customdata.append(
            "<b>{lbl}</b>"
            "<br>{focus_label} (cyber = {cyber_pct}% of total)"
            "<br>Strategy: {strat}"
            "<br>Premium: ${p:.2f}B"
            "<br>{hover}"
            "<extra></extra>".format(
                lbl=_lbl,
                focus_label=_focus_label,
                cyber_pct=_c["cyber_pct"],
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
            texttemplate="<b>%{label}</b><br>$%{value:.2f}B",
        )
    )

    treemap_fig.update_layout(
        title="Cyber insurer strategy archetypes (2025, by premium volume)<br><sup>◆ = Cyber specialist | ◇ = Diversified insurer (cyber is one line among many)</sup>",
        margin=dict(t=90, l=10, r=10, b=10),
    )

    treemap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Strategy archetype notes:

    The traditional Carrier vs. MGA distinction matters less than HOW each company competes:

    1. Scale / mass writers (Beazley, Chubb, AIG, Travelers): Optimize for volume, broad appetite, large books. Beazley writes ~15,000 policies — a fundamentally different business than a 375-policy book. Risk: correlated loss in a soft market.
    2. Technical underwriters (Trium Cyber, Hiscox, QBE, Brit): Selective, deep-diligence approach. Trium's zero-claims track record across 375 policies is the extreme end. These carriers win on underwriting margin, not premium volume.
    3. Insurtech + bundled security (Coalition, At-Bay, Cowbell, Resilience, Stoik, Measured, Elpha Secure): The "InsurSec" segment — ~\$1.5-2B in combined GWP. They differentiate by bundling free security scanning, monitoring, and tooling with policies. Loss prevention as competitive moat. At-Bay's +345% YoY growth shows this model scales fast in SME. Stoik is the European equivalent (~EUR 50M, 200%+ YoY).
    4. Reinsurance / capacity (Munich Re, Swiss Re, Hannover Re): Provide the balance sheet behind all of the above. Reinsurance rates fell -32% at Jan 1, 2026 renewals — capacity is abundant but pricing discipline is eroding.

    Where are traditional security vendors? CrowdStrike, SentinelOne, Palo Alto, Sophos, and Arctic Wolf do NOT originate premium. They provide data/services to insurers: CrowdStrike runs "Falcon for Insurability" (6 carrier partners), SentinelOne has its Risk Assurance Initiative, Unit 42 sits on 70+ insurer IR panels, and Arctic Wolf is Chubb's preferred MDR provider. These programs drive platform subscriptions, not insurance revenue. The security vendor ecosystem earns an estimated \$3-5B/year from insurance-adjacent activities (mostly IR panel fees), but none of it is premium. The closest a traditional vendor has come is Trend Micro's exclusive partnership with Invision Cyber MGA (Sept 2025), where Trend Micro telemetry drives underwriting — but Invision writes the policies. The reverse movement is equally notable: Beazley (insurer) launched Beazley Security as a standalone 176-person cybersecurity company.
    """
    )
    return


@app.cell
def _(go):
    years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
    global_gwp_b = [4.0, 5.5, 7.5, 11.5, 13.5, 15.3, 16.5]
    us_loss_ratio_pct = [47, 67, 72, 55, 43, 49, 51]

    from plotly.subplots import make_subplots

    dual_fig = make_subplots(specs=[[{"secondary_y": True}]])

    dual_fig.add_trace(
        go.Bar(
            x=years,
            y=global_gwp_b,
            name="Global GWP ($B)",
            marker_color="steelblue",
            hovertemplate="<b>Global GWP</b><br>Year: %{x}<br>$%{y:.1f}B<extra></extra>",
        ),
        secondary_y=False,
    )

    dual_fig.add_trace(
        go.Scatter(
            x=years,
            y=us_loss_ratio_pct,
            name="US loss ratio (%)",
            mode="lines+markers",
            line=dict(color="crimson", width=3),
            marker=dict(size=8),
            hovertemplate="<b>US Loss Ratio</b><br>Year: %{x}<br>%{y}%<extra></extra>",
        ),
        secondary_y=True,
    )

    dual_fig.update_layout(
        title="Cyber insurance premium growth vs. loss ratios (2019-2025)",
        xaxis=dict(title="Year", type="category"),
        hovermode="x unified",
        margin=dict(t=70, l=50, r=50, b=40),
        legend=dict(x=0.01, y=0.99),
    )
    dual_fig.update_yaxes(title_text="Global GWP (USD billions)", secondary_y=False)
    dual_fig.update_yaxes(title_text="US loss ratio (%)", secondary_y=True)

    dual_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Premium growth vs. loss ratio notes:
    - The 2020-2021 ransomware crisis (Colonial Pipeline, Kaseya, JBS) pushed US loss ratios above 70%, triggering the hard market.
    - Hard-market re-pricing in 2022 compressed loss ratios back to ~55%, then further to ~43% in 2023 as rates kept rising while claims stabilized.
    - Now rates are softening (10 consecutive quarters of decline) while loss ratios are ticking back up to ~51%. S&P forecasts 15-20% premium rate increases in 2026 to correct the cycle.
    - The 4x premium growth from 2019 (\$4B) to 2025 (\$16.5B) reflects both rate increases and new buyer adoption, not just volume.
    """
    )
    return


@app.cell
def _(go):
    rate_data = [
        {"period": "Q1 2022", "rate_change": 15},
        {"period": "Q2 2022", "rate_change": 10},
        {"period": "Q3 2022", "rate_change": 5},
        {"period": "Q4 2022", "rate_change": 2},
        {"period": "Q1 2023", "rate_change": -3},
        {"period": "Q2 2023", "rate_change": -6},
        {"period": "Q3 2023", "rate_change": -8},
        {"period": "Q4 2023", "rate_change": -10},
        {"period": "Q1 2024", "rate_change": -9},
        {"period": "Q2 2024", "rate_change": -8},
        {"period": "Q3 2024", "rate_change": -7},
        {"period": "Q4 2024", "rate_change": -5},
        {"period": "Q1 2025", "rate_change": -7},
        {"period": "Q2 2025", "rate_change": -7},
    ]

    _periods = [d["period"] for d in rate_data]
    _changes = [d["rate_change"] for d in rate_data]
    _colors = ["green" if v >= 0 else "crimson" for v in _changes]

    rate_fig = go.Figure(
        go.Bar(
            y=_periods,
            x=_changes,
            orientation="h",
            marker_color=_colors,
            hovertemplate="<b>%{y}</b><br>Rate change: %{x:+d}%<extra></extra>",
            text=[f"{v:+d}%" for v in _changes],
            textposition="outside",
        )
    )

    rate_fig.update_layout(
        title="Cyber insurance rate-on-line changes (quarterly, %)",
        xaxis=dict(title="Rate change (%)", zeroline=True, zerolinewidth=2, zerolinecolor="grey"),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=100, r=60, b=40),
        height=500,
    )

    rate_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Rate cycle notes:
    - Green bars = hard market (rates rising), red bars = soft market (rates falling).
    - 10 consecutive quarters of rate decline from Q1 2023 through Q2 2025.
    - Reinsurance pricing fell -32% at Jan 1, 2026 renewals (Gallagher Re), further enabling primary rate cuts.
    - The soft cycle is driven by surplus capacity: new MGAs, ILS capital, and reinsurers all chasing cyber premium.
    - Historical parallel: the 2001-2006 commercial soft market ended with the 2008 financial crisis. Cyber's equivalent trigger would be a systemic event (major cloud outage, critical infrastructure attack).
    """
    )
    return


@app.cell
def _(go):
    sankey_labels = [
        "Infostealers", "Phishing / social eng.", "Vulnerability exploit",
        "Credential stuffing", "Insider threat", "Supply chain",
        "Ransomware / extortion", "Data exfiltration", "BEC / funds transfer",
        "Business interruption", "System compromise",
        "First-party: BI loss", "First-party: forensics & recovery",
        "First-party: ransom payment", "Third-party: notification & regulatory",
        "Third-party: liability / lawsuits", "Tech E&O claims",
    ]

    sankey_links = {
        "source": [
            0, 0, 0,
            1, 1, 1,
            2, 2, 2,
            3, 3, 3,
            4, 4, 4,
            5, 5, 5,
            6, 6, 6,
            7, 7, 7,
            8, 8,
            9, 9,
            10, 10,
        ],
        "target": [
            6, 7, 8,
            8, 6, 10,
            6, 7, 9,
            10, 7, 6,
            7, 9, 10,
            6, 7, 9,
            11, 12, 13,
            14, 15, 12,
            14, 15,
            11, 12,
            11, 16,
        ],
        "value": [
            10, 5, 7,
            8, 6, 2,
            12, 5, 3,
            4, 3, 1,
            4, 2, 2,
            7, 4, 4,
            25, 18, 15,
            10, 7, 4,
            12, 8,
            15, 5,
            6, 5,
        ],
    }

    _node_colors = (
        ["#4e79a7"] * 6 +
        ["#f28e2b"] * 5 +
        ["#59a14f"] * 6
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
        title="Threat vector → breach type → claim category (directional flows)",
        margin=dict(t=70, l=30, r=30, b=30),
        height=600,
    )

    sankey_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Threat-to-claim flow notes:
    - Left column (blue): Initial access vectors. Stolen credentials account for 22% of breaches (Verizon DBIR 2025), with infostealers the dominant mechanism — 75% of 3.2B credentials stolen in 2024 came from infostealers (SpyCloud). Vulnerability exploitation is 20% (+34% YoY). Supply chain/third-party involvement reached 30% of breaches.
    - Middle column (orange): Breach types. BEC + funds transfer fraud = 60% of claims by volume (Coalition 2025). Ransomware = only 21% of claims by count, but shifting from encryption to pure data exfiltration — 57% of extortion attacks are now theft-only.
    - Right column (green): Claim categories. Ransomware accounts for 91% of incurred claims by dollar value (76% direct + 15% vendor-related; Resilience 2025 Midyear Report). First-party BI loss is the largest payout category.
    - Flows are directional weights (not dollar values) illustrating relative frequency of each path. Sources: Verizon DBIR 2025, Coalition 2025 Cyber Claims Report, Resilience 2025 Midyear Report, Mandiant M-Trends 2025.
    """
    )
    return


@app.cell
def _(go):
    claim_timeline = [
        {"era": "Pre-2020", "avg_years": 1.0, "label": "~1 year"},
        {"era": "2020-2022", "avg_years": 2.0, "label": "~2 years"},
        {"era": "2023-2025", "avg_years": 4.5, "label": "4-6 years"},
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
        title="Average time to cyber insurance claim resolution (years)",
        xaxis=dict(title="Years to resolution", range=[0, 6.5]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=100, r=80, b=40),
        height=300,
    )

    claim_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Claim timeline elongation notes:
    - Business interruption claims are now taking 4-6 years to resolve, up from ~1 year pre-2020.
    - This strains actuarial reserving models: insurers must hold reserves for years longer than originally projected.
    - The practical consequence: today's soft-market pricing (10 quarters of rate cuts) will only show its true loss picture 3-5 years from now.
    - Regulatory investigations (GDPR, state-level breach notification), class action lawsuits, and complex forensics are the primary drivers of elongation.
    """
    )
    return


@app.cell
def _(go):
    systemic_events = [
        {
            "event": "NotPetya (2017)",
            "insured_loss_b": 3.0,
            "total_loss_b": 10.0,
            "affected": "Maersk, Merck, FedEx, Mondelez, 65+ countries",
            "vector": "Supply chain (M.E.Doc update)",
        },
        {
            "event": "SolarWinds (2020)",
            "insured_loss_b": 0.9,
            "total_loss_b": 5.0,
            "affected": "18,000 orgs, US govt agencies, Fortune 500",
            "vector": "Supply chain (Orion update)",
        },
        {
            "event": "Kaseya VSA (2021)",
            "insured_loss_b": 0.5,
            "total_loss_b": 1.5,
            "affected": "1,500+ businesses via 60 MSPs",
            "vector": "Supply chain (RMM exploit)",
        },
        {
            "event": "Log4Shell (2021)",
            "insured_loss_b": 0.3,
            "total_loss_b": 2.0,
            "affected": "Millions of servers, widespread scanning",
            "vector": "Vulnerability (ubiquitous library)",
        },
        {
            "event": "CrowdStrike outage (2024)",
            "insured_loss_b": 1.5,
            "total_loss_b": 5.4,
            "affected": "8.5M Windows devices, airlines, hospitals, banks",
            "vector": "Software update (single vendor)",
        },
        {
            "event": "Hypothetical: major cloud provider\noutage (72hr)",
            "insured_loss_b": 15.0,
            "total_loss_b": 80.0,
            "affected": "Millions of businesses globally",
            "vector": "Single point of failure",
        },
    ]

    _events = [e["event"] for e in systemic_events]
    _insured = [e["insured_loss_b"] for e in systemic_events]
    _total = [e["total_loss_b"] for e in systemic_events]
    _uninsured = [t - i for t, i in zip(_total, _insured)]
    _hovers = [
        f"<b>{e['event']}</b><br>Vector: {e['vector']}<br>Affected: {e['affected']}"
        f"<br>Total loss: ${e['total_loss_b']:.1f}B<br>Insured: ${e['insured_loss_b']:.1f}B"
        f"<br>Gap: ${e['total_loss_b'] - e['insured_loss_b']:.1f}B"
        for e in systemic_events
    ]

    systemic_fig = go.Figure()

    systemic_fig.add_trace(
        go.Bar(
            y=_events,
            x=_insured,
            name="Insured loss",
            orientation="h",
            marker_color="#4e79a7",
            customdata=_hovers,
            hovertemplate="%{customdata}<extra></extra>",
            text=[f"${v:.1f}B" for v in _insured],
            textposition="inside",
        )
    )

    systemic_fig.add_trace(
        go.Bar(
            y=_events,
            x=_uninsured,
            name="Uninsured loss (gap)",
            orientation="h",
            marker_color="#e15759",
            marker_opacity=0.6,
            customdata=_hovers,
            hovertemplate="%{customdata}<extra></extra>",
            text=[f"${v:.1f}B" for v in _uninsured],
            textposition="inside",
        )
    )

    systemic_fig.add_shape(
        type="line", x0=16.5, x1=16.5, y0=-0.5, y1=5.5,
        line=dict(color="black", width=2, dash="dash"),
    )
    systemic_fig.add_annotation(
        x=16.5, y=5.5,
        text="← Total annual cyber<br>    insurance premiums ($16.5B)",
        showarrow=False,
        font=dict(size=11),
        xanchor="left",
    )

    systemic_fig.update_layout(
        title="Systemic cyber events: insured vs. uninsured loss (USD billions)",
        barmode="stack",
        xaxis=dict(title="Economic loss (USD billions)"),
        yaxis=dict(autorange="reversed"),
        legend=dict(x=0.6, y=1.05, orientation="h"),
        margin=dict(t=90, l=220, r=40, b=50),
        height=450,
    )

    systemic_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Systemic risk notes:
    - Each historical event above was a correlated loss — a single cause triggering claims across hundreds or thousands of policyholders simultaneously.
    - The CrowdStrike outage (July 2024) caused ~\$5.4B in economic damage from a non-malicious software update. Insured losses (~\$1.5B) nearly equalled 10% of the entire annual cyber premium pool.
    - The hypothetical 72-hour major cloud provider outage (AWS, Azure, or GCP) is the scenario Lloyd's and Munich Re model as the "cyber hurricane." At \$80B total loss, the insured portion (\$15B) would consume an entire year's global premium in a single event.
    - The dashed line shows total annual cyber insurance premiums (\$16.5B) for scale. Any event where the insured bar crosses that line threatens the industry's solvency in that year.
    - This is why cyber cat bonds (Beazley PoleStar Re \$300M, Hannover Re renewals) are emerging — traditional reinsurance balance sheets cannot absorb truly systemic cyber tail risk.
    - Lloyd's is focused on hyperscaler outages, but the real systemic risk may be third-party software dependencies: SAP (97% of FTSE 500), monday.com, or a compromised NPM package in thousands of codebases.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Structural observations

    1. MGA dominance in innovation. MGAs originate ~33% of cyber premium and growing. The "insurtech + free security tooling" model (Coalition, At-Bay) is the most disruptive force in the market — they sell loss prevention, not just risk transfer.

    2. Scale vs. precision. Beazley writes ~15,000 policies optimizing for volume. Trium writes 375 policies with zero claims. Both models can work, but the market hasn't yet decided which wins in a downturn. The next systemic event will be the test.

    3. Soft market danger. 10 quarters of rate cuts, reinsurance down 32%. Loss ratios ticking up. S&P forecasts 15-20% increases in 2026. The carriers cutting rates deepest today will have the worst reserve development in 2028-2030.

    4. AI insurance confusion. The market thinks AI cyber risk is already covered by existing policies. Munich Re tried a standalone AI product — the market didn't bite. Lloyd's is modeling the wrong catastrophes (hyperscaler outages) while the real systemic risk is third-party software dependencies (SAP = 97% of FTSE 500 revenue, a single NPM package in thousands of codebases).

    5. Claim timeline elongation. From 1-2 years to 4-6 years for BI claims. This is a structural problem for reserving — actuarial models calibrated on historical claim durations are systematically underestimating tail development.

    6. Silent cyber runoff. Lloyd's mandated affirmative-only coverage since Jan 1, 2025. The US market is slower but moving in the same direction. The implication: cyber risk that was previously hidden inside property and liability policies must now be explicitly priced — or explicitly excluded.

    7. Systemic risk unsolved. A single cloud outage = industry-wide correlated loss. Traditional reinsurance balance sheets can't absorb it. Cyber cat bonds (\$300M Beazley PoleStar Re) are emerging but tiny relative to total exposure. The gap between insured cyber loss and actual cyber economic loss remains enormous.
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
    ## A. Why are the technical cyber underwriters all British?

    The strategy archetype treemap reveals a striking geographic pattern: technical/selective cyber underwriters are overwhelmingly Lloyd's of London syndicates or global specialty carriers (Trium, Hiscox, QBE, Brit, Mosaic), while scale writers are predominantly US-based (Chubb, AIG, Travelers) with Beazley (UK) as the notable exception, and insurtechs are almost entirely US-based (Coalition, At-Bay, Cowbell, Resilience). This is not cultural — it is structural.

    Lloyd's institutional architecture is uniquely optimized for specialist underwriting:

    - Syndicate-in-a-Box (SIAB): A team of 5-10 cyber experts can launch a syndicate writing \$50-100M GWP without building a full carrier. Trium did this — first-ever monoline cyber syndicate (1322), launched 2023 with Asta as third-party managing agent. CFC converted from MGA to Syndicate 1988 in 2021.
    - Capital separation: Underwriting judgment is separated from capital provision. Third-party investors (ILS funds, pension funds) supply the balance sheet; specialists supply the risk selection. No US equivalent exists.
    - Single regulator: Lloyd's mandated affirmative cyber clarity (2019), state-backed attack exclusions (2023), and affirmative-only products (Jan 2025). This forced every participant to treat cyber as a distinct, expert-driven peril class. The US has no comparable centralized mandate — 50 state regulators, each with different rules.
    - Central Fund rating: Even a tiny specialist syndicate benefits from Lloyd's AA- (S&P) rating. A US startup carrier would need hundreds of millions in surplus and years of state-by-state licensing.
    - 77 cyber risk insurers operate within Lloyd's, writing ~20-30% of global cyber premium (\$3.3-5B).

    The US market structurally produces a different species:

    - 50-state regulation favors large incumbents with regulatory affairs teams (Chubb, AIG, Travelers) and penalizes specialist startups.
    - Retail agent distribution rewards broad appetite and fast turnaround, pushing toward algorithmic mass-market underwriting over bespoke judgment.
    - VC funding produces insurtechs optimized for distribution scale (Coalition: 300,000+ policies) rather than underwriting precision (Trium: 375 policies).

    The pipeline: Complex cyber risks flow from US retail brokers to London wholesale brokers (Tysers, Miller, McGill) to Lloyd's subscription market. Lloyd's handles the tail — large limits, novel exposures, bespoke wordings. US domestic carriers handle the commoditized volume. Lloyd's is where cyber underwriting expertise concentrates. The US is where cyber distribution innovation concentrates. They serve different functions in the same ecosystem.
    """
    )
    return


@app.cell
def _(go, mo):
    from plotly.subplots import make_subplots as _make_subplots_struct

    _struct_dimensions = [
        "Regulators",
        "Min. capital to enter market",
        "Avg. policies per specialist",
        "Share of global cyber premium",
        "Cyber-specialist carriers",
        "Years to full market access",
    ]

    _uk_display = ["1 (+ Lloyd's)", "$5M (SIAB)", "375-2,000", "~22%", "77 syndicates", "~1 yr"]
    _us_display = ["50 states", "$300M+", "15,000-300,000", "~67%", "~200 carriers", "3-5 yrs"]

    _struct_fig = _make_subplots_struct(
        rows=1,
        cols=2,
        subplot_titles=("UK / Lloyd's", "US domestic"),
        horizontal_spacing=0.12,
        shared_yaxes=True,
    )

    _uk_normalized = [50, 5, 0.75, 22, 77, 1]
    _us_normalized = [50, 30, 50, 67, 200, 5]

    _struct_fig.add_trace(
        go.Bar(
            y=_struct_dimensions,
            x=[-v for v in _uk_normalized],
            orientation="h",
            name="UK / Lloyd's",
            marker_color="#1f77b4",
            customdata=_uk_display,
            text=_uk_display,
            textposition="inside",
            insidetextanchor="middle",
            hovertemplate="<b>%{y}</b><br>UK / Lloyd's: %{customdata}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    _struct_fig.add_trace(
        go.Bar(
            y=_struct_dimensions,
            x=_us_normalized,
            orientation="h",
            name="US domestic",
            marker_color="#e4572e",
            customdata=_us_display,
            text=_us_display,
            textposition="inside",
            insidetextanchor="middle",
            hovertemplate="<b>%{y}</b><br>US domestic: %{customdata}<extra></extra>",
        ),
        row=1,
        col=2,
    )

    _struct_fig.update_xaxes(
        showticklabels=False, showgrid=False, zeroline=False, row=1, col=1
    )
    _struct_fig.update_xaxes(
        showticklabels=False, showgrid=False, zeroline=False, row=1, col=2
    )
    _struct_fig.update_yaxes(autorange="reversed", row=1, col=1)
    _struct_fig.update_yaxes(showticklabels=False, autorange="reversed", row=1, col=2)

    _struct_fig.update_layout(
        title="UK / Lloyd's vs. US market structure comparison",
        height=400,
        margin=dict(t=80, l=220, r=40, b=40),
        showlegend=False,
    )

    mo.ui.plotly(_struct_fig)
    return


@app.cell
def _(go, mo):
    _node_labels = [
        "Policyholder (complex / large)",
        "Policyholder (SME / mid-market)",
        "UK retail broker",
        "London wholesale broker",
        "Lloyd's syndicate (specialist)",
        "Lloyd's Central Fund (AA-)",
        "US retail broker / agent",
        "US admitted carrier (scale)",
        "US MGA / insurtech",
        "US capacity provider",
        "Reinsurer (global)",
        "ILS / cat bond investors",
    ]

    _node_colors = [
        "#636efa", "#636efa",
        "#1f77b4", "#1f77b4", "#1f77b4", "#1f77b4",
        "#e4572e", "#e4572e", "#e4572e", "#e4572e",
        "#9467bd", "#9467bd",
    ]

    _sources = [0, 0, 1, 1, 2, 3, 4, 4, 4, 6, 6, 7, 7, 8, 9, 9]
    _targets = [2, 6, 6, 8, 3, 4, 5, 10, 11, 7, 8, 10, 11, 9, 10, 11]
    _values =  [4, 2, 6, 3, 4, 4, 1, 2, 1, 4, 4, 3, 1, 7, 5, 2]

    _link_colors = [
        "rgba(31,119,180,0.3)", "rgba(228,87,46,0.3)",
        "rgba(228,87,46,0.3)", "rgba(228,87,46,0.3)",
        "rgba(31,119,180,0.3)", "rgba(31,119,180,0.3)",
        "rgba(31,119,180,0.3)", "rgba(148,103,189,0.3)", "rgba(148,103,189,0.3)",
        "rgba(228,87,46,0.3)", "rgba(228,87,46,0.3)",
        "rgba(148,103,189,0.3)", "rgba(148,103,189,0.3)",
        "rgba(228,87,46,0.3)",
        "rgba(148,103,189,0.3)", "rgba(148,103,189,0.3)",
    ]

    _flow_fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                pad=20,
                thickness=25,
                label=_node_labels,
                color=_node_colors,
                hovertemplate="<b>%{label}</b><extra></extra>",
            ),
            link=dict(
                source=_sources,
                target=_targets,
                value=_values,
                color=_link_colors,
                hovertemplate="<b>%{source.label}</b> → <b>%{target.label}</b><extra></extra>",
            ),
        )
    )

    _flow_fig.update_layout(
        title="How cyber premium flows: UK/Lloyd's (blue) vs. US (red) ecosystems",
        height=500,
        margin=dict(t=70, l=10, r=10, b=30),
        font=dict(size=11),
    )

    mo.ui.plotly(_flow_fig)
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the two charts above:

    The butterfly chart compares six structural dimensions. The numbers are not on the same scale — they are displayed as labels to highlight the qualitative contrast. Key takeaways: Lloyd's lets a 5-person team launch a cyber syndicate with ~\$5M and start writing within a year; the US requires ~\$300M+ in surplus and 3-5 years of state-by-state licensing. Lloyd's produces specialists (375-2,000 policies each); the US produces scale writers (15,000-300,000 policies).

    The Sankey shows how premium flows through each ecosystem. Blue links trace the UK/Lloyd's path: complex risks go from policyholder to UK retail broker to London wholesale broker (Tysers, Miller, McGill) to a Lloyd's specialist syndicate, which is backed by the Central Fund (AA- rating) and lays off tail risk to reinsurers or ILS/cat bond investors. Red links trace the US path: SME and mid-market risks go from policyholder to US retail broker/agent, then split between admitted carriers (Chubb, AIG, Travelers) and MGA/insurtechs (Coalition, At-Bay, Cowbell), which use external capacity providers. Both systems ultimately feed into the same global reinsurance and ILS pool (purple links).

    The two ecosystems are complementary, not competitive. Complex, bespoke, high-limit cyber risks flow to London; commoditized, high-volume, algorithmically-underwritten risks stay in the US. The wholesale broker pipeline connecting them is one of the least visible but most structurally important features of the global cyber insurance market.
    """
    )
    return


@app.cell
def _(go, mo):
    from plotly.subplots import make_subplots as _make_subplots_gaps

    _gap_categories = [
        "Crypto / digital assets",
        "OT / ICS / critical infrastructure",
        "SME cyber coverage",
        "Emerging markets (APAC, LatAm, Africa)",
        "Cyber cat bonds vs. total cat bonds",
        "Supply-chain / systemic risk",
        "AI liability",
        "War / nation-state exclusions",
    ]

    _total_exposure = [3310, 1000, 400, 300, 56, 80, 50, 30]
    _currently_covered = [1.28, 5, 60, 15, 0.8, 15, 0.5, 0.2]

    _coverage_pct = [
        round(c / t * 100, 2) if t > 0 else 0
        for c, t in zip(_currently_covered, _total_exposure)
    ]

    _gap_fig = _make_subplots_gaps(
        rows=1,
        cols=2,
        column_widths=[0.55, 0.45],
        subplot_titles=(
            "Total exposure vs. insured coverage (USD billions, log scale)",
            "Coverage ratio (% of exposure insured)",
        ),
        horizontal_spacing=0.15,
    )

    _gap_fig.add_trace(
        go.Bar(
            y=_gap_categories,
            x=_total_exposure,
            orientation="h",
            name="Total exposure / addressable",
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
            x=_currently_covered,
            orientation="h",
            name="Currently insured",
            marker_color="#2ca02c",
            hovertemplate="<b>%{y}</b><br>Insured: $%{x:,.1f}B<extra></extra>",
        ),
        row=1,
        col=1,
    )

    _bar_colors = [
        "#d62728" if p < 5 else "#ff7f0e" if p < 15 else "#2ca02c"
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
    _gap_fig.update_xaxes(title_text="% of exposure insured", range=[0, 25], row=1, col=2)
    _gap_fig.update_yaxes(autorange="reversed", row=1, col=1)
    _gap_fig.update_yaxes(autorange="reversed", row=1, col=2)

    _gap_fig.update_layout(
        title="Cyber insurance market gaps: exposure vs. coverage by segment",
        barmode="overlay",
        height=550,
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

    The chart above maps eight major coverage gaps in the cyber insurance market. Left panel shows total exposure (red) vs. amount currently insured (green) on a log scale; right panel shows the coverage ratio as a percentage.

    Key gaps:

    1. Crypto and digital assets (\$3.31T market cap, ~\$1.3B insured). Less than 0.04% coverage. Most mainstream insurers exclude digital assets entirely. Only a handful of specialists (Evertas, Canopius, Arch) offer custody or hot-wallet policies, and capacity is thin.

    2. OT / ICS / critical infrastructure (\$1T+ exposure, ~\$5B insured). DeNexus estimates the operational technology protection gap at \$1T. Industrial control systems in energy, water, manufacturing, and transportation are largely uninsured — policies often exclude physical damage resulting from cyber events.

    3. SME cyber coverage (~\$400B exposure, ~\$60B insured). Large enterprises buy cyber insurance at 60-80% penetration rates; SMEs at 10-20%. The economics are hard — small premiums (\$2-5K) vs. high acquisition costs. Coalition and Cowbell target this with automated underwriting.

    4. Emerging markets (\$300B+ exposure, ~\$15B insured). North America accounts for ~68% of global cyber premium. APAC is growing fast but from a tiny base. Africa and Latin America are below 5% penetration. Regulatory frameworks are still forming.

    5. Cyber catastrophe bonds (\$800M issued vs. \$56B total cat bond market). Only 1.4% of the cat bond market addresses cyber risk. Beazley's PoleStar Re (\$300M) and Hannover Re have pioneered, but ILS investors remain wary of cyber aggregation modeling. This is the primary bottleneck for scaling systemic risk capacity.

    6. Supply-chain and systemic risk (\$80B modeled loss, ~\$15B insured). Lloyd's models a 72-hour major cloud outage at \$80B economic loss with ~\$15B insured — nearly an entire year's global premium consumed by a single event. The CrowdStrike outage (July 2024) gave a preview: \$5.4B economic loss, only \$0.4-1.5B insured. Traditional reinsurance balance sheets cannot absorb correlated cyber losses of this magnitude.

    7. AI liability (\$50B+ emerging exposure, ~\$500M covered). AI-generated code vulnerabilities, model poisoning, deepfake-enabled fraud, and autonomous agent errors are largely uncovered. Munich Re's standalone AI liability product saw limited uptake — the market hasn't figured out how to price AI-specific risk.

    8. War and nation-state exclusions (\$30B+ exposure, ~\$200M covered). Lloyd's mandated state-backed attack exclusions from March 2023. NotPetya (\$10B+ total loss) was the catalyst. The coverage boundary between "cybercrime" and "cyberwar" remains legally contested (Merck v. Zurich settled for \$1.4B). This creates a structural gap for any organization targeted by APT groups with state affiliations.
    """
    )
    return


if __name__ == "__main__":
    app.run()
