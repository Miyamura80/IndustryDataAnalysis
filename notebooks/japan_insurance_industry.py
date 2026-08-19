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
    # Japan's Big Three insurers are escaping a shrinking home market

    ## Japanese insurance market structure

    Japan is the ~3rd-4th largest insurance market globally (~JPY 52.6T / ~\$350B in annual premiums; ~4th by total premiums, behind the US, China and the UK). The non-life (P&C) market is extremely concentrated — the "Big Three" groups (Tokio Marine, MS&AD, Sompo) hold ~85% domestic market share. The life insurance market is the 3rd largest globally (behind the US and China; China overtook Japan years ago), with ~90% household penetration. All three P&C giants are aggressively expanding overseas to escape Japan's shrinking domestic market.
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    return (go,)


@app.cell
def _(go, mo):
    _big3_names = ["Tokio Marine", "MS&AD", "Sompo"]
    _domestic_jpy = [3004, 3147, 2046]
    _intl_jpy = [2886, 1527, 1308]
    _total_jpy = [d + i for d, i in zip(_domestic_jpy, _intl_jpy)]

    _big3_fig = go.Figure()

    _big3_fig.add_trace(
        go.Bar(
            y=_big3_names,
            x=_domestic_jpy,
            name="Domestic P&C",
            orientation="h",
            marker_color="#1f77b4",
            text=[f"¥{v / 1000:.1f}T" for v in _domestic_jpy],
            textposition="inside",
            insidetextanchor="middle",
            customdata=[round(v / 150, 1) for v in _domestic_jpy],
            hovertemplate="<b>%{y}</b><br>Domestic P&C: ¥%{x:,.0f}B (~$%{customdata:.1f}B)<extra></extra>",
        )
    )

    _big3_fig.add_trace(
        go.Bar(
            y=_big3_names,
            x=_intl_jpy,
            name="International P&C",
            orientation="h",
            marker_color="#ff7f0e",
            text=[f"¥{v / 1000:.1f}T" for v in _intl_jpy],
            textposition="inside",
            insidetextanchor="middle",
            customdata=[round(v / 150, 1) for v in _intl_jpy],
            hovertemplate="<b>%{y}</b><br>International P&C: ¥%{x:,.0f}B (~$%{customdata:.1f}B)<extra></extra>",
        )
    )

    for _i, (_comp, _tot, _intl) in enumerate(
        zip(_big3_names, _total_jpy, _intl_jpy)
    ):
        _big3_fig.add_annotation(
            x=_tot,
            y=_comp,
            text=f"  {_intl / _tot * 100:.0f}% intl",
            showarrow=False,
            xanchor="left",
            font=dict(size=11, color="#ff7f0e"),
        )

    _big3_fig.update_layout(
        title=(
            "Japan's Big Three P&C insurers: domestic vs. international NPW (FY2024, JPY billions)"
        ),
        barmode="stack",
        xaxis=dict(title="Premiums (JPY billions)"),
        yaxis=dict(autorange="reversed"),
        height=300,
        margin=dict(t=90, l=130, r=100, b=50),
        legend=dict(x=0.45, y=1.18, orientation="h"),
    )

    mo.ui.plotly(_big3_fig)
    return


