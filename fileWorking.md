## Objective of the Prototype

The objective of this prototype is to design and demonstrate a structured, explainable framework for analyzing agricultural yield trends and exploring future outcomes using statistically grounded, transparent methods.

The prototype is intended to:
- Model the relationships between environmental, soil, and management factors and crop yield
- Demonstrate a clear end-to-end data pipeline, from data generation to analysis and visualization
- Enable scenario-based exploration of future yield outcomes under controlled assumptions
- Serve as a foundation for integrating real-world datasets in later development stages
- This prototype prioritizes interpretability, methodological clarity, and system design over predictive complexity.

---

## Data Requirements (Round 1)

For the prototype, **tabular data (CSV/Excel)** is required.

| year | rainfall_mm | temperature_c | soil_index | irrigation_pct | fertilizer_kg_ha | pest_pressure_index |
yield_kg_ha |

## File Responsibilities

#### [Folder 1 : data](./data)
  - Stores datasets in given data parameters.


#### [Folder 2 : data_generation](./data_generation)
  - Generates synthetic data within constraints to simulate real life conditions.


#### [Folder 3 : notebooks](./notebooks)
  - Contains **jupyter** notebook that has deep explanation with code side by side _(must view to understand the work behind the scene)_


#### [Folder 4 : outputs](./outputs)
  - Stores the graphs from the code
  - Stores the generated reports from the code


#### [Folder 5 : src](./src)

- ##### [File 1 : data_loader](./src/data_loader.py)
  - Loads CSV files into pandas DataFrames
  - Handles file paths and basic validation

- ##### [File 2 : data_input](./src/data_loader.py)
  - Takes the data from the user for real prediction

- ##### [File 2 : model.py](./src/model.py)
  - Learns the historical data
  - Predicts the future data according to trends 

- ##### [File 3 : visualization.py](./src/visualization.py)
  - Generates plots from the existing data
  - Saves plots to [output/graphs](./outputs/graphs)
  - Saves plots to [output/reports](./outputs/reports)

#### [File 1 : AgriTrend_simulation.py](/AgirTrend_simulation.py)
  - The main file that is used to execute the whole program 

#### [File 2 : fileWorking.py](/fileWorking.md)
  - this file itself

#### [File 3 : requirements](/requirements.txt)
  - Lists of the required libraries for the smooth execution of the file

---

## Notes

This prototype prioritizes **clarity, honesty, and feasibility**.  
Complexity is intentionally limited to ensure correctness and explainability.
