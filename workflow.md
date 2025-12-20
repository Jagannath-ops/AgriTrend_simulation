# AgriTrend – Prototype Development Plan

This document outlines the development plan for the AgriTrend prototype, including data requirements, file responsibilities, and execution strategy for Round 1 of the hackathon.

---

## Objective of the Prototype

The goal of the prototype is to **validate the feasibility** of analyzing historical agricultural trends and predicting future crop yield using simple, explainable statistical methods.

The prototype focuses on:
- Concept clarity
- Data flow
- System structure
- Research-oriented reasoning

---

## Data Requirements (Prototype)

For the prototype, **tabular data (CSV/Excel)** is required.  
Maps and GIS data are explicitly excluded at this stage.

### Required Data (Year-wise)

#### 1. Crop Yield Data (Mandatory)
- Year
- Crop name
- Region
- Yield (kg/hectare or total production)

Example:
| year | crop | region | yield_kg_per_hectare |

---

#### 2. Rainfall Data (Mandatory)
- Year
- Region
- Average rainfall (mm)

---

#### 3. Temperature Data (Mandatory)
- Year
- Region
- Average temperature (°C)

---

#### 4. Cultivated Land Area (Highly Recommended)
- Year
- Region
- Area under cultivation (hectares)

---

#### 5. Farmer Count / Rural Population (Optional)
- Year
- Region
- Number of farmers or rural population

---

## Data Assumptions

- Data may be incomplete or approximate
- Missing values will be handled during preprocessing
- All datasets will be aligned by year
- Clear assumptions will be documented in the README

---

## File Responsibilities

### `data/raw/`
- Stores raw CSV datasets
- Prototype may use sample or dummy data initially

---

### `data_loader.py`
- Loads CSV files into pandas DataFrames
- Handles file paths and basic validation

---

### `preprocess.py`
- Cleans missing or inconsistent values
- Normalizes numerical data
- Sorts data by year
- Prepares final dataset for analysis

---

### `visualization.py`
- Generates time-series plots:
  - Yield vs Year
  - Rainfall vs Year
  - Temperature vs Year
  - Cultivated Area vs Year
- Saves plots to `outputs/graphs`

---

### `model.py`
- Implements a simple predictive model
- Uses linear regression or trend extrapolation
- Predicts future crop yield based on historical data

---

### `main.py`
Acts as the entry point:
1. Load data
2. Preprocess data
3. Generate visualizations
4. Run prediction model
5. Save outputs and insights

---

## Libraries Used

- pandas
- numpy
- matplotlib
- scikit-learn 

The focus is on **interpretability**, not complex AI.

---

## Execution Timeline

- **Day 1–2:** Repository setup, dummy data, basic plots
- **Day 3:** Prediction model and outputs
- **Day 4:** Diagrams and README improvements
- **Day 5:** Data replacement (if available) and polishing
- **Day 6:** Final review and submission

---

## Future Expansion Plan (Round 2)

- Modular data ingestion for multiple regions
- GIS (.shp) file support
- Improved statistical and ML models
- API layer for frontend integration
- Scalable system architecture

---

## Notes

This prototype prioritizes **clarity, honesty, and feasibility**.  
Complexity is intentionally limited to ensure correctness and explainability.
