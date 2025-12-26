## Objective of the Prototype

The objective of this prototype is to design and demonstrate a clear, explainable framework for analyzing long-term agricultural yield trends and exploring future outcomes under controlled assumptions.

Rather than focusing on short-term prediction accuracy, the system prioritizes transparency, interpretability, and system-level understanding.

The prototype is intended to :

- Model relationships between environmental, soil, and management factors and crop yield  
- Demonstrate a complete end to end data pipeline, from data generation to analysis and visualization  
- Enable scenario-based exploration of future yield outcomes  
- Highlight long-term trends, risks, and trade-offs in agricultural systems  
- Serve as a foundation for integrating real-world datasets in later stages  

This prototype intentionally prioritizes methodological clarity and system
design over predictive complexity.

---

## Data Requirements (Round 1)

For this prototype, the system operates on **tabular agricultural data** stored in CSV or Excel format.

- Required Data Format

| year | rainfall_mm | temperature_c | soil_index | irrigation_pct | fertilizer_kg_ha | pest_pressure_index | yield_kg_ha |
|------|-------------|---------------|------------|----------------|------------------|---------------------|-------------|
| x    | x           | x             | x          | x              | x                | x                   | x           |

> Synthetic data following this structure is used in Round 1.

---
## Repository Structure and Responsibilities

- ### [data/](/data)
  Stores all datasets used by the system.

    - `syntheticData/` — synthetic datasets used in the current prototype  
    - `realData/` — reserved for future real-world datasets  

  Each subfolder contains its own README describing usage and format.

---

- ### [notebooks/](/notebooks)
  Contains Jupyter notebooks used for explanation and documentation.

    - `documentation_code.ipynb` — **recommended** notebook that explains the full pipeline with code, outputs, and reasoning.
    - `sample_notebook/` — simplified example notebooks using pseudo data  

  These notebooks are not required to run the program, but they provide the clearest view of how and why the system works.

---

- ### [outputs/](/outputs)
  Stores all generated outputs from the simulation.

    - `graphs/` — plots created during analysis and scenario comparison  
    - `reports/` — automatically generated PDF reports  

  All files in this folder are generated programmatically and can be deleted and recreated by re-running the main script.

---

- ### [src/](/src)
  Contains all core source code, organized in a modular way.

    - `data_generation.py` — generates synthetic agricultural data  
    - `data_loader.py` — loads and saves datasets  
    - `analysis.py` — regression and factor contribution analysis  
    - `model.py` — model training and baseline future projection  
    - `scenarios.py` — intervention and improvement scenarios  
    - `visualization.py` — graph generation and saving  
    - `report_builder.py` — automatic PDF report generation  
    - `paths.py` — centralized path management  

---

- ### [AgriTrend_simulation.py](/AgriTrend_simulation.py)
  > The main execution file.

  Running this file executes the full pipeline:
  - `data generation → analysis → visualization → scenario simulation → report generation.`

---

### [requirements.txt](/requirements.txt)
  Lists all Python dependencies required to run the project.


## Note

- The project does not aim to predict real-world yields or provide decision-making tools.
- Its purpose is to explore long term behavior, identify dominant drivers, and demonstrate how coordinated changes can alter system trajectories.

> The design choices made in Round 1 focus on **clarity, honesty, and feasibility**.