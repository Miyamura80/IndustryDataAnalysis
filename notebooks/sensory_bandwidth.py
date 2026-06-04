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
    # A human takes in ~10 million bits per second and acts on about 10 of them.

    The eyes alone stream roughly 10,000,000 bit/s into the brain. Yet the deliberate, conscious "you" -- the part that reads this sentence, decides, and speaks -- runs at something like 10-50 bit/s. That is a compression ratio of about 1,000,000:1 between what enters and what becomes experience.

    This notebook is about that gap. It asks two questions and refuses to give either a single number:

    1. How much information enters and leaves a human?
    2. Why does subjective experience look nothing like the raw bandwidth numbers?

    ---

    ## The headline tension
    - Vision dominates raw sensory throughput (~90% of all input bits). It does NOT dominate conscious experience by anything close to 90%.
    - A burning hand (a low-bandwidth pain signal) can erase awareness of a high-bandwidth visual scene instantly.
    - Human output ranges from ~39 bit/s for speech to millions of bit/s for observable body motion -- depending entirely on what you choose to measure.
    - Almost every number here is an order-of-magnitude estimate. They measure different things and should not be compared naively. That caveat is the point, not a footnote.

    Sources for the framing: Nørretranders, "The User Illusion" (1991/1998); Zheng & Meister, "The unbearable slowness of being" (2024); Coupé et al., "Different languages, similar encoding efficiency" (Science Advances, 2019).
    """
    )
    return


@app.cell
def _():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots


@app.cell
def _():
    # Shared palette + the classic five-senses raw input table.
    # Bandwidth figures are widely cited order-of-magnitude estimates
    # (Nørretranders 1998, after Zimmermann 1986). They measure the
    # information capacity of the afferent nerves, NOT what reaches awareness.
    SENSE_COLORS = {
        "Vision": "#4e79a7",
        "Touch / Skin": "#f28e2b",
        "Hearing": "#59a14f",
        "Smell": "#e15759",
        "Taste": "#b07aa1",
    }

    SENSES = [
        {
            "sense": "Vision",
            "bw": 10_000_000,
            "note": "~10 Mbit/s down the optic nerve. ~1 million retinal ganglion cells, each firing a few bits/s after the retina has already thrown most of the photoreceptor data away.",
        },
        {
            "sense": "Touch / Skin",
            "bw": 1_000_000,
            "note": "~2 m^2 of skin, millions of mechanoreceptors. Bandwidth is spread across the whole body surface.",
        },
        {
            "sense": "Hearing",
            "bw": 100_000,
            "note": "~3,500 inner hair cells feeding the auditory nerve. Lower raw bandwidth than vision, but exquisite temporal resolution.",
        },
        {
            "sense": "Smell",
            "bw": 100_000,
            "note": "~400 functional olfactory receptor types, ~10 million receptor neurons. Estimates vary wildly; chemical senses are hard to quantify in bits.",
        },
        {
            "sense": "Taste",
            "bw": 1_000,
            "note": "~5 basic qualities, ~10,000 taste buds. The lowest-bandwidth channel by far -- yet capable of dominating a meal.",
        },
    ]

    TOTAL_BW = sum(s["bw"] for s in SENSES)
    return SENSES, SENSE_COLORS, TOTAL_BW


@app.cell
def _(SENSES, SENSE_COLORS, TOTAL_BW, go):
    _labels = [s["sense"] for s in SENSES]
    _values = [s["bw"] for s in SENSES]

    raw_pie = go.Figure(
        data=[
            go.Pie(
                labels=_labels,
                values=_values,
                hole=0.4,
                marker=dict(colors=[SENSE_COLORS[s] for s in _labels]),
                textinfo="label+percent",
                texttemplate="<b>%{label}</b><br>%{percent}",
                customdata=[s["bw"] for s in SENSES],
                hovertemplate="<b>%{label}</b><br>Raw bandwidth: %{customdata:,} bit/s<br>Share: %{percent}<extra></extra>",
                sort=False,
            )
        ]
    )

    raw_pie.update_layout(
        title="Raw sensory input bandwidth -- the classic five senses",
        annotations=[
            dict(
                text=f"~{TOTAL_BW/1e6:.1f}M<br>bit/s",
                x=0.5,
                y=0.5,
                font_size=16,
                showarrow=False,
            )
        ],
        showlegend=True,
        height=520,
    )

    raw_pie
    return


@app.cell
def _(mo):
    mo.md(
        """
    Reading the pie:
    - Total raw input is ~11.2 million bit/s. Vision is ~89% of it, touch ~9%, and hearing, smell, and taste together are barely 2%.
    - This single chart is responsible for the popular claim that "vision is 90% of perception." That claim is true ONLY for raw afferent bandwidth. It is false for nearly every other definition of "perception."
    - Taste (1,000 bit/s) is four orders of magnitude below vision. On this chart it is an invisible sliver. In a good meal it is the entire experience. Hold that contradiction -- the rest of the notebook unpacks it.
    - These are nerve-capacity estimates, not measurements of conscious content. The optic nerve can carry 10 Mbit/s the way a fibre-optic cable can carry a Netflix stream: the capacity exists, but it is not the same thing as what you watch.
    """
    )
    return


@app.cell
def _(SENSES, SENSE_COLORS, go):
    _sorted = sorted(SENSES, key=lambda s: s["bw"], reverse=True)

    log_bar = go.Figure(
        go.Bar(
            y=[s["sense"] for s in _sorted],
            x=[s["bw"] for s in _sorted],
            orientation="h",
            marker_color=[SENSE_COLORS[s["sense"]] for s in _sorted],
            text=[f"{s['bw']:,} bit/s" for s in _sorted],
            textposition="outside",
            customdata=[s["note"] for s in _sorted],
            hovertemplate="<b>%{y}</b><br>%{x:,} bit/s<br>%{customdata}<extra></extra>",
        )
    )

    log_bar.update_layout(
        title="Same data, log scale -- the five senses span 4 orders of magnitude",
        xaxis=dict(
            title="Raw bandwidth (bit/s, log scale)",
            type="log",
            range=[2.5, 7.6],
        ),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=120, r=140, b=50),
        height=420,
    )

    log_bar
    return


@app.cell
def _(mo):
    mo.md(
        """
    Why a log scale matters here:
    - On a linear axis (the pie), vision crushes everything and the four other senses are visually indistinguishable from zero. That is honest about magnitude but useless for comparing the small channels.
    - On a log axis, the structure appears: each step down -- vision -> touch -> hearing/smell -> taste -- is roughly a 10x drop. Taste is 10,000x smaller than vision, not "a bit smaller."
    - Crucially, the brain does NOT allocate attention on a log scale OR a linear scale of input bandwidth. It allocates on relevance. A 1,000 bit/s pain or taste signal routinely outcompetes a 10,000,000 bit/s visual stream for conscious access. Bandwidth and salience are different currencies.
    """
    )
    return


@app.cell
def _(go):
    import math

    # Six filters that turn ~10^7 bit/s of input into the ~40 bit/s conscious "now".
    # Each band = one mechanism. Width is bandwidth on a log scale (illustrative);
    # the example is the everyday case where you can feel that filter working.
    stages = [
        {
            "mech": "Peripheral compression",
            "ex": "a blank wall: all pixels, no information",
            "enter": 11_200_000,
            "exit": 1_000_000,
            "detail": "The retina, cochlea and skin discard redundancy before the signal leaves the sense organ -- edge detection, lateral inhibition, gain control. The eye is not a camera.",
        },
        {
            "mech": "Predictive coding",
            "ex": "reading: you confirm, you don't transduce",
            "enter": 1_000_000,
            "exit": 100_000,
            "detail": "The brain transmits only prediction error; expected input is cancelled. Fluent reading feels effortless because almost nothing is unpredicted (Rao & Ballard 1999; Friston).",
        },
        {
            "mech": "Novelty / adaptation",
            "ex": "you stop feeling your clothes",
            "enter": 100_000,
            "exit": 10_000,
            "detail": "Neurons adapt; a constant stimulus fades. A steady signal carries zero bits -- only change is informative. A sudden silence grabs you as hard as a sudden noise.",
        },
        {
            "mech": "Redundancy reduction",
            "ex": "eating: many channels, one percept",
            "enter": 10_000,
            "exit": 1_000,
            "detail": "Natural scenes are massively correlated across space and time. Taste, smell, texture and temperature fuse into a single low-bit but high-impact percept.",
        },
        {
            "mech": "Attentional bottleneck",
            "ex": "music: melody OR bassline, not both",
            "enter": 1_000,
            "exit": 100,
            "detail": "Conscious access is a narrow gate. Attention rations a channel millions of times narrower than the input -- you route one stream in at a time.",
        },
        {
            "mech": "Salience override",
            "ex": "a burning hand erases everything",
            "enter": 100,
            "exit": 40,
            "detail": "Some low-bandwidth channels jump the queue. A ~1,000 bit/s pain signal seizes the whole workspace and suppresses the 10,000,000 bit/s visual stream. Evolution wired pain to win.",
        },
    ]

    _n = len(stages)
    _cx = 5.0
    _max_hw = 4.6
    _max_v = math.log10(stages[0]["enter"])

    def _hw(bw):
        return (math.log10(bw) / _max_v) * _max_hw

    _blues = ["#08306b", "#08519c", "#2171b5", "#4292c6", "#6baed6", "#9ecae1"]

    mech_fig = go.Figure()
    _hx, _hy, _htext = [], [], []

    for _k, _s in enumerate(stages):
        _y_top = _n - _k
        _y_bot = _n - _k - 1
        _hwt = _hw(_s["enter"])
        _hwb = _hw(_s["exit"])
        _path = (
            f"M {_cx - _hwt},{_y_top} L {_cx + _hwt},{_y_top} "
            f"L {_cx + _hwb},{_y_bot} L {_cx - _hwb},{_y_bot} Z"
        )
        mech_fig.add_shape(
            type="path",
            path=_path,
            fillcolor=_blues[_k],
            line=dict(color="white", width=2),
            layer="below",
        )
        _yc = (_y_top + _y_bot) / 2
        mech_fig.add_annotation(
            x=_cx,
            y=_yc + 0.17,
            text=f"<b>{_s['mech']}</b>",
            showarrow=False,
            font=dict(size=13, color="white"),
        )
        mech_fig.add_annotation(
            x=_cx,
            y=_yc - 0.21,
            text=f"<i>{_s['ex']}</i>",
            showarrow=False,
            font=dict(size=10, color="white"),
        )
        mech_fig.add_annotation(
            x=_cx + _max_hw + 0.6,
            y=_y_bot,
            text=(
                f"{_s['exit']:,} bit/s"
                if _s["exit"] >= 1000
                else f"~{_s['exit']} bit/s"
            ),
            showarrow=False,
            font=dict(size=10, color="#444"),
            xanchor="left",
        )
        _hx.append(_cx)
        _hy.append(_yc)
        _htext.append(f"<b>{_s['mech']}</b><br>{_s['detail']}")

    mech_fig.add_annotation(
        x=_cx + _max_hw + 0.6,
        y=_n,
        text=f"{stages[0]['enter']:,} bit/s in",
        showarrow=False,
        font=dict(size=11, color="#08306b"),
        xanchor="left",
    )

    mech_fig.add_trace(
        go.Scatter(
            x=_hx,
            y=_hy,
            mode="markers",
            marker=dict(size=46, color="rgba(0,0,0,0)"),
            hovertext=_htext,
            hoverinfo="text",
            showlegend=False,
        )
    )

    mech_fig.update_layout(
        title="The perception funnel: six filters collapse ~10^7 bit/s into the ~40 bit/s conscious 'now'",
        xaxis=dict(visible=False, range=[0, 11]),
        yaxis=dict(visible=False, range=[-0.4, _n + 0.6]),
        margin=dict(t=70, l=20, r=20, b=20),
        height=600,
        plot_bgcolor="white",
    )

    mech_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Reading the funnel: each band is a filter that throws information away -- or, for salience, decides which survivors win. Width is bandwidth on a log scale; the stack collapses ~10^7 bit/s of input to the ~40 bit/s conscious "now", a ~250,000:1 cut. The italic line in each band is the everyday case where you can feel that filter working; hover for the science.

    The throughline: experience tracks prediction error, salience, and bodily relevance -- not raw bit count. A low-bandwidth signal wins whenever it is surprising, painful, or self-relevant. (The six filters overlap and interact; the strict top-to-bottom order and per-band numbers are illustrative, not a measured pipeline. Predictive coding: Rao & Ballard 1999; Friston's free-energy account.)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    ## The missing senses: the five-senses model is incomplete

    The classic table omits the senses that arguably matter MOST for experience -- they rarely appear in bandwidth charts because their information content resists being counted in bits. The matrix below shows the pattern at a glance: most carry little raw bandwidth (light cells, left column) yet can seize awareness completely (dark cells, right column). That mirror image is the whole point. Hover any row for what the sense is and when it takes over; the scatter that follows plots the same anti-correlation.
    """
    )
    return


