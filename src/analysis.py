import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# headings are taken from : documentation_code.ipynb so that u can match and understand from teh notebook


######################################################################## 4.a Raw Regression 

def run_regression_analysis(df: pd.DataFrame) -> dict:
    """
    Analyzes which factors affect crop yield using linear regression.
    Takes a DataFrame with climate, soil, irrigation, fertilizer, and year data.
    Runs two models: one on raw values and one on standardized values.
    Raw model shows real-world impact per unit change.
    Standardized model shows relative importance of each factor.
    Calculates percentage contribution of each factor to yield.
    Returns models, coefficients tables, and the scaler in a dictionary.
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

######################################################################## 4.b Standardized Regression 

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    std_model = LinearRegression()
    std_model.fit(X_scaled, y)

    std_coeffs = pd.DataFrame({
        "Factor": X.columns,
        "Standardized_Impact": std_model.coef_
    })

######################################################################## 4.c Summary of Regression 

    std_coeffs["Absolute_Impact"] = std_coeffs["Standardized_Impact"].abs()

    std_coeffs["Relative_Contribution (%)"] = (
        std_coeffs["Absolute_Impact"]
        / std_coeffs["Absolute_Impact"].sum()
        * 100
    )

######################################################################## return statement

    return {
        "raw_model": raw_model,
        "raw_coeffs": raw_coeffs,
        "std_model": std_model,
        "std_coeffs": std_coeffs,
        "scaler": scaler,
    }