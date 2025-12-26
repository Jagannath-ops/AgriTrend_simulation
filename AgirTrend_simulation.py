from src.data_generation import generate_synthetic_data
from src.data_loader import save_synthetic_data, load_synthetic_data
from src.analysis import run_regression_analysis
from src.model import train_yield_model, predict_baseline_future
from src.scenarios import run_best_case_1pct_scenario
from src.report_builder import build_pdf_report
from src.visualization import plot_yield_trend,plot_standardized_trends,plot_factor_contributions,plot_baseline_vs_scenario,plot_factor_timeseries


def main():

# 1 Generate and store synthetic historical data
    df = generate_synthetic_data()
    save_synthetic_data(df)

# 2 Load data (simulates real-world data pipeline)
    df = load_synthetic_data()

# 3 Analyze historical yield drivers
    analysis_results = run_regression_analysis(df)

# 4 Visualize historical trends
    plot_yield_trend(df)
    plot_standardized_trends(df)
    plot_factor_timeseries(df)
    plot_factor_contributions(analysis_results["std_coeffs"])

# 5 Train yield prediction model
    model_bundle = train_yield_model(df)

# 6 Predict baseline future (no intervention)
    baseline_future = predict_baseline_future(df, model_bundle)

# 7 Run best-case 1% improvement scenario
    best_case = run_best_case_1pct_scenario(baseline_future,model_bundle)

# 8 Compare baseline vs intervention
    plot_baseline_vs_scenario(historical_df=df,baseline_future=baseline_future,scenario_future=best_case,)

# 9 Build final PDF report
    build_pdf_report()
    print("Report Created Successfully \nLocation: outputs/reports/universal_data.pdf")

if __name__ == "__main__":
    main()