@app.cell
def _(go):
    # The missing-senses matrix. Rows = senses, columns = three rateable dimensions.
    # z encodes Low=1 / Med=2 / High=3 so darkness = intensity. The visual argument:
    # the left column (bandwidth) and right column (hijack power) are near mirror images.
    _rows = [
        "Vision (reference)",
        "Proprioception",
        "Vestibular",
        "Pain",
        "Temperature",
        "Interoception",
    ]
    _cols = [
        "Raw<br>bandwidth",
        "Normal conscious<br>presence",
        "Power to<br>hijack awareness",
    ]

    # [bandwidth, normal presence, hijack power]
    _z = [
        [3, 3, 2],  # Vision
        [3, 1, 2],  # Proprioception
        [1, 1, 3],  # Vestibular
        [1, 1, 3],  # Pain
        [1, 2, 2],  # Temperature
        [1, 2, 3],  # Interoception
    ]

    _detail = {
        "Vision (reference)": "The high-bandwidth anchor: ~10^7 bit/s, always present, but not the strongest at hijacking awareness.",
        "Proprioception": "Limb position, from millions of muscle spindles. High bandwidth, near-zero conscious presence -- until it fails (Ian Waterman could not stand or hold a cup without watching his hands).",
        "Vestibular": "Balance and head acceleration, from the inner ear. Tiny bandwidth, but a clash with vision (boat, car, VR) triggers nausea that obliterates every other sense.",
        "Pain": "Nociception -- a separate system with its own fibres (A-delta, C), not 'touch turned up'. Minimal bandwidth, maximum priority, engineered to win.",
        "Temperature": "Thermoception -- warm and cold receptors distinct from touch and pain. Low bandwidth, strong affective punch (relief of warmth, shock of cold).",
        "Interoception": "The body's internal state: hunger, thirst, heartbeat, breath, gut. Increasingly seen as the substrate of emotion itself; colours the whole background of experience.",
    }

    _level = {1: "Low", 2: "Med", 3: "High"}
    _customdata = [[_detail[r]] * len(_cols) for r in _rows]

    matrix_fig = go.Figure(
        go.Heatmap(
            z=_z,
            x=_cols,
            y=_rows,
            customdata=_customdata,
            colorscale=[[0.0, "#f7fbff"], [0.5, "#9ecae1"], [1.0, "#08519c"]],
            zmin=1,
            zmax=3,
            xgap=3,
            ygap=3,
            showscale=False,
            hovertemplate="<b>%{y}</b><br>%{x}: %{z}/3<br>%{customdata}<extra></extra>",
        )
    )

    for _i, _r in enumerate(_rows):
        for _j in range(len(_cols)):
            _v = _z[_i][_j]
            matrix_fig.add_annotation(
                x=_cols[_j],
                y=_r,
                text=_level[_v],
                showarrow=False,
                font=dict(size=12, color="white" if _v == 3 else "#333"),
            )

    matrix_fig.update_layout(
        title="The missing senses: low bandwidth, high power to hijack awareness",
        xaxis=dict(side="top", tickfont=dict(size=11)),
        yaxis=dict(autorange="reversed", tickfont=dict(size=12)),
        margin=dict(t=110, l=140, r=40, b=20),
        height=420,
    )

    matrix_fig
    return