@app.cell
def _(go, mo):
    _fy_labels = [f"FY{y}" for y in range(2014, 2027)]

    _tokio_intl_pct = [39, 44, 45, 45, 45, 44, 46, 45, 43, 46, 49, 57, 59]
    _sompo_intl_pct = [8, 13, 17, 23, 24, 21, 25, 28, 38, 39, 39, 44, 51]
    _msad_intl_pct = [11, 12, 14, 16, 18, 18, 19, 21, 27, 29, 33, 35, 37]

    _intl_fig = go.Figure()

    _intl_fig.add_trace(
        go.Scatter(
            x=_fy_labels,
            y=_tokio_intl_pct,
            name="Tokio Marine",
            mode="lines+markers",
            line=dict(color="#1f77b4", width=3),
            marker=dict(size=7),
            hovertemplate="<b>Tokio Marine</b><br>%{x}: %{y}% international<extra></extra>",
        )
    )

    _intl_fig.add_trace(
        go.Scatter(
            x=_fy_labels,
            y=_sompo_intl_pct,
            name="Sompo",
            mode="lines+markers",
            line=dict(color="#ff7f0e", width=3),
            marker=dict(size=7),
            hovertemplate="<b>Sompo</b><br>%{x}: %{y}% international<extra></extra>",
        )
    )

    _intl_fig.add_trace(
        go.Scatter(
            x=_fy_labels,
            y=_msad_intl_pct,
            name="MS&AD",
            mode="lines+markers",
            line=dict(color="#2ca02c", width=3),
            marker=dict(size=7),
            hovertemplate="<b>MS&AD</b><br>%{x}: %{y}% international<extra></extra>",
        )
    )

    _intl_fig.add_hline(
        y=50,
        line_dash="dash",
        line_color="grey",
        line_width=1,
        annotation_text="50% — majority international",
        annotation_position="top left",
        annotation_font_size=10,
        annotation_font_color="grey",
    )

    _intl_fig.add_annotation(
        x="FY2015",
        y=44,
        text="HCC ($7.5B)",
        showarrow=True,
        arrowhead=2,
        ax=40,
        ay=-30,
        font=dict(size=9, color="#1f77b4"),
    )

    _intl_fig.add_annotation(
        x="FY2017",
        y=23,
        text="Endurance ($6.3B)",
        showarrow=True,
        arrowhead=2,
        ax=55,
        ay=25,
        font=dict(size=9, color="#ff7f0e"),
    )

    _intl_fig.add_annotation(
        x="FY2016",
        y=14,
        text="MS Amlin (£3.5B / ~$5.3B)",
        showarrow=True,
        arrowhead=2,
        ax=-55,
        ay=25,
        font=dict(size=9, color="#2ca02c"),
    )

    _intl_fig.add_annotation(
        x="FY2025",
        y=44,
        text="Aspen ($3.5B)",
        showarrow=True,
        arrowhead=2,
        ax=-50,
        ay=30,
        font=dict(size=9, color="#ff7f0e"),
    )

    _intl_fig.add_vrect(
        x0="FY2025",
        x1="FY2026",
        fillcolor="grey",
        opacity=0.08,
        line_width=0,
    )
    _intl_fig.add_annotation(
        x="FY2026",
        y=3,
        text="← FY2026 projected",
        showarrow=False,
        font=dict(size=9, color="grey"),
        xanchor="center",
    )

    _intl_fig.update_layout(
        title="Big Three internationalization: overseas share of P&C premiums (FY2014-FY2026)",
        xaxis=dict(title=""),
        yaxis=dict(title="International % of total P&C premiums", range=[0, 65]),
        height=450,
        margin=dict(t=80, l=60, r=40, b=50),
        legend=dict(x=0.02, y=0.98),
        hovermode="x unified",
    )

    mo.ui.plotly(_intl_fig)
    return


