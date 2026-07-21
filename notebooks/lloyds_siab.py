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
    # Only 2 of 14 Lloyd's Syndicates-in-a-Box have graduated. The remaining active SiaBs write just 0.23% of Lloyd's GWP.

    Lloyd's launched the Syndicate-in-a-Box (SiaB) programme in 2020 as a "fail-fast" innovation sandbox under the "Future at Lloyd's" strategy. The idea: let entrepreneurial underwriters enter Lloyd's at lower cost, with reduced reporting, a GBP 100m year-one cap, and a 3-year review window. Six years in, 14 SiaBs have been approved (Insurance Insider's 2026 analysis counts 13 "entrants"); ~6 have closed or entered run-off, and the survivors collectively write GBP 133.7m -- a rounding error against Lloyd's GBP 57.9bn market.

    ---

    ## Lloyd's Syndicate-in-a-Box Programme Deep Dive (2020-2026)
    - Programme launched 2020 as part of Blueprint One / "Future at Lloyd's" under CEO John Neal.
    - 14 SiaBs approved on this roster (Insurance Insider counts 13 entrants). 2 graduated to full syndicate, ~6 remain active, ~6 closed or in run-off.
    - Combined active SiaB GWP: ~GBP 133.7m = 0.23% of Lloyd's total GWP (GBP 57.9bn in 2025). Excludes graduated Carbon 4747.
    - Year-one GWP cap: less than GBP 100m. Must predominantly write short-tail, monoline business with only incidental catastrophe exposure.
    - Only 1 clear success story: Carbon Syndicate 4747, which graduated in 2.5 years and wrote ~GBP 204m in 2024. A planned second syndicate (5757) was approved in principle in 2024 but had not begun trading as of late 2025, so the mooted ~GBP 400m two-syndicate figure did not materialize.
    - Industry verdict: "an interesting experiment; it probably hasn't worked" (Insurance Insider, 2026).
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go):
    scale_data = [
        {"label": "Lloyd's total GWP (2025)", "value_m": 57900, "color": "#4e79a7"},
        {"label": "Largest syndicate book (Beazley 623/2623, ~GBP 3.2bn)", "value_m": 3200, "color": "#76b7b2"},
        {"label": "Average syndicate capacity", "value_m": 667, "color": "#59a14f"},
        {"label": "Carbon 4747 (graduated SiaB)", "value_m": 204, "color": "#f28e2b"},
        {"label": "All active SiaBs combined", "value_m": 133.7, "color": "#e15759"},
        {"label": "SiaB year-one GWP cap", "value_m": 100, "color": "#b07aa1"},
    ]

    scale_fig = go.Figure()
    scale_fig.add_trace(
        go.Bar(
            y=[d["label"] for d in scale_data],
            x=[d["value_m"] for d in scale_data],
            orientation="h",
            marker_color=[d["color"] for d in scale_data],
            text=[
                f"GBP {d['value_m']:,.0f}m"
                if d["value_m"] >= 100
                else f"GBP {d['value_m']:.1f}m"
                for d in scale_data
            ],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>GBP %{x:,.1f}m<extra></extra>",
        )
    )

    scale_fig.add_annotation(
        x=133.7,
        y="All active SiaBs combined",
        text="0.23% of Lloyd's total",
        showarrow=True,
        arrowhead=2,
        ax=120,
        ay=-30,
        font=dict(size=13, color="#e15759"),
    )

    scale_fig.update_layout(
        title="Lloyd's market scale vs. Syndicates-in-a-Box (2025, GBP millions, log scale)",
        xaxis=dict(title="GBP millions (log scale)", type="log", range=[1.5, 5.0]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=320, r=80, b=50),
        height=400,
    )

    scale_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Scale context:
    - Lloyd's total GWP reached GBP 57.9bn in 2025, delivering its third consecutive year of 20%+ return on capital (22.0%).
    - The combined GWP of all active SiaBs (GBP 133.7m) is less than a single mid-sized syndicate.
    - A single large syndicate book -- Beazley 623/2623 together write ~GBP 3.2bn -- is bigger than all SiaBs combined by a factor of ~24x. (For the 2025 year, Canopius 4444 is the largest single syndicate by capacity.)
    - The GBP 100m year-one cap constrains SiaBs to niche, monoline business -- by design.
    - Sources: Lloyd's Full Year Results 2025; Insurance Insider SiaB analysis (2026); Howden Re.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## What is a Syndicate-in-a-Box?

    A SiaB is a lighter, faster, cheaper alternative to a traditional Lloyd's syndicate -- designed for entrepreneurial underwriters who want Lloyd's paper without the full cost and complexity of a conventional startup. The table below shows the key structural differences.
    """
    )
    return


@app.cell
def _(go):
    requirements = [
        "Year-one GWP cap",
        "Time to market",
        "Application cost",
        "Internal capital model",
        "Cat exposure",
        "Physical Lloyd's presence",
        "Financial reporting",
        "Expense ratio target",
        "Review period",
    ]

    siab_vals = [
        "< GBP 100m",
        "~3 months",
        "~GBP 100k",
        "Lloyd's provides for years 1-4",
        "Incidental only (5 major perils excluded)",
        "Not permitted (electronic only)",
        "Exempt from several requirements",
        "< 35% net operating by year 3",
        "3-year KPI review, then graduate or exit",
    ]

    trad_vals = [
        "No cap",
        "12-24 months",
        "GBP 200k",
        "Required from day one (Solvency II)",
        "Full cat classes permitted",
        "Required (underwriting room)",
        "Full reporting obligations",
        "No specific mandated target",
        "Ongoing (annual oversight)",
    ]

    req_fig = go.Figure()

    req_fig.add_trace(
        go.Table(
            header=dict(
                values=[
                    "Requirement",
                    "Syndicate-in-a-Box",
                    "Traditional Syndicate",
                ],
                fill_color="#4e79a7",
                font=dict(color="white", size=13),
                align="left",
            ),
            cells=dict(
                values=[requirements, siab_vals, trad_vals],
                fill_color=[
                    ["#f0f0f0"] * 9,
                    ["#e8f4e8"] * 9,
                    ["#f0f0f0"] * 9,
                ],
                font=dict(size=12),
                align="left",
                height=30,
            ),
        )
    )

    req_fig.update_layout(
        title="SiaB vs. traditional syndicate: key structural differences",
        margin=dict(t=60, l=20, r=20, b=20),
        height=380,
    )

    req_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Structural notes:
    - The reduced capital burden is significant: Lloyd's performs internal capital modelling for SiaBs (using its Lloyd's Syndicate Model) for years 1-4, eliminating the need to build an expensive Solvency II internal model from scratch.
    - However, the same 35% SCR uplift to produce the Economic Capital Assessment (ECA) applies to both SiaBs and traditional syndicates.
    - The "light-touch" regulatory promise has been criticized: multiple market sources told Insurance Insider that running a SiaB is "not much less than a full-on syndicate" in practice.
    - From 2026, Lloyd's will introduce Principles-Based Oversight (PBO) categories for new syndicates after their first year of trading (rather than third year), increasing lifecycle transparency.
    - The trade-off: lower barriers in exchange for a smaller sandbox and tighter leash. SiaBs get speed and cost savings but are constrained to monoline, short-tail, non-cat business with a 3-year clock.
    - Sources: Lloyd's SiaB Guide (April 2024 PDF); Lloyd's Capital Requirements page; Carrier Management; PwC.
    """
    )
    return


