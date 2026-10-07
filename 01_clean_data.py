# ==========================================================
# Project: London Housing Market Intelligence Dashboard
# File: 01_clean_data.py
# Author: Fernando Ferraz
# Purpose:
# Load the UK HPI dataset, filter London boroughs,
# clean the data and export a clean dataset.
# ==========================================================

import pandas as pd

# ----------------------------------------------------------
# STEP 1 - Load Raw Dataset
# ----------------------------------------------------------

print("Loading dataset...")

df = pd.read_csv(
    "data/UK-HPI-full-file-2026-04.csv",
    encoding="cp1252"
)

print("Dataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# ----------------------------------------------------------
# STEP 2 - London Boroughs
# ----------------------------------------------------------

london_areas = [
    "Barking and Dagenham",
    "Barnet",
    "Bexley",
    "Brent",
    "Bromley",
    "Camden",
    "City of London",
    "City of Westminster",
    "Croydon",
    "Ealing",
    "Enfield",
    "Greenwich",
    "Hackney",
    "Hammersmith and Fulham",
    "Haringey",
    "Harrow",
    "Havering",
    "Hillingdon",
    "Hounslow",
    "Islington",
    "Kensington and Chelsea",
    "Kingston upon Thames",
    "Lambeth",
    "Lewisham",
    "Merton",
    "Newham",
    "Redbridge",
    "Richmond upon Thames",
    "Southwark",
    "Sutton",
    "Tower Hamlets",
    "Waltham Forest",
    "Wandsworth"
]

# ----------------------------------------------------------
# STEP 3 - Filter London Data
# ----------------------------------------------------------

london_df = df[df["RegionName"].isin(london_areas)].copy()

print("\nLondon boroughs selected.")
print(f"Rows: {london_df.shape[0]}")

print("\nNumber of London areas:")
print(london_df["RegionName"].nunique())

print("\nLondon areas:")
print(sorted(london_df["RegionName"].unique()))

# ----------------------------------------------------------
# STEP 4 - Convert Date
# ----------------------------------------------------------

# ----------------------------------------------------------
# STEP 4 - Standardise Date
# ----------------------------------------------------------

# The UK HPI source uses the first day of the month
# as the reporting period, e.g. 1/4/2026 = April 2026.

london_df["Date"] = pd.to_datetime(
    london_df["Date"],
    format="%d/%m/%Y",
    errors="coerce"
)

# Create a dedicated monthly period column
london_df["YearMonth"] = london_df["Date"].dt.to_period("M")

print("\nDate data type:")
print(london_df["Date"].dtype)

print("\nDate range:")
print(london_df["Date"].min(), "to", london_df["Date"].max())

print("\nLatest reporting month:")
print(london_df["YearMonth"].max())



# ----------------------------------------------------------
# STEP 5 - Convert Numeric Columns
# ----------------------------------------------------------

numeric_columns = [
    "AveragePrice",
    "SalesVolume",
    "DetachedPrice",
    "SemiDetachedPrice",
    "TerracedPrice",
    "FlatPrice",
    "CashPrice",
    "MortgagePrice",
    "FTBPrice",
    "FOOPrice",
    "NewPrice",
    "OldPrice",
    "1m%Change",
    "12m%Change"
]

for col in numeric_columns:

    if col in london_df.columns:

        london_df[col] = pd.to_numeric(
            london_df[col],
            errors="coerce"
        )

# ----------------------------------------------------------
# STEP 6 - Remove Duplicate Rows
# ----------------------------------------------------------

duplicates = london_df.duplicated().sum()

print(f"\nDuplicate rows: {duplicates}")

london_df = london_df.drop_duplicates()

# ----------------------------------------------------------
# STEP 7 - Missing Values
# ----------------------------------------------------------

print("\nMissing Values")

missing_values = london_df.isnull().sum()

print(missing_values)

print("\nTotal missing values:")
print(missing_values.sum())
# ----------------------------------------------------------
# STEP 8 - Data Types
# ----------------------------------------------------------

print("\nData Types")

print(london_df.dtypes)

# ----------------------------------------------------------
# STEP 9 - Save Clean Dataset
# ----------------------------------------------------------

london_df.to_csv(
    "data/london_housing_clean.csv",
    index=False
)

print("\nClean dataset exported successfully!")

print("Location:")
print("data/london_housing_clean.csv")



