# AgriTrend_simulation

### Crop Yield Trend Analysis & Scenario Simulation Framework

AgriTrend_simulation is a research-oriented simulation project designed to study
long-term crop yield behavior under environmental and management stress.

The project emphasizes:
- explainability
- trend analysis
- scenario-based reasoning
- automated report generation

The system processes data through a **complete analysis pipeline** and
automatically generates **visualizations** and a **structured PDF report**
summarizing trends, factor influence, and future scenarios.

This prototype was developed for **Hack The Winter : Round 1**, with the goal of
demonstrating clear system thinking, modular design, and research-oriented analysis.

---

## Problem Statement

Modern agriculture is under increasing pressure from climate change, soil degradation, and growing input dependency.

In many cases:
- Irrigation and fertilizer usage increase every year,
- Crop yield does not improve at the same rate,
- Yield becomes more unstable over time.

Most existing solutions either focus on short term prediction or rely on API, black-box models that are difficult to explain.

There is a need for a transparent system that answers a simpler but more important question:

**If current trends continue, what happens to crop yield in the long run and what changes actually matter?**

---
## Theme 
- ### AI/ML

## Solution Overview

AgriTrend_simulation addresses this problem by providing a structured and explainable simulation pipeline that :
1. Generates realistic synthetic agricultural data,
2. Analyzes long term relationships between factors and yield,
3. Identifies which factors matter most,
4. Projects a baseline future assuming no intervention,
5. Compares it against controlled improvement scenarios.

**The system does not aim to predict exact future yields. Instead, it highlights long term patterns, risks, and trade offs.**

---

## Prototype Scope (Round 1)

This repository contains a **proof of concept prototype** with the following scope :

### Data Assumptions
- One synthetic region
- One synthetic crop
- Year wise tabular data (CSV) (_~25 years_)
- Statistically realistic trends and variability

### Modeling Approach
- Linear regression (raw + standardized)
- Focus on interpretability over complexity
- No black-box or deep learning models


### Result of Simulation
- Historical yield shows increasing instability over time
- Input intensification does not guarantee yield growth
- Standardized analysis highlights dominant yield drivers
- Baseline future shows gradual decline and higher risk
- Coordinated 1% improvements significantly stabilize outcomes

> These results are exploratory and meant to highlight system behavior,
not to provide exact predictions.


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


---

<details>
<summary><b>Project structure</b></summary>

- Must go through the [**RepoWorking**](RepoWorking.md) file to know the structure used.
- Each folder includes its own `README.md` for clarity.
</details>

<details>
<summary><b>Documentation Notebook (Recommended)</b></summary>
<br>

Notebook : [**Documentation Notebook**](/notebooks/documentation_code.ipynb)

The Jupyter notebook below explains the full pipeline step by step :
- data generation logic
- analysis reasoning
- model behavior
- scenario design
- interpretation of results

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

- macOS / Linux 
```bash
python -m venv venv
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

> These limitations are intentional for a clean and explainable prototype.

## Future Work (Round 2 Plan)
Planned extensions include:
- GUI interface (local web app or Flutter-based app)
- Multiple selectable crops and regions (_synthetic_)
- Improved data handling and validation
- Integration of real-world datasets (_if possible_)
- Interactive scenario experimentation

## Team
>This project was developed by a 4-member team **The Eskimos!** as part of Hack The Winter:
- Abhinav
- Anubhav
- Hariom Chamoli
- Abhinav Benjwal

Roles and responsibilities will be formalized in the system design round.

## License

This project is intended for academic, educational, and research demonstration purposes.