@app.cell
def _(go):
    outcome_data = [
        {"status": "Active", "count": 6, "color": "#59a14f"},
        {"status": "Closed / run-off", "count": 6, "color": "#e15759"},
        {"status": "Graduated (confirmed)", "count": 1, "color": "#4e79a7"},
        {"status": "Graduated (likely)", "count": 1, "color": "#7fb3d8"},
    ]

    outcome_fig = go.Figure(
        data=[
            go.Pie(
                labels=[d["status"] for d in outcome_data],
                values=[d["count"] for d in outcome_data],
                hole=0.4,
                marker=dict(colors=[d["color"] for d in outcome_data]),
                texttemplate="<b>%{label}</b><br>%{value} SiaBs<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>%{value} SiaBs<br>%{percent}<extra></extra>",
            )
        ]
    )

    outcome_fig.update_layout(
        title="SiaB programme outcomes: 14 approved, only 2 graduated (2020-2026)",
        annotations=[
            dict(text="14<br>Total", x=0.5, y=0.5, font_size=16, showarrow=False)
        ],
        showlegend=True,
        height=400,
    )

    outcome_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Outcome notes:
    - Lloyd's original expectation was "a third transitioning, a third failing, and a third remaining small." Actual results roughly match.
    - Graduated (14%): Carbon 4747 is the unambiguous success. MCI 1902 may be the second, based on its GBP 143.5m stamp capacity suggesting transition beyond SiaB constraints.
    - Active but small (43%): Most SiaBs remain niche operations writing GBP 7-66m -- well below the average Lloyd's syndicate capacity of ~GBP 667m.
    - Closed/run-off (43%): Munich Re 1840, Beazley ESG 4321, MIC Global 5183, Wakam 1347, Picnic 2460, MCI 1966 (shutting down 2025).
    - Wakam 1347 holds the record for shortest SiaB lifespan -- shuttered after less than one year of trading.
    """
    )
    return


@app.cell
def _(go):
    siab_capacity = [
        {"name": "Carbon 4747 (graduated)", "capacity": 225, "color": "#4e79a7"},
        {"name": "MCI 1902 (likely graduated)", "capacity": 143.5, "color": "#7fb3d8"},
        {"name": "Sukoon 2880", "capacity": 65.8, "color": "#59a14f"},
        {"name": "Greenlight Re 3456", "capacity": 51.1, "color": "#59a14f"},
        {"name": "Agile 2427", "capacity": 46.5, "color": "#59a14f"},
        {"name": "MCI 1966", "capacity": 35, "color": "#76b7b2"},
        {"name": "MIC Global 5183 (closed)", "capacity": 27.5, "color": "#e15759"},
        {"name": "Parsyl 1796", "capacity": 15.8, "color": "#59a14f"},
        {"name": "Wildfire Def. 1996", "capacity": 10, "color": "#76b7b2"},
        {"name": "Oka 1922", "capacity": 7, "color": "#59a14f"},
    ]

    siab_capacity.sort(key=lambda x: x["capacity"])

    cap_fig = go.Figure()
    cap_fig.add_trace(
        go.Bar(
            y=[d["name"] for d in siab_capacity],
            x=[d["capacity"] for d in siab_capacity],
            orientation="h",
            marker_color=[d["color"] for d in siab_capacity],
            text=[f"GBP {d['capacity']:.1f}m" for d in siab_capacity],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Stamp capacity: GBP %{x:.1f}m<extra></extra>",
        )
    )

    cap_fig.update_layout(
        title="SiaB stamp capacity (2026 or last reported, GBP millions)",
        xaxis=dict(title="GBP millions", range=[0, 280]),
        margin=dict(t=70, l=220, r=80, b=50),
        height=450,
    )

    cap_fig.add_annotation(
        x=180,
        y="Oka 1922",
        text="Green = active | Blue = graduated | Red = closed | Teal = estimated",
        showarrow=False,
        font=dict(size=11),
    )

    cap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Stamp capacity notes:
    - Carbon 4747 graduated January 2023 and wrote ~GBP 204m in 2024. A second syndicate (5757) was approved in principle in 2024 but had not begun trading as of late 2025, so the ~GBP 400m two-syndicate target was a forecast that did not materialize.
    - MCI 1902 has the largest stamp capacity among non-graduated SiaBs at GBP 143.5m, well above the GBP 100m year-one cap, suggesting it has likely graduated to full syndicate status.
    - MIC Global 5183 peaked at GBP 27.5m before closing at end of 2024 YoA; now operates as a coverholder of Greenlight Re 3456.
    - Wildfire Defense 1996 and MCI 1966 capacities are estimates based on reported GWP targets and year-one constraints.
    - Munich Re 1840 (nil capacity), Beazley 4321 (~GBP 15m, closed), Picnic 2460, and Wakam 1347 are omitted due to small, nil, or unreported capacity and ceased/run-off status. MIC Global 5183 is included (despite closing) because it has a meaningful reported peak.
    - Sources: Asta client page; Lloyd's syndicate accounts; Insurance Journal; Reinsurance News.
    """
    )
    return


