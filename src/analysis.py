import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


def run_regression_analysis(df: pd.DataFrame) -> dict:
    """
    Runs raw and standardized regression analysis on yield drivers.
    Returns a dictionary of results.
    """

    X = df[[
            "rainfall_mm",
            "temperature_c",
            "soil_index",
            "irrigation_pct",
            "fertilizer_kg_ha",
            "year"
        ]]
    y = df["yield_kg_ha"]

    raw_model = LinearRegression()
    raw_model.fit(X, y)

    raw_coeffs = pd.DataFrame({
        "Factor": X.columns,
        "Impact_on_Yield_kg_per_unit": raw_model.coef_
    })

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    std_model = LinearRegression()
    std_model.fit(X_scaled, y)

    std_coeffs = pd.DataFrame({
        "Factor": X.columns,
        "Standardized_Impact": std_model.coef_
    })

    std_coeffs["Absolute_Impact"] = std_coeffs["Standardized_Impact"].abs()

    std_coeffs["Relative_Contribution (%)"] = (
        std_coeffs["Absolute_Impact"]
        / std_coeffs["Absolute_Impact"].sum()
        * 100
    )


    return {
        "raw_model": raw_model,
        "raw_coeffs": raw_coeffs,
        "std_model": std_model,
        "std_coeffs": std_coeffs,
        "scaler": scaler,
    }

