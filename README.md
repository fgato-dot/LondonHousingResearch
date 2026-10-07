# London Housing Market Intelligence Dashboard

A data analytics project analysing house prices and housing market trends across London boroughs using UK House Price Index (UK HPI) data.

The project combines Python, Pandas, data analysis, and Tableau to transform housing data into actionable market insights.

## Project Overview

The London Housing Market Intelligence Dashboard is a data analytics project designed to analyse residential property prices and housing market trends across London's boroughs.

The project uses UK House Price Index (UK HPI) data to explore differences in average house prices between boroughs and how the London housing market has changed over time.

The analysis follows a complete data analytics workflow:

- Data collection and preparation
- Data cleaning using Python and Pandas
- Exploratory Data Analysis (EDA)
- Borough-level price analysis
- Identification of housing market trends and patterns
- Interactive dashboard development using Tableau
- Presentation of key findings and insights

The Tableau dashboard is currently under development and will be added to the project once completed.

## Business Objectives

The main objectives of the project are to:

- Analyse house price trends across London over time.
- Compare average house prices between London boroughs.
- Identify the most and least expensive boroughs.
- Understand geographical differences in the London housing market.
- Transform raw housing data into clear and useful insights.
- Develop an interactive Tableau dashboard to support housing market analysis and decision-making.

## Data Source & Dataset

The project uses data from the **UK House Price Index (UK HPI)**, which provides information on residential property prices across the UK.

The analysis focuses specifically on London and its boroughs.

### Dataset Used

The original dataset contains historical UK HPI data with information covering:

- Date
- London borough
- Average house price
- House price indices
- Property sales and transaction-related measures
- Other housing market indicators

The original dataset was imported into Python using Pandas and prepared for analysis.

### Data Preparation

The data preparation process included:

1. Loading the original UK HPI dataset.
2. Handling the dataset encoding using `cp1252`.
3. Converting the `Date` field into a proper date format.
4. Removing duplicate records.
5. Handling missing values where required.
6. Filtering the dataset to London boroughs.
7. Exporting the cleaned dataset for subsequent analysis and visualisation.

The cleaned dataset was saved as:

`london_housing_clean.csv`

## Data Cleaning with Python

The raw UK HPI dataset was cleaned and prepared for analysis using **Python and Pandas**.

The main data-cleaning steps were implemented in the `01_clean_data.py` script.

### Cleaning Process

1. **Load the raw dataset**
   - Imported the UK HPI CSV file using Pandas.
   - The `cp1252` encoding was used to correctly read the source file.

2. **Date conversion**
   - Converted the `Date` column into a proper date format to support time-series analysis.

3. **Remove duplicates**
   - Checked the dataset for duplicate records and removed duplicates where required.

4. **Handle missing values**
   - Identified missing values and applied appropriate cleaning procedures.

5. **Filter London boroughs**
   - Selected the London boroughs required for the analysis.

6. **Create the cleaned dataset**
   - Exported the prepared data to:

```text
data/london_housing_clean.csv
```

### Python Tools

- Python
- Pandas
- NumPy
- CSV data processing

The cleaning process provides a consistent dataset for the subsequent exploratory analysis and Tableau visualisations.

## Exploratory Data Analysis (EDA)

After cleaning the dataset, I performed exploratory data analysis using **Python and Pandas** to identify patterns and trends in the London housing market.

The cleaned dataset contains approximately **150,706 records and 54 columns**.

### Analysis Performed

The EDA focused on:

- Analysing London house price trends over time.
- Calculating average house prices by borough.
- Identifying the most expensive London boroughs.
- Identifying lower-priced boroughs.
- Comparing house prices across London boroughs.
- Examining changes in average house prices over time.
- Preparing the results for visualisation in Tableau.

### Latest House Price Analysis

The latest available date in the analysed dataset was **4 January 2026**.

The highest average house prices at the latest date included:

| Borough | Average House Price |
|---|---:|
| Kensington and Chelsea | £1,272,760 |
| City of Westminster | £814,679 |
| Camden | £794,527 |
| Richmond upon Thames | £794,027 |
| Hammersmith and Fulham | £741,612 |
| Wandsworth | £670,960 |
| Islington | £665,067 |

These results demonstrate substantial differences in average property prices between London boroughs and provide a basis for further geographical and time-series analysis.

## Key Findings

The exploratory analysis identified several important characteristics of the London housing market.

### 1. Significant variation between boroughs

Average house prices vary considerably across London boroughs. The latest analysis shows particularly high average prices in **Kensington and Chelsea, Westminster, Camden and Richmond upon Thames**.

### 2. Central and high-value areas command premium prices

The analysis indicates that several central and traditionally high-value London areas have substantially higher average property prices than other boroughs.

### 3. Housing affordability differs significantly across London

The large variation in average prices highlights significant differences in housing affordability between boroughs. This makes borough-level analysis particularly useful when assessing the London housing market.

### 4. Time-series analysis provides additional market context

Analysing average prices over time helps identify longer-term housing market trends rather than relying only on a single period.

### 5. Data visualisation can improve market interpretation

The Python analysis provides the analytical foundation for an interactive **Tableau dashboard**, which will make it easier to compare boroughs, examine trends and communicate the results visually.

> **Note:** The findings presented above are based on the current Python EDA. Additional insights will be added after the Tableau dashboard is completed and the visual analysis has been finalised.

## Technologies & Tools

The project uses the following technologies and tools:

### Programming & Data Analysis

- **Python** — data processing and analysis
- **Pandas** — data cleaning, transformation and analysis
- **NumPy** — numerical data processing

### Data Visualisation

- **Tableau** — interactive dashboard development and visualisation

### Development Environment

- **PyCharm** — Python development environment
- **Git** — version control
- **GitHub** — project versioning, documentation and portfolio hosting

### Data

- **UK House Price Index (UK HPI)** — source housing market dataset

## Project Structure

The project is organised into separate components for data preparation, analysis and visualisation.

```text
LondonHousingResearch/
│
├── data/
│   └── london_housing_clean.csv
│
├── 01_clean_data.py
│
├── 02_eda.py
│
├── .gitignore
│
└── README.md
```

### Main Components

**`data/`**  
Contains the prepared dataset used for the analysis.

**`01_clean_data.py`**  
Cleans and prepares the original UK HPI dataset using Python and Pandas.

**`02_eda.py`**  
Performs exploratory data analysis, including borough-level price comparisons and analysis of house price trends over time.

**`.gitignore`**  
Specifies files and folders that should not be tracked by Git, such as the Python virtual environment and local development files.

**`README.md`**  
Provides documentation of the project, methodology, findings and technologies used.

### Dashboard

The interactive **Tableau dashboard** is currently under development and will be added to the project once the dashboard is finalised.

