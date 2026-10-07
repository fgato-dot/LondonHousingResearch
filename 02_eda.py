import pandas as pd

# Load cleaned London housing data
london_df = pd.read_csv(
    "data/london_housing_clean.csv",
    encoding="cp1252"
)

# Convert Date to datetime
london_df["Date"] = pd.to_datetime(
    london_df["Date"]
)
# Convert YearMonth back to Period after loading CSV
london_df["YearMonth"] = pd.to_datetime(
    london_df["YearMonth"].astype(str)
).dt.to_period("M")

print(london_df.head())

print("\nLatest reporting month:")
print(london_df["YearMonth"].max())

# ==========================================================
# PHASE 3 - EXPLORATORY DATA ANALYSIS
# ==========================================================

# Step 1 - Average house price by London borough

borough_prices = (
    london_df
    .groupby("RegionName")["AveragePrice"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage house price by London borough:")

print(borough_prices)

# ----------------------------------------------------------
# EDA 1 - Top 10 Most Expensive London Boroughs
# ----------------------------------------------------------

top_10_expensive = (
    london_df
    .groupby("RegionName")["AveragePrice"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Format prices as £
top_10_expensive_formatted = top_10_expensive.apply(
    lambda x: f"£{x:,.0f}"
)

print("\nTop 10 Most Expensive London Boroughs:")
print(top_10_expensive_formatted)

# ----------------------------------------------------------
# EDA 2 - Bottom 10 Cheapest London Boroughs
# ----------------------------------------------------------

bottom_10_cheapest = (
    london_df
    .groupby("RegionName")["AveragePrice"]
    .mean()
    .sort_values(ascending=True)
    .head(10)
)

# Format prices as £
bottom_10_cheapest_formatted = bottom_10_cheapest.apply(
    lambda x: f"£{x:,.0f}"
)

print("\nBottom 10 Cheapest London Boroughs:")
print(bottom_10_cheapest_formatted)

# ----------------------------------------------------------
# EDA 3 - London Average House Price Over Time
# ----------------------------------------------------------

london_price_trend = (
    london_df
    .groupby("Date")["AveragePrice"]
    .mean()
    .sort_index()
)

print("\nLondon Average House Price Over Time:")

print(london_price_trend)


# ----------------------------------------------------------
# EDA 4 - Average 12-Month Price Growth
# ----------------------------------------------------------

price_growth = (
    london_df
    .groupby("Date")["12m%Change"]
    .mean()
    .sort_index()
)

print("\nAverage London 12-Month Price Growth:")
print(price_growth)

# ----------------------------------------------------------
# EDA 5 - Average Price by Property Type
# ----------------------------------------------------------

property_types = [
    "DetachedPrice",
    "SemiDetachedPrice",
    "TerracedPrice",
    "FlatPrice"
]

property_type_prices = (
    london_df[property_types]
    .mean()
    .sort_values(ascending=False)
)

# Format as £
property_type_prices_formatted = property_type_prices.apply(
    lambda x: f"£{x:,.0f}"
)

print("\nAverage Price by Property Type:")
print(property_type_prices_formatted)

# ----------------------------------------------------------
# EDA 6 - Sales Volume by London Borough
# ----------------------------------------------------------

sales_by_borough = (
    london_df
    .groupby("RegionName")["SalesVolume"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 London Boroughs by Total Sales Volume:")
print(sales_by_borough)

# ----------------------------------------------------------
# EDA 7 - Latest House Prices by London Borough
# ----------------------------------------------------------

# ----------------------------------------------------------
# EDA 7 - Latest House Prices by London Borough
# ----------------------------------------------------------

latest_month = london_df["YearMonth"].max()

latest_data = london_df[
    london_df["YearMonth"] == latest_month
]

latest_prices = (
    latest_data
    .groupby("RegionName")["AveragePrice"]
    .mean()
    .sort_values(ascending=False)
)

latest_prices_formatted = latest_prices.apply(
    lambda x: f"£{x:,.0f}"
)

print(f"\nLatest reporting month: {latest_month}")

print("\nLatest Average House Prices by Borough:")
print(latest_prices_formatted)

# ----------------------------------------------------------
# EDA 8 - Strongest and Weakest 12-Month Price Growth
# ----------------------------------------------------------

latest_month = london_df["YearMonth"].max()

latest_growth = (
    london_df[london_df["YearMonth"] == latest_month]
    .groupby("RegionName")["12m%Change"]
    .mean()
    .sort_values(ascending=False)
)

# Top 10 strongest growth
top_10_growth = latest_growth.head(10)

# Bottom 10 / weakest growth
bottom_10_growth = latest_growth.tail(10).sort_values()

print(f"\n12-Month Price Growth by Borough - {latest_month}")

print("\nTop 10 Strongest Growth:")
print(top_10_growth.round(2).astype(str) + "%")

print("\nBottom 10 Weakest Growth:")
print(bottom_10_growth.round(2).astype(str) + "%")

# ----------------------------------------------------------
# EDA 9 - Latest Price vs Sales Volume
# ----------------------------------------------------------

# ----------------------------------------------------------
# EDA 9 - Latest Available Sales Volume
# ----------------------------------------------------------

# Find the latest month with available SalesVolume data
latest_sales_month = (
    london_df.loc[
        london_df["SalesVolume"].notna(),
        "YearMonth"
    ]
    .max()
)

print(f"\nLatest month with SalesVolume data: {latest_sales_month}")

# Select data for that month
latest_sales = (
    london_df[
        london_df["YearMonth"] == latest_sales_month
    ]
    [["RegionName", "AveragePrice", "SalesVolume"]]
    .copy()
)

# Sort by sales volume
latest_sales = latest_sales.sort_values(
    "SalesVolume",
    ascending=False
)

print("\nTop 10 Boroughs by Latest Available Sales Volume:")

print(
    latest_sales
    .head(10)
    .to_string(index=False)
)

# ----------------------------------------------------------
# EDA 10 - Correlation Between Price and Sales Volume
# ----------------------------------------------------------

correlation = latest_sales["AveragePrice"].corr(
    latest_sales["SalesVolume"]
)

print("\nCorrelation between Average Price and Sales Volume:")
print(round(correlation, 2))

# ----------------------------------------------------------
# EDA 11 - Borough Price vs London Average
# ----------------------------------------------------------

# Latest reporting month
latest_month = london_df["YearMonth"].max()

# Filter latest month
latest_data = london_df[
    london_df["YearMonth"] == latest_month
].copy()

# Calculate London-wide average price
london_average = latest_data["AveragePrice"].mean()

print(f"\nLondon-wide Average House Price - {latest_month}:")
print(f"£{london_average:,.0f}")

# Calculate difference from London average
latest_data["DifferenceFromLondon"] = (
    latest_data["AveragePrice"] - london_average
)

# Calculate percentage difference
latest_data["PercentFromLondon"] = (
    latest_data["DifferenceFromLondon"]
    / london_average
) * 100

# Sort by difference
borough_vs_london = latest_data[
    [
        "RegionName",
        "AveragePrice",
        "DifferenceFromLondon",
        "PercentFromLondon"
    ]
].sort_values(
    "DifferenceFromLondon",
    ascending=False
)

print("\nBorough Price vs London Average:")

print(
    borough_vs_london.to_string(
        index=False,
        formatters={
            "AveragePrice": lambda x: f"£{x:,.0f}",
            "DifferenceFromLondon": lambda x: f"£{x:,.0f}",
            "PercentFromLondon": lambda x: f"{x:.1f}%"
        }
    )
)


# ----------------------------------------------------------
# EDA 12 - Historical Price Growth by Borough
# ----------------------------------------------------------

# First and latest reporting months
first_month = london_df["YearMonth"].min()
latest_month = london_df["YearMonth"].max()

print(f"\nFirst reporting month: {first_month}")
print(f"Latest reporting month: {latest_month}")

# Get first available AveragePrice for each borough
first_prices = (
    london_df[
        london_df["YearMonth"] == first_month
    ]
    .groupby("RegionName")["AveragePrice"]
    .mean()
)

# Get latest AveragePrice for each borough
latest_prices = (
    london_df[
        london_df["YearMonth"] == latest_month
    ]
    .groupby("RegionName")["AveragePrice"]
    .mean()
)

# Combine first and latest prices
historical_growth = pd.DataFrame({
    "FirstPrice": first_prices,
    "LatestPrice": latest_prices
})

# Calculate absolute price increase
historical_growth["PriceIncrease"] = (
    historical_growth["LatestPrice"]
    - historical_growth["FirstPrice"]
)

# Calculate percentage growth
historical_growth["GrowthPercent"] = (
    historical_growth["PriceIncrease"]
    / historical_growth["FirstPrice"]
) * 100

# Sort by percentage growth
historical_growth = historical_growth.sort_values(
    "GrowthPercent",
    ascending=False
)

print("\nHistorical Price Growth by Borough:")

print(
    historical_growth.to_string(
        formatters={
            "FirstPrice": lambda x: f"£{x:,.0f}",
            "LatestPrice": lambda x: f"£{x:,.0f}",
            "PriceIncrease": lambda x: f"£{x:,.0f}",
            "GrowthPercent": lambda x: f"{x:.1f}%"
        }
    )
)


# ----------------------------------------------------------
# EDA 13 - Compound Annual Growth Rate (CAGR)
# ----------------------------------------------------------

# Calculate number of years between first and latest period
years = (
    latest_month.year - first_month.year
)

print(f"\nNumber of years: {years}")

# Calculate CAGR
historical_growth["CAGR"] = (
    (
        historical_growth["LatestPrice"]
        / historical_growth["FirstPrice"]
    ) ** (1 / years)
    - 1
) * 100

# Sort by CAGR
cagr_by_borough = historical_growth.sort_values(
    "CAGR",
    ascending=False
)

print("\nCAGR by London Borough:")

print(
    cagr_by_borough[
        [
            "FirstPrice",
            "LatestPrice",
            "GrowthPercent",
            "CAGR"
        ]
    ].to_string(
        formatters={
            "FirstPrice": lambda x: f"£{x:,.0f}",
            "LatestPrice": lambda x: f"£{x:,.0f}",
            "GrowthPercent": lambda x: f"{x:.1f}%",
            "CAGR": lambda x: f"{x:.2f}%"
        }
    )
)

# ----------------------------------------------------------
# EDA 14 - London Borough Price Volatility
# ----------------------------------------------------------

# Calculate volatility of monthly 12-month price growth
volatility = (
    london_df
    .groupby("RegionName")["12m%Change"]
    .std()
    .sort_values(ascending=False)
)

print("\nLondon Borough Price Volatility:")
print(
    volatility
    .round(2)
    .astype(str)
    .add("%")
)

# Top 10 most volatile boroughs
top_10_volatility = volatility.head(10)

print("\nTop 10 Most Volatile Boroughs:")
print(
    top_10_volatility
    .round(2)
    .astype(str)
    .add("%")
)

# Bottom 10 least volatile boroughs
bottom_10_volatility = volatility.tail(10).sort_values()

print("\nBottom 10 Least Volatile Boroughs:")
print(
    bottom_10_volatility
    .round(2)
    .astype(str)
    .add("%")
)
