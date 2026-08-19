# Industry Data Analysis

<p align="center">
  <img src="media/banner.png" alt="2" width="400">
</p>

<p align="center">
<b>📊〽️ Interactive market segmentation analysis across industries.</b>
</p>

<p align="center">
<p align="center">
  <a href="#industries-covered">Industries</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#credits">Credits</a> •
  <a href="#about-the-core-contributors">About the Core Contributors</a>
</p>

</p>

<p align="center">
  <img alt="Project Version" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FIndustryDataAnalysis%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version&color=blue">
  <img alt="Python Version" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FIndustryDataAnalysis%2Fmain%2Fpyproject.toml&query=%24.project['requires-python']&label=python&logo=python&color=blue">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Miyamura80/IndustryDataAnalysis">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Miyamura80/IndustryDataAnalysis/test_target_tests.yaml?branch=main">

</p>

---

<p align="center">
  <img src="media/industry_data.gif" alt="2" width="600">
</p>


## Industries Covered

Interactive [marimo](https://marimo.io/) notebooks with pie charts and icicle visualizations showing market segments, sizes, and top companies:

| Industry | Notebook | Market Focus |
|----------|----------|--------------|
| Construction | `construction_industry.py` | Residential, infrastructure, non-residential buildings |
| Semiconductor | `semiconductor_industry.py` | Chip design, fabrication, equipment |
| Chemical | `chemical_industry.py` | Specialty chemicals, petrochemicals, materials |
| Cybersecurity | `cyber_industry.py` | Network, endpoint, cloud, identity, GRC |
| Space | `space_industry.py` | Launch, satellites, ground systems |
| Actuators | `actuator_industry.py` | Electric, hydraulic, pneumatic actuators. Appendix: robotics actuator deep dive — precision reducers, servo/drives, integrated joint modules and robot OEMs across Japan/China/Europe-US; sourced market-share table, China RV substitution trend, humanoid BOM split, and a "value accrues in the joint" thesis |
| Robotics | `robotics_industry.py` | Industrial, service, collaborative robots |
| Safety Compliance | `safety_compliance_industry.py` | EHS, process safety, aviation/maritime/railway safety |
| Insurance | `insurance_industry.py` | Life, P&C, health, reinsurance — global premium pools. Appendix: insurance market structure entry — the signal/distribution/risk-transfer layer model, the revenue-multiple gradient, cyber insurance conditions (2024-2026), and who funds cyber insurance (worked case: Evolution Equity Partners) |
| Cyber Insurance | `cyber_insurance_industry.py` | Carriers, MGAs, reinsurers, strategy archetypes, threat-to-claim flows |
| Japan Insurance | `japan_insurance_industry.py` | Japanese market structure: Big Three P&C (Tokio Marine, MS&AD, Sompo), internationalization trend (FY2014-FY2026), domestic line-of-business mix, Big Three cyber books, and a life/non-life/third-sector company treemap |
| Japan Economy | `japan_economy.py` | GDP-equivalent sector mix and representative listed leaders |
| Ocean / Blue Economy | `ocean_industry.py` | Shipping, offshore energy, fisheries, tourism, shipbuilding, naval defense, subsea infrastructure. Appendix: shipping decarbonization deep dive |
| Lloyd's Syndicate-in-a-Box | `lloyds_siab.py` | All 14 SiaBs approved (2020-2026): sectors, stamp capacity, outcomes, Carbon 4747 growth, managing agent concentration, new entrant comparison |
| Human Sensory Bandwidth | `sensory_bandwidth.py` | Raw sensory input vs. conscious experience: bandwidth funnel, the missing senses, interactive effective-bandwidth toy model, scenario presets, output channels, five definitions of "human bandwidth" |

## Requirements

- [uv](https://docs.astral.sh/uv/)
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Quick Start

Run any industry notebook:
```bash
uv run marimo run notebooks/<industry>_industry.py
```

Other commands:
- `make all` - runs `main.py`
- `make fmt` - format code with Black
- `make test` - run all tests

## Credits

This software uses the following tools:
- [marimo](https://marimo.io/) - Reactive Python notebooks
- [Plotly](https://plotly.com/) - Interactive visualizations
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager

## About the Core Contributors

<a href="https://github.com/Miyamura80/IndustryDataAnalysis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Miyamura80/IndustryDataAnalysis" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