@app.cell
def _(go):
    sector_data = [
        {"sector": "Property / casualty", "count": 3},
        {"sector": "Reinsurance", "count": 3},
        {"sector": "Life science / medical", "count": 2},
        {"sector": "Insurtech / MGA platform", "count": 2},
        {"sector": "Cargo / logistics", "count": 1},
        {"sector": "ESG multi-line", "count": 1},
        {"sector": "Carbon / climate", "count": 1},
        {"sector": "Parametric / emerging", "count": 1},
    ]

    sector_fig = go.Figure(
        data=[
            go.Pie(
                labels=[d["sector"] for d in sector_data],
                values=[d["count"] for d in sector_data],
                hole=0.4,
                texttemplate="<b>%{label}</b><br>%{value}<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>%{value} SiaBs<br>%{percent}<extra></extra>",
            )
        ]
    )

    sector_fig.update_layout(
        title="SiaB sector distribution: property/casualty and reinsurance lead",
        annotations=[
            dict(text="14<br>SiaBs", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
        height=450,
    )

    sector_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Sector notes:
    - Property / casualty (3 SiaBs): Carbon 4747 (coverholder partnerships), Agile 2427 (ANZ multi-line), Wildfire Defense 1996 (California commercial wildfire E&S lines).
    - Reinsurance (3): Sukoon 2880 (regional facultative), Picnic 2460 (Australian community mutuals), Wakam 1347 (European reinsurance).
    - Life science / medical (2): MCI 1902 (medical malpractice, life science) and MCI 1966 (clinical trial funding insurance). MCI is the only sponsor to launch two SiaBs.
    - Insurtech / MGA platform (2): Greenlight Re 3456 (capacity for insurtechs/MGAs), MIC Global 5183 (micro/embedded insurance).
    - The sector mix reflects SiaB design intent: niche, innovative, or underserved markets where a monoline focus is viable.
    """
    )
    return


@app.cell
def _(go):
    siab_timeline = [
        {"name": "Munich Re 1840", "year": 2020, "color": "#e15759"},
        {"name": "Carbon 4747", "year": 2020, "color": "#4e79a7"},
        {"name": "Parsyl 1796", "year": 2020, "color": "#59a14f"},
        {"name": "Picnic 2460", "year": 2020, "color": "#e15759"},
        {"name": "MCI 1902", "year": 2021, "color": "#4e79a7"},
        {"name": "Beazley ESG 4321", "year": 2021, "color": "#e15759"},
        {"name": "Greenlight Re 3456", "year": 2022, "color": "#59a14f"},
        {"name": "MIC Global 5183", "year": 2022, "color": "#e15759"},
        {"name": "Sukoon 2880", "year": 2022, "color": "#59a14f"},
        {"name": "Wakam 1347", "year": 2022, "color": "#e15759"},
        {"name": "Wildfire Def. 1996", "year": 2023, "color": "#59a14f"},
        {"name": "Oka 1922", "year": 2023, "color": "#59a14f"},
        {"name": "MCI 1966", "year": 2024, "color": "#e15759"},
        {"name": "Agile 2427", "year": 2024, "color": "#59a14f"},
    ]

    timeline_fig = go.Figure()
    timeline_fig.add_trace(
        go.Scatter(
            x=[s["year"] for s in siab_timeline],
            y=[s["name"] for s in siab_timeline],
            mode="markers",
            marker=dict(
                size=18,
                color=[s["color"] for s in siab_timeline],
                symbol="square",
            ),
            hovertemplate="<b>%{y}</b><br>Approved: %{x}<extra></extra>",
        )
    )

    timeline_fig.update_layout(
        title="SiaB launch timeline: each dot is one syndicate (green = active, blue = graduated, red = closed)",
        xaxis=dict(
            title="Year of approval",
            dtick=1,
            range=[2019.5, 2025.5],
        ),
        yaxis=dict(title=""),
        margin=dict(t=80, l=200, r=40, b=50),
        height=500,
        showlegend=False,
    )

    timeline_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Timeline notes:
    - 2020 cohort (4 SiaBs): Munich Re 1840 and Picnic 2460 have closed; Carbon 4747 graduated; Parsyl 1796 remains active.
    - 2021: MCI 1902 and Beazley ESG 4321 received in-principle approval (both commenced underwriting January 2022).
    - 2022 had the most approvals (4): Greenlight Re 3456, MIC Global 5183 (later closed), Sukoon 2880, and Wakam 1347 (approved late 2022, shuttered after less than one year of trading).
    - 2023: Wildfire Defense 1996 and Oka 1922 remain active.
    - 2024: MCI 1966 (clinical trial funding) and Agile 2427 (ANZ multi-line) -- both still early stage.
    - No new SiaB has been approved since 2024 as of mid-2026, prompting questions about whether the programme needs a reboot.
    """
    )
    return


@app.cell
def _(go):
    carbon_years = [
        "2020\n(H2 launch)",
        "2021",
        "2022",
        "2023\n(graduated)",
        "2024",
    ]
    carbon_gwp = [15, 40, 62.5, 150, 204]
    carbon_colors = [
        "#f28e2b",
        "#f28e2b",
        "#f28e2b",
        "#4e79a7",
        "#4e79a7",
    ]

    carbon_fig = go.Figure(
        go.Bar(
            x=carbon_years,
            y=carbon_gwp,
            marker_color=carbon_colors,
            text=[f"GBP {v:.0f}m" for v in carbon_gwp],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>GWP: GBP %{y:.0f}m<extra></extra>",
        )
    )

    carbon_fig.update_layout(
        title="Carbon 4747: the SiaB success story (GWP growth, GBP millions)",
        xaxis=dict(title="", type="category"),
        yaxis=dict(title="GWP (GBP millions)", range=[0, 260]),
        margin=dict(t=70, l=60, r=40, b=70),
        height=400,
    )

    carbon_fig.add_annotation(
        x="2023\n(graduated)",
        y=150,
        text="Graduated to<br>full syndicate",
        showarrow=True,
        arrowhead=2,
        ax=70,
        ay=-50,
        font=dict(size=12, color="#4e79a7"),
    )


    carbon_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Carbon 4747 notes:
    - Carbon Underwriting is an independent MGU with no parent insurer sponsor, managed by Asta.
    - Grew from 4 employees at launch to 51 by 2025.
    - First SiaB to graduate to full syndicate (January 2023), having met all KPIs within 2.5 years.
    - Received approval in principle for a second syndicate (5757) in 2024; as of late 2025 it had not yet begun trading.
    - Described as delivering "consistently profitable and stable underwriting results" with "top-quartile" ambitions.
    - Orange bars = SiaB period. Blue bars = full syndicate period.
    - The poster child -- but also the exception. No other SiaB has come close to this trajectory.
    - Sources: Lloyd's "Carbon 4747: One Year On"; Davies Group; Reinsurance News; Carbon Underwriting.
    """
    )
    return


@app.cell
def _(go):
    ma_data = [
        {"agent": "Asta Managing Agency", "count": 10, "color": "#4e79a7"},
        {"agent": "Polo Managing Agency", "count": 2, "color": "#f28e2b"},
        {"agent": "Munich Re Syndicate Ltd", "count": 1, "color": "#76b7b2"},
        {"agent": "Beazley Management Ltd", "count": 1, "color": "#e15759"},
    ]

    ma_fig = go.Figure(
        data=[
            go.Pie(
                labels=[d["agent"] for d in ma_data],
                values=[d["count"] for d in ma_data],
                hole=0.4,
                marker=dict(colors=[d["color"] for d in ma_data]),
                texttemplate="<b>%{label}</b><br>%{value} SiaBs<br>%{percent}",
                hovertemplate="<b>%{label}</b><br>%{value} SiaBs managed<br>%{percent}<extra></extra>",
            )
        ]
    )

    ma_fig.update_layout(
        title="Managing agent concentration: Asta dominates the SiaB market",
        annotations=[
            dict(text="14<br>SiaBs", x=0.5, y=0.5, font_size=14, showarrow=False)
        ],
        showlegend=True,
        height=400,
    )

    ma_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Asta dominance:
    - Asta Managing Agency manages ~10 of 14 SiaBs ever launched, plus 18 full syndicates, with GBP 5.5bn total GWP under management.
    - Asta's full syndicate portfolio includes Ki/ARTes 1618 (GBP 730m stamp capacity), Fidelis 3123 (GBP 581m), CFC 1988 (GBP 300m), Convex 1984 (GBP 294m), and graduated SiaB Carbon 4747 (GBP 225m stamp capacity; 2024 GWP ~GBP 204m, 4747 only).
    - Polo Managing Agency hosted Wakam 1347 (closed after <1 year) and Wildfire Defense 1996 (active).
    - The concentration is notable: if an entrant wants a SiaB at Lloyd's, Asta is effectively the only viable managing agent.
    - Sources: Asta website; Lloyd's market data.
    """
    )
    return


