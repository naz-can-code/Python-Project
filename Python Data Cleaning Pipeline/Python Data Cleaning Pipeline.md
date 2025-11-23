# Python Data Cleaning Pipeline

A fully automated, reusable **data-cleaning pipeline** built with **Python** and **pandas**.  
This project transforms messy, inconsistent raw data into clean, analysis-ready datasets, reducing manual data preparation time and improving data quality.


## Features

- **Column Standardization**  
  Converts column names to snake_case and removes invalid characters.

- **Data Type Conversion**  
  Automatically parses dates (even with mixed formats) and coerces numeric fields.

- **Missing Value Handling**  
  Configurable strategies:
  - Median / Mean / Zero for numeric fields  
  - Mode / Constant value for categorical fields  

- **Duplicate Removal**  
  Detects and removes duplicate records.

- **Outlier Handling (Optional)**  
  Supports IQR-based capping and customizable rules.

- **Reusable Class-Based Design**  
  Easy to integrate into new ETL scripts or analysis workflows.

- **Sample Raw Dataset Included**  
  A 50-row real-world–style dataset with invalid values, missing fields, inconsistent formats, and duplicates.


##  How It Works

The pipeline performs the following steps:

1. Load the raw CSV file  
2. Standardize column names  
3. Convert date & numeric fields  
4. Fill missing values using chosen strategies  
5. Remove duplicate rows  
6. Output a clean, analysis-ready dataset  

## Project Structure
├── data_cleaning_pipeline.py     
├── raw_data.csv                 
├── cleaned_data.csv             
└── README.md                     

## Running the Pipeline

Install dependencies:
```bash
pip install pandas
```

Run the Pipeline
```bash
python data_cleaning_pipeline.py
```