@app.cell
def _(go):
    # x = log10(raw bandwidth, bit/s, very rough); y = illustrative capacity to
    # dominate conscious experience (0-10, subjective). The whole point is the
    # ANTI-correlation: the senses that can hijack awareness are not the high-bandwidth ones.
    classic = [
        {"name": "Vision", "logbw": 7.0, "exp": 8.0},
        {"name": "Hearing", "logbw": 5.0, "exp": 6.5},
        {"name": "Touch / Skin", "logbw": 6.0, "exp": 5.5},
        {"name": "Smell", "logbw": 5.0, "exp": 3.5},
        {"name": "Taste", "logbw": 3.0, "exp": 4.5},
    ]
    missing = [
        {"name": "Proprioception", "logbw": 6.0, "exp": 5.0},
        {"name": "Vestibular", "logbw": 4.0, "exp": 9.0},
        {"name": "Pain", "logbw": 3.5, "exp": 10.0},
        {"name": "Temperature", "logbw": 3.0, "exp": 7.0},
        {"name": "Interoception", "logbw": 3.5, "exp": 8.0},
    ]

    quad = go.Figure()

    quad.add_trace(
        go.Scatter(
            x=[d["logbw"] for d in classic],
            y=[d["exp"] for d in classic],
            mode="markers+text",
            text=[d["name"] for d in classic],
            textposition="top center",
            marker=dict(size=18, color="#4e79a7", line=dict(width=1, color="white")),
            name="Classic five (quantified)",
            hovertemplate="<b>%{text}</b><br>~10^%{x:.1f} bit/s raw<br>Experiential weight: %{y}/10<extra></extra>",
        )
    )
    quad.add_trace(
        go.Scatter(
            x=[d["logbw"] for d in missing],
            y=[d["exp"] for d in missing],
            mode="markers+text",
            text=[d["name"] for d in missing],
            textposition="top center",
            marker=dict(
                size=18,
                color="#e15759",
                symbol="diamond-open",
                line=dict(width=2, color="#e15759"),
            ),
            name="Missing senses (hard to quantify)",
            hovertemplate="<b>%{text}</b><br>~10^%{x:.1f} bit/s raw (very uncertain)<br>Experiential weight: %{y}/10<extra></extra>",
        )
    )

    quad.add_annotation(
        x=3.5,
        y=10.0,
        ax=6.5,
        ay=8.2,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        text="",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#999",
        arrowwidth=1,
    )
    quad.add_annotation(
        x=4.6,
        y=9.6,
        text="Low bandwidth, total conscious capture",
        showarrow=False,
        font=dict(size=11, color="#e15759"),
    )

    quad.update_layout(
        title="Raw bandwidth vs. capacity to dominate experience (illustrative)",
        xaxis=dict(title="Raw bandwidth -- log10(bit/s), rough", range=[2.5, 7.6]),
        yaxis=dict(
            title="Capacity to dominate conscious experience (0-10, subjective)",
            range=[2, 11],
        ),
        margin=dict(t=70, l=70, r=40, b=60),
        height=560,
        legend=dict(x=0.01, y=0.99),
    )

    quad
    return


