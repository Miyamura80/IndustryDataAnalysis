import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
 
    """)
    return


@app.cell
def _():
    import plotly.graph_objects as go

    # Data based on the "How this hangs together" section
    segment_data = [
        {"segment": "Specialty Chemicals", "value_trillion": 0.95},
        {"segment": "Petrochemicals & Polymers", "value_trillion": 0.70},
        {"segment": "Agrochemicals", "value_trillion": 0.25},
        {"segment": "Consumer & Care Chemicals", "value_trillion": 0.125},
        {"segment": "Industrial Gases", "value_trillion": 0.11},
    ]

    labels = [entry["segment"] for entry in segment_data]
    values_trillion = [entry["value_trillion"] for entry in segment_data]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values_trillion,
        hole=0.4,
        textinfo="label+percent",
        texttemplate="<b>%{label}</b><br>$%{value:.3f}T<br>%{percent}",
        hovertemplate="<b>%{label}</b><br>Market Size: $%{value}T<br><extra></extra>"
    )])

    fig.update_layout(
        title="Global Chemicals Industry Segmentation (2024 Estimates)",
        annotations=[dict(text="Major<br>Segments", x=0.5, y=0.5, font_size=14, showarrow=False)],
        showlegend=True
    )

    fig
    return


@app.cell
def _(mo):
    mo.md("""
    **Note on Data:**
    The chart above visualizes the major functional segments described in the text.
    The sum of these specific segments is approximately **US$2.14T**.

    The text notes that the total global chemicals market is estimated between **US$3.5T** (narrow definition) and **US$5.8T** (broad definition including pharma). The difference is accounted for by overlapping categories, pharmaceuticals, fertilizers, and other downstream formulated products not explicitly categorized in the five main functional buckets.
    """)
    return


if __name__ == "__main__":
    app.run()