@app.cell
def _(go):
    entrant_data = [
        {
            "name": "Ki 1618\n(follow platform)",
            "gwp": 715,
            "type": "Full syndicate",
            "color": "#4e79a7",
        },
        {
            "name": "Inigo 1301\n(specialty)",
            "gwp": 869,
            "type": "Full syndicate",
            "color": "#4e79a7",
        },
        {
            "name": "Carbon 4747\n(graduated SiaB)",
            "gwp": 204,
            "type": "Graduated SiaB",
            "color": "#f28e2b",
        },
        {
            "name": "Convex 1984\n(reinsurance)",
            "gwp": 294,
            "type": "Full syndicate",
            "color": "#4e79a7",
        },
        {
            "name": "All other SiaBs\n(combined)",
            "gwp": 134,
            "type": "SiaB",
            "color": "#e15759",
        },
    ]

    entrant_fig = go.Figure(
        go.Bar(
            x=[d["name"] for d in entrant_data],
            y=[d["gwp"] for d in entrant_data],
            marker_color=[d["color"] for d in entrant_data],
            text=[f"GBP {d['gwp']:,.0f}m" for d in entrant_data],
            textposition="outside",
            customdata=[d["type"] for d in entrant_data],
            hovertemplate="<b>%{x}</b><br>GWP: GBP %{y:,.0f}m<br>Type: %{customdata}<extra></extra>",
        )
    )

    entrant_fig.update_layout(
        title="Lloyd's recent new entrants: SiaBs vs. full syndicate startups (approximate GBP millions)",
        xaxis=dict(title=""),
        yaxis=dict(title="GWP (GBP millions, approximate)", range=[0, 1050]),
        margin=dict(t=70, l=60, r=40, b=80),
        height=450,
    )

    entrant_fig
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    New entrant comparison:
    - Ki (Syndicate 1618) is NOT a SiaB -- it launched as a full algorithmically-driven follow syndicate in 2021, backed by Brit (Fairfax Financial). It reached \$1.11bn Gross Managed Premium (~GBP 877m) in 2025 -- of which Syndicate 1618 itself wrote ~\$905m (~GBP 715m), the rest via capacity partners -- with a 91.3% adjusted combined ratio and \$171.4m adjusted PBT. Became standalone within Fairfax in January 2025, now managed by Asta.
    - Inigo (Syndicate 1301) is also not a SiaB -- it acquired StarStone's managing agency and syndicate. GWP grew from \$411m (2021) to \$1.1bn (~GBP 869m, 2023) with an 85.5% combined ratio and \$144.5m PBT.
    - Convex (Syndicate 1984) entered Lloyd's in 2025 as a new full syndicate, targeting GBP 150m year one, GBP 294m stamp for 2026.
    - The contrast is stark: full syndicate startups with institutional backing scale 5-10x faster than SiaBs.
    - Ki and Inigo report in USD; values converted at ~0.79 GBP/USD for the chart. S&P Global: mature syndicates outperform newer ones by ~7pp on weighted-average combined ratios.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## How hard is it to get approved as a Syndicate-in-a-Box?

    Lloyd's claims the SiaB process takes ~3 months from triage to permission to underwrite. The reality is more nuanced: most proposals never reach formal application. The funnel is shaped like a pyramid with heavy informal filtering at every stage.
    """
    )
    return


@app.cell
def _(go):
    funnel_stages = [
        "Initial enquiries to managing agents",
        "Taken forward for pre-application",
        "Formal application submitted",
        "In-principle approval (Council)",
        "Permission to underwrite (BOC)",
        "Active at end-2024 (incl. graduated)",
    ]
    funnel_values = [200, 80, 30, 14, 14, 9]
    funnel_colors = [
        "#d4e6f1",
        "#a9cce3",
        "#7fb3d8",
        "#5499c7",
        "#2e86c1",
        "#1a5276",
    ]

    funnel_fig = go.Figure(
        go.Funnel(
            y=funnel_stages,
            x=funnel_values,
            marker=dict(color=funnel_colors),
            textinfo="value+percent initial",
            hovertemplate="<b>%{y}</b><br>~%{x} proposals<br>%{percentInitial} of initial enquiries<extra></extra>",
        )
    )

    funnel_fig.update_layout(
        title="SiaB approval funnel: ~200 enquiries yielded 14 approvals over 6 years (estimated)",
        margin=dict(t=80, l=20, r=20, b=40),
        height=450,
    )

    funnel_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Approval funnel notes:
    - Asta CEO Lorraine Harfitt disclosed that of ~50 enquiries in a single recent quarter, ~30 were not taken forward because they were "not new enough" -- a ~60% rejection rate at the very first informal stage.
    - Extrapolating: across ~6 years and multiple managing agents, total enquiries are estimated at 150-250+. Only 14 reached formal approval.
    - Lloyd's does not publish rejection statistics. Unviable proposals are filtered out informally to preserve the applicant's reputation.
    - The funnel values above are estimates based on the Asta disclosure and the 14 confirmed approvals. The informal filtering is the real gate.
    - Sources: Insurance Insider; Asta CEO commentary; Lloyd's SiaB Guide.
    """
    )
    return