@app.cell
def _(mo):
    mo.md(
        """
    Internationalization trend notes:
    - Tokio Marine led earliest and most aggressively. The HCC Insurance acquisition (FY2015, \$7.5B) was the inflection point that lifted international to ~44%. In FY2025, Tokio Marine crossed the 50% threshold at ~57% — international NPW (JPY 3.57T) now substantially exceeds domestic (~JPY 2.7T). The majority of Tokio Marine's P&C business is now outside Japan.
    - Sompo's overseas expansion was catalyzed by the Endurance Specialty acquisition (FY2017, \$6.3B). International share jumped from ~8% to ~23% in three years. The Aspen acquisition (\$3.5B, completed Feb 2026) adds >US\$4.6B in annual GWP — only ~2 months are captured in FY2025, but FY2026 will be the first full year. Sompo is projected to cross 50% international by FY2026.
    - MS&AD has been the most conservative. The MS Amlin acquisition (FY2016, ~£3.5B / ~\$5.3B) gave it Lloyd's access but overseas share has grown more slowly, reaching ~35% by FY2025. MS&AD has earmarked \$4.4B for further North American acquisitions and will merge its two domestic subsidiaries (MSI + ADI) by April 2027.
    - FY2026 figures (shaded area) are projected from mid-term management plan targets and analyst estimates. FY2025 figures are from annual results published May 20, 2026 — Tokio Marine international NPW is confirmed; Sompo domestic (JPY 2,126B) is confirmed; MS&AD total NPW (~JPY 5.0T) is confirmed. Segment splits for MS&AD and Sompo international are estimated from available data.
    - Caveat: the FY2022-FY2025 acceleration in international % partly reflects JPY depreciation (USD/JPY moved from ~110 to ~150), which mechanically inflates yen-denominated overseas premiums. Organic growth is real but somewhat overstated in JPY terms.
    - All three are unwinding ~\$60B in cross-held equity shares (by March 2031), freeing capital for further international M&A.
    """
    )
    return


@app.cell
def _(go, mo):
    _big3_co = ["Tokio Marine\n(TMNF)", "MS&AD\n(MSI+ADI)", "Sompo\n(Sompo Japan)"]
    _big3_totals = [3004, 3147, 2046]

    _lob_names = [
        "Voluntary Auto",
        "Fire & Allied",
        "Casualty / Liability",
        "CALI (compulsory auto)",
        "Personal Accident",
        "Marine & Other",
    ]
    _lob_colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc949"]
    _lob_data = {
        "Voluntary Auto": [1415, 1518, 970],
        "Fire & Allied": [721, 729, 480],
        "Casualty / Liability": [550, 582, 385],
        "CALI (compulsory auto)": [144, 157, 105],
        "Personal Accident": [99, 96, 65],
        "Marine & Other": [75, 65, 41],
    }

    _lob_fig = go.Figure()
    for _line, _color in zip(_lob_names, _lob_colors):
        _vals = _lob_data[_line]
        _pcts = [v / t * 100 for v, t in zip(_vals, _big3_totals)]
        _lob_fig.add_trace(
            go.Bar(
                y=_big3_co,
                x=_pcts,
                name=_line,
                orientation="h",
                marker_color=_color,
                customdata=_vals,
                hovertemplate=(
                    "<b>%{y}</b><br>"
                    + _line
                    + "<br>¥%{customdata:,.0f}B (%{x:.1f}%)<extra></extra>"
                ),
                text=[f"{p:.0f}%" if p >= 4 else "" for p in _pcts],
                textposition="inside",
                insidetextanchor="middle",
            )
        )

    for _i, (_co, _tot) in enumerate(zip(_big3_co, _big3_totals)):
        _lob_fig.add_annotation(
            x=100,
            y=_co,
            text=f"  ¥{_tot / 1000:.1f}T",
            showarrow=False,
            xanchor="left",
            font=dict(size=10, color="grey"),
        )

    _lob_fig.update_layout(
        title="Domestic P&C premium by line of business (FY2024 est., % of domestic NPW)",
        barmode="stack",
        xaxis=dict(title="% of domestic P&C NPW", range=[0, 108]),
        yaxis=dict(autorange="reversed"),
        height=300,
        margin=dict(t=80, l=160, r=60, b=50),
        legend=dict(x=0.0, y=-0.35, orientation="h"),
    )

    mo.ui.plotly(_lob_fig)
    return


