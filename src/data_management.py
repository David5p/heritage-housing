from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """Load dataset from a CSV file"""
    return pd.read_csv(file_path)


def clean_data(df):
    df = df.copy()

    # Drop columns with too many missing values
    cols_to_drop = ["EnclosedPorch", "WoodDeckSF"]
    df = df.drop(columns=cols_to_drop, errors="ignore")

    # Fill numeric columns with many zeros
    numeric_impute_zero = ["MasVnrArea", "2ndFlrSF"]

    for col in numeric_impute_zero:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # Fill numeric columns with median
    numeric_impute_median = ["BedroomAbvGr", "GarageYrBlt", "LotFrontage"]

    for col in numeric_impute_median:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # Fill categorical missing values
    categorical_cols = ["BsmtExposure", "BsmtFinType1", "GarageFinish"]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].replace(["NA", "", " ", "nan"], np.nan)
            df[col] = df[col].fillna("Missing")

    return df

 # Feature Engineering (encoding step)


def encode_features(df):
    df = df.copy()

    # One-hot encoding
    categorical_cols = ["BsmtExposure", "BsmtFinType1", "GarageFinish"]

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Ordinal encoding for KitchenQual
    if "KitchenQual" in df.columns:
        kitchen_mapping = {
            "Ex": 4,
            "Gd": 3,
            "TA": 2,
            "Fa": 1
        }
        df["KitchenQual"] = df["KitchenQual"].map(kitchen_mapping)

    return df


def split_data(df, test_size=0.2, random_state=42):
    """Split dataset into train and test sets"""
    return train_test_split(df, test_size=test_size, random_state=random_state)


def save_split(train, test, output_dir):
    """Save train and test sets to CSV"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train.to_csv(output_dir / "train.csv", index=False)
    test.to_csv(output_dir / "test.csv", index=False)
