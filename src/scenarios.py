import pandas as pd
import numpy as np

def run_intervention_scenario(baseline_future: pd.DataFrame,model_bundle: dict,rates: dict) -> pd.DataFrame:
    """
    Applies sustained annual percentage changes to baseline future factors
    and predicts resulting yield.
    """

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

def run_best_case_1pct_scenario(
    baseline_future: pd.DataFrame,
    model_bundle: dict
) -> pd.DataFrame:
    """
    Best-case coordinated improvement scenario:
    +1% rainfall
    -1% temperature
    +1% soil
    +1% irrigation
    +0% fertilizer
    """

    rates = {
        "rainfall": 0.01,
        "temperature": -0.01,
        "soil": 0.01,
        "irrigation": 0.01,
        "fertilizer": 0.00,
    }

    return run_intervention_scenario(baseline_future, model_bundle, rates)
