# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pyzmq",
#     "plotly",
#     "pandas",
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


@app.cell
def _(mo):
    mo.md(
        """
    ---

    # Robotics actuators: the value is in the joint, not the motor

    The headline actuator market above is dominated by valves, HVAC and automotive mechatronics. The interesting structural story is narrower: the actuation stack inside robotic arms, cobots, humanoids and legged robots.

    Core thesis (tested below):

    - The most valuable layer is not generic motors. It is the precision reducer and the integrated joint module.
    - Precision reducers (RV/cycloidal and harmonic/strain-wave) carry the strongest moat today, evidenced by Nabtesco's dominance of medium/large robot joints.
    - Integrated joint modules (motor + reducer + encoder + brake + drive + sensors in one package) are the emerging battleground for humanoids and cheap robotics.

    Do not treat "actuators" as one market. The robotics actuation stack splits into four layers, analysed separately below: precision reducers, motors and drives, integrated joint modules, and the robot OEMs that buy from all three.
    """
    )
    return


@app.cell
def _():
    import pandas as pd

    nan = float("nan")

    robotics_actuator_companies = [
        # --- Precision reducers ---
        {
            "company": "Nabtesco",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Precision reducer",
            "product_category": "RV / cycloidal reducers",
            "robotics_relevance": "Core joints of medium/large industrial robot arms",
            "known_market_share_pct": 60.0,
            "market_share_scope": "Precision reducers for medium/large industrial robot joints",
            "market_share_geography": "Global",
            "market_share_year": 2019,
            "source_url": "https://www.nabtesco.com/en/products/robot/",
            "confidence": "high",
            "notes": "Company's own estimate; ~90% in heavy-load RV specifically. Chinese entrants eroding share since.",
        },
        {
            "company": "Harmonic Drive Systems (HDSI)",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Precision reducer",
            "product_category": "Harmonic / strain-wave reducers + integrated actuators",
            "robotics_relevance": "Wrists, cobots, humanoid rotary joints",
            "known_market_share_pct": 12.1,
            "market_share_scope": "China strain-wave gearing devices market",
            "market_share_geography": "China",
            "market_share_year": 2024,
            "source_url": "",
            "confidence": "low",
            "notes": "Global strain-wave segment est. ~50% (research-firm, low conf). HDSI / Harmonic Drive SE / LLC are affiliated; some reports lump them. Primary URL for the 12.1% China figure still pending.",
        },
        {
            "company": "Sumitomo Drive Technologies",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Precision reducer",
            "product_category": "Fine Cyclo cycloidal reducers",
            "robotics_relevance": "Robot joints",
            "known_market_share_pct": nan,
            "market_share_scope": "Global precision reducers (#3 behind Nabtesco, Harmonic)",
            "market_share_geography": "Global",
            "market_share_year": nan,
            "source_url": "https://growthmarketreports.com/report/industrial-robot-speed-reducer-market-global-industry-analysis",
            "confidence": "low",
            "notes": "No clean standalone %; consistently named #3, low-single-digit residual after Nabtesco + Harmonic.",
        },
        {
            "company": "Leaderdrive (绿的谐波)",
            "hq_country": "China",
            "region": "China",
            "layer": "Precision reducer",
            "product_category": "Harmonic / strain-wave reducers",
            "robotics_relevance": "Cobot, humanoid, light robot joints",
            "known_market_share_pct": 60.0,
            "market_share_scope": "China domestic robot-grade harmonic reducers (legacy company claim)",
            "market_share_geography": "China",
            "market_share_year": 2017,
            "source_url": "https://www.leaderdrive.com/about/profile.html",
            "confidence": "low",
            "notes": "Legacy promotional figure. Total China harmonic share ~26% (2022); global ~7-8% (2023, GGII). NOT apples-to-apples with Nabtesco's 60%.",
        },
        {
            "company": "Laifual (来福谐波)",
            "hq_country": "China",
            "region": "China",
            "layer": "Precision reducer",
            "product_category": "Harmonic / strain-wave reducers",
            "robotics_relevance": "Cobot, light robot joints",
            "known_market_share_pct": nan,
            "market_share_scope": "China domestic harmonic reducers (#2 domestic)",
            "market_share_geography": "China",
            "market_share_year": nan,
            "source_url": "",
            "confidence": "low",
            "notes": "26% claim circulates in trade press, not a filing; likely conflated with Leaderdrive. Treat as unknown.",
        },
        {
            "company": "Qinchuan Machine Tool (秦川机床)",
            "hq_country": "China",
            "region": "China",
            "layer": "Precision reducer",
            "product_category": "RV reducers",
            "robotics_relevance": "Industrial robot joints",
            "known_market_share_pct": nan,
            "market_share_scope": "China RV reducers (sub-5%, non-top-tier)",
            "market_share_geography": "China",
            "market_share_year": 2023,
            "source_url": "https://www.chyxx.com/industry/1160839.html",
            "confidence": "low",
            "notes": "Real domestic RV maker but absent from GGII top-share tables.",
        },
        {
            "company": "Shuanghuan / Huandong (双环传动 / 环动科技)",
            "hq_country": "China",
            "region": "China",
            "layer": "Precision reducer",
            "product_category": "RV reducers",
            "robotics_relevance": "Industrial robot joints",
            "known_market_share_pct": 18.89,
            "market_share_scope": "China RV reducer market",
            "market_share_geography": "China",
            "market_share_year": 2023,
            "source_url": "http://static.sse.com.cn/stock/disclosure/announcement/c/202411/002040_20241125_ZBJC.pdf",
            "confidence": "high",
            "notes": "GGII data via Huandong STAR-board IPO prospectus. 2021/22/23 = 10.11/13.65/18.89%; #2 domestic behind Nabtesco.",
        },
        # --- Motors and drives ---
        {
            "company": "Yaskawa",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Servo motor / drive",
            "product_category": "AC servo motors & drives; Motoman robots",
            "robotics_relevance": "Servo leader + top-tier robot OEM",
            "known_market_share_pct": 16.0,
            "market_share_scope": "Global AC servo-drive market",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.mordorintelligence.com/industry-reports/global-servo-motor-market",
            "confidence": "moderate",
            "notes": "Also ~7-8% global industrial robots (by value). Largest servo vendor by units.",
        },
        {
            "company": "Mitsubishi Electric",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Servo motor / drive",
            "product_category": "MELSERVO AC servo motors & drives",
            "robotics_relevance": "General + robot servo",
            "known_market_share_pct": nan,
            "market_share_scope": "Global AC servo (est. 15-20%, leader in APAC)",
            "market_share_geography": "Global",
            "market_share_year": 2025,
            "source_url": "https://www.gminsights.com/industry-analysis/asia-pacific-ac-servo-motors-and-drives-market",
            "confidence": "low",
            "notes": "Range estimate from research firms; not robotics-specific. Vies with Yaskawa for #1.",
        },
        {
            "company": "Panasonic Industry",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Servo motor / drive",
            "product_category": "MINAS AC servo motors",
            "robotics_relevance": "General servo",
            "known_market_share_pct": nan,
            "market_share_scope": "Global AC servo (~10%, low conf)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "",
            "confidence": "low",
            "notes": "Single weak secondary source for the ~10%.",
        },
        {
            "company": "Inovance (汇川技术)",
            "hq_country": "China",
            "region": "China",
            "layer": "Servo motor / drive",
            "product_category": "AC servo systems, drives, inverters",
            "robotics_relevance": "Component servo for robots & automation",
            "known_market_share_pct": 28.0,
            "market_share_scope": "China general AC servo systems",
            "market_share_geography": "China",
            "market_share_year": 2024,
            "source_url": "https://jzgkchina.com/node/2856",
            "confidence": "high",
            "notes": "MIR data; #1 China general servo ahead of Siemens (~10-11%) and Yaskawa (~7-8%).",
        },
        {
            "company": "Leadshine (雷赛智能)",
            "hq_country": "China",
            "region": "China",
            "layer": "Servo motor / drive",
            "product_category": "Stepper & servo drives/motors",
            "robotics_relevance": "Component motion control",
            "known_market_share_pct": nan,
            "market_share_scope": "China stepper (leader) & general servo (#2-tier)",
            "market_share_geography": "China",
            "market_share_year": 2023,
            "source_url": "https://www.chinabaogao.com/detail/699671.html",
            "confidence": "low",
            "notes": "No clean sourced %.",
        },
        {
            "company": "Siemens",
            "hq_country": "Germany",
            "region": "Europe",
            "layer": "Servo motor / drive",
            "product_category": "SINAMICS drives, SIMOTICS motors",
            "robotics_relevance": "Factory servo + physical-AI orchestration",
            "known_market_share_pct": nan,
            "market_share_scope": "Global drives/servo; ~10-11% China servo",
            "market_share_geography": "Global",
            "market_share_year": 2025,
            "source_url": "https://press.siemens.com/global/en/pressrelease/siemens-and-humanoid-bring-physical-ai-factory-floor-deploying-humanoids-industrial",
            "confidence": "low",
            "notes": "Component servo + automation software; not a humanoid joint maker.",
        },
        {
            "company": "Kollmorgen",
            "hq_country": "United States",
            "region": "US",
            "layer": "Servo motor / drive",
            "product_category": "TBM2G frameless servo motors",
            "robotics_relevance": "Direct-drive motors inside humanoid joints",
            "known_market_share_pct": nan,
            "market_share_scope": "Frameless servo for robotics (unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2025,
            "source_url": "https://www.kollmorgen.com/en-us/solutions/robotics/humanoid-robots",
            "confidence": "moderate",
            "notes": "Active humanoid-joint marketing; frameless motor is the core of the joint module.",
        },
        # --- Integrated joint modules ---
        {
            "company": "CubeMars / T-Motor",
            "hq_country": "China",
            "region": "China",
            "layer": "Integrated joint module",
            "product_category": "BLDC / frameless / QDD actuators",
            "robotics_relevance": "Merchant humanoid & legged-robot joints",
            "known_market_share_pct": nan,
            "market_share_scope": "Merchant QDD actuator niche (unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.cubemars.com/about-us.html",
            "confidence": "low",
            "notes": "Brand of Nanchang Sanrui; claims ~6M units/yr. No market-share figure exists.",
        },
        {
            "company": "MyActuator",
            "hq_country": "China",
            "region": "China",
            "layer": "Integrated joint module",
            "product_category": "RMD integrated joint modules (QDD)",
            "robotics_relevance": "Quadruped, cobot, exoskeleton joints",
            "known_market_share_pct": nan,
            "market_share_scope": "Merchant integrated-joint vendor (unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.myactuator.com/aboutus",
            "confidence": "low",
            "notes": "Small specialist; exports to 20+ countries. No share figure.",
        },
        {
            "company": "Synapticon",
            "hq_country": "Germany",
            "region": "Europe",
            "layer": "Integrated joint module",
            "product_category": "SOMANET servo drives, ACTILINK actuators, safety",
            "robotics_relevance": "Humanoid & cobot motion control",
            "known_market_share_pct": nan,
            "market_share_scope": "Full-stack motion control for humanoids (unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2025,
            "source_url": "https://www.synapticon.com/en/applications/humanoids",
            "confidence": "moderate",
            "notes": "Supplies humanoid/cobot makers; POSITRON safety platform. No public share.",
        },
        {
            "company": "maxon",
            "hq_country": "Switzerland",
            "region": "Europe",
            "layer": "Integrated joint module",
            "product_category": "BLDC motors, gearheads, High Efficiency Joint",
            "robotics_relevance": "Humanoid/legged joints; NASA Mars heritage",
            "known_market_share_pct": nan,
            "market_share_scope": "Integrated joint & precision motors (unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2025,
            "source_url": "https://www.therobotreport.com/maxon-unveils-high-efficiency-joint-70-actuator-for-dynamic-robots/",
            "confidence": "moderate",
            "notes": ">100 drives across NASA Mars missions; moving from component motors into integrated joints.",
        },
        # --- Robot OEMs ---
        {
            "company": "FANUC",
            "hq_country": "Japan",
            "region": "Japan",
            "layer": "Robot OEM",
            "product_category": "Industrial robots + CNC + captive servo",
            "robotics_relevance": "Robot OEM + dominant CNC/servo supplier",
            "known_market_share_pct": 10.5,
            "market_share_scope": "Global industrial robots (by value)",
            "market_share_geography": "Global",
            "market_share_year": 2023,
            "source_url": "https://www.statista.com/chart/32239/global-market-share-of-industrial-robotics-companies/",
            "confidence": "moderate",
            "notes": "Also ~50-65% global CNC controls. Robot sales fell ~16% in FY2024.",
        },
        {
            "company": "Estun (埃斯顿)",
            "hq_country": "China",
            "region": "China",
            "layer": "Robot OEM",
            "product_category": "Industrial robots + in-house servo",
            "robotics_relevance": "Vertically integrated OEM",
            "known_market_share_pct": 8.5,
            "market_share_scope": "China industrial robots (shipment volume)",
            "market_share_geography": "China",
            "market_share_year": 2023,
            "source_url": "https://file.finance.qq.com/finance/hs/pdf/2024/04/30/1219913415.PDF",
            "confidence": "high",
            "notes": "#1 domestic brand; #2 overall in China. ~10.5% in H1 2025.",
        },
        {
            "company": "Unitree",
            "hq_country": "China",
            "region": "China",
            "layer": "Robot OEM",
            "product_category": "Humanoid & quadruped robots; in-house joint motors",
            "robotics_relevance": "Vertically integrated OEM",
            "known_market_share_pct": nan,
            "market_share_scope": "Humanoid/quadruped OEM (share unquantified)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.docs.quadruped.de/projects/h1/html/h1_overview.html",
            "confidence": "moderate",
            "notes": "Builds own joint motors/reducers/drivers; also sells motors externally (GO/B series). No external merchant supplier of its core joints.",
        },
        # --- Bearings / transmission ---
        {
            "company": "Schaeffler",
            "hq_country": "Germany",
            "region": "Europe",
            "layer": "Bearings / transmission",
            "product_category": "Bearings; strain-wave + planetary humanoid actuators",
            "robotics_relevance": "Bearings giant entering humanoid actuators",
            "known_market_share_pct": 10.0,
            "market_share_scope": "TARGET share of addressable humanoid component market by 2030 (not current)",
            "market_share_geography": "Global",
            "market_share_year": 2030,
            "source_url": "https://www.humanoidsdaily.com/news/building-the-backlog-schaeffler-targets-multi-million-euro-order-book-for-humanoid-components-by-2030",
            "confidence": "high",
            "notes": "Aspiration, not current share. Pegs actuators + gears at ~50% of humanoid BOM.",
        },
        # --- Hydraulic / high-performance actuators ---
        {
            "company": "Moog",
            "hq_country": "United States",
            "region": "US",
            "layer": "Hydraulic / high-performance actuator",
            "product_category": "EM/EH/EHA actuators; Integrated Smart Actuators",
            "robotics_relevance": "Aerospace/defense + research quadrupeds",
            "known_market_share_pct": nan,
            "market_share_scope": "High-performance actuation (unquantified in robotics)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.moog.com/products/actuators-servoactuators/actuation-technologies/electromechanical.html",
            "confidence": "low",
            "notes": "Mostly hydraulic research actuators (IIT HyQ) + industrial EM; not a volume humanoid joint supplier.",
        },
        {
            "company": "Parker Hannifin",
            "hq_country": "United States",
            "region": "US",
            "layer": "Hydraulic / high-performance actuator",
            "product_category": "Linear/rotary positioning, fluid power, exoskeleton",
            "robotics_relevance": "Industrial motion + exoskeleton",
            "known_market_share_pct": nan,
            "market_share_scope": "Motion control & fluid power (unquantified in robotics)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://ph.parker.com/us/en/series/positioning-robots-and-systems",
            "confidence": "low",
            "notes": "Indego exoskeleton heritage; no confirmed humanoid joint-module program.",
        },
        {
            "company": "Bosch Rexroth",
            "hq_country": "Germany",
            "region": "Europe",
            "layer": "Hydraulic / high-performance actuator",
            "product_category": "ctrlX drives, linear motion, Smart Flex Effector",
            "robotics_relevance": "Factory motion + compliant end-effectors",
            "known_market_share_pct": nan,
            "market_share_scope": "Drive & motion control (unquantified in robotics)",
            "market_share_geography": "Global",
            "market_share_year": 2024,
            "source_url": "https://www.boschrexroth.com/en/us/smart-mechatronix/smart-flex-effector/",
            "confidence": "moderate",
            "notes": "Compliance/sensing at the wrist + factory motion control; not humanoid joints.",
        },
    ]

    robotics_companies_df = pd.DataFrame(robotics_actuator_companies)
    robotics_companies_df
    return pd, robotics_companies_df