@app.cell
def _(mo):
    mo.md(
        """
    How to read this (and how NOT to):
    - The x-axis (raw bandwidth) is real but rough -- orders of magnitude only, and the missing senses are genuinely hard to put a number on. The y-axis (experiential weight) is openly subjective and illustrative. This chart is an argument, not a measurement.
    - The pattern is the message: the points do not lie on a rising diagonal. Pain, vestibular, and interoception sit top-left -- minimal bandwidth, maximal capacity to seize awareness. Vision sits bottom-right of the high-bandwidth zone -- enormous bandwidth, high but not maximal experiential dominance.
    - If raw bandwidth determined experience, every point would line up bottom-left to top-right. It doesn't. That non-alignment is the entire thesis of the notebook in one picture.
    - Proprioception is the trap: high bandwidth, low conscious presence -- because it is working. Its experiential weight spikes only when it fails. "Importance to experience" and "presence in experience" are not the same thing.
    """
    )
    return


@app.cell
def _(go, make_subplots):
    # The expanded model used by the interactive sections below: the classic five
    # PLUS two of the missing senses (vestibular, pain) so that scenarios like
    # injury and VR sickness can actually surface those channels in the mix.
    CHANNELS = ["Vision", "Touch", "Hearing", "Smell", "Taste", "Vestibular", "Pain"]

    RAW_BW = {
        "Vision": 10_000_000,
        "Touch": 1_000_000,
        "Hearing": 100_000,
        "Smell": 100_000,
        "Taste": 1_000,
        "Vestibular": 10_000,  # very uncertain
        "Pain": 10_000,  # very uncertain; overlaps with Touch
    }

    CHANNEL_COLORS = {
        "Vision": "#4e79a7",
        "Touch": "#f28e2b",
        "Hearing": "#59a14f",
        "Smell": "#e15759",
        "Taste": "#b07aa1",
        "Vestibular": "#76b7b2",
        "Pain": "#edc948",
    }

    import math as _math

    # Consciousness sees sharply diminishing returns on raw throughput, so we weight
    # by PERCEIVED bandwidth = log10(raw) -- a Weber-Fechner-style compression -- not
    # by raw bit/s. Without this, vision's 1000x raw-bandwidth lead would swamp every
    # gate and a maxed-out pain or vestibular channel could never take over the mix,
    # which is the opposite of the notebook's thesis.
    PERCEIVED_BW = {c: _math.log10(RAW_BW[c]) for c in CHANNELS}

    # Tiny helper so the two interactive cells stay in sync.
    def effective_profile(gates: dict[str, float]) -> dict[str, float]:
        """gates: channel -> 0..1 conscious-gate weight.

        Returns a unitless 'experienced salience score' per channel
        (perceived bandwidth x gate), NOT literal bit/s. Only the
        relative shares are meaningful.
        """
        return {c: PERCEIVED_BW[c] * gates.get(c, 0.0) for c in CHANNELS}

    return (
        CHANNELS,
        CHANNEL_COLORS,
        RAW_BW,
        effective_profile,
        make_subplots,
    )


@app.cell
def _(mo):
    mo.md(
        """
    ---

    ## Interactive: the effective-bandwidth toy model

    This is an intentionally crude model. Its only goal is to build intuition, not scientific accuracy.

    For each channel, define a conscious gate -- a single 0-100% knob standing in for the product of three factors:

    experienced_share  ∝  perceived_bandwidth  x  attention  x  novelty  x  salience

    The catch: if perceived_bandwidth were raw bit/s, vision's 1000x lead would swamp every gate and a low-bandwidth channel like pain could never take over -- the opposite of this notebook's thesis. So we use perceived_bandwidth = log10(raw_bandwidth), a Weber-Fechner-style compression: consciousness sees sharply diminishing returns on raw throughput. The output is therefore a unitless experienced-share score, not literal bit/s -- only the relative slices matter.

    A channel contributes to experience to the extent it is attended to, novel (not predicted away), and salient (relevant). Drag the sliders to re-weight the senses and watch the experienced mix change -- even though the raw bandwidth underneath never moves.
    """
    )
    return


@app.cell
def _(mo):
    gate_vision = mo.ui.slider(0, 100, value=35, label="Vision gate %", show_value=True)
    gate_touch = mo.ui.slider(0, 100, value=15, label="Touch gate %", show_value=True)
    gate_hearing = mo.ui.slider(
        0, 100, value=55, label="Hearing gate %", show_value=True
    )
    gate_smell = mo.ui.slider(0, 100, value=20, label="Smell gate %", show_value=True)
    gate_taste = mo.ui.slider(0, 100, value=10, label="Taste gate %", show_value=True)
    gate_vestibular = mo.ui.slider(
        0, 100, value=10, label="Vestibular gate %", show_value=True
    )
    gate_pain = mo.ui.slider(0, 100, value=5, label="Pain gate %", show_value=True)

    _controls = mo.vstack(
        [
            mo.md(
                "Set each channel's conscious gate (attention x novelty x salience):"
            ),
            gate_vision,
            gate_touch,
            gate_hearing,
            gate_smell,
            gate_taste,
            gate_vestibular,
            gate_pain,
        ]
    )
    _controls
    return (
        gate_hearing,
        gate_pain,
        gate_smell,
        gate_taste,
        gate_touch,
        gate_vestibular,
        gate_vision,
    )


