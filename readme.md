# AgriTrend  
### Crop Yield Trend Analysis & Forecasting System (Prototype)

AgriTrend is a data-driven research prototype designed to analyze how long-term environmental and land-use changes affect crop yield in a specific region, and to forecast future yield trends using simple, explainable statistical models.

This project is built as part of **Hack The Winter** hackathon and focuses on concept validation, system thinking, and research-oriented analysis rather than UI polish.

---

## Problem Statement

Rapid urbanization, climate change, and declining agricultural land are negatively impacting crop production.  
At the same time, population continues to grow, increasing pressure on food systems.

Currently, most agricultural decisions are made using short-term or static data, without sufficient visibility into long-term trends. Researchers and policymakers lack simple tools that combine historical data with predictive insights to understand **where crop yield is heading if current trends continue**.

---

## Solution Overview

AgriTrend addresses this gap by providing:

- Historical trend analysis of crop yield and influencing factors  
- Visual representations of environmental and land-use changes  
- Simple, explainable prediction of future crop yield trends  

The system is designed as a **research and decision-support tool**, not a farmer-facing application.

---

## Prototype Scope (Round 1)

This repository contains a **proof-of-concept prototype** with the following scope:

- **One region**
- **One crop**
- **Year-wise tabular data (CSV format)**
- Limited historical data (5–15 years)
- Simple statistical prediction model (linear regression)

### What the prototype does:
- Loads historical agricultural and environmental data
- Cleans and preprocesses the data
- Visualizes trends using graphs
- Predicts future crop yield based on past trends

### What the prototype does NOT do:
- Multi-region or multi-crop analysis
- GIS or shapefile processing
- Complex machine learning or deep learning
- Production deployment

These are planned for future stages.

---

## Tech Stack

**Backend / Analysis**
- Python
- pandas – data handling
- numpy – numerical computation
- matplotlib – data visualization
- scikit-learn – simple predictive modeling

**Frontend (Optional / Minimal)**
- Flutter (for displaying results only)

---

## Current Results

- Time-series graphs showing trends in:
  - Crop yield
  - Rainfall
  - Temperature
  - Cultivated land area
- A basic forecast indicating future yield direction if current trends continue

(Sample outputs are included in the `outputs/graphs` directory.)

---

## Limitations

- Prototype uses limited and possibly coarse data
- Prediction model is intentionally simple
- Results depend heavily on data quality and availability
- Only one crop and region are analyzed

These limitations are acknowledged and addressed in future plans.

---

## Future Work (Round 2 & Beyond)

- Support for multiple crops and regions
- GIS and shapefile (.shp) data integration
- More robust prediction models
- Policy-level dashboards and reports
- API-based data ingestion
- Improved visualization and interactivity

---

## Team

This project is developed as part of a 4-member team.  
Roles will be expanded and formalized in the system design round.

---

## License

This project is for academic and research demonstration purposes.
