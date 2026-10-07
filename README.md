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