@app.cell
def _(
    CHANNELS,
    CHANNEL_COLORS,
    RAW_BW,
    effective_profile,
    gate_hearing,
    gate_pain,
    gate_smell,
    gate_taste,
    gate_touch,
    gate_vestibular,
    gate_vision,
    go,
    make_subplots,
):
    _gates = {
        "Vision": gate_vision.value / 100,
        "Touch": gate_touch.value / 100,
        "Hearing": gate_hearing.value / 100,
        "Smell": gate_smell.value / 100,
        "Taste": gate_taste.value / 100,
        "Vestibular": gate_vestibular.value / 100,
        "Pain": gate_pain.value / 100,
    }

    _eff = effective_profile(_gates)
    _eff_total = sum(_eff.values()) or 1.0
    _raw_total = sum(RAW_BW[c] for c in CHANNELS)
    _dom = max(_eff, key=_eff.get)
    _dom_share = 100 * _eff[_dom] / _eff_total

    play_fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "domain"}, {"type": "domain"}]],
        subplot_titles=("Raw input share", "Experienced share (salience-weighted)"),
    )

    play_fig.add_trace(
        go.Pie(
            labels=CHANNELS,
            values=[RAW_BW[c] for c in CHANNELS],
            hole=0.45,
            sort=False,
            marker=dict(colors=[CHANNEL_COLORS[c] for c in CHANNELS]),
            texttemplate="%{label}<br>%{percent}",
            hovertemplate="<b>%{label}</b><br>Raw: %{value:,} bit/s<br>%{percent}<extra></extra>",
        ),
        row=1,
        col=1,
    )
    play_fig.add_trace(
        go.Pie(
            labels=CHANNELS,
            values=[_eff[c] for c in CHANNELS],
            hole=0.45,
            sort=False,
            marker=dict(colors=[CHANNEL_COLORS[c] for c in CHANNELS]),
            texttemplate="%{label}<br>%{percent}",
            hovertemplate="<b>%{label}</b><br>Salience score: %{value:.2f}<br>Experienced share: %{percent}<extra></extra>",
        ),
        row=1,
        col=2,
    )

    play_fig.update_layout(
        title="Raw input mix vs. experienced mix (drag the sliders above)",
        height=480,
        showlegend=True,
        margin=dict(t=90, l=20, r=20, b=20),
        annotations=[
            dict(
                text=f"{_raw_total/1e6:.1f}M<br>bit/s",
                x=0.185,
                y=0.5,
                font_size=13,
                showarrow=False,
            ),
            dict(
                text=f"{_dom}<br>{_dom_share:.0f}%",
                x=0.815,
                y=0.5,
                font_size=13,
                showarrow=False,
            ),
        ],
    )

    play_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    What to try:
    - Turn Vision down to 5% and Hearing up to 90% (eyes closed, listening hard). The left pie -- raw input -- does not budge: vision is still ~89% of the bits arriving. The right pie flips to hearing-dominated. That divergence between the two pies IS the mismatch between bandwidth and experience.
    - Push Pain to 100% while leaving the others mid-range. Despite pain's tiny raw bandwidth, its slice swells to dominate the right pie -- because the gate, plus the log-compressed perceived bandwidth, decides conscious share. Under a raw-bit/s model this would be impossible; pain would stay a rounding error.
    - The two pies disagree, and that disagreement is the whole point. The left (raw input) stays pinned vision-dominated no matter what you do; the right (experienced share) reshuffles completely. There is no single "human input bandwidth" -- it depends on which layer you measure and what the body is doing.
    - This is a toy. attention, novelty, and salience are collapsed into one knob; perceived bandwidth is a crude log compression; channels are treated as independent; the right-pie numbers are a unitless salience score, not bit/s. It is a thinking tool, not a model of the brain.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    ## Interactive: scenario presets

    Real life sets these gates for you. Each scenario below encodes a plausible per-channel (attention x novelty x salience) profile. Switching scenarios shows how the SAME raw senses produce wildly different experienced mixes -- and how the missing senses (vestibular, pain) step to the front in the edge cases.
    """
    )
    return


@app.cell
def _(mo):
    scenario = mo.ui.dropdown(
        options=[
            "Reading a book",
            "Walking through a city",
            "Quiet office work",
            "Eating a meal",
            "Listening to music",
            "Playing sport",
            "Injury / acute pain",
            "VR motion sickness",
        ],
        value="Reading a book",
        label="Scenario",
    )
    scenario
    return (scenario,)


@app.cell
def _(CHANNELS, CHANNEL_COLORS, RAW_BW, effective_profile, go, scenario):
    # Each scenario: channel -> (attention, novelty, salience), all 0..1.
    # gate = attention * novelty * salience ; effective = raw * gate.
    # Values are illustrative, chosen to make the qualitative point.
    SCENARIOS = {
        "Reading a book": {
            "Vision": (0.9, 0.35, 0.8),
            "Touch": (0.1, 0.1, 0.2),
            "Hearing": (0.15, 0.2, 0.2),
            "Smell": (0.05, 0.1, 0.1),
            "Taste": (0.02, 0.05, 0.05),
            "Vestibular": (0.05, 0.05, 0.1),
            "Pain": (0.05, 0.1, 0.1),
        },
        "Walking through a city": {
            "Vision": (0.8, 0.8, 0.7),
            "Touch": (0.3, 0.3, 0.3),
            "Hearing": (0.6, 0.7, 0.6),
            "Smell": (0.4, 0.7, 0.4),
            "Taste": (0.02, 0.05, 0.05),
            "Vestibular": (0.5, 0.4, 0.5),
            "Pain": (0.1, 0.2, 0.2),
        },
        "Quiet office work": {
            "Vision": (0.7, 0.25, 0.6),
            "Touch": (0.15, 0.1, 0.2),
            "Hearing": (0.2, 0.2, 0.2),
            "Smell": (0.05, 0.1, 0.1),
            "Taste": (0.02, 0.05, 0.05),
            "Vestibular": (0.05, 0.05, 0.1),
            "Pain": (0.1, 0.2, 0.3),
        },
        "Eating a meal": {
            "Vision": (0.4, 0.3, 0.4),
            "Touch": (0.3, 0.3, 0.4),
            "Hearing": (0.2, 0.2, 0.2),
            "Smell": (0.7, 0.7, 0.8),
            "Taste": (0.9, 0.8, 0.95),
            "Vestibular": (0.05, 0.05, 0.1),
            "Pain": (0.05, 0.1, 0.1),
        },
        "Listening to music": {
            "Vision": (0.2, 0.2, 0.2),
            "Touch": (0.2, 0.2, 0.3),
            "Hearing": (0.95, 0.7, 0.95),
            "Smell": (0.05, 0.1, 0.1),
            "Taste": (0.02, 0.05, 0.05),
            "Vestibular": (0.1, 0.1, 0.2),
            "Pain": (0.05, 0.1, 0.1),
        },
        "Playing sport": {
            "Vision": (0.85, 0.7, 0.8),
            "Touch": (0.6, 0.6, 0.7),
            "Hearing": (0.5, 0.5, 0.5),
            "Smell": (0.1, 0.2, 0.2),
            "Taste": (0.05, 0.05, 0.1),
            "Vestibular": (0.8, 0.7, 0.8),
            "Pain": (0.4, 0.5, 0.6),
        },
        "Injury / acute pain": {
            "Vision": (0.3, 0.3, 0.3),
            "Touch": (0.5, 0.5, 0.6),
            "Hearing": (0.2, 0.2, 0.2),
            "Smell": (0.05, 0.1, 0.1),
            "Taste": (0.02, 0.05, 0.05),
            "Vestibular": (0.2, 0.2, 0.3),
            "Pain": (1.0, 0.95, 1.0),
        },
        "VR motion sickness": {
            "Vision": (0.9, 0.8, 0.7),
            "Touch": (0.3, 0.3, 0.3),
            "Hearing": (0.4, 0.4, 0.4),
            "Smell": (0.05, 0.1, 0.1),
            "Taste": (0.05, 0.05, 0.1),
            "Vestibular": (0.95, 0.9, 1.0),
            "Pain": (0.2, 0.3, 0.4),
        },
    }

    _profile = SCENARIOS[scenario.value]
    _gates = {c: _profile[c][0] * _profile[c][1] * _profile[c][2] for c in CHANNELS}
    _eff = effective_profile(_gates)
    _eff_total = sum(_eff.values()) or 1.0
    _raw_total = sum(RAW_BW[c] for c in CHANNELS)
    _dom = max(_eff, key=_eff.get)

    _raw_share = [100 * RAW_BW[c] / _raw_total for c in CHANNELS]
    _eff_share = [100 * _eff[c] / _eff_total for c in CHANNELS]

    scenario_fig = go.Figure()
    scenario_fig.add_trace(
        go.Bar(
            x=CHANNELS,
            y=_raw_share,
            name="Raw input share %",
            marker_color="#bab0ac",
            hovertemplate="<b>%{x}</b><br>Raw share: %{y:.1f}%<extra></extra>",
        )
    )
    scenario_fig.add_trace(
        go.Bar(
            x=CHANNELS,
            y=_eff_share,
            name="Experienced share %",
            marker_color=[CHANNEL_COLORS[c] for c in CHANNELS],
            customdata=[
                f"attention {_profile[c][0]:.2f} x novelty {_profile[c][1]:.2f} "
                f"x salience {_profile[c][2]:.2f} = gate {_gates[c]:.3f}"
                for c in CHANNELS
            ],
            hovertemplate="<b>%{x}</b><br>Experienced share: %{y:.1f}%<br>%{customdata}<extra></extra>",
        )
    )

    scenario_fig.update_layout(
        title=f"Scenario: {scenario.value} -- raw input share vs. experienced share",
        barmode="group",
        xaxis=dict(title=""),
        yaxis=dict(title="Share of total (%)"),
        margin=dict(t=70, l=60, r=30, b=50),
        height=480,
        legend=dict(x=0.7, y=0.99),
        annotations=[
            dict(
                text=f"Dominant experienced channel this scenario: {_dom} ({100 * _eff[_dom] / _eff_total:.0f}% of the mix)",
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.10,
                showarrow=False,
                font=dict(size=12, color="#444"),
            )
        ],
    )

    scenario_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    What the scenarios show:
    - The grey bars (raw input share) are identical in every scenario -- vision ~89%, always. Raw bandwidth is a property of the hardware; it does not care what you are doing.
    - The coloured bars (experienced share) reshuffle completely. Reading is vision-locked. Listening to music is hearing-locked. Eating swings to taste and smell -- the two lowest-bandwidth channels -- because attention, novelty, and salience all spike there.
    - Injury / acute pain is the cleanest punchline. Pain -- a channel with only ~10,000 bit/s of raw bandwidth -- takes the largest experienced slice (~75% in this toy), while vision's 10,000,000 bit/s recedes to a sliver. The eyes are still flooding the brain; the brain just isn't listening.
    - VR motion sickness is a conflict, not a takeover. Vision and vestibular come out roughly co-dominant (each ~45% of the mix): vision says "moving," the inner ear says "still," and the salience of that mismatch -- not its bandwidth -- generates nausea. The damage is done by two channels disagreeing, not by one swallowing the rest.
    - Hover any coloured bar to see the attention x novelty x salience decomposition behind that channel's gate.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    ## Human output bandwidth: there is no single number

    Output is even messier than input, because "output" means at least three different things. Collapsing them into one figure is the most common mistake. The estimates below are midpoints of cited ranges; hover for the range and method.
    """
    )
    return


