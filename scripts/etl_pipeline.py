from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/vehicles_raw.csv")


def load_raw_vehicles_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw vehicles dataset for profiling and preprocessing."""
    return pd.read_csv(path, low_memory=False)


if __name__ == "__main__":
    df = load_raw_vehicles_data()
    print(f"Loaded dataset with shape: {df.shape}")