@app.cell
def _(go, mo):
    _cyber_names = ["Tokio Marine", "Sompo", "MS&AD"]
    _cyber_usd_m = [425, 325, 30]
    _total_usd_b = [34, 29, 31]
    _us_rank = ["#4 (5.0%)", "#9 (3.7%)", "#37 (0.3%)"]
    _cyber_pct = [1.3, 1.1, 0.1]
    _cyber_entity = [
        "TMHCC Cyber & Professional Lines",
        "Sompo Intl North America",
        "Small US subsidiary book",
    ]

    _cyber_fig = go.Figure()

    _cyber_fig.add_trace(
        go.Bar(
            y=_cyber_names,
            x=_cyber_usd_m,
            orientation="h",
            marker_color=["#1f77b4", "#ff7f0e", "#2ca02c"],
            hovertemplate="<b>%{y}</b><br>Cyber premium: $%{x}M<extra></extra>",
        )
    )

    for _i, (_name, _cyber, _total, _rank, _pct, _ent) in enumerate(
        zip(
            _cyber_names,
            _cyber_usd_m,
            _total_usd_b,
            _us_rank,
            _cyber_pct,
            _cyber_entity,
        )
    ):
        _cyber_fig.add_annotation(
            x=_cyber + 10,
            y=_name,
            text=f"${_cyber}M — US rank {_rank} — {_pct}% of ~${_total}B total P&C",
            showarrow=False,
            xanchor="left",
            font=dict(size=10),
        )

    _cyber_fig.update_layout(
        title="Cyber insurance books: Big Three global cyber premium (est. USD millions, 2024)",
        xaxis=dict(
            title="Estimated global cyber premium (USD millions)",
            range=[0, 800],
        ),
        yaxis=dict(autorange="reversed"),
        height=260,
        margin=dict(t=80, l=130, r=40, b=50),
    )

    mo.ui.plotly(_cyber_fig)
    return


@app.cell
def _(mo):
    mo.md(
        """
    P&C portfolio and cyber exposure notes:

    The domestic P&C mix is remarkably uniform across all three — auto insurance dominates at ~47%, followed by fire/property at ~23% and casualty and other lines at ~30%. This is a structural feature of the Japanese market: auto insurance is mandatory, homeowner fire policies are widespread, and the Big Three's agent/dealer distribution channels are optimized for these mass-market products. The breakdown is based on GIAJ industry data applied to each company's domestic total.

    Cyber is tiny relative to total P&C. Tokio Marine is the largest cyber writer among the Big Three, with an estimated ~\$425M global cyber book (~1.3% of total P&C), primarily through TMHCC's Cyber & Professional Lines Group — ranked #4 in the US with 5.0% market share. Sompo writes ~\$325M (~1.1% of total P&C), ranked #9 in the US, through Sompo International North America; the Aspen acquisition (closed FY2025) adds further cyber capacity. MS&AD is a negligible cyber player at ~\$30M (0.1% of total P&C) — notably, MS Amlin exited cyber underwriting at Lloyd's entirely in October 2020. Combined, the Big Three write ~\$780M in cyber, roughly 4.7% of the \$16.5B global cyber market.

    International P&C composition varies dramatically. Tokio Marine's overseas platform is the most diversified: TMHCC (specialty, 18 product lines, ~\$8B GWP), PHLY (120+ niche commercial markets, ~\$3B), DFG (excess workers' comp market leader, ~\$3B), and Tokio Marine Kiln (Lloyd's syndicate, ~\$2.3B GWP). Sompo International operates five segments: North America (\$5.0B), SompoRe reinsurance (\$4.5B), Global Markets (\$3.0B), AgriSompo crop insurance (\$2.6B), and Consumer (\$1.4B). The Aspen acquisition (\$4.6B GWP, completed Feb 2026) will add substantially to this platform from FY2025 onward. MS&AD's international presence is narrower, centered on MS Amlin (Lloyd's reinsurance, \$2.2B GWP, combined ratio 87.2%).

    Data sources: NAIC US cyber DWP rankings (2024 statutory data via Beinsure/Insurance Business). Domestic line breakdown estimated from GIAJ FY2024 industry class data. International platform data from company IR presentations and annual reports. Cyber estimates combine US NAIC data with Lloyd's and other international disclosures.
    """
    )
    return


