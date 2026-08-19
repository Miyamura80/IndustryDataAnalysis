# Insurance market sizes: sources and method

Compiled 19 August 2026. All values in USD billions, one decimal.

Two rules govern every cell below:

1. A non-blank cell traces to a named public source listed here.
2. Where no reputable public figure could be found, the cell is **blank**. No cell has been filled by extrapolation, trend-fitting, or judgement.

Cells that are arithmetic on sourced numbers (a sum, a published percentage share applied to a published total, a currency conversion at the stated rate) are marked **derived** and the arithmetic is shown.

---

## Global FX assumption

All EUR figures are converted at a **single rate: EUR 1 = USD 1.0824**, the 2024 annual average of the ECB euro reference rate (Deutsche Bundesbank, *Exchange rate statistics*, table "Euro-Referenzkurse der EZB", 2024 annual average = 1.0824; the same table gives 1.1300 for 2025).

A single rate is used deliberately. The Allianz series is published at *constant* exchange rates chosen by each report vintage (the 2023 report converts at 2022 rates, the 2025 report at 2024 rates, the 2026 report at 2025 rates), so its year-on-year movement is already FX-neutral within a vintage. Applying one stated rate keeps the conversion reproducible and does not introduce a second, inconsistent FX effect.

**Consequence to be aware of:** levels are not comparable *across* Allianz vintages. Allianz reports EUR 7.0trn of global premium for 2024 (2025 report) and EUR 6.9trn for 2025 (2026 report) while simultaneously reporting +7.1% growth in 2025. The apparent decline is a rebasing artefact, not a contraction. Where this affects a cell it is flagged below.

---

# Deliverable 1: US P&C market sizes

File: `insurance_us_pc_market_sizes_2020_2025.csv`

## Primary source for all Net premiums written rows

Insurance Information Institute (Triple-I), table **"Net Premiums Written By Line, Property/Casualty Insurance"**, archived vintages at <https://www.iii.org/table-archive/21227>.
Underlying data: **NAIC statutory annual statement data, sourced from S&P Global Market Intelligence**.

