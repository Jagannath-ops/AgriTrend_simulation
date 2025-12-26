import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path
from src.paths import GRAPHS_DIR


######################################################################## 1.a - 1.f

def plot_factor_timeseries(df: pd.DataFrame) -> list[Path]:
    """
    Saves small time-series plots for each major factor.
    Returns list of image paths.
    """

    factors = [
        {
            "column": "rainfall_mm",
            "label": "Rainfall (mm)",
            "color": "blue",
        },
        {
            "column": "temperature_c",
            "label": "Temperature (°C)",
            "color": "orange",
        },
        {
            "column": "soil_index",
            "label": "Soil Quality Index",
            "color": "brown",
        },
        {
            "column": "irrigation_pct",
            "label": "Irrigation Coverage (%)",
            "color": None,
        },
        {
            "column": "fertilizer_kg_ha",
            "label": "Fertilizer (kg/ha)",
            "color": "purple",
        },
        {
            "column": "pest_pressure_index",
            "label": "Pest Pressure Index",
            "color": "red",
        },
    ]

    image_paths = []

    for factor in factors:
        plt.figure(figsize=(4, 2))

        if factor["color"] is not None:
            plt.plot(
                df["year"],
                df[factor["column"]],
                linewidth=1.5,
                color=factor["color"],
            )
        else:
            plt.plot(
                df["year"],
                df[factor["column"]],
                linewidth=1.5,
            )

        plt.title(factor["label"], fontsize=9)
        plt.xlabel("Year", fontsize=8)
        plt.ylabel(factor["label"], fontsize=8)
        plt.grid(True, alpha=0.4)

        output_path = GRAPHS_DIR / f"factor_{factor['column']}.png"
        plt.savefig(output_path, dpi=200, bbox_inches="tight")
        plt.close()

        image_paths.append(output_path)

    return image_paths


######################################################################## 1.g

def plot_yield_trend(df: pd.DataFrame) -> Path:
    years = df["year"]
    yield_kg_ha = df["yield_kg_ha"]

    plt.figure(figsize=(15, 5))

    plt.xticks(range(2000, 2025), rotation=30)
    plt.xlim(1999, 2025)
    plt.grid(True)

    plt.plot(years, yield_kg_ha, marker="o", color="green")
    plt.xlabel("Year")
    plt.ylabel("Yield (kg/ha)")
    plt.title("Synthetic Crop Yield (All Factors Combined)")

    output_path = GRAPHS_DIR / "yield_trend.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path

######################################################################## 3.b

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

    plt.xticks(range(2000, 2030), rotation=30)
    plt.xlim(1999, 2030)
    plt.grid(True)

    plt.plot(
        scaled_df["year"],
        scaled_df["rainfall_mm"],
        label="rainfall",
        linestyle="--",
        color="blue",
    )
    plt.plot(
        scaled_df["year"],
        scaled_df["temperature_c"],
        label="temperature",
        linestyle="--",
        color="orange",
    )
    plt.plot(
        scaled_df["year"],
        scaled_df["soil_index"],
        label="soil index",
        linestyle="--",
        color="brown",
    )
    plt.plot(
        scaled_df["year"],
        scaled_df["irrigation_pct"],
        label="irrigation",
        linestyle="--",
        color="lightblue",
    )
    plt.plot(
        scaled_df["year"],
        scaled_df["fertilizer_kg_ha"],
        label="fertilizer",
        linestyle="--",
        color="purple",
    )
    plt.plot(
        scaled_df["year"],
        scaled_df["yield_kg_ha"],
        label="yield",
        color="green",
        linewidth=2,
    )

    plt.axhline(
        0,
        linestyle="--",
        color="gray",
        linewidth=1,
        label="Historical Average",
    )

    plt.xlabel("Year")
    plt.ylabel("Standardized Value (Z-score)")
    plt.title("Relative Trends of Agricultural Factors and Yield")
    plt.legend()

    output_path = GRAPHS_DIR / "standardized_trends.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path


######################################################################## 4.c.1

def plot_factor_contributions(std_coeffs: pd.DataFrame) -> Path:
    """
    Visualizes how much each factor contributes to crop yield.
    Uses standardized regression results.
    Shows relative importance as a percentage.
    """

    viz_data = std_coeffs.sort_values(
        "Relative_Contribution (%)",
        ascending=True
    )

    plt.figure(figsize=(10, 5))

    plt.barh(
        viz_data["Factor"],
        viz_data["Relative_Contribution (%)"],
        color="steelblue"
    )

    plt.xlabel("Relative Contribution to Yield (%)")
    plt.title("Relative Influence of Factors on Crop Yield")

    for i, v in enumerate(viz_data["Relative_Contribution (%)"]):
        plt.text(v + 0.5, i, f"{v:.1f}%", va="center")

    plt.xlim(0, viz_data["Relative_Contribution (%)"].max() + 5)
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    output_path = GRAPHS_DIR / "factor_contributions.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path


######################################################################## 5.b.2

def plot_baseline_vs_scenario(historical_df: pd.DataFrame,baseline_future: pd.DataFrame,scenario_future: pd.DataFrame,) -> Path:
    
    years_hist = historical_df["year"]
    yield_hist = historical_df["yield_kg_ha"]

    years_future = baseline_future["year"]
    yield_baseline = baseline_future["baseline_yield_kg_ha"]
    yield_scenario = scenario_future["scenario_yield_kg_ha"]

    plt.figure(figsize=(15, 5))

    max_year = int(years_future.max())
    plt.xticks(range(2000, max_year + 1), rotation=30)
    plt.xlim(1999, max_year)
    plt.grid(True)

    plt.plot(
        years_hist,
        yield_hist,
        label="Historical Yield",
        linewidth=2,
        color="green",
    )

    plt.plot(
        years_future,
        yield_baseline,
        linestyle="--",
        linewidth=3,
        label="Baseline Future Yield (No Intervention)",
        color="lightgreen",
    )

    plt.plot(
        years_future,
        yield_scenario,
        linestyle=":",
        linewidth=3,
        label="Scenario Yield (With Interventions)",
        color="blue",
    )

    plt.axvline(
        years_hist.iloc[-1],
        linestyle=":",
        color="gray",
        label="Present",
    )

    plt.xlabel("Year")
    plt.ylabel("Crop Yield (kg/hectare)")
    plt.title("Scenario Analysis: Yield Response to Factor Changes")
    plt.legend()

    output_path = GRAPHS_DIR / "baseline_vs_best_case.png"
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()

    return output_path