@app.cell
def _(go):
    process_steps = [
        "1. Contact New Entrants team",
        "2. Triage (qual + quant submission)",
        "3. BOC presentation (25 min + Q&A)",
        "4. Council in-principle approval",
        "5. Making it Happen (capital, KPIs, ops)",
        "6. Permission to Underwrite",
    ]
    step_durations = [
        "Days",
        "2-4 weeks",
        "1 day",
        "2-4 weeks",
        "4-12 weeks",
        "1-2 weeks",
    ]
    step_details = [
        "Informal sounding-out; Lloyd's advises in writing if not progressed",
        "Submit business plan, 3-year P&L, Lloyd's Standard Model; weekly Triage Group reviews",
        "Max 20-page deck; 25 min presentation + 20 min questions + 15 min deliberation; 8 voting members",
        "Council grants formal in-principle; application fee (GBP 100k) invoiced",
        "Lodge Funds at Lloyd's; agree KPIs; finalise managing agent; set up operations",
        "BOC reviews completion; grants final permission; underwriting can commence",
    ]

    process_fig = go.Figure()
    process_fig.add_trace(
        go.Table(
            header=dict(
                values=["Step", "Duration", "What happens"],
                fill_color="#2e86c1",
                font=dict(color="white", size=13),
                align="left",
            ),
            cells=dict(
                values=[process_steps, step_durations, step_details],
                fill_color=[
                    ["#eaf2f8", "#d4e6f1"] * 3,
                    ["#eaf2f8", "#d4e6f1"] * 3,
                    ["#eaf2f8", "#d4e6f1"] * 3,
                ],
                font=dict(size=11),
                align="left",
                height=35,
            ),
        )
    )

    process_fig.update_layout(
        title="SiaB approval process: 6 steps from first contact to underwriting",
        margin=dict(t=60, l=20, r=20, b=20),
        height=320,
    )

    process_fig
    return


@app.cell
def _(go):
    cost_items = [
        {"item": "Lloyd's application fee", "gbp": 100000, "color": "#2e86c1"},
        {"item": "Managing agent setup fees (est.)", "gbp": 250000, "color": "#5499c7"},
        {"item": "Legal / consulting", "gbp": 200000, "color": "#7fb3d8"},
        {"item": "Actuarial / reserving", "gbp": 100000, "color": "#a9cce3"},
        {"item": "IT / systems infrastructure", "gbp": 150000, "color": "#d4e6f1"},
    ]

    cost_fig = go.Figure(
        go.Bar(
            y=[c["item"] for c in cost_items],
            x=[c["gbp"] for c in cost_items],
            orientation="h",
            marker_color=[c["color"] for c in cost_items],
            text=[f"GBP {c['gbp']:,.0f}" for c in cost_items],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>GBP %{x:,.0f}<extra></extra>",
        )
    )

    total_cost = sum(c["gbp"] for c in cost_items)
    cost_fig.update_layout(
        title=f"Estimated cost to establish a SiaB (excl. Funds at Lloyd's): ~GBP {total_cost:,.0f}",
        xaxis=dict(title="GBP", range=[0, 350000]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=250, r=80, b=50),
        height=350,
    )

    cost_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Approval difficulty notes:

    What Lloyd's looks for (and why most proposals fail):
    - Innovation/differentiation is the primary gate. Must be accretive to Lloyd's -- "not just another source of underwriting capacity for normal lines." Innovation can be in product, distribution, geography, or technology.
    - Financial targets: net combined ratio < 100% by year 3; net operating expense ratio < 35% by year 3.
    - Capital: must lodge Funds at Lloyd's determined by Lloyd's Standard Model at 99.5% confidence with 35% uplift.
    - Management team: named active underwriter with demonstrated competence.
    - Business plan: 3-year GAAP P&L, completed Lloyd's Standard Model, max 20-page BOC presentation.

    The Business Opportunities Committee (BOC):
    - 8 voting members: Lloyd's Directors/Heads of Underwriting, Oversight, Exposure Management, Finance, Actuarial, Market Development.
    - Chaired by Dawn Miller (Chief Commercial Officer / CEO Americas).
    - Triage Group meets weekly to filter submissions before they reach the BOC.
    - BOC has delegated authority for final Permission to Underwrite -- the real decision point.

    Common reasons applications fail or stall:
    - Insufficient innovation (~60% of enquiries dropped at first stage for being "not new enough").
    - Capital sourcing difficulties, especially during volatile markets.
    - Broker perception: "you're just a syndicate in a box -- you're not a full syndicate."
    - Lloyd's internal appetite has shifted toward larger, corporate-backed entrants.
    - Expense ratio challenge: <35% target is demanding at GBP 50m scale.

    Cost reality:
    - Application fee: GBP 100k (half the GBP 200k for traditional syndicates).
    - Total pre-underwriting costs (incl. MA setup, legal, actuarial, IT): estimated GBP 700k-1m+ before any premium is written.
    - Central Fund contribution: 1.40% of GWP for years 1-3 (vs. 0.35% for established syndicates), with option to defer to years 4-6.
    - Subscription fee: 0.36% of GWP.

    Timeline reality:
    - Lloyd's claims ~3 months triage-to-permission. Munich Re (first SiaB) achieved this, but Munich Re is exceptional.
    - Realistic timeline from first approach to underwriting: 6-12 months for most applicants.
    - Pre-application engagement (managing agent selection, business plan development) can itself take months before the clock starts.

    Sources: Lloyd's SiaB Guide (April 2024 PDF); Lloyd's Assessment Criteria (June 2020 PDF); Lloyd's Capital Guidance (August 2024 PDF); Insurance Insider; Asta CEO; Carrier Management.
    """
    )
    return


@app.cell
def _(go):
    perf_names = [
        "Lloyd's market\n(2025)",
        "Inigo 1301\n(2023)",
        "Carbon 4747\n(est.)",
        "Ki 1618\n(2025 adj.)",
        "Parsyl 1796\n(2024)",
    ]
    perf_cr = [87.6, 85.5, 90, 91.3, 112.2]
    perf_colors = ["#4e79a7", "#76b7b2", "#f28e2b", "#76b7b2", "#e15759"]

    perf_fig = go.Figure(
        go.Bar(
            x=perf_names,
            y=perf_cr,
            marker_color=perf_colors,
            text=[f"{v:.1f}%" for v in perf_cr],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Combined ratio: %{y:.1f}%<extra></extra>",
        )
    )

    perf_fig.add_hline(
        y=100,
        line_dash="dash",
        line_color="red",
        annotation_text="Breakeven (100%)",
        annotation_position="top right",
    )

    perf_fig.update_layout(
        title="Combined ratios: SiaBs vs. Lloyd's market and notable new entrants",
        xaxis=dict(title=""),
        yaxis=dict(title="Combined ratio (%)", range=[0, 130]),
        margin=dict(t=70, l=60, r=40, b=80),
        height=400,
    )

    perf_fig
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Performance notes:
    - Most SiaBs do not publicly disclose combined ratios. The chart shows only those with publicly available data.
    - Carbon 4747's combined ratio (~90%) is estimated from public statements about "superior underwriting results" and "top-quartile" ambitions.
    - Parsyl 1796 reported a 112.2% combined ratio in 2024 with \$14.05m GWP, contracting 4.4% YoY -- indicating underwriting losses.
    - Munich Re 1840 is excluded: its 380% combined ratio in 2024 reflects terminal run-off with negligible premium, not operating performance.
    - Beazley ESG 4321 reported a -6.0% loss on capacity for 2022 YoA before entering run-off.
    - Lloyd's market overall: 87.6% combined ratio in 2025. Top quartile syndicates earned 32.1% of net premium; bottom quartile 6.5%.
    - 3 of the 5 worst-performing syndicates in 2025 only began trading in 2024; 4 of the 5 posted losses. New entrants structurally populate the bottom quartile in early years.
    - No SiaB or Ki publicly discloses average policy sizes, policy counts, or quote-to-bind conversion rates. Ki notes 1,200+ active broker users and sub-10-second quoting, but does not disclose volumes.
    - Sources: Lloyd's 2025 Annual Report; Ki 2025 results; Inigo 2023 results; Munich Re 1840 syndicate accounts; Parsyl 1796 accounts.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Why SiaBs struggle to match established syndicates

    The 7pp combined-ratio gap between new entrants and mature syndicates (S&P Global) is not an accident. SiaBs face a stack of structural disadvantages, each compounding the others. The factors below are ordered from hardest to overcome (top) to most manageable (bottom).
    """
    )
    return