@app.cell
def _(mo):
    mo.md(
        """
    Company master table (read me first):

    - known_market_share_pct uses NaN where no credible public figure exists. These are deliberately blank, not zero. We are not founding a consultancy, so no numbers were invented.
    - The four high-confidence figures are Nabtesco (60%, own estimate), Shuanghuan/Huandong (18.89% China RV, IPO prospectus via GGII), Inovance (28% China servo, MIR) and Estun (8.5% China robots, filing).
    - Every other share is moderate/low confidence or unknown. Where a figure is a company's own marketing claim (Leaderdrive 60%) or a 2030 aspiration (Schaeffler 10%), the scope/notes columns say so explicitly.
    - market_share_scope and market_share_geography are the most important columns: a 60% in "China robot-grade harmonic" and a 60% in "global medium/large RV" describe entirely different markets.
    """
    )
    return


@app.cell
def _(go):
    # A treemap is the WRONG chart for these figures: treemap box area implies a
    # share of one common whole, but each figure below is a share of a DIFFERENT
    # market (different product, different geography). Two 60% boxes would falsely
    # read as "they split the same pie". Instead we use labelled horizontal bars:
    # each bar names the market it is a share OF, so the bars are explicitly not
    # comparable. Dot legend: \U0001f535 solid current figure | \U0001f7e0 legacy/
    # narrow-scope claim | \U000026aa 2030 target, not current.
    share_rows = [
        # (label incl. flag+dot+market, value, color, hover/confidence)
        (
            "\U0001f1ef\U0001f1f5 \U0001f535 Nabtesco  ·  global med/large industrial-robot RV reducers",
            60.0,
            "#1f4e79",
            "Global precision reducers for medium/large industrial robot joints (2019, company estimate). Confidence: high.",
        ),
        (
            "\U0001f1e8\U0001f1f3 \U0001f7e0 Leaderdrive  ·  China robot-grade harmonic (legacy claim; ~7-8% global)",
            60.0,
            "#c55a11",
            "China domestic robot-grade harmonic reducers, ~2017 company claim. Total China harmonic ~26% (2022); global ~7-8%. Confidence: low.",
        ),
        (
            "\U0001f1ef\U0001f1f5 \U0001f535 Yaskawa  ·  global AC servo-drive market",
            16.0,
            "#2e75b6",
            "Global AC servo-drive market (2024). Confidence: moderate.",
        ),
        (
            "\U0001f1ef\U0001f1f5 \U0001f7e0 Harmonic Drive / HDSI  ·  China strain-wave gearing ('24)",
            12.1,
            "#c55a11",
            "China strain-wave gearing devices market (2024). Global strain-wave segment est. ~50%. Confidence: low.",
        ),
        (
            "\U0001f1e9\U0001f1ea \U000026aa Schaeffler  ·  TARGET: humanoid components by 2030",
            10.0,
            "#7f7f7f",
            "TARGET share of addressable humanoid component market by 2030 - NOT current share. Confidence: high (that it is a target).",
        ),
        (
            "\U0001f1ef\U0001f1f5 \U0001f535 Yaskawa  ·  global industrial robots (by value)",
            7.0,
            "#2e75b6",
            "Global industrial robots by value (2023). Confidence: moderate.",
        ),
    ]

    # Display largest at top: list in ascending order and reverse the y-axis.
    share_rows_plot = list(reversed(share_rows))
    share_labels = [r[0] for r in share_rows_plot]
    share_values = [r[1] for r in share_rows_plot]
    share_colors = [r[2] for r in share_rows_plot]
    share_hover = [r[3] for r in share_rows_plot]

    share_fig = go.Figure(
        go.Bar(
            x=share_values,
            y=share_labels,
            orientation="h",
            marker_color=share_colors,
            customdata=share_hover,
            text=[f"{v}%" for v in share_values],
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>%{x}% - %{customdata}<extra></extra>",
        )
    )
    share_fig.update_layout(
        title="Selected public market-share figures in robotics actuation / motion control<br>"
        "<sup>figure status: mix of ACTUAL/reported, a LEGACY claim, and a 2030 TARGET - see dot legend below</sup>",
        xaxis_title="share of its OWN market (%) - bars are NOT comparable",
        xaxis_range=[0, 70],
        annotations=[
            dict(
                text="Each bar is a share of a DIFFERENT market, named on the axis. They do NOT sum and bar length is NOT comparable across rows "
                "(Nabtesco's 60% of global RV reducers and Leaderdrive's 60% of China harmonic are unrelated). "
                "Dots: \U0001f535 current | \U0001f7e0 legacy/narrow | \U000026aa 2030 target.",
                x=0.5,
                y=1.16,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
        margin=dict(t=160, l=10, r=30, b=50),
        height=480,
    )
    share_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Caveat (this chart is a trap if read naively):

    - Each bar is a percentage of a different market, named on the axis. Bar length is not comparable across rows - you cannot rank these companies against each other from the bars. This is exactly why a treemap was the wrong chart here: equal-area boxes would falsely imply they share one pie.
    - Nabtesco 60% = global medium/large industrial-robot RV reducers. Leaderdrive 60% = China domestic robot-grade harmonic, a legacy promotional claim; its defensible global share is ~7-8%. Same number, unrelated markets.
    - Yaskawa 16% (AC servo drive) and 7% (industrial robots) are two different markets for the same firm.
    - Schaeffler 10% is a 2030 ambition for humanoid components, not a position it holds today (shown grey).
    - HDSI 12.1% is China strain-wave only; the global strain-wave figure is much higher (~50%, low confidence).

    Data sources: each figure's primary source, geography, year and confidence are in the company master table above (source_url column). Headline references - Nabtesco IR (nabtesco.com/en/products/robot), Yaskawa via Mordor Intelligence global servo report, Leaderdrive company profile (leaderdrive.com) cross-checked against GGII, and Schaeffler's 2030 target via humanoidsdaily.com.
    """
    )
    return


@app.cell
def _(go, pd, robotics_companies_df):
    category_order = [
        "Precision reducer",
        "Servo motor / drive",
        "Integrated joint module",
        "Robot OEM",
        "Bearings / transmission",
        "Hydraulic / high-performance actuator",
    ]
    region_order = ["Japan", "China", "Europe", "US"]
    region_palette = {
        "Japan": "#d1495b",  # rosy red
        "China": "#edae49",  # gold
        "Europe": "#2a9d8f",  # teal
        "US": "#5f4b8b",  # purple
    }

    count_matrix = pd.crosstab(
        robotics_companies_df["layer"], robotics_companies_df["region"]
    ).reindex(index=category_order, columns=region_order, fill_value=0)

    count_fig = go.Figure()
    for region_name in region_order:
        count_fig.add_bar(
            name=region_name,
            x=category_order,
            y=[int(count_matrix.loc[cat, region_name]) for cat in category_order],
            marker_color=region_palette[region_name],
            hovertemplate="<b>%{x}</b><br>"
            + region_name
            + ": %{y} companies<extra></extra>",
        )
    count_fig.update_layout(
        barmode="stack",
        title="Robotics actuator companies tracked, by layer and region",
        xaxis_title="",
        yaxis_title="company count (this sample)",
        legend_title="Region",
        xaxis_tickangle=-20,
        height=480,
        margin=dict(t=70, b=120),
    )
    count_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the layer/region chart:

    - This counts companies in this curated sample, not market value. It shows clustering, not size.
    - Japan clusters in precision reducers and servo (Nabtesco, Harmonic, Yaskawa, Mitsubishi, Panasonic, FANUC). China spreads across every layer, heaviest in reducers and servo (the substitution drive). Europe/US sit in integrated modules, bearings and high-performance/hydraulic actuation.
    - Companies are assigned to a single primary layer. Yaskawa and FANUC straddle servo and OEM; Schaeffler straddles bearings and reducers. The assignment reflects their most distinctive robotics role.
    """
    )
    return


@app.cell
def _(go):
    bom_components = [
        ("Precision reducers / gears", [35, 0], "#1f4e79"),
        ("Servo / frameless motors", [20, 0], "#2e75b6"),
        ("Drives / controllers", [15, 0], "#5b9bd5"),
        ("Integrated actuators (motor+gear+drive)", [0, 37], "#1f4e79"),
        ("Battery", [0, 17], "#70ad47"),
        ("Compute / sensors", [0, 13], "#ffc000"),
        ("Structure / assembly / other", [30, 33], "#a6a6a6"),
    ]
    bom_targets = ["Industrial robot arm", "Humanoid robot"]

    bom_fig = go.Figure()
    for comp_name, comp_values, comp_color in bom_components:
        bom_fig.add_bar(
            name=comp_name,
            y=bom_targets,
            x=comp_values,
            orientation="h",
            marker_color=comp_color,
            hovertemplate="<b>%{y}</b><br>" + comp_name + ": ~%{x}%<extra></extra>",
        )
    bom_fig.update_layout(
        barmode="stack",
        title="Where the bill of materials sits: industrial arm vs humanoid",
        xaxis_title="approx. % of bill of materials",
        height=380,
        margin=dict(t=110, b=40),
        annotations=[
            dict(
                text="Industrial split is reducer-industry consensus (~35/20/15 reducer/motor/drive). "
                "Humanoid is Goldman Sachs framing (actuators ~35-40%, battery ~15-20%, compute ~10-15%). Illustrative, not summable across bars.",
                x=0.5,
                y=1.13,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
    )
    bom_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Why the BOM chart matters to the thesis:

    - In an industrial arm, the reducer is the single largest line item (~35%), ahead of the motor (~20%) and the drive/controller (~15%). The mechanical reduction, not the motor, is where the money and the moat concentrate. Sources: reducer-industry consensus (Nabtesco IR / GGII-derived breakdowns).
    - In a humanoid, actuators (the integrated motor+gear+drive joint) are the largest BOM block at ~35-40% per Goldman Sachs, with battery ~15-20% and compute ~10-15%. Schaeffler independently pegs actuators+gears at ~50% of humanoid material cost.
    - Tesla's Optimus uses ~28 body actuators (commonly described as ~14 rotary using harmonic drives + ~14 linear using planetary roller screws). That is the integrated-joint battleground in physical form.
    """
    )
    return


@app.cell
def _(go):
    substitution_years = ["2021", "2022", "2023"]
    nabtesco_china_rv = [51.77, 50.87, 40.17]
    huandong_china_rv = [10.11, 13.65, 18.89]

    substitution_fig = go.Figure()
    substitution_fig.add_bar(
        name="\U0001f1ef\U0001f1f5 Nabtesco",
        x=substitution_years,
        y=nabtesco_china_rv,
        marker_color="#bc002d",
        text=[f"{v}%" for v in nabtesco_china_rv],
        textposition="outside",
        hovertemplate="Nabtesco %{x}: %{y}%<extra></extra>",
    )
    substitution_fig.add_bar(
        name="\U0001f1e8\U0001f1f3 Shuanghuan / Huandong",
        x=substitution_years,
        y=huandong_china_rv,
        marker_color="#de2910",
        text=[f"{v}%" for v in huandong_china_rv],
        textposition="outside",
        hovertemplate="Huandong %{x}: %{y}%<extra></extra>",
    )
    substitution_fig.update_layout(
        barmode="group",
        title="China RV-reducer market: domestic substitution in motion",
        xaxis_title="",
        yaxis_title="share of China RV reducer market (%)",
        legend_title="",
        height=440,
        margin=dict(t=110, b=40),
        annotations=[
            dict(
                text="Source: GGII data via Huandong (环动科技) STAR-board IPO prospectus. "
                "The incumbent's China RV share fell from ~52% to ~40% in two years as the #2 domestic player nearly doubled.",
                x=0.5,
                y=1.13,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
    )
    substitution_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    The substitution chart is the single most important sourced datapoint in this notebook. It is filing-grade (an IPO prospectus citing GGII), and it shows the moat is real but not permanent: Nabtesco's China RV share fell from ~52% (2021) to ~40% (2023) while Shuanghuan/Huandong climbed from ~10% to ~19%. The Japanese incumbency is being eroded fastest exactly where China has the most volume and the most policy pressure.
    """
    )
    return


@app.cell
def _(go):
    # Annual revenue in NATIVE reporting currency (millions), for the listed
    # companies anchoring our dedicated segment sections. Indexing growth on the
    # native series avoids conflating real growth with FX moves. Sources: company
    # IR / annual reports cross-checked against stockanalysis.com, Yahoo Finance,
    # irbank.net and IPO prospectuses (see notes cell below).
    # group=True  -> robotics/actuators are only a fraction of group revenue.
    # dashed line -> group-level; solid line -> robotics/actuator-pure(ish).
    revenue_history = {
        "\U0001f1ef\U0001f1f5 Nabtesco": {
            "region": "Japan",
            "ccy": "JPY",
            "color": "#d1495b",
            "group": False,
            "rev": {
                2019: 289808,
                2020: 279358,
                2021: 299802,
                2022: 308691,
                2023: 333631,
                2024: 323384,
            },
        },
        "\U0001f1ef\U0001f1f5 Harmonic Drive": {
            "region": "Japan",
            "ccy": "JPY",
            "color": "#e8743b",
            "group": False,
            "rev": {
                2019: 37488,
                2020: 37034,
                2021: 57087,
                2022: 71527,
                2023: 55796,
            },
        },
        "\U0001f1ef\U0001f1f5 Yaskawa": {
            "region": "Japan",
            "ccy": "JPY",
            "color": "#9c6644",
            "group": True,
            "rev": {
                2019: 410957,
                2020: 389712,
                2021: 479082,
                2022: 555955,
                2023: 575658,
                2024: 537682,
            },
        },
        "\U0001f1ef\U0001f1f5 FANUC": {
            "region": "Japan",
            "ccy": "JPY",
            "color": "#c44536",
            "group": True,
            "rev": {
                2019: 508252,
                2020: 551287,
                2021: 733008,
                2022: 851956,
                2023: 795274,
            },
        },
        "\U0001f1e8\U0001f1f3 Leaderdrive": {
            "region": "China",
            "ccy": "CNY",
            "color": "#2a9d8f",
            "group": False,
            "rev": {
                2019: 186,
                2020: 217,
                2021: 443,
                2022: 446,
                2023: 356,
                2024: 387,
            },
        },
        "\U0001f1e8\U0001f1f3 Inovance": {
            "region": "China",
            "ccy": "CNY",
            "color": "#1f77b4",
            "group": True,
            "rev": {
                2019: 7390,
                2020: 11511,
                2021: 23008,
                2022: 30420,
                2023: 37041,
                2024: 41367,
            },
        },
        "\U0001f1e8\U0001f1f3 Estun": {
            "region": "China",
            "ccy": "CNY",
            "color": "#17becf",
            "group": False,
            "rev": {
                2019: 1462,
                2020: 2510,
                2021: 3020,
                2022: 3881,
                2023: 4652,
                2024: 4009,
            },
        },
        "\U0001f1e8\U0001f1f3 Shuanghuan": {
            "region": "China",
            "ccy": "CNY",
            "color": "#5fa8d3",
            "group": False,
            "rev": {
                2019: 3236,
                2020: 3664,
                2021: 5391,
                2022: 6838,
                2023: 8074,
                2024: 8781,
            },
        },
        "\U0001f1e9\U0001f1ea Schaeffler": {
            "region": "Europe",
            "ccy": "EUR",
            "color": "#5f4b8b",
            "group": True,
            "rev": {
                2019: 14427,
                2020: 12600,
                2021: 13852,
                2022: 15808,
                2023: 16309,
                2024: 18200,
            },
        },
    }

    growth_years = [2019, 2020, 2021, 2022, 2023, 2024]

    growth_fig = go.Figure()
    for company_name, info in revenue_history.items():
        rev = info["rev"]
        base_year = min(rev)
        base_value = rev[base_year]
        x_vals = [yr for yr in growth_years if yr in rev]
        index_vals = [round(rev[yr] / base_value * 100, 1) for yr in x_vals]
        native_vals = [rev[yr] for yr in x_vals]
        legend_name = company_name + (" (group)" if info["group"] else "")
        growth_fig.add_scatter(
            name=legend_name,
            x=x_vals,
            y=index_vals,
            mode="lines+markers",
            line=dict(
                color=info["color"],
                width=2.5,
                dash="dash" if info["group"] else "solid",
            ),
            marker=dict(size=6),
            customdata=list(zip(native_vals, [info["ccy"]] * len(x_vals))),
            hovertemplate="<b>"
            + company_name
            + "</b><br>FY%{x}: index %{y}"
            + "<br>revenue: %{customdata[0]:,} M %{customdata[1]}<extra></extra>",
        )

    growth_fig.add_hline(y=100, line_dash="dot", line_color="#999999", line_width=1)
    growth_fig.update_layout(
        title="Revenue growth of key listed robotics-actuator companies (FY2019 = 100)",
        xaxis_title="fiscal year",
        yaxis_title="indexed revenue (native currency, FY2019 = 100)",
        legend_title="Company",
        height=560,
        margin=dict(t=120, b=40),
        annotations=[
            dict(
                text="Indexed on native-currency revenue (FX-neutral). Dashed = group-level revenue (robotics/actuators a fraction). "
                "China challengers compound far faster than Japanese incumbents; Schaeffler's FY2024 step is inorganic (Vitesco consolidation).",
                x=0.5,
                y=1.11,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
    )
    growth_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read the revenue-growth chart:

    - Each line is rebased to 100 at its base year (FY2019 for all; Japanese FYs end Feb/Mar, so a label like FY2019 is the year ending early 2020). Indexing is on native-currency revenue, so the lines show real top-line growth, not yen/yuan/euro FX swings.
    - The thesis shows up immediately. The China challenger cluster compounds fast: Inovance ~5.6x (group; drives + EV, robotics a slice), Estun ~2.7x, Shuanghuan ~2.7x, Leaderdrive ~2x but volatile. The Japan incumbent cluster is comparatively flat: Nabtesco ~1.1x, Yaskawa ~1.3x, FANUC ~1.6x, Harmonic Drive ~1.5x with a sharp 2021-2023 cobot/automation cycle.
    - Dashed lines are group-level revenue where actuators are a fraction (Yaskawa, FANUC, Inovance, Schaeffler) - read those as direction, not pure-play actuator demand. Solid lines (Nabtesco, Harmonic Drive, Leaderdrive, Estun, Shuanghuan) are closer to robotics/actuator-pure.

    Caveats and sources:

    - Revenue is native reporting currency (JPY/CNY/EUR), in millions, from company IR / annual reports cross-checked against stockanalysis.com, Yahoo Finance, irbank.net and IPO prospectuses. Nabtesco and Yaskawa report under IFRS (lower than old J-GAAP "net sales").
    - Fiscal-year ends differ: Nabtesco, Leaderdrive, Inovance, Estun, Shuanghuan, Schaeffler end Dec 31; FANUC ends Mar 31; Harmonic Drive ends Mar 31; Yaskawa ends ~Feb 28. FANUC and Harmonic Drive FY2024 (ending early 2025) were not captured, so their lines stop at FY2023.
    - Lower-confidence base figures: Leaderdrive FY2019 (~CNY 186M, pre-IPO; sources range 158-186M) and Harmonic Drive's series around its COVID trough. Estun's FY2024 dip (-13.8%) coincided with its first net loss.
    - Schaeffler's FY2024 jump (~EUR 16.3B to ~EUR 18.2B) is largely the Vitesco acquisition/merger, not organic growth - do not read it as robotics demand.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## The robotics actuation stack: where value is captured

    Four layers, and value does not distribute evenly up them. The diagram below shows the qualitative thesis: today the reducer-led component layer captures most value; in the humanoid era it migrates into the integrated joint module.
    """
    )
    return


@app.cell
def _(go):
    # Illustrative, qualitative value-capture across the stack. NOT measured
    # shares - it encodes the thesis that value migrates from the reducer-led
    # component layer (today) into the integrated joint module (humanoid era).
    stack_eras = ["Today:<br>industrial-arm era", "Tomorrow:<br>humanoid era"]
    stack_layers = [
        # (layer label, [today, tomorrow], color)  -- added bottom -> top
        ("Materials / bearings / electronics", [20, 15], "#a6a6a6"),
        ("Components: reducers / motors / drives", [50, 28], "#2e75b6"),
        ("Integrated joint module", [10, 45], "#1f4e79"),
        ("Robot OEM (system integration)", [20, 12], "#c55a11"),
    ]

    stack_fig = go.Figure()
    for stack_name, stack_vals, stack_color in stack_layers:
        stack_fig.add_bar(
            name=stack_name,
            x=stack_eras,
            y=stack_vals,
            marker_color=stack_color,
            text=[f"{stack_name}<br>{v}%" for v in stack_vals],
            textposition="inside",
            insidetextanchor="middle",
            hovertemplate="<b>%{x}</b><br>"
            + stack_name
            + ": ~%{y}% of captured value<extra></extra>",
        )
    stack_fig.add_annotation(
        x=1,
        y=72,
        ax=0,
        ay=88,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        text="value migrates<br>into the joint",
        showarrow=True,
        arrowhead=3,
        arrowwidth=2,
        arrowcolor="#1f4e79",
        font=dict(size=11, color="#1f4e79"),
    )
    stack_fig.update_layout(
        barmode="stack",
        title="Where value is captured across the actuation stack (illustrative, qualitative)",
        yaxis_title="approx. share of captured value (%)",
        showlegend=False,
        height=520,
        margin=dict(t=80, b=40),
    )
    stack_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Read it as a thesis, not data: the OEM layer (top) is competitive and commoditising; the integrated joint module (dark) is thin today but swells in the humanoid era as it absorbs the reducer + motor + drive margin plus a bundling premium. Players by layer: OEMs (FANUC, Yaskawa, Estun, Unitree); modules (CubeMars, MyActuator, Synapticon, maxon, Harmonic Drive, Schaeffler); components (Nabtesco, Harmonic Drive, Inovance, Kollmorgen); materials (Schaeffler bearings, gear steel, power electronics).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Segment analysis

    The four layers do not compete on the same terms. The map below positions each by moat / pricing power against growth & strategic importance; bubble size approximates its share of the robot/humanoid bill of materials.
    """
    )
    return


@app.cell
def _(go):
    # Qualitative positioning (analyst judgment, not measured). x = moat / pricing
    # power, y = growth & strategic importance (0-10). Bubble size ~ share of
    # robot/humanoid BOM (%).
    segmap_points = [
        # (segment, x_moat, y_growth, bom_size, color, key_players)
        (
            "Precision reducers",
            8.5,
            6.0,
            35,
            "#1f4e79",
            "Nabtesco, Harmonic Drive, Sumitomo",
        ),
        (
            "Integrated joint modules",
            6.0,
            9.0,
            45,
            "#2a9d8f",
            "CubeMars, MyActuator, Synapticon, maxon, Schaeffler",
        ),
        (
            "Servo motors / drives",
            4.0,
            5.0,
            20,
            "#edae49",
            "Yaskawa, Mitsubishi, Inovance, Siemens",
        ),
        (
            "Robot OEMs",
            3.0,
            6.0,
            18,
            "#c55a11",
            "FANUC, Yaskawa, Estun, Unitree",
        ),
    ]
    segmap_sizes = [p[3] for p in segmap_points]
    segmap_sizeref = 2.0 * max(segmap_sizes) / (95.0**2)

    segmap_fig = go.Figure()
    for seg_name, seg_x, seg_y, seg_bom, seg_color, seg_players in segmap_points:
        segmap_fig.add_scatter(
            x=[seg_x],
            y=[seg_y],
            mode="markers+text",
            text=[seg_name],
            textposition="bottom center",
            textfont=dict(size=12),
            marker=dict(
                size=[seg_bom],
                sizemode="area",
                sizeref=segmap_sizeref,
                sizemin=6,
                color=seg_color,
                opacity=0.8,
                line=dict(width=1, color="white"),
            ),
            name=seg_name,
            customdata=[[seg_bom, seg_players]],
            hovertemplate="<b>"
            + seg_name
            + "</b><br>moat: %{x}/10 | growth: %{y}/10"
            + "<br>~%{customdata[0]}% of BOM<br>players: %{customdata[1]}<extra></extra>",
        )
    segmap_fig.add_vline(x=5, line_dash="dot", line_color="#cccccc")
    segmap_fig.add_hline(y=5, line_dash="dot", line_color="#cccccc")
    segmap_fig.update_layout(
        title="Robotics actuation layers: moat vs growth (bubble = share of BOM)",
        xaxis=dict(title="Moat / pricing power (qualitative →)", range=[1, 10]),
        yaxis=dict(
            title="Growth & strategic importance (qualitative →)",
            range=[3, 10.5],
        ),
        showlegend=False,
        height=520,
        margin=dict(t=80, b=50),
        annotations=[
            dict(
                text="Qualitative positioning (analyst judgment, not measured). Bubble size approximates share of robot/humanoid BOM.",
                x=0.5,
                y=1.10,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
    )
    segmap_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    The map captures the whole argument: reducers sit top-right on moat (hard to make, qualified-locked in) and are the biggest single arm-BOM block; integrated joint modules sit highest on growth/strategic importance (the humanoid battleground) with rising moat; servo/drives and robot OEMs are lower-moat, more commoditised layers. Value lives in the two right-hand bubbles.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Why precision reducers are structurally concentrated

    The moat is manufacturing physics plus customer behaviour, not patents. The funnel below shows why the field narrows to a handful: each stage is a barrier most aspiring entrants fail.
    """
    )
    return


@app.cell
def _(go):
    # Illustrative qualification funnel (not measured counts) - each stage is one
    # of the structural barriers that concentrates the precision-reducer field.
    funnel_stages = [
        "Firms attempting precision reducers",
        "Hold micron tolerances at volume",
        "Pass fatigue-life & low-backlash over years",
        "Win OEM platform qualification",
        "Survive reliability + incumbency lock-in",
    ]
    funnel_values = [100, 45, 22, 11, 5]

    funnel_fig = go.Figure(
        go.Funnel(
            y=funnel_stages,
            x=funnel_values,
            textinfo="value+percent initial",
            marker=dict(color=["#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#084594"]),
            hovertemplate="<b>%{y}</b><br>~%{x} of every 100 entrants survive this stage<extra></extra>",
        )
    )
    funnel_fig.update_layout(
        title="Why the reducer field narrows to a few: a qualification funnel (illustrative)",
        height=460,
        margin=dict(t=80, l=10, r=10, b=40),
        annotations=[
            dict(
                text="Illustrative, not measured. China domestic-substitution policy is the one force actively widening the bottom of the funnel for local champions.",
                x=0.5,
                y=1.13,
                xref="paper",
                yref="paper",
                showarrow=False,
                font_size=10.5,
            )
        ],
    )
    funnel_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Each narrowing is a real barrier: micron tolerances at volume, fatigue life and low backlash sustained for years, then OEM qualification (requalifying a whole joint to swap suppliers), then the reliability premium and compounding field-reliability data that make incumbents sticky. The result is a few survivors per reducer type - and the one crack in the moat is China's policy-backed substitution, visible in the share chart above.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Why this is not really a duopoly

    Reading "Nabtesco ~60%" and "Leaderdrive ~60%" as a two-horse race is wrong: they are shares of different markets (global RV reducers vs China domestic harmonic, a legacy claim worth ~7-8% globally). The real structure is three clusters competing on different axes, mapped below.
    """
    )
    return


@app.cell
def _(go):
    # Qualitative positioning of the three clusters. x = cost competitiveness
    # (price/value), y = robotics incumbency / installed base (0-10).
    cluster_data = {
        "Japan incumbent": {
            "color": "#d1495b",
            "companies": [
                ("\U0001f1ef\U0001f1f5 Nabtesco", 4.2, 9.0),
                ("\U0001f1ef\U0001f1f5 Harmonic Drive", 4.5, 8.0),
                ("\U0001f1ef\U0001f1f5 Yaskawa", 5.0, 8.0),
                ("\U0001f1ef\U0001f1f5 FANUC", 4.0, 8.3),
                ("\U0001f1ef\U0001f1f5 Mitsubishi", 5.0, 7.0),
                ("\U0001f1ef\U0001f1f5 Sumitomo", 4.3, 6.8),
            ],
        },
        "China challenger": {
            "color": "#edae49",
            "companies": [
                ("\U0001f1e8\U0001f1f3 Leaderdrive", 8.0, 5.0),
                ("\U0001f1e8\U0001f1f3 Laifual", 8.3, 3.5),
                ("\U0001f1e8\U0001f1f3 Shuanghuan", 7.8, 4.5),
                ("\U0001f1e8\U0001f1f3 Inovance", 8.0, 5.5),
                ("\U0001f1e8\U0001f1f3 Estun", 8.2, 4.8),
                ("\U0001f1e8\U0001f1f3 Unitree", 8.8, 4.0),
            ],
        },
        "Europe/US premium": {
            "color": "#5f4b8b",
            "companies": [
                ("\U0001f1e9\U0001f1ea Schaeffler", 3.5, 4.0),
                ("\U0001f1e9\U0001f1ea Siemens", 3.0, 4.5),
                ("\U0001f1e8\U0001f1ed maxon", 2.8, 3.5),
                ("\U0001f1e9\U0001f1ea Synapticon", 3.0, 2.8),
                ("\U0001f1fa\U0001f1f8 Kollmorgen", 3.3, 3.2),
                ("\U0001f1fa\U0001f1f8 Moog", 2.3, 3.0),
                ("\U0001f1fa\U0001f1f8 Parker", 3.0, 2.5),
                ("\U0001f1e9\U0001f1ea Bosch Rexroth", 3.2, 3.3),
            ],
        },
    }

    cluster_fig = go.Figure()
    for cluster_name, cluster_info in cluster_data.items():
        cluster_fig.add_scatter(
            x=[c[1] for c in cluster_info["companies"]],
            y=[c[2] for c in cluster_info["companies"]],
            mode="markers+text",
            text=[c[0] for c in cluster_info["companies"]],
            textposition="top center",
            textfont=dict(size=9),
            marker=dict(
                size=13,
                color=cluster_info["color"],
                opacity=0.85,
                line=dict(width=1, color="white"),
            ),
            name=cluster_name,
            hovertemplate="<b>%{text}</b><br>"
            + cluster_name
            + "<br>cost-competitiveness: %{x}/10 | incumbency: %{y}/10<extra></extra>",
        )
    cluster_fig.add_annotation(
        x=8.3,
        y=6.2,
        ax=8.0,
        ay=4.3,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        text="rising",
        showarrow=True,
        arrowhead=3,
        arrowwidth=2,
        arrowcolor="#edae49",
        font=dict(size=11, color="#b8860b"),
    )
    cluster_fig.update_layout(
        title="Not a duopoly: three clusters competing on different axes",
        xaxis=dict(title="Cost competitiveness (price / value →)", range=[1, 10]),
        yaxis=dict(title="Robotics incumbency / installed base →", range=[1, 10.5]),
        legend_title="Cluster",
        height=560,
        margin=dict(t=80, b=50),
    )
    cluster_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    The clusters separate cleanly: Japan (red) sits high on robotics incumbency at premium pricing; China (gold) competes on cost with rising-but-lower installed base (arrow), pushed by domestic-substitution policy; Europe/US (purple) is a premium / safety-critical niche with limited robotics installed base today but the loudest humanoid-actuator ambitions. Positioning is qualitative analyst judgment, not measured data.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Research gaps

    Where this notebook is still under-sourced. These are the figures worth paying for or digging into filings to nail down:

    - Harmonic Drive global strain-wave share - only a low-confidence ~50% research-firm estimate; the 12.1% China figure lacks a primary URL.
    - Mitsubishi Electric servo share - only a 15-20% research-firm range; no filing-grade number.
    - FANUC robot vs servo/CNC share - robot ~10.5% (Statista/IFR) is decent; the ~50-65% CNC figure needs a primary source.
    - Inovance China servo share - 28% (MIR) is good but secondary; cross-check against the annual report.
    - Estun robotics share - 8.5% (filing) is solid; refresh for full-year 2024/2025.
    - Laifual, Qinchuan, Shuanghuan(full-group), Sumitomo reducer share - only Huandong's RV number is filing-grade; the rest are weak or missing.
    - Robot BOM share from reducers/motors/drives - the ~35/20/15 split is consensus but not anchored to an open bank PDF.
    - Humanoid BOM share from actuators - Goldman Sachs ~35-40% (good), McKinsey 40-60% (secondhand); pull the primary GS "Humanoid Robot: The AI Accelerant" chart and the Morgan Stanley Optimus teardown.
    - Known OEM-supplier relationships - e.g. who supplies whom for humanoid joints; mostly undisclosed. Confirmed: Unitree builds its own actuators in-house (no external merchant supplier).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## Executive summary and final thesis

    Executive summary:

    - The robotics actuation stack has four layers - reducers, motors/drives, integrated joint modules, and robot OEMs - and value is not evenly distributed across them.
    - Precision reducers are the strongest moat today. Nabtesco (~60% global, high confidence) and Harmonic Drive anchor a concentrated layer that is ~35% of an industrial arm's BOM. The concentration is driven by manufacturing physics and OEM qualification lock-in, not patents.
    - The moat is real but eroding in China. Filing-grade data shows Nabtesco's China RV share falling from ~52% to ~40% (2021-2023) as domestic players doubled. This is the clearest, best-sourced trend in the notebook.
    - Servo motors/drives are more fragmented and more commoditised - useful revenue, weaker pricing power.
    - Integrated joint modules are the emerging battleground. Actuators are ~35-50% of a humanoid's BOM, and whoever owns the integrated joint owns that cost. This layer is unconsolidated and unmeasured today - which is precisely why it is contestable.

    Final thesis on where value accrues (see the value-capture and segment-map diagrams above):

    Value sits in the precision reducer today and migrates into the integrated joint module for the humanoid era; generic motors/drives and the robot-OEM layer are the commoditising middle. The two defensible positions: (1) own a qualified precision reducer with decades of reliability data, or (2) own the integrated joint module. Everything else is a feature, not a moat.
    """
    )
    return


if __name__ == "__main__":
    app.run()