@app.cell
def _(go, mo):
    _jp = "\U0001f1ef\U0001f1f5"
    _us = "\U0001f1fa\U0001f1f8"
    _root_jp = f"Japan Insurance Market {_jp}"

    _tm_labels_jp = [
        _root_jp,
        "Non-Life (P&C)", "Life Insurance",
        "Big Three (P&C)", "Foreign / Other (P&C)",
        "Big Four Life", "Other Major Life", "Other Life Insurers",
        f"MS&AD {_jp}", f"Tokio Marine {_jp}", f"Sompo {_jp}",
        f"AIG Japan {_us}", "Other Non-Life",
        f"Nippon Life {_jp}", f"Dai-ichi Life {_jp}",
        f"Meiji Yasuda {_jp}", f"Sumitomo Life {_jp}",
        f"T&D Holdings {_jp}", f"Japan Post (Kampo) {_jp}",
        f"Sony Life {_jp}", f"Aflac Japan {_us}",
    ]

    _tm_parents_jp = [
        "",
        _root_jp, _root_jp,
        "Non-Life (P&C)", "Non-Life (P&C)",
        "Life Insurance", "Life Insurance", "Life Insurance",
        "Big Three (P&C)", "Big Three (P&C)", "Big Three (P&C)",
        "Foreign / Other (P&C)", "Foreign / Other (P&C)",
        "Big Four Life", "Big Four Life", "Big Four Life", "Big Four Life",
        "Other Major Life", "Other Major Life", "Other Major Life", "Other Major Life",
    ]

    _tm_values_jp = [
        52600,
        9600, 43000,
        8197, 1403,
        22330, 7080, 13590,
        3147, 3004, 2046,
        463, 940,
        7860, 6800, 4300, 3370,
        2500, 2480, 1100, 1000,
    ]

    _tm_hover_jp = [
        "~4th largest insurance market globally by total premiums (~3rd in life). ~$350B in annual premiums.",
        "Big Three hold ~85% domestic share. Motor (~47%), property (~23%), other lines (~30%).",
        "3rd largest life market globally (behind US and China). ~90% of households carry life insurance.",
        "~85% combined domestic P&C market share. All three expanding aggressively overseas.",
        "AIG is the largest foreign non-life insurer in Japan.",
        "Four largest private life insurers by premium income.",
        "Includes govt-affiliated (Kampo), foreign (Aflac), and conglomerate players.",
        "Smaller mutuals (Asahi), foreign players (Zurich, Allianz), cooperative insurance.",
        "Largest domestic P&C group (FY2024). MSI + ADI planning merger by April 2027.",
        "Oldest (est. 1879). International NPW (¥2.9T) rivals domestic (¥3.0T).",
        "3rd largest domestic P&C. Acquired Aspen for $3.5B (Feb 2026). Also runs 300+ nursing care facilities.",
        "Largest foreign non-life insurer. ¥463B premiums. Medical and group accident focus.",
        "Kyoei Fire, Nisshin Fire, Chubb Japan, Zurich, Allianz, and others.",
        "Largest private life insurer. Group assets >¥89T. GWP ¥7.86T.",
        "2nd largest. Adjusted profit ¥440B (+38% YoY). Strong overseas expansion.",
        "Targeting ¥5T by FY2026. Yen-denominated savings products booming (+30% H1).",
        "4th largest private life insurer. Premium growth +4.0% in H1 FY2025.",
        "Taiyo Life + Daido Life. Daido specializes in SME insurance market.",
        "Govt-affiliated. Declining book, but new policies doubled to 628K in FY2024.",
        "Sony Financial Group subsidiary. Growing in savings-type products.",
        "US company, but Japan = >70% of global pretax earnings. ~70% cancer insurance share.",
    ]

    _tm_colors_jp = [
        "lightgrey",
        "#4e79a7", "#e88c2a",
        "#6a9ecf", "#a5cae8",
        "#f5a54a", "#f7bc6d", "#f9d390",
        "#5b8db8", "#6fa3c7", "#83b5d1",
        "#90c4de", "#aed4ea",
        "#e8942f", "#eda04a", "#f2ac65", "#f5b87e",
        "#f0c06a", "#f3ca7f", "#f6d494", "#f9deaa",
    ]

    _jp_treemap = go.Figure(
        go.Treemap(
            labels=_tm_labels_jp,
            parents=_tm_parents_jp,
            values=_tm_values_jp,
            branchvalues="total",
            customdata=_tm_hover_jp,
            hovertemplate="<b>%{label}</b><br>¥%{value:,.0f}B<br>%{customdata}<extra></extra>",
            texttemplate="<b>%{label}</b><br>¥%{value:,.0f}B<br>%{percentParent:.1%}",
            marker=dict(colors=_tm_colors_jp),
        )
    )

    _jp_treemap.update_layout(
        title="Japanese insurance market by company (FY2024, JPY billions, domestic premiums)",
        height=700,
        margin=dict(t=80, l=10, r=10, b=10),
    )

    mo.ui.plotly(_jp_treemap)
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the charts above:

    The stacked bar shows how each of the Big Three splits between domestic Japan P&C and international operations (all figures NPW; the bar is charted on FY2024). On that FY2024 basis Tokio Marine's international segment (JPY 2.9T) roughly rivals its domestic book (JPY 3.0T); on FY2025 reported results international (JPY 3.57T) has moved clearly ahead of domestic (~JPY 2.7T) — a shift driven by acquisitions like HCC Insurance (\$7.5B, 2015) and Philadelphia Consolidated. Sompo's international NPW (~JPY 1.3T after reinsurance cessions; GWP is ~JPY 2.5T including Endurance; the Aspen acquisition closed in FY2025 and will shift this balance further). MS&AD has the largest domestic P&C book but the smallest international presence, though it plans further North American acquisitions and will merge its two domestic subsidiaries (MSI + ADI) by April 2027. All three groups are diversifying overseas because Japan's shrinking population caps domestic growth — the Big Three already control ~85% of a market that cannot expand.

    The treemap shows the full domestic insurance landscape. Life insurance (JPY 43T) dwarfs P&C (JPY 9.6T) by premium volume — Japan has the 3rd largest life market globally (behind the US and China), with ~90% household penetration. Nippon Life (JPY 7.86T) alone is about 82% the size of the entire domestic P&C market. Notable foreign players include AIG (largest foreign non-life insurer) and Aflac, a US company that earns >70% of its global pretax profits from Japan and holds ~70% of the cancer insurance market.

    On health insurance: Japan has universal public health coverage (National Health Insurance / Employee Health Insurance), so private health products occupy the "third sector" — supplementary medical, cancer, and nursing care policies. This segment (~JPY 7.2T in annualized premiums in force) sits between life and non-life regulation. Aflac pioneered cancer insurance in Japan in 1974 and still dominates it. The aging population (29% of Japanese are 65+) is shifting demand from traditional death-benefit life policies toward medical and nursing care products — health/medical insurance is now the leading category for new individual policy sales.

    Data sources: Tokio Marine, MS&AD, and Sompo FY2024 investor presentations (May 2025). Life insurance data from Japan FSA and Life Insurance Association of Japan. Third-sector figures from LIAJ Fact Book 2025. Exchange rate: ~JPY 150/USD. All stacked bar figures use NPW (net premiums written, i.e. after ceding to reinsurers). Sompo International's GWP is substantially higher (~JPY 2.5T) than its NPW (~JPY 1.3T) due to large reinsurance cessions, particularly through SompoRe.
    """
    )
    return


if __name__ == "__main__":
    app.run()