@app.cell
def _(go):
    # Midpoints of cited ranges. Categories deliberately kept separate.
    output_channels = [
        # A) Symbolic communication -- the actual linguistic/intentional content
        {
            "channel": "Speech (linguistic content)",
            "bw": 39,
            "cat": "Symbolic",
            "detail": "~39 bit/s, strikingly constant across languages (Coupe et al. 2019). Fast/dense languages speak slower, and vice versa.",
        },
        {
            "channel": "Typing",
            "bw": 70,
            "cat": "Symbolic",
            "detail": "~20-120 bit/s depending on speed/skill. A fast typist out-bandwidths speech.",
        },
        {
            "channel": "Handwriting",
            "bw": 15,
            "cat": "Symbolic",
            "detail": "~6-25 bit/s. The slowest mainstream symbolic channel.",
        },
        # B) Physical body output -- observable motion, intentional or not
        {
            "channel": "Eye movements (gaze)",
            "bw": 5_000,
            "cat": "Physical body",
            "detail": "~1k-10k bit/s of fixations/saccades. Carries far more than the linguistic content of what you say.",
        },
        {
            "channel": "Facial motion",
            "bw": 100_000,
            "cat": "Physical body",
            "detail": "~10k-1M bit/s of micro-expressions and muscle activity captured as observable motion.",
        },
        {
            "channel": "Full-body motion",
            "bw": 1_000_000,
            "cat": "Physical body",
            "detail": "~100k-5M bit/s of joint angles and dynamics -- everything a mocap rig would record.",
        },
        # C) Instrumented output -- what a sensor can pull off the body
        {
            "channel": "Full-body motion capture",
            "bw": 2_000_000,
            "cat": "Instrumented",
            "detail": "~100k-5M bit/s. Marker/markerless 3D pose at high frame rate.",
        },
        {
            "channel": "EMG (muscle electrical)",
            "bw": 500_000,
            "cat": "Instrumented",
            "detail": "~10k-1M+ bit/s of raw muscle electrical activity across channels.",
        },
        {
            "channel": "Raw speech acoustics",
            "bw": 75_000,
            "cat": "Instrumented",
            "detail": "~50k-100k bit/s of waveform -- ~2000x the 39 bit/s of meaning it carries.",
        },
    ]

    _cat_colors = {
        "Symbolic": "#e15759",
        "Physical body": "#4e79a7",
        "Instrumented": "#59a14f",
    }

    _sorted = sorted(output_channels, key=lambda d: d["bw"])

    output_fig = go.Figure(
        go.Bar(
            y=[d["channel"] for d in _sorted],
            x=[d["bw"] for d in _sorted],
            orientation="h",
            marker_color=[_cat_colors[d["cat"]] for d in _sorted],
            text=[f"{d['bw']:,} bit/s" for d in _sorted],
            textposition="outside",
            customdata=[f"{d['cat']}: {d['detail']}" for d in _sorted],
            hovertemplate="<b>%{y}</b><br>~%{x:,} bit/s<br>%{customdata}<extra></extra>",
        )
    )

    output_fig.update_layout(
        title="Human output bandwidth by channel (log scale, midpoints of cited ranges)",
        xaxis=dict(title="bit/s (log scale)", type="log", range=[0.8, 7.0]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=90, l=210, r=140, b=50),
        height=560,
        annotations=[
            dict(
                text="<span style='color:#e15759'>● Symbolic</span>   "
                "<span style='color:#4e79a7'>● Physical body</span>   "
                "<span style='color:#59a14f'>● Instrumented</span>",
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.08,
                showarrow=False,
                font=dict(size=12),
            )
        ],
    )

    output_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Reading the output chart -- three categories that should never be averaged together:

    A) Symbolic communication (red): the intentional, decodable content -- ~6-120 bit/s. This is the bandwidth of "you" as a deliberate communicator. Speech sits at ~39 bit/s and, remarkably, stays there across languages: Japanese and Spanish pack fewer bits per syllable but are spoken faster; English and Mandarin do the reverse. The information rate converges (Coupe et al. 2019). Note this lands in the same ~10-50 bit/s band as the conscious "now" from the funnel -- the deliberate input and deliberate output of a human are about the same tiny size.

    B) Physical body output (blue): everything your body radiates as observable motion -- gaze, face, posture, gesture -- ~10^3 to 10^6 bit/s. This is why a video call leaks far more than a phone call, and why poker players wear sunglasses. Your linguistic channel is 39 bit/s; your body is broadcasting thousands of times more.

    C) Instrumented output (green): what a sensor can extract -- mocap, EMG, raw audio -- ~10^4 to 10^6+ bit/s. Raw speech acoustics (~75,000 bit/s) carry ~2,000x more data than the 39 bit/s of meaning inside them; the rest is timbre, prosody, identity, emotion, and redundancy. This gap is exactly what voice-cloning and emotion-recognition systems mine.

    The 5-order-of-magnitude spread (39 bit/s to ~2,000,000 bit/s) is not measurement error. The channels measure genuinely different things: intended meaning, observable behaviour, and extractable signal. "Human output bandwidth" is undefined until you say which one you mean.
    """
    )
    return


@app.cell
def _(go):
    # Five legitimate, mutually-inconsistent definitions of "human bandwidth".
    definitions = [
        {
            "defn": "Raw signal bandwidth",
            "bw": 11_200_000,
            "detail": "Total afferent nerve capacity. The 'fibre-optic cable' number.",
        },
        {
            "defn": "Entropy-adjusted bandwidth",
            "bw": 1_000_000,
            "detail": "After removing redundancy / predictable structure. True information content of the input.",
        },
        {
            "defn": "Attention-weighted bandwidth",
            "bw": 10_000,
            "detail": "What survives the attentional bottleneck toward working memory.",
        },
        {
            "defn": "Subjective / conscious bandwidth",
            "bw": 40,
            "detail": "The experienced 'now'. Norretranders ~16-40 bit/s; behaviour ~10 bit/s (Zheng & Meister 2024).",
        },
        {
            "defn": "Symbolic communication bandwidth",
            "bw": 39,
            "detail": "Deliberate linguistic output. Speech ~39 bit/s (Coupe et al. 2019).",
        },
    ]

    _colors = ["#08306b", "#2171b5", "#4292c6", "#e15759", "#f28e2b"]

    defn_fig = go.Figure(
        go.Bar(
            y=[d["defn"] for d in definitions],
            x=[d["bw"] for d in definitions],
            orientation="h",
            marker_color=_colors,
            text=[f"{d['bw']:,} bit/s" for d in definitions],
            textposition="outside",
            customdata=[d["detail"] for d in definitions],
            hovertemplate="<b>%{y}</b><br>~%{x:,} bit/s<br>%{customdata}<extra></extra>",
        )
    )

    defn_fig.update_layout(
        title="Five definitions of 'human bandwidth' -- spanning 6 orders of magnitude",
        xaxis=dict(title="bit/s (log scale)", type="log", range=[1.3, 7.6]),
        yaxis=dict(autorange="reversed"),
        margin=dict(t=70, l=270, r=140, b=50),
        height=430,
    )

    defn_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Five answers to "what is a human's bandwidth?", each correct under its own definition:
    - Raw signal bandwidth (~10^7 bit/s): the nerve-capacity number. Real, but it is the capacity of the cable, not the content of the call.
    - Entropy-adjusted (~10^6 bit/s): strip out redundancy and prediction, and the true information content of the input is roughly 10x smaller.
    - Attention-weighted (~10^4 bit/s): what actually clears the attentional gate toward working memory.
    - Subjective / conscious (~40 bit/s): the felt present. Six orders of magnitude below the raw input. This is the number that feels like "me."
    - Symbolic communication (~39 bit/s): deliberate linguistic output -- and almost exactly the same size as the conscious input. The deliberate human is a ~40 bit/s device wrapped around a ~10,000,000 bit/s sensor array.

    Anyone who quotes a single "human bandwidth" figure has silently picked one of these and dropped the other four. The honest answer is the whole ladder.
    """
    )
    return