@app.cell
def _(go):
    difficulty_factors = [
        {
            "factor": "Expense ratio economics",
            "score": 10,
            "detail": "GBP 50m book @ 35% = GBP 17.5m OpEx budget vs. GBP 233m for avg syndicate",
        },
        {
            "factor": "Broker / distribution access",
            "score": 9,
            "detail": "No underwriting room; electronic-only; brokers default to proven capacity",
        },
        {
            "factor": "Reinsurance purchasing power",
            "score": 8,
            "detail": "Small cedants pay higher rates; less leverage at renewals",
        },
        {
            "factor": "Regulatory burden vs. size",
            "score": 8,
            "detail": "\"Not much less than a full-on syndicate\" despite light-touch promise",
        },
        {
            "factor": "3-year graduation clock",
            "score": 7,
            "detail": "Must hit KPIs or exit; creates pressure to chase volume or underprice",
        },
        {
            "factor": "Talent acquisition",
            "score": 7,
            "detail": "Competing with Beazley/Hiscox/QBE for specialist underwriters on startup pay",
        },
        {
            "factor": "Cat exposure restrictions",
            "score": 6,
            "detail": "5 major perils excluded; limits diversification and class mix",
        },
        {
            "factor": "Capital efficiency",
            "score": 6,
            "detail": "Same 35% SCR uplift as full syndicates; expensive per unit of premium",
        },
        {
            "factor": "Pricing data / actuarial credibility",
            "score": 5,
            "detail": "Novel lines lack historical loss data; models are thin in early years",
        },
        {
            "factor": "Brand and market reputation",
            "score": 4,
            "detail": "No track record; policyholders and brokers prefer rated, established names",
        },
        {
            "factor": "Technology infrastructure",
            "score": 3,
            "detail": "Asta provides back-office; but creates dependency and concentration risk",
        },
    ]

    difficulty_factors_sorted = sorted(
        difficulty_factors, key=lambda x: x["score"], reverse=True
    )

    diff_fig = go.Figure()

    colors = []
    for d in difficulty_factors_sorted:
        if d["score"] >= 9:
            colors.append("#e15759")
        elif d["score"] >= 7:
            colors.append("#f28e2b")
        elif d["score"] >= 5:
            colors.append("#edc948")
        else:
            colors.append("#59a14f")

    diff_fig.add_trace(
        go.Bar(
            y=[d["factor"] for d in difficulty_factors_sorted],
            x=[d["score"] for d in difficulty_factors_sorted],
            orientation="h",
            marker_color=colors,
            text=[f"{d['score']}/10" for d in difficulty_factors_sorted],
            textposition="inside",
            textfont=dict(color="white", size=13),
            customdata=[d["detail"] for d in difficulty_factors_sorted],
            hovertemplate="<b>%{y}</b><br>Difficulty: %{x}/10<br>%{customdata}<extra></extra>",
        )
    )

    diff_fig.update_layout(
        title="Difficulty factors for SiaBs matching established syndicates (ordered hardest to easiest)",
        xaxis=dict(title="Difficulty (1 = manageable, 10 = near-impossible)", range=[0, 11]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=80, l=250, r=40, b=50),
        height=500,
    )

    diff_fig.add_annotation(
        x=10.5,
        y="Cat exposure restrictions",
        text="Red = structural / near-impossible<br>Orange = severe<br>Yellow = significant<br>Green = manageable",
        showarrow=False,
        font=dict(size=10),
        align="left",
    )

    diff_fig
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Difficulty factor analysis (hardest to easiest):

    1. Expense ratio economics (10/10). This is the single biggest killer. A SiaB writing GBP 50m has ~GBP 17.5m to cover all operating expenses at the mandated 35% target. An average Lloyd's syndicate at GBP 667m has GBP 233m -- 13x more. Fixed costs (managing agent fees, actuarial, compliance, IT, audit) consume a much larger share of small books. Carbon 4747 solved this by growing fast enough to amortize costs; most SiaBs never reach escape velocity. The Lloyd's market-wide expense ratio is 35.6% -- SiaBs must hit the same target with a fraction of the premium base.

    2. Broker and distribution access (9/10). SiaBs cannot have a physical presence in Lloyd's underwriting room. They must use electronic placement only. This is a severe disadvantage in a market where relationships drive flow. Brokers have established panel capacity with proven syndicates; a new SiaB must convince brokers to route business to an unproven, small-capacity platform. Ki solved this by building an algorithmic quoting platform that delivers quotes in under 10 seconds -- but Ki launched as a full syndicate with \$350m+ capacity and Brit's entire book as a launchpad, not as a GBP 50m SiaB.

    3. Reinsurance purchasing power (8/10). Small cedants pay disproportionately higher reinsurance rates. A SiaB ceding GBP 10-20m of premium has minimal negotiating leverage compared to a syndicate ceding GBP 500m+. This directly impacts net combined ratios. The constraint is structural: you can't buy reinsurance at scale prices without scale premium.

    4. Regulatory burden relative to size (8/10). Despite the "light-touch" promise, multiple market participants told Insurance Insider that running a SiaB is "not much less than a full-on syndicate." Compliance, reporting, and governance costs are substantially fixed regardless of book size. Lloyd's provides the internal capital model for years 1-4, but every other regulatory obligation (conduct risk, sanctions screening, claims governance, reserving) applies in full. A GBP 50m syndicate bears essentially the same governance costs as a GBP 500m one.

    5. Three-year graduation clock (7/10). SiaBs must hit pre-agreed KPIs within 3 years or face exit. This creates perverse incentives: pressure to grow volume can lead to underpricing or writing marginal risks. The clock also means SiaBs cannot afford a bad loss year -- one major claim on a GBP 20m book can blow the combined ratio and jeopardize graduation. Established syndicates can absorb volatility across a diversified, multi-year book.

    6. Talent acquisition (7/10). SiaBs compete with Beazley, Hiscox, QBE, and other established Lloyd's syndicates for specialist underwriters, actuaries, and claims managers. Carbon grew from 4 to 51 employees -- but it had a clear growth trajectory and equity upside. Most SiaBs remain at 5-15 employees and lack the compensation packages or career stability that established syndicates offer. The talent pool for London market specialists is small and well-connected; the best underwriters know which platforms have staying power.

    7. Cat exposure restrictions (6/10). SiaBs can only write incidental exposure to Lloyd's five most significant catastrophe perils (US Wind, NA Earthquake, Japanese Wind/Earthquake, European Storm). This limits the classes of business available and reduces diversification. A monoline SiaB writing only clinical trials or carbon credits has no natural hedge against correlated losses in its book. Traditional syndicates can balance volatile cat business with stable short-tail lines.

    8. Capital efficiency (6/10). The same 35% SCR uplift applies to SiaBs and full syndicates. On a small book, the required Funds at Lloyd's represent a higher proportion of expected profit, reducing return on capital. The capital allocated to a GBP 50m SiaB might earn 5-8% RoC in good years vs. the Lloyd's market average of 22% in 2025.

    9. Pricing data and actuarial credibility (5/10). SiaBs often target novel or niche lines (carbon credits, clinical trial funding, parametric weather). By definition, these lack decades of historical loss data. Pricing models are thin, and actuarial reserving is uncertain. This is a genuine disadvantage but also the source of SiaBs' potential edge -- if they price correctly in an underserved market, the lack of competition can offset the data gap.

    10. Brand and market reputation (4/10). New SiaBs have no track record, no AM Best rating tied to their own history, and no established claims-paying reputation. Policyholders and brokers weigh these factors, especially for larger placements. However, the Lloyd's brand itself provides a baseline of credibility (Lloyd's security rating, Central Fund backing), which partially mitigates this. Carbon and Ki both leveraged the Lloyd's brand effectively in their early years.

    11. Technology infrastructure (3/10). This is the most manageable factor. Asta provides comprehensive back-office infrastructure (actuarial, compliance, finance, operations) to its ~10 SiaBs, eliminating the need to build from scratch. The trade-off is dependency: if Asta has capacity constraints or operational issues, multiple SiaBs are affected simultaneously. But as a practical matter, outsourcing to Asta is what makes the SiaB model viable at all.
    """
    )
    return


@app.cell
def _(go):
    names = [
        "Munich Re Innovation",
        "Carbon Underwriting",
        "Parsyl",
        "Picnic",
        "MCI",
        "Beazley ESG",
        "Greenlight Re",
        "MIC Global",
        "Sukoon (OIC)",
        "Wakam",
        "Wildfire Defense",
        "Oka",
        "MCI (2nd)",
        "Agile",
    ]
    synd_nums = [
        "1840", "4747", "1796", "2460",
        "1902", "4321", "3456", "5183",
        "2880", "1347", "1996", "1922",
        "1966", "2427",
    ]
    approved_years = [
        "2020", "2020", "2020", "2020",
        "2021", "2021", "2022", "2022",
        "2022", "2022", "2023", "2023",
        "2024", "2024",
    ]
    sectors = [
        "Parametric / emerging risks",
        "Property / casualty (coverholder)",
        "Cargo / logistics (perishables)",
        "Reinsurance (AU community mutuals)",
        "Life science / medical malpractice",
        "ESG multi-line consortium",
        "Insurtech / MGA capacity platform",
        "Micro / embedded insurance",
        "Reinsurance / property / marine",
        "European reinsurance",
        "Property (CA wildfire E&S)",
        "Carbon credit risk insurance",
        "Clinical trial funding insurance",
        "ANZ multi-line property / casualty",
    ]
    managing_agents = [
        "Munich Re Syn. Ltd",
        "Asta",
        "Asta (ex-Ascot)",
        "Asta",
        "Asta",
        "Beazley Mgmt",
        "Asta",
        "Asta",
        "Asta",
        "Polo",
        "Polo",
        "Asta",
        "Asta",
        "Asta",
    ]
    statuses = [
        "Ceased (2022)",
        "Graduated (2023)",
        "Active",
        "Inactive / run-off",
        "Graduated (likely)",
        "Run-off (2024)",
        "Active",
        "Closed (2024)",
        "Active (DIFC)",
        "Closed (<1yr)",
        "Active",
        "Active",
        "Run-off (2025)",
        "Active",
    ]
    capacities = [
        "Nil",
        "225.0",
        "15.8",
        "N/A",
        "143.5",
        "~15",
        "51.1",
        "27.5 (peak)",
        "65.8",
        "N/A",
        "~10",
        "7.0",
        "~35",
        "46.5",
    ]
    sponsors = [
        "Munich Re",
        "Independent MGU",
        "Parsyl Inc. / Gavi",
        "Picnic Labs",
        "MCI (specialist)",
        "Beazley",
        "Greenlight Capital Re",
        "MIC Global (Miami)",
        "Sukoon Insurance (UAE)",
        "Wakam (France)",
        "Wildfire Defense Sys.",
        "Oka (carbon insurer)",
        "MCI (specialist)",
        "Agile UW (Sydney)",
    ]

    status_colors = []
    for s in statuses:
        if "Ceased" in s or "Run-off" in s or "Closed" in s or "Inactive" in s:
            status_colors.append("#ffcccc")
        elif "Graduated" in s:
            status_colors.append("#cce5ff")
        else:
            status_colors.append("#ccffcc")

    roster_fig = go.Figure()

    roster_fig.add_trace(
        go.Table(
            header=dict(
                values=[
                    "Name",
                    "Syn #",
                    "Approved",
                    "Sector",
                    "Managing Agent",
                    "Sponsor / Backer",
                    "Status",
                    "Capacity<br>(GBP m)",
                ],
                fill_color="#4e79a7",
                font=dict(color="white", size=11),
                align="left",
            ),
            cells=dict(
                values=[
                    names,
                    synd_nums,
                    approved_years,
                    sectors,
                    managing_agents,
                    sponsors,
                    statuses,
                    capacities,
                ],
                fill_color=[
                    status_colors,
                    status_colors,
                    status_colors,
                    status_colors,
                    status_colors,
                    status_colors,
                    status_colors,
                    status_colors,
                ],
                font=dict(size=10),
                align="left",
                height=28,
            ),
        )
    )

    roster_fig.update_layout(
        title="Complete SiaB roster: all 14 approved syndicates (2020-2024)",
        margin=dict(t=60, l=20, r=20, b=20),
        height=520,
    )

    roster_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Roster notes:
    - Green = active. Blue = graduated. Red = closed/ceased/run-off.
    - Parsyl 1796 was created in partnership with Gavi (The Vaccine Alliance) to insure COVID-19 vaccine transportation to emerging economies via the Global Health Risk Facility (GHRF). It transferred from Ascot Underwriting to Asta in August 2022.
    - Sukoon 2880 is the first SiaB to operate outside London, based in the Dubai International Financial Centre (DIFC). Oman Insurance Company rebranded to Sukoon Insurance in October 2022 (legal name change completed shortly after).
    - Greenlight Re 3456 accepted third-party capital for the first time in 2025 and absorbed MIC Global (former SiaB 5183) as a coverholder after its closure.
    - MCI is the only sponsor to launch two SiaBs: 1902 (medical malpractice/life science) and 1966 (clinical trial funding using AI-assisted underwriting via GATC Health).
    - Oka 1922 insures carbon credit buyer-side risks -- a novel product covering financial, reputational, regulatory, and climate risks on carbon credits.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Appendix: SiaB Application and Approval Process

    Lloyd's formal 6-step process (the table above condenses steps 2-3 into "Triage" and adds a post-approval "Making it Happen" phase):
    1. Initial confidential discussion with Lloyd's Entrants team (outcome within 2 working days)
    2. Pre-application engagement -- applicant need not have finalized their managing agent choice
    3. Formal application submission
    4. Business Opportunities Committee review -- managing agent must be identified; application fee invoiced
    5. Council of Lloyd's grants "in-principle" approval
    6. Final "Permission to Underwrite" granted after completion of remaining checks

    Selectivity indicators:
    - Only 14 approvals across ~6 years of the programme
    - Lloyd's stated there were "10 proposals in the pipeline" early on, but many never materialized
    - Requirements: differentiation/innovation in product or distribution, operation through existing and tested technology, credible disruption to traditional practices
    - All entrants must have a credible capital backer, competent management team, and viable business plan
    - Approvals slowed but did not stop between the 2022 cohort and the 2023 approvals (Wildfire Defense 1996 in July 2023, Oka 1922 in October 2023) -- a gap of roughly 7-8 months, suggesting selectivity rather than absent demand
    - Lloyd's does not publicly disclose rejection rates

    Lloyd's Lab pipeline: Lloyd's Lab is a 10-week insurtech accelerator selecting ~10 teams from 150-200 applications per cohort. Parsyl and Oka came through innovation channels, but the Lab-to-SiaB pipeline is informal -- most Lab graduates become coverholders or technology partners, not syndicate operators.

    ---

    ## Assessment: stepping stone or failed experiment?

    Lloyd's original expectation was "a third transitioning, a third failing, and a third remaining small." Actual results roughly match -- but the total pool of entrants (14) was far smaller than hoped.

    Key structural problems:
    - The GBP 100m year-one cap and monoline/short-tail restriction constrain diversification and scale.
    - The "light-touch" regulatory promise did not materialise -- running a SiaB is "not much less than a full-on syndicate."
    - Munich Re as the inaugural SiaB sent the wrong message about the programme targeting innovative startups.
    - Combined active SiaB GWP of ~GBP 133.7m (excluding graduated Carbon 4747) is negligible against Lloyd's GBP 57.9bn total (0.23%).

    Counterargument:
    - Carbon 4747 is genuine proof-of-concept: startup to ~GBP 204m GWP (2024) via the SiaB launchpad.
    - The broader market trend favours smaller syndicates: small-syndicate capacity share grew 22% YoY in 2025.
    - Lloyd's projects 62.5% of accretive 2026 growth from new entrants and structured solutions.
    - "There is a need to accept some failures are inevitable in innovation, rather than treating each closure as a programme-level setback."

    The SiaB concept is sound -- lower barriers, faster time to market, fail-fast ethos. The execution has been mixed, and 14 entrants in 7 years is a thin pipeline for a GBP 58bn market. The programme may evolve or be superseded by alternative low-barrier entry mechanisms.

    ---

    Sources: Lloyd's official reports and SiaB guides (January 2023, April 2024 PDFs); Insurance Insider SiaB analysis (2026); Carrier Management; Insurance Journal; Reinsurance News; Asta website; Ki, Inigo, Carbon, Greenlight Re financial disclosures; S&P Global; Howden Re; Oxbow Partners; Lloyd's Lab Impact Report; PwC Lloyd's Market Oversight 2026.
    """
    )
    return


if __name__ == "__main__":
    app.run()
