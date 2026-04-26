from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/vehicles_raw.csv")
PROCESSED_DATA_PATH = Path("data/processed/vehicles_cleaned.csv")


def load_raw_vehicles_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load raw dataset."""
    return pd.read_csv(path, low_memory=False)


def load_processed_vehicles_data(path: Path = PROCESSED_DATA_PATH) -> pd.DataFrame:
    """Load cleaned dataset."""
    return pd.read_csv(path)


if __name__ == "__main__":
    df = load_processed_vehicles_data()
    print(f"Loaded CLEANED dataset with shape: {df.shape}")