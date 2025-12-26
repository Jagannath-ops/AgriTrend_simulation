from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

GRAPHS_DIR = OUTPUTS_DIR / "graphs"
REPORTS_DIR = OUTPUTS_DIR / "reports"

SYNTHETIC_DATA = DATA_DIR / "syntheticData" / "universal_synthetic_data.csv"