- 2020 values are taken from the **2018-2020** vintage of that table (values stated in USD millions).
- 2021, 2022 and 2023 values are taken from the **2021-2023** vintage (values stated in USD thousands despite the table's "$ millions" caption; the "Total, all lines" of $715,937,546 for 2021 confirms the unit, reconciling to $715.9bn).

All these are **actual / reported** statutory figures, not estimates or projections.

### Per-row detail (USD bn, converted from the source units)

| Row | 2020 | 2021 | 2022 | 2023 | Source line item |
|---|---|---|---|---|---|
| Private Passenger Auto | 243.7 | 252.9 | 268.0 | 306.6 | "Private passenger auto" (liability + collision/comprehensive) |
| Commercial Auto | 39.9 | 46.6 | 51.7 | 55.8 | "Commercial auto" (liability + collision/comprehensive) |
| Homeowners | 97.0 | 103.4 | 113.9 | 128.0 | "Homeowners multiple peril" |
| Workers Compensation | 42.5 | 43.1 | 47.5 | 48.0 | "Workers compensation" (excludes the separate "Excess workers compensation" line) |
| Other/General Liability | 69.4 | 84.6 | 94.2 | 95.6 | "Other liability" |
| Commercial Multi-Peril | 41.0 | 43.7 | 48.4 | 54.6 | "Commercial multiple peril" |
| Commercial Property - Fire | 13.2 | 15.6 | 16.5 | 21.0 | "Fire" |
| Commercial Property - Allied Lines | 13.2 | 14.8 | 15.7 | 19.4 | "Allied lines" |
| Commercial Property - Fire + Allied (combined) | 26.4 | 30.3 | 32.1 | 40.4 | **derived**: Fire + Allied lines, summed at source precision then rounded |
| Inland Marine | 14.9 | 17.6 | 21.2 | 22.7 | "Inland marine" |
| Medical Professional Liability | 9.0 | 10.0 | 10.6 | 11.0 | "Medical professional liability" |

The combined Fire + Allied row is computed from unrounded source values, so it will not always equal the sum of the two rounded rows above it (2020: 13,196.2 + 13,156.8 = 26,353.0 thousand-USD-millions, rounding to 26.4, not 26.2). **Do not sum the two component rows and the combined row together.**

### Definitional caveats on the NPW rows

- **Net, not direct.** These are premiums *after* reinsurance transactions. NAIC and S&P Global also publish direct premiums written (DPW) by line, which are materially larger (2024 industry DPW was $1.05trn against industry NPW of roughly $0.93trn). Do not mix the two series.
- **Excludes state funds.** The Triple-I table footnote states "After reinsurance transactions, excludes state funds." Note one apparent inconsistency worth flagging: the table's 2023 workers compensation figure of $48.0bn matches NCCI's *state-fund-inclusive* total for 2023 ($48.0bn) rather than its private-carrier figure ($43.0bn). Treat the workers compensation row as state-fund-inclusive when comparing to NCCI.
- **Total does not tie to other published totals.** The table's own footnote: "May not match total premiums shown elsewhere in this book because of the use of different exhibits from S&P Global Market Intelligence." For context, the same period has at least four published industry NPW totals: Triple-I/S&P $857.4bn for 2023; NAIC $863.4bn (2023) and $934.8bn (2024, from the *2024 Full Year Results* release — later revised to $938.7bn in the NAIC year-end 2025 snapshot, see below); Verisk/APCIA $926bn (2024); Triple-I "at a glance" $932.5bn (2024).
- **Inland marine breaks in 2024.** From the 2024 data year, pet insurance is reported as a separate NAIC line of business and is no longer inside inland marine (NAIC, *2024 Market Share Reports for Property/Casualty Groups and Companies*, technical notes). Inland marine 2024 onward is therefore not comparable to 2020-2023 on a like-for-like basis. AM Best put pet premium at roughly $4bn to $4.5bn for 2024.

### Why 2024 and 2025 are blank on the NPW rows

The Triple-I table archive publishes vintages only up to 2021-2023. The current 2022-2024 vintage exists but its tables are not rendered in the public HTML (the page returns the footnotes without the table body), and the underlying line-of-business NPW detail otherwise sits behind the Triple-I *Insurance Fact Book* and S&P Global Market Intelligence subscriptions. Rather than mix a different basis into the middle of a time series, these cells are left blank.

Partial 2024 and 2025 evidence that **was** sourced, for whoever fills these in later:

- **Industry NPW totals (actual).** NAIC: $934.8bn (2024), $863.4bn (2023). NAIC year-end 2025 snapshot: $976.8bn (2025), $938.7bn (2024), $863.4bn (2023), $781.7bn (2022), $719.9bn (2021). Sources: NAIC, *U.S. Property & Casualty and Title Insurance Industries 2024 Full Year Results*; NAIC 2025 year-end industry snapshot.
- **Workers compensation NPW 2024 (actual).** NCCI *2025 State of the Line Guide*: $41.6bn private carriers, $46.3bn including state funds. NCCI's basis is NAIC Insurance Expense Exhibit Part II, net of reinsurance. Total P&C net written premium for private carriers: $927.1bn (2024), $852bn (2023).
- **2024 DPW by line (actual, wrong metric for this table).** S&P Global Market Intelligence, March 2025: private auto $358.8bn, homeowners $169.6bn, commercial auto $70.9bn, workers compensation $55.4bn, "other liability" $123.3bn, three commercial property lines combined $104.0bn. NAIC's own 2024 report gives personal auto liability $182.4bn, personal auto physical damage $158.5bn, homeowners $173.2bn, fire $31.8bn, allied lines $31.2bn, other liability occurrence $83.6bn, other liability claims-made $40.4bn, commercial MP non-liability $45.5bn, commercial MP liability $21.6bn, commercial auto liability $54.6bn, commercial auto physical damage $16.4bn, workers compensation $57.5bn.

## Cyber row

Metric is **Direct premiums written**, not NPW, as specified. Cyber is reported through the NAIC Cybersecurity Insurance Coverage Supplement to the P&C annual statement, which collects DWP only.

Source: **NAIC, *Report on the Cybersecurity Insurance Market*, 2025 edition**, Figure 2 ("Direct Written Premium ... Does not Include Alien Surplus Lines"), <https://content.naic.org/sites/default/files/inline-files/2025_Cybersecurity_Insurance%20Report.pdf>. Actual / reported.

| Year | Figure 2 value (USD) | CSV value |
|---|---|---|
| 2020 | 2,753,782,002 | 2.8 |
| 2021 | 4,827,263,153 | 4.8 |
| 2022 | 7,264,592,270 | 7.3 |
| 2023 | 7,248,231,390 | 7.2 |
| 2024 | 7,082,935,371 | 7.1 |

Caveats:

- **Scope: US-domiciled insurers only.** Including alien surplus lines carriers writing in the US, the same report's Figure 1 gives $4.07bn (2020), $6.54bn (2021), $9.69bn (2022), $9.84bn (2023), $9.14bn (2024). The US-domiciled series was chosen because it is the statutory filing basis and matches the `geo = US` convention of the rest of the file. If the notebook wants the full addressable US cyber pool, use the Figure 1 series instead and say so.
- **Internal inconsistency in the source.** Figure 3 of the same report gives slightly different domestic totals for the early years ($2,774.5m for 2020, $4,795.8m for 2021, $7,237.2m for 2022) against Figure 2. The differences are under 0.8%. Figure 2 was used because it is the report's own five-year comparable series.
- **2024 definition change.** From the 2024 filing year the supplement replaced the stand-alone/package split with a primary/excess/endorsement split, and dropped identity-theft reporting. Totals remain comparable; the sub-splits do not.
- **Package cyber premium is partly estimated by filers.** The NAIC only required package cyber DWP to be filed "if available or estimable." Aon's 2023 market update put roughly 18% of reported package cyber premium as filer-estimated rather than exactly broken out.
- **2025 is blank.** The NAIC cyber report covering calendar 2025 had not been published as at the compilation date (the 2025 edition covers data year 2024).

---

# Deliverable 2: global premium pools

File: `insurance_global_market_size_proxies_2020_2025.csv`

## Structural notes

**These are proxy estimates, not statutory actuals.** Every cell in this file is either a published market estimate or simple arithmetic on one.

**Total rows.** Each segment carries a `... (total)` subsegment row alongside its component rows. **Do not sum a total row together with its component rows.** The totals are included because they are better sourced than the component splits for most years.

**Segment definitions differ between the two anchor sources, and that is the main driver of the bands:**

- **Swiss Re Institute (sigma)** splits the world into *life* and *non-life*, and allocates all accident and health business to **non-life**, regardless of which carrier type writes it. So sigma's "non-life" = this file's Health + Property & Casualty.
- **Allianz Research (Global Insurance Report)** splits into *life*, *p&c* and *health* as three separate segments, closer to this file's structure. Japan is a known exception: Allianz reports Japanese health inside life (third-sector products).
- Neither is wrong. The Health and P&C bands are wide for 2024 precisely because the two houses draw the health/P&C line differently.

**Reinsurance double-counts primary premium.** The Reinsurance segment measures premium ceded by primary carriers to reinsurers. That premium is already inside the Life, Health and P&C pools as gross/direct written premium. **Reinsurance must not be added to the other three segments to get a world total.**

**Basis: gross/direct written premium.** Swiss Re's world series is explicitly "before reinsurance transactions." Allianz reports gross written premiums. This is the opposite convention to Deliverable 1, which is net of reinsurance. The two files are not summable.

## Band method

`low` and `high` span the reputable published estimates found for that cell. Where only one estimate exists, the band is set to **±2.5%** of the point estimate. That figure is not arbitrary: it is the observed magnitude of Swiss Re's own vintage-to-vintage revisions to the same year (2020 life was revised from $2,797.4bn to $2,727.2bn, a 2.6% move; 2021 life from $2,997.6bn to $2,940.3bn, 1.9%). Single-source bands are flagged below.

Where a source published a figure rounded to EUR 0.1trn, the band spans ±EUR 50bn (±EUR 100bn for the health rounding) converted at the stated rate, rather than ±2.5%.

Point estimates are the midpoint of the band where two independent sources disagree, and the sourced value itself where only one source exists.

## Source inventory

| Tag | Source | Coverage used |
|---|---|---|
| SR-a | Swiss Re Institute *sigma* world DPW series, republished by Triple-I at <https://www.iii.org/table-archive/20964> (vintages cite *sigma* 3/2024 and the sigma database) | World life and non-life totals, 2020-2023, USD, actual/reported |
| SR-b | Swiss Re Institute, *sigma* 2/2025, "World insurance in 2025: a riskier, more fragmented world order" | 2024 non-life volume and line-of-business split (Figure 16); life/savings-risk shares (Figure 22); 2025 non-life forecast USD 4.8trn |
| SR-c | Swiss Re Institute, *sigma* 5/2024 and press release 19 Nov 2024 | Global life premium pool USD 3.1trn in 2024 |
| SR-d | Swiss Re Institute, *sigma* 3/2025, "Growing stronger: Property & Casualty market adapts to riskier world" | "USD 2.4 trillion global property and casualty insurance market" (2024), used as a cross-check |
| AZ-22 | Allianz Global Insurance Report 2022 | 2021: total EUR 4.2trn, life EUR 2.5trn, p&c EUR 1.7trn (no separate health segment in this vintage) |
| AZ-23 | Allianz Global Insurance Report 2023 | 2022: total EUR 5.6trn, life EUR 2.6trn, p&c EUR 1.8trn, health EUR 1.1trn |
| AZ-24 | Allianz Global Insurance Report 2024 | 2023: total EUR 6.2trn, life EUR 2,620bn, p&c EUR 2,153bn, health EUR 1,427bn |
| AZ-25 | Allianz Global Insurance Report 2025 | 2024: total EUR 7.0trn, life EUR 2,902bn, p&c EUR 2,424bn, health EUR 1,682bn |
| AZ-26 | Allianz Global Insurance Report 2026 | 2025: total EUR 6.9trn, life EUR 2,861bn, p&c EUR 2,320bn, health EUR 1,688bn |
| ATL | Atlas Magazine, *Reinsurance Reports* / "Global reinsurance market" statistics, compiled from 143-148 reinsurers' accounts | Global reinsurance GWP 2022-2024 |
| BBK | Deutsche Bundesbank, *Exchange rate statistics*, ECB euro reference rates | EUR/USD 2024 annual average 1.0824 |

## Row-by-row

### Life, All life products (total)

| Year | Point | Low | High | Basis |
|---|---|---|---|---|
| 2020 | 2762.3 | 2727.2 | 2797.4 | SR-a, two vintages of the same year: $2,727,176m (2019-2021 vintage) and $2,797,437m (2018-2020 vintage). Point = midpoint. Actual/reported, revised. |
| 2021 | 2940.3 | 2706.0 | 2997.6 | SR-a two vintages: $2,940,266m (*sigma* 3/2024) and $2,997,569m (earlier). Low = AZ-22 EUR 2,500bn **derived** × 1.0824. Point = the current sigma vintage. |
| 2022 | 2813.6 | 2760.1 | 2868.4 | SR-a $2,813,032m; AZ-23 EUR 2.6trn **derived** × 1.0824 = 2814.2, with ±EUR 50bn rounding band. Point = midpoint of the two. |
| 2023 | 2862.5 | 2835.9 | 2889.0 | SR-a $2,888,998m; AZ-24 EUR 2,620bn **derived** × 1.0824 = 2835.9. Point = midpoint. |
| 2024 | 3120.6 | 3100.0 | 3141.1 | SR-c USD 3.1trn (estimated at time of publication); AZ-25 EUR 2,902bn **derived** × 1.0824 = 3141.1. Point = midpoint. |
| 2025 | 3096.8 | 3019.4 | 3174.2 | AZ-26 EUR 2,861bn **derived** × 1.0824. Single-source ±2.5% band. **Estimated.** |

**2025 caveat:** AZ-26 is stated at 2025 exchange rates while AZ-25 is stated at 2024 rates, so the converted 2025 point sits below the converted 2024 point even though Allianz reports +6.9% life growth in 2025. Do not read a decline into that pair. A Swiss Re USD-native 2025 life figure was not published as at the compilation date; *sigma* 2/2025 gives USD 3.5trn for 2026 and USD 5.1trn for 2035, both forecasts.

### Life, Savings and annuities / Risk protection

Populated for **2020 and 2024 only**.

Shares are from SR-b Figure 22, "shares of savings and risk premiums": savings 77.8% / risk 22.2% in 2020, savings 79.5% / risk 20.5% in 2024. **Derived**: share applied to the Life total point, low and high above.

- 2020: 0.778 × 2762.3 = 2149.1 savings; 0.222 × 2762.3 = 613.2 risk.
- 2024: 0.795 × 3120.6 = 2480.9 savings; 0.205 × 3120.6 = 639.7 risk.

2021, 2022, 2023 and 2025 are **blank on purpose**. Swiss Re publishes the savings/risk split as a chart with labels only on 2020, 2024 and 2028F. Interpolating a share for the intervening years would be inventing a precise figure, so those cells are left empty. The 2028F share (savings 79.7% / risk 20.3%) is available if a forecast row is ever wanted.

Note this split is savings-vs-protection, not the individual/group/annuity cut suggested in the brief. It was chosen because it is the split Swiss Re actually publishes; no comparable public individual/group/annuity global series was found.

### Health, Private health (all products)

| Year | Point | Low | High | Basis |
|---|---|---|---|---|
| 2020 | blank | | | No public global health premium pool found for 2020. AZ-22 did not yet report health as a separate segment. |
| 2021 | blank | | | Same. |
| 2022 | 1190.6 | 1136.5 | 1244.8 | AZ-23 EUR 1.1trn **derived** × 1.0824, ±EUR 50bn rounding band. **Estimated.** |
| 2023 | 1544.6 | 1506.0 | 1583.2 | AZ-24 EUR 1,427bn **derived** × 1.0824. Single-source ±2.5%. **Estimated.** |
| 2024 | 2015.8 | 1820.6 | 2211.0 | Low = AZ-25 EUR 1,682bn **derived** × 1.0824. High = SR-b Figure 16 health block, USD 2,211bn. Point = midpoint. **Estimated.** |
| 2025 | 1827.1 | 1781.4 | 1872.8 | AZ-26 EUR 1,688bn **derived** × 1.0824. Single-source ±2.5%. **Estimated.** |

**The 2024 band is wide (21% from low to high) and that is the honest answer, not a data error.** Swiss Re allocates all accident and health business to non-life and counts the full US private health pool; Allianz's health segment is drawn more narrowly and puts Japanese third-sector business in life. Any figure inside that band is defensible depending on which definition the notebook wants.

No sub-split of Health is provided. Neither anchor source publishes a global private-health versus supplemental/third-sector breakdown, so the suggested two-way split could not be sourced.

### Property & Casualty, All P&C lines (total)

| Year | Point | Low | High | Basis |
|---|---|---|---|---|
| 2020 | blank | | | AZ-22 covers 2021 forward; no separate 2020 p&c figure found on a consistent basis. Swiss Re's 2020 non-life ($3,489.6bn to $3,564.7bn) cannot be split into health and P&C without a 2020 global health figure, which is also blank above. |
| 2021 | 1840.1 | 1786.0 | 1894.2 | AZ-22 EUR 1.7trn **derived** × 1.0824, ±EUR 50bn rounding band. **Estimated.** |
| 2022 | 1948.3 | 1894.2 | 2002.4 | AZ-23 EUR 1.8trn **derived** × 1.0824, ±EUR 50bn rounding band. **Estimated.** |
| 2023 | 2330.4 | 2272.1 | 2388.7 | AZ-24 EUR 2,153bn **derived** × 1.0824. Single-source ±2.5%. **Estimated.** |
| 2024 | 2508.4 | 2393.0 | 2623.8 | Low = SR-b, non-life total 4,604 less health 2,211 = 2,393 (**derived**, and independently corroborated by SR-d's "USD 2.4 trillion global P&C market"). High = AZ-25 EUR 2,424bn **derived** × 1.0824. Point = midpoint. **Estimated.** |
| 2025 | 2511.1 | 2448.3 | 2573.9 | AZ-26 EUR 2,320bn **derived** × 1.0824. Single-source ±2.5%. **Estimated.** Same cross-vintage FX rebasing caveat as the Life 2025 row. Swiss Re's USD-native forecast is non-life USD 4.8trn for 2025, which is not separable into health and P&C. |

### Property & Casualty, Motor / Property / Liability / Specialty and other

Populated for **2024 only**.

Source: SR-b **Figure 16**, "Global non-life premiums market share and volumes in 2024, by lines of business (USD billion)." The figure reports eight blocks summing to 4,604, matching Swiss Re's stated 2024 non-life total of USD 4.6trn, with shares of 48% health, 28% personal lines, 24% commercial lines:

- Health 2,211 (48.0% of 4,604)
- Personal lines: motor 725, property 340, other 225 (sum 1,290 = 28.0%)
- Commercial lines: property 296, liability 253, other 305, motor 249 (sum 1,103 = 24.0%)

CSV rows are **derived** by combining personal and commercial:

- Motor = 725 + 249 = **974.0**
- Property = 340 + 296 = **636.0**
- Liability = **253.0** (commercial only; Swiss Re does not report a personal liability block)
- Specialty and other = 305 + 225 = **530.0**
- These four sum to 2,393, which is the P&C 2024 low bound above.

**Band is ±5%, wider than the ±2.5% default, and here is why.** These values were read off a chart's data labels rather than from a tabulated series, and the assignment of individual labels to individual blocks is partly inferred from reading order. The block totals are firm (the personal-lines pair 340 + 225 = 565 reconciles exactly to 28% less motor, and the commercial four reconcile exactly to 24%), but the personal-versus-commercial attribution of the property and motor components carries some risk. Verify against Swiss Re's sigma explorer before relying on the personal/commercial cut.

2020 to 2023 and 2025 are blank: Swiss Re publishes this line-of-business decomposition only for the current data year in the public report, and no equivalent prior-year split was found in a public source.

### Reinsurance

Source: **ATL** (Atlas Magazine reinsurance statistics, compiled from the published accounts of 143 reinsurers for 2023 and 148 for 2024). This is a company-accounts aggregation, not a regulator series, and the reinsurer sample changes year to year.

| Row | Year | Point | Low | High | Basis |
|---|---|---|---|---|---|
| All reinsurance (total) | 2022 | 364.0 | 364.0 | 400.0 | **Derived** from ATL "2023 GWP of $378.543bn, up 4% on 2022" = 363.98. High = a separate Atlas vintage quoted as $400bn for 2022. The two vintages genuinely disagree; the band spans both. **Estimated.** |
| All reinsurance (total) | 2023 | 378.5 | 369.1 | 388.0 | ATL $378.543bn. Single-source ±2.5%. Actual/reported for the sample. |
| All reinsurance (total) | 2024 | 394.7 | 384.8 | 404.6 | ATL $394.694bn. Single-source ±2.5%. Actual/reported for the sample. |
| Non-life reinsurance | 2022 | 256.7 | 250.3 | 263.1 | ATL $256.7bn. Single-source ±2.5%. |
| Non-life reinsurance | 2023 | 277.0 | 275.0 | 279.0 | Two ATL vintages: $279bn (2023 report, 136 reinsurers, 73.7% of total) and $275bn (2024 report, restated). Point = midpoint. |
| Non-life reinsurance | 2024 | 293.0 | 285.7 | 300.3 | ATL $293bn, 148 companies, 74% of total. Single-source ±2.5%. |
| Life reinsurance | 2023 | 99.5 | 99.5 | 103.5 | **Derived** from ATL "2024 life premiums of $101.5bn, up 2% from the previous year" = 99.5. High = 378.5 total less 275.0 non-life = 103.5, the alternative implied value. **Estimated.** |
| Life reinsurance | 2024 | 101.5 | 99.0 | 104.0 | ATL $101.5bn across 74 life-writing reinsurers. Single-source ±2.5%. |

2020, 2021 and 2025 are blank. For 2021 two Atlas vintages imply materially different levels (roughly $384bn against a level consistent with $364bn for 2022) and the discrepancy could not be resolved to a band worth publishing. 2025 full-year reinsurance aggregates were not published as at the compilation date.

Other reinsurance datapoints found but **not** used, because they measure capital rather than premium: Gallagher Re puts global reinsurance dedicated capital at USD 769bn at full-year 2024, up 5.4%. AM Best's "World's 50 Largest Reinsurers" ranks individual carriers (Swiss Re USD 36.2bn reinsurance revenue in 2024, Munich Re USD 32.6bn, Berkshire Hathaway USD 26.9bn GWP, Lloyd's USD 23.5bn) but does not publish a market total on a single accounting basis; note AM Best's own caveat that IFRS 17 and non-IFRS 17 filers are ranked on different measures and are not directly comparable.

---

## Summary of what is deliberately missing

| Gap | Reason |
|---|---|
| US P&C NPW by line, 2024 and 2025 | Current Triple-I vintage not publicly rendered; underlying detail is subscription-only. Substituting DPW would change the metric mid-series. |
| US cyber DWP, 2025 | NAIC cyber report for data year 2025 not yet published. |
| Global Life savings/risk split, 2021-2023 and 2025 | Swiss Re labels the chart only for 2020, 2024 and 2028F. |
| Global Health, 2020 and 2021 | Allianz introduced health as a separate segment from its 2023 report; no earlier global pool found. |
| Global P&C total, 2020 | Requires a 2020 global health figure to net off Swiss Re non-life; that figure is itself unsourced. |
| Global P&C line split, all years except 2024 | Swiss Re publishes the decomposition only for the current data year. |
| Reinsurance, 2020, 2021 and 2025 | 2021 vintages conflict irreconcilably; 2020 and 2025 not found. |
