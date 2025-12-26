import pandas as pd
import numpy as np

# headings are taken from : documentation_code.ipynb so that u can match and understand from teh notebook


######################################################################## 5.b Scenario Interventions

def run_intervention_scenario(baseline_future: pd.DataFrame, model_bundle: dict, rates: dict) -> pd.DataFrame:
    """
    Applies yearly percentage changes to future baseline factors.
    Takes baseline future data and modifies it using given rates.
    Changes are applied every year and compound over time.
    Rates can increase or decrease rainfall, temperature, soil, irrigation, and fertilizer.
    All values are kept within realistic physical limits.
    Uses the trained model to predict yield after intervention.
    Returns a DataFrame with updated factors and scenario yield.
    """

######################################################################## 5.b.1 Calculation Future when an given Factor Changes at a specific rate

    scenario = baseline_future.copy()

    t = scenario["year"] - scenario["year"].iloc[0]

    # Apply compounding interventions
    scenario["rainfall_mm"] *= (1 + rates.get("rainfall", 0.0)) ** t
    scenario["temperature_c"] *= (1 + rates.get("temperature", 0.0)) ** t
    scenario["soil_index"] *= (1 - rates.get("soil", 0.0)) ** t
    scenario["irrigation_pct"] *= (1 + rates.get("irrigation", 0.0)) ** t
    scenario["fertilizer_kg_ha"] *= (1 + rates.get("fertilizer", 0.0)) ** t

    # Physical bounds
    scenario["soil_index"] = scenario["soil_index"].clip(0.5, 0.85)
    scenario["irrigation_pct"] = scenario["irrigation_pct"].clip(30, 70)
    scenario["fertilizer_kg_ha"] = scenario["fertilizer_kg_ha"].clip(50, 200)

    # Predict yield
    X = scenario[model_bundle["features"]]
    X_scaled = model_bundle["scaler"].transform(X)

    scenario["scenario_yield_kg_ha"] = model_bundle["model"].predict(X_scaled)

    return scenario

######################################################################## 1% scenario (given in the notebook image)

def run_best_case_1pct_scenario(baseline_future: pd.DataFrame,model_bundle: dict) -> pd.DataFrame:
    """
    Runs an ideal improvement scenario with small yearly changes.
    Rainfall, soil, and irrigation improve by 1% per year.
    Temperature reduces by 1% per year.
    Fertilizer use is kept the same.
    This shows how small, coordinated improvements affect yield.
    Returns a DataFrame with predicted best-case yield.
    """

    rates = {
        "rainfall": 0.01,
        "temperature": -0.01,
        "soil": 0.01,
        "irrigation": 0.01,
        "fertilizer": 0.00,
    }

    return run_intervention_scenario(baseline_future, model_bundle, rates)
