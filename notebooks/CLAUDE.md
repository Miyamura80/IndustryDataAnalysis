# Notebooks CLAUDE.md

## Marimo Markdown Rendering

- **Escape dollar signs in `mo.md()` blocks.** Marimo interprets `$...$` as LaTeX math. Any `$` in prose text (e.g. `$16.5B`, `$212B`) must be written as `\$` inside `mo.md("""...""")` strings. Unescaped `$` will cause words between two dollar signs to be concatenated into a single italicized blob (e.g. `$16.5 billion in premiums and pays out ~$8.3 billion` renders as "billioninpremiumsandpaysout").
- **Do not use `**bold**` in `mo.md()` blocks.** Marimo's markdown renderer sometimes concatenates words around `**` markers instead of bolding them. Use plain text instead. Bold in Plotly chart annotations (`<b>...</b>` HTML) is fine — the issue is only in `mo.md()`.
- **Plotly HTML bold is fine.** `<b>%{label}</b>` in `hovertemplate` and `texttemplate` works correctly — this is Plotly's own renderer, not marimo's markdown.

## Notebook Structure Conventions

- Every notebook follows the pattern: `import marimo` + `__generated_with` + `app = marimo.App(width="medium")`
- First cell: `import marimo as mo`
- Second cell: title + intro markdown via `mo.md()`
- Third cell: `import plotly.graph_objects as go`
- Subsequent cells alternate between visualization cells and explanatory markdown cells
- Final line: `if __name__ == "__main__": app.run()`
- Each `@app.cell` function uses `def _():` or `def _(go):` etc. for dependencies

## Visualization Preferences

- **Plotly only** — no matplotlib, no altair
- **Donut charts** (`go.Pie` with `hole=0.4`) for top-level market segmentation. Center annotation shows total market size. `texttemplate` shows label + value + percent.
- **Icicle charts** (`go.Icicle`) for hierarchical market maps. Load node data from JSON files in `notebooks/data/`. Use `branchvalues="total"` — parent values must exactly equal the sum of children.
- **Treemaps** (`go.Treemap`) for company-level competitive landscapes grouped by a strategic dimension (not just org type). Country flag emojis on company labels.
- **Sankey diagrams** (`go.Sankey`) for flow relationships (e.g. threat vector -> breach type -> claim category). Three-color node scheme by column.
- **Dual-axis charts** via `make_subplots(specs=[[{"secondary_y": True}]])` for overlaying bars and lines (e.g. premium growth vs loss ratios).
- **Horizontal bars** for rate changes (green = positive, red/crimson = negative) and timelines.
- Rich hover templates everywhere: `<b>%{label}</b><br>...` format with `<extra></extra>` to suppress trace info.
- `height=800` for icicle charts, `height=350-500` for simpler charts.

## Data Conventions

- Icicle/treemap node data goes in `notebooks/data/<name>_nodes.json` as a flat array of `{"label", "parent", "value", "hover"}` objects.
- The root node has `"parent": ""`.
- Always verify parent-child value sums before writing JSON: run a script to check `branchvalues="total"` consistency.
- Hardcode data directly in cells for simpler charts (donuts, bar charts, time series). Only use JSON files for hierarchical data with many nodes.
- Country flags as unicode emoji in labels: `"\U0001f1fa\U0001f1f8"` for US, etc.
- When data has uncertainty ranges (low/high), use midpoints for sizing and show the range in hover text.
- Always cite sources and note whether figures are actual/reported vs estimated/projected.

## Analytical Style

- Lead with the most consequential insight as the notebook title (e.g. "Only 0.17% of cyber economic losses are insured").
- Markdown notes after each chart explain how to read it, cite data sources, and flag caveats (double-counting, overlapping definitions, estimate uncertainty).
- Use log scale when values span multiple orders of magnitude (e.g. protection gap chart: $8.3B to $9,500B).
- When showing market targets or projections, visually distinguish actual data from forecasts using color.
- Strategy/archetype groupings are more insightful than org-type groupings (e.g. "Scale / mass writers" vs "Technical underwriters" is better than "Carrier" vs "MGA").

## Data Sourcing

- Anchor year should be the most recent with available data (prefer 2025 over 2024 when figures exist).
- Cross-reference multiple sources for market sizes and note the range (e.g. Munich Re \$16.3B, Swiss Re \$15.6B, Gallagher Re \$16.9B).
- For company-level data, prefer statutory filings (NAIC, AM Best, Lloyd's) over analyst estimates.
- Spawn subagents for web research when building a new notebook — data gathering is the bottleneck, not code.

## Common Pitfalls

- Marimo server must be restarted to pick up file changes: `pkill -f "marimo run notebooks/..."` then re-launch.
- `uv run python` not `python` — the project uses uv.
- JSON node files: if parent-child sums don't match, the icicle chart will silently render incorrectly. Always verify with a script before committing.
- The `__file__` variable is not always available in marimo. Use the fallback pattern: `Path(__file__).parent if "__file__" in globals() else Path.cwd() / "notebooks"`.
