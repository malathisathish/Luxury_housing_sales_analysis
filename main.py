import os
import numpy as np
import pandas as pd
from Data_loader import load_data
from Cleaning import drop_duplicates, handle_missing_values,convert_types,normalize_columns,absolute_values
from Feature_engineering import derive_columns
from db_operations import upload_to_database
from EDA import eda_plots
from utils import log_start, log_end

def main():
    log_start()

    # File path
    file_path = r"C:\Users\sathishkumar\Downloads\Luxury_housing_sales_analysis\Data\Luxury_Housing_Bangalore.csv"
    df = load_data(file_path)

    if df.empty:
        print(" No data to process. Exiting...")
        return

    # Cleaning
    df = drop_duplicates(df)
    df = handle_missing_values(df)
    df = convert_types(df)
    df = normalize_columns(df)
    df = absolute_values(df)

    # Feature Engineering
    df = derive_columns(df)
    
    #upload the database
    db_url = "postgresql+psycopg2://postgres:MALATHI28@localhost:5432/luxury_housingdb"
    upload_to_database(df, "luxury_housing", db_url)

    #EDA
    df = eda_plots(df)

    log_end()

if __name__ == "__main__":
    main()