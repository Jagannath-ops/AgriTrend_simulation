# AgriTrend_simulation

### Crop Yield Trend Analysis & Scenario Simulation Framework

AgriTrend_simulation is a research-oriented simulation project designed to study long term crop yield behavior under environmental and management stress.

Instead of focusing on short-term prediction accuracy, the project emphasizes:
- explainability
- trend analysis
- system-level understanding
- scenario-based reasoning

This prototype was developed for **Hack The Winter : Round 1**, with the goal of demonstrating clear system thinking and modular design.

---

## Problem Statement

Modern agriculture is under increasing pressure from climate change, soil
degradation, and growing input dependency.

In many cases:
- irrigation and fertilizer usage increase every year
- crop yield does not improve at the same rate
- yield becomes more unstable over time

Most existing solutions either focus on short term prediction or rely on API, black-box models that are difficult to interpret.

There is a need for a transparent system that answers a simpler but more important question:

**If current trends continue, what happens to crop yield in the long run and what changes actually matter?**

---

## Solution Overview

AgriTrend_simulation addresses this problem by providing a structured and explainable simulation pipeline that:
- generates realistic synthetic agricultural data
- analyzes long-term relationships between factors and yield
- identifies which factors matter most
- projects a baseline future assuming no intervention
- compares it against controlled improvement scenarios

**The system does not aim to predict exact future yields. Instead, it highlights long-term patterns, risks, and trade-offs.**

---

## Prototype Scope (Round 1)

This repository contains a **proof of concept prototype** with the following scope:

### Data Assumptions
- One synthetic region
- One synthetic crop
- Year wise tabular data (CSV)
- ~25 years of historical data
- Statistically realistic trends and variability

### Modeling Approach
- Linear regression (raw + standardized)
- Focus on interpretability over complexity
- No black-box or deep learning models


<details>
<summary><b>What the prototype does / does not do</b></summary>

- What the prototype DOES
  - Generates realistic synthetic agricultural data  
  - Analyzes historical yield trends  
  - Quantifies relative impact of key factors  
  - Projects a baseline future scenario  
  - Simulates a best-case improvement scenario (+1% coordinated changes)  
  - Produces clear graphs and a final PDF report automatically  

- What the prototype DOES NOT do
  - Predict real-world yields  
  - Model multiple crops or regions (yet)  
  - Use real datasets (planned for Round 2)  
  - Provide a GUI or web interface (planned for Round 2)
</details>


<details>
<summary><b>Project structure (high level)</b></summary>

- `src/` — core simulation and analysis code  
- `data/` — synthetic and future real datasets  
- `notebooks/` — explanation and documentation notebooks  
- `outputs/graphs/` — generated visualizations  
- `outputs/reports/` — final PDF report  
- `AgriTrend_simulation.py` — main execution file  

Each folder includes its own `README.md` for clarity.

<br></br>
</details>


### Result of Simulation
- Historical yield shows increasing instability over time
- Input intensification does not guarantee yield growth
- Standardized analysis highlights dominant yield drivers
- Baseline future shows gradual decline and higher risk
- Coordinated 1% improvements significantly stabilize outcomes

> These results are exploratory and meant to highlight system behavior,
not to provide exact predictions.

---

<details>
<summary><b>Documentation Notebook (Recommended)</b></summary>

The Jupyter notebook below explains the full pipeline step by step:
- data generation logic
- analysis reasoning
- model behavior
- scenario design
- interpretation of results

Notebook : [**Documentation Notebook**](/notebooks/documentation_code.ipynb)

Strongly recommended if you want to understand the project
> This notebook is not required to run the project, but it provides the best context for understanding the design decisions.
</details>

---

## How To Use

### 1. Check Python version (3.9 or above)
```bash
python --version
```

### 2. Clone the repository
```bash
git clone https://github.com/Abhinav08bhatt/AgriTrend_simulation.git
```
```bash
cd AgriTrend_simulation
```

### 3. Create a virtual environment (recommended)

- Windows
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

- macOS / Linux / Arch
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

### 4. Install requirements
```bash
pip install -r requirements.txt
```

### 5. Run the simulation
```bash
python AgriTrend_simulation.py
```

### 6. View the final report
> The simulation automatically generates a PDF report.
- Location: `outputs/reports/universal_data.pdf`
```bash
open outputs/reports/universal_data.pdf
```

## Limitations
- Uses synthetic data, not real field observations
- Linear modeling only
- No regional or crop diversity
- No economic or policy constraints
- Focused on trends rather than accuracy

> These limitations are intentional for a clean and explainable prototype.

## Future Work (Round 2 Plan)
Planned extensions include:
- GUI interface (local web app or Flutter-based app)
- Multiple selectable crops and regions
- Expanded synthetic datasets
- Improved data handling and validation
- Integration of real-world datasets
- Interactive scenario exploration

## Team
>This project was developed by a 4-member team **The Eskimos!** as part of Hack The Winter:
- Abhinav
- Anubhav
- Hariom Chamoli
- 

Roles and responsibilities will be formalized in the system design round.

## License

This project is intended for academic, educational, and research demonstration purposes.