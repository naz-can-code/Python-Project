"""
Data Cleaning Pipeline
----------------------

A reusable Python/pandas pipeline designed to automate repetitive 
data-preparation tasks. This script standardizes column names, 
converts data types, handles missing values, removes duplicates, 
and prepares datasets for downstream analytics.

"""

import pandas as pd
from pathlib import Path


class DataCleaningPipeline:
    def __init__(
        self,
        date_columns=None,
        numeric_columns=None,
        categorical_columns=None,
        fill_numeric="median",
        fill_categorical="mode",
        constant_fill_value="Unknown",
    ):
        self.date_columns = date_columns or []
        self.numeric_columns = numeric_columns or []
        self.categorical_columns = categorical_columns or []
        self.fill_numeric = fill_numeric
        self.fill_categorical = fill_categorical
        self.constant_fill_value = constant_fill_value

    # Core Cleaning Steps

    def standardize_column_names(self, df):
        df = df.copy()
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^0-9a-zA-Z_]", "", regex=True)
        )
        return df

    def convert_dates(self, df):
        df = df.copy()
        for col in self.date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        return df

    def convert_numeric(self, df):
        df = df.copy()
        for col in self.numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        return df

    def fill_missing_values(self, df):
        df = df.copy()

        # Fill numeric
        for col in self.numeric_columns:
            if col not in df.columns:
                continue

            if self.fill_numeric == "median":
                value = df[col].median()
            elif self.fill_numeric == "mean":
                value = df[col].mean()
            elif self.fill_numeric == "zero":
                value = 0
            else:
                value = df[col].median()

            df[col].fillna(value, inplace=True)

        # Fill categorical
        for col in self.categorical_columns:
            if col not in df.columns:
                continue

            if self.fill_categorical == "mode":
                value = df[col].mode().iat[0] if not df[col].mode().empty else self.constant_fill_value
            elif self.fill_categorical == "constant":
                value = self.constant_fill_value
            else:
                value = self.constant_fill_value

            df[col].fillna(value, inplace=True)

        return df

    def remove_duplicates(self, df):
        return df.drop_duplicates()

    # Run the full cleaning pipeline

    def run(self, df):
        df = self.standardize_column_names(df)
        df = self.convert_dates(df)
        df = self.convert_numeric(df)
        df = self.fill_missing_values(df)
        df = self.remove_duplicates(df)
        return df


# Example_usage

if __name__ == "__main__":
    INPUT = "raw_data.csv"
    OUTPUT = "cleaned_data.csv"

    pipeline = DataCleaningPipeline(
        date_columns=["order_date", "signup_date"],
        numeric_columns=["quantity", "price", "discount"],
        categorical_columns=["country", "segment"],
        fill_numeric="median",
        fill_categorical="mode",
    )

    print("[*] Loading data...")
    df_raw = pd.read_csv(INPUT)

    print("[*] Cleaning data...")
    df_clean = pipeline.run(df_raw)

    print("[*] Saving cleaned dataset...")
    Path(OUTPUT).parent.mkdir(exist_ok=True)
    df_clean.to_csv(OUTPUT, index=False)

    print("[✓] Pipeline complete! Saved to:", OUTPUT)
