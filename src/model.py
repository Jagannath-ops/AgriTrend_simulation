import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


def train_yield_model(df: pd.DataFrame) -> dict:
    """
    Trains a standardized linear regression model on historical data.
    Returns model + scaler.
    """
    X = df[
        [
            "rainfall_mm",
            "temperature_c",
            "soil_index",
            "irrigation_pct",
            "fertilizer_kg_ha",
            "year",
        ]
    ]
    y = df["yield_kg_ha"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    return {
        "model": model,
        "scaler": scaler,
        "features": X.columns.tolist(),
    }


def predict_baseline_future(df: pd.DataFrame,model_bundle: dict,years_ahead: int = 10) -> pd.DataFrame:
    """
    Predicts baseline future yield assuming historical trends continue.
    """

    years = df["year"].values
    future_years = np.arange(years[-1] + 1, years[-1] + years_ahead + 1)

    n_future = len(future_years)

    # rainfall
    baseline_rainfall = 800
    rainfall_trend = -3
    baseline_rainfall_future = (
        baseline_rainfall
        + rainfall_trend * (future_years - years[0])
        + np.random.normal(0, 60, n_future)
    )
    baseline_rainfall_future = np.clip(baseline_rainfall_future, 300, None)

    # temperature
    baseline_temperature = 25.0
    temperature_trend = 0.03
    baseline_temperature_future = (
        baseline_temperature
        + temperature_trend * (future_years - years[0])
        + np.random.normal(0, 0.4, n_future)
    )

    # soil
    soil_index_last = df["soil_index"].iloc[-1]
    natural_degradation = 0.003
    soil_noise = 0.005

    baseline_soil_future = np.zeros(n_future)
    baseline_soil_future[0] = soil_index_last

    for i in range(1, n_future):
        baseline_soil_future[i] = (
            baseline_soil_future[i - 1]
            - natural_degradation
            + np.random.normal(0, soil_noise)
        )

    baseline_soil_future = np.clip(baseline_soil_future, 0.5, 0.85)


    base_irrigation = 30.0
    irrigation_trend = 1.0
    mean_rainfall = df["rainfall_mm"].mean()
    rainfall_sensitivity = -0.03

    baseline_irrigation_future = (
        base_irrigation
        + irrigation_trend * (future_years - years[0])
        + rainfall_sensitivity * (baseline_rainfall_future - mean_rainfall)
        + np.random.normal(0, 2.0, n_future)
    )
    baseline_irrigation_future = np.clip(baseline_irrigation_future, 30, 70)

    base_fertilizer = 80.0
    irrigation_effect = 0.8
    soil_compensation = -60.0
    fertilizer_trend = 1.2

    baseline_fertilizer_future = (
        base_fertilizer
        + irrigation_effect * baseline_irrigation_future
        + soil_compensation * (baseline_soil_future - 0.7)
        + fertilizer_trend * (future_years - years[0])
        + np.random.normal(0, 10.0, n_future)
    )
    baseline_fertilizer_future = np.clip(baseline_fertilizer_future, 50, 200)

    future_df = pd.DataFrame({
        "year": future_years,
        "rainfall_mm": baseline_rainfall_future,
        "temperature_c": baseline_temperature_future,
        "soil_index": baseline_soil_future,
        "irrigation_pct": baseline_irrigation_future,
        "fertilizer_kg_ha": baseline_fertilizer_future,
    })

    X_future = future_df[
        model_bundle["features"]
    ]

    X_future_scaled = model_bundle["scaler"].transform(X_future)

    future_df["baseline_yield_kg_ha"] = model_bundle["model"].predict(X_future_scaled)

    return future_df

