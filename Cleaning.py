import pandas as pd
import numpy as np

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows and report how many were dropped."""
    before = df.shape[0]   # number of rows before
    df = df.drop_duplicates()
    after = df.shape[0]    # number of rows after
    print(f"Dropped {before - after} duplicate rows.")
    return df

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert necessary columns to proper dtypes."""
    df['Purchase_Quarter'] = pd.to_datetime(df['Purchase_Quarter'], errors='coerce')
    df['Ticket_Price_Cr'] = pd.to_numeric(df['Ticket_Price_Cr'], errors='coerce')
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names and key fields."""
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    # Clean up Ticket_Price_Cr
    df['Ticket_Price_Cr'] = (
        df['Ticket_Price_Cr']
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace("Cr", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .astype(float)
    )
    # Normalize categorical text fields
    text_cols = [
        "Micro_Market", "Project_Name", "Developer_Name",
        "Configuration", "Transaction_Type", "Buyer_Type",
        "Purchase_Quarter", "Possession_Status", "Sales_Channel",
        "Buyer_Comments", "NRI_Buyer"
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()
    return df


def absolute_values(df: pd.DataFrame) -> pd.DataFrame:
    """Convert possible negative numbers to absolute."""
    for col in ['Unit_Size_Sqft', 'Ticket_Price_Cr']:
        if col in df.columns:
            df[col] = df[col].abs()
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill and handle missing values for numeric and categorical columns."""
    print(" Handling missing values...")

    # Step 1: Define numeric columns explicitly
    numeric_cols = ["Unit_Size_Sqft", "Ticket_Price_Cr", "Amenity_Score"]

    for col in numeric_cols:
        if col in df.columns:
            # Convert to numeric safely (ignore non-numeric values)
            df[col] = pd.to_numeric(df[col], errors='coerce')
            median_value = df[col].median(skipna=True)
            df[col] = df[col].fillna(median_value)
            print(f" Filled missing values in numeric column '{col}' with median = {median_value}")

    # Step 2: Handle Buyer_Comments separately
    if "Buyer_Comments" in df.columns:
        df["Buyer_Comments"] = df["Buyer_Comments"].replace(["Nan", "nan", "NaN"], np.nan)
        df["Buyer_Comments"] = df["Buyer_Comments"].fillna("No Comments Provided")
        print("Filled missing Buyer_Comments with 'No Comments Provided'")

    # Step 3: General categorical fill (for other text columns if any)
    for col in df.select_dtypes(include="object").columns:
        if col != "Buyer_Comments":  # Already handled
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)
            print(f" Filled missing values in categorical column '{col}' with mode = {mode_value}")

    return df

          