@app.cell
def _(go):
    # End-to-end flow: input senses -> processing layers -> conscious bottleneck -> output.
    sankey_labels = [
        "Vision",
        "Touch",
        "Hearing",
        "Smell/Taste",  # 0-3 raw inputs
        "Peripheral compression",
        "Predictive coding",  # 4-5
        "Attentional bottleneck",  # 6
        "Conscious 'now' (~40 bit/s)",  # 7
        "Symbolic output (~39 bit/s)",
        "Body / motion output (~10^6 bit/s)",  # 8-9
    ]

    sankey_links = {
        "source": [
            0,
            1,
            2,
            3,  # inputs -> peripheral compression
            4,
            4,  # compression -> predictive coding & (leak) attention
            5,  # predictive coding -> attention
            6,  # attention -> conscious
            7,
            7,  # conscious -> outputs
            6,  # attention -> body output (much behaviour bypasses full consciousness)
        ],
        "target": [
            4,
            4,
            4,
            4,
            5,
            6,
            6,
            7,
            8,
            9,
            9,
        ],
        "value": [
            89,
            9,
            1,
            1,  # input shares (~% of raw)
            70,
            30,
            70,
            40,
            20,
            20,
            55,
        ],
    }

    _node_colors = (
        ["#4e79a7", "#f28e2b", "#59a14f", "#b07aa1"]
        + ["#9ecae1", "#6baed6", "#2171b5"]
        + ["#e15759"]
        + ["#f28e2b", "#76b7b2"]
    )

    flow_fig = go.Figure(
        go.Sankey(
            arrangement="snap",
            node=dict(
                pad=22,
                thickness=24,
                line=dict(color="black", width=0.5),
                label=sankey_labels,
                color=_node_colors,
                hovertemplate="<b>%{label}</b><extra></extra>",
            ),
            link=dict(
                source=sankey_links["source"],
                target=sankey_links["target"],
                value=sankey_links["value"],
                hovertemplate="<b>%{source.label}</b> -> <b>%{target.label}</b><extra></extra>",
            ),
        )
    )

    flow_fig.update_layout(
        title="Input -> processing -> conscious bottleneck -> output (widths illustrative, NOT to scale)",
        margin=dict(t=70, l=20, r=20, b=30),
        height=520,
    )

    flow_fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    Reading the flow (and its deliberate distortion):
    - Link widths are illustrative, not to scale. If they were to scale, the conscious bottleneck and symbolic output would be invisible hairlines next to the input -- a ~1,000,000:1 ratio cannot be drawn honestly on one diagram. The Sankey shows topology (what connects to what), not true magnitudes.
    - Two paths leave the attentional stage. One funnels into the conscious "now" and then into deliberate symbolic output (~39 bit/s). The other routes straight to body/motion output -- most behaviour (walking, balancing, expressing) is generated without passing through the narrow conscious channel at all.
    - The body-output link is wide on purpose: you broadcast far more through motion and expression than through deliberate words. The conscious self is a low-bandwidth narrator sitting on top of a high-bandwidth sensorimotor machine.
    - Smell and taste are merged here purely to keep the diagram legible; nothing rests on it.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ---

    # Final synthesis: there is no single human bandwidth number

    The answer to "how much information enters and leaves a human?" depends entirely on the layer being measured.

    - Vision dominates raw external sensory throughput -- roughly 10^7 bit/s, about 89% of all input bits. This is real, and it is the source of the "vision is 90% of perception" cliche. It is also nearly irrelevant to what experience feels like.
    - Conscious experience is shaped far more by attention, prediction error, salience, and bodily state than by raw bandwidth. A 1,000 bit/s pain or taste signal routinely overrides a 10,000,000 bit/s visual stream. The senses missing from the classic table -- proprioception, vestibular, pain, temperature, interoception -- carry little measurable bandwidth yet can seize the entire conscious workspace.
    - The deliberate, conscious human is astonishingly slow: ~10-50 bit/s in and ~39 bit/s out. The "self" that reads, decides, and speaks is a ~40 bit/s device bolted onto a ~10^7 bit/s sensor array and a ~10^6 bit/s motor system.
    - Human output ranges from tens of bit/s for symbolic communication to millions of bit/s for observable physical state. Which figure is "right" depends only on whether you mean intended meaning, observable behaviour, or extractable signal.

    So: there is no single human bandwidth number. There is a ladder of them -- raw, entropy-adjusted, attention-weighted, subjective, and symbolic -- spanning six orders of magnitude, each measuring something genuinely different. Anyone who gives you one number has quietly chosen a rung and hidden the ladder.

    ---

    Caveats, stated plainly:
    - Almost every figure here is an order-of-magnitude estimate. The classic sensory numbers (Nørretranders, after Zimmermann) are decades old and methodology-dependent. The chemical senses (smell, taste) and the missing senses (proprioception, vestibular, interoception) are especially uncertain -- arguably not meaningfully expressible in bit/s at all.
    - "Bits" across these layers are not the same bits. Nerve-capacity bits, entropy bits, and linguistic-content bits measure different things and should not be arithmetically compared, even though they share a unit.
    - The effective-bandwidth model is a toy. Attention, novelty, and salience are not independent multiplicative factors, channels are not independent, and consciousness is not a weighted sum of sensory streams. The model is a tool for intuition, not a theory of mind.
    - The point of the uncertainty is not that the numbers are useless. It is that the GAPS between the layers -- the ~1,000,000:1 collapse from input to awareness -- are robust to any plausible revision of the individual figures. The structure survives even if every number is off by 10x.

    Key sources: Nørretranders, "The User Illusion" (1991/1998); Zheng & Meister, "The unbearable slowness of being" (Neuron, 2024); Coupé, Oh, Dediu & Pellegrino, "Different languages, similar encoding efficiency" (Science Advances, 2019); Rao & Ballard, "Predictive coding in the visual cortex" (Nature Neuroscience, 1999); Friston, "The free-energy principle" (2010).
    """
    )
    return


if __name__ == "__main__":
    app.run()
