import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path

from src.paths import GRAPHS_DIR


def plot_yield_trend(df: pd.DataFrame) -> Path:
    years = df["year"]
    yield_kg_ha = df["yield_kg_ha"]

    plt.figure(figsize=(15, 5))
    plt.plot(years, yield_kg_ha, marker="o", color="green")
    plt.xlabel("Year")
    plt.ylabel("Yield (kg/ha)")
    plt.title("Synthetic Crop Yield Over Time")
    plt.grid(True)

    output_path = GRAPHS_DIR / "yield_trend.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path


def plot_standardized_trends(df: pd.DataFrame) -> Path:
    trend_vars = [
        "rainfall_mm",
        "temperature_c",
        "soil_index",
        "irrigation_pct",
        "fertilizer_kg_ha",
        "yield_kg_ha",
    ]

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df[trend_vars])

    scaled_df = pd.DataFrame(
        scaled_values,
        columns=trend_vars
    )
    scaled_df["year"] = df["year"]

    plt.figure(figsize=(15, 5))
    plt.plot(scaled_df["year"], scaled_df["rainfall_mm"], label="Rainfall")
    plt.plot(scaled_df["year"], scaled_df["temperature_c"], label="Temperature")
    plt.plot(scaled_df["year"], scaled_df["soil_index"], label="Soil Index")
    plt.plot(scaled_df["year"], scaled_df["irrigation_pct"], label="Irrigation")
    plt.plot(scaled_df["year"], scaled_df["fertilizer_kg_ha"], label="Fertilizer")
    plt.plot(scaled_df["year"], scaled_df["yield_kg_ha"], label="Yield", linewidth=3)

    plt.axhline(0, linestyle="--", color="gray")
    plt.xlabel("Year")
    plt.ylabel("Standardized Value (Z-score)")
    plt.title("Relative Trends of Agricultural Factors and Yield")
    plt.legend()
    plt.grid(True)

    output_path = GRAPHS_DIR / "standardized_trends.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path


def plot_baseline_vs_scenario(
    historical_df: pd.DataFrame,
    baseline_future: pd.DataFrame,
    scenario_future: pd.DataFrame
) -> Path:
    years_hist = historical_df["year"]
    yield_hist = historical_df["yield_kg_ha"]

    years_future = baseline_future["year"]
    yield_baseline = baseline_future["baseline_yield_kg_ha"]
    yield_scenario = scenario_future["scenario_yield_kg_ha"]

    plt.figure(figsize=(15, 5))

    # Historical
    plt.plot(
        years_hist,
        yield_hist,
        label="Historical Yield",
        linewidth=2,
        color="green"
    )

    # Baseline future
    plt.plot(
        years_future,
        yield_baseline,
        linestyle="--",
        linewidth=3,
        label="Baseline Future (No Intervention)",
        color="lightgreen"
    )

    # Scenario future
    plt.plot(
        years_future,
        yield_scenario,
        linestyle=":",
        linewidth=3,
        label="Best-Case Scenario (+1% coordinated improvement)",
        color="blue"
    )

    # Present divider
    plt.axvline(
        years_hist.iloc[-1],
        linestyle=":",
        color="gray",
        label="Present"
    )

    plt.xlabel("Year")
    plt.ylabel("Crop Yield (kg/ha)")
    plt.title("Future Yield Trajectories: Baseline vs Best-Case Scenario")
    plt.legend()
    plt.grid(True)

    output_path = GRAPHS_DIR / "baseline_vs_best_case.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path
