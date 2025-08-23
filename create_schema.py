# SQL/create_schema.py
# Creates star schema in PostgreSQL

import pandas as pd
from sqlalchemy import create_engine, text

# === 1. Load Cleaned CSV ===
CLEANED_CSV_PATH = r"C:\Users\sathishkumar\Downloads\Luxury_housing_sales_analysis\Data\luxury_housing_cleaned.csv"
df = pd.read_csv(CLEANED_CSV_PATH)
print(f" Loaded cleaned data with {df.shape[0]} rows")

# === 2. Connect to PostgreSQL ===
db_url = "postgresql+psycopg2://postgres:MALATHI28@localhost:5432/luxury_housingdb"
engine = create_engine(db_url)

# Helper: Safe drop with CASCADE
def replace_table_with_cascade(df, table_name, engine, pk_name):
    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE"))
        df.to_sql(table_name, conn, if_exists='fail', index_label=pk_name)
        print(f" {table_name} created")

# === 3. Create Dimension Tables ===

# dim_builder
dim_builder = df[['Developer_Name']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_builder, 'dim_builder', engine, 'Builder_ID')

# dim_market
dim_market = df[['Micro_Market']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_market, 'dim_market', engine, 'Market_ID')

# dim_property_type
dim_property_type = df[['Configuration']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_property_type, 'dim_property_type', engine, 'Property_Type_ID')

# dim_buyer_type
dim_buyer_type = df[['Buyer_Type']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_buyer_type, 'dim_buyer_type', engine, 'Buyer_Type_ID')

# dim_sales_channel
dim_sales_channel = df[['Sales_Channel']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_sales_channel, 'dim_sales_channel', engine, 'Channel_ID')

# dim_possession_status
dim_possession_status = df[['Possession_Status']].drop_duplicates().dropna().reset_index(drop=True)
replace_table_with_cascade(dim_possession_status, 'dim_possession_status', engine, 'Status_ID')

# === 4. Read Back Dimensions to Map IDs ===
dim_builder_db = pd.read_sql("SELECT * FROM dim_builder", engine).set_index('Developer_Name')
dim_market_db = pd.read_sql("SELECT * FROM dim_market", engine).set_index('Micro_Market')
dim_property_type_db = pd.read_sql("SELECT * FROM dim_property_type", engine).set_index('Configuration')
dim_buyer_type_db = pd.read_sql("SELECT * FROM dim_buyer_type", engine).set_index('Buyer_Type')
dim_sales_channel_db = pd.read_sql("SELECT * FROM dim_sales_channel", engine).set_index('Sales_Channel')
dim_possession_status_db = pd.read_sql("SELECT * FROM dim_possession_status", engine).set_index('Possession_Status')

# Map IDs to fact
df['Builder_ID'] = df['Developer_Name'].map(dim_builder_db['Builder_ID'])
df['Market_ID'] = df['Micro_Market'].map(dim_market_db['Market_ID'])
df['Property_Type_ID'] = df['Configuration'].map(dim_property_type_db['Property_Type_ID'])
df['Buyer_Type_ID'] = df['Buyer_Type'].map(dim_buyer_type_db['Buyer_Type_ID'])
df['Sales_Channel_ID'] = df['Sales_Channel'].map(dim_sales_channel_db['Channel_ID'])
df['Possession_Status_ID'] = df['Possession_Status'].map(dim_possession_status_db['Status_ID'])

# === 5. Create Fact Table ===
fact_columns = [
    'Property_ID', 'Builder_ID', 'Market_ID', 'Property_Type_ID',
    'Buyer_Type_ID', 'Sales_Channel_ID', 'Possession_Status_ID',
    'Ticket_Price_Cr', 'Unit_Size_Sqft', 'Price_per_Sqft',
    'Amenity_Score', 'Locality_Infra_Score', 'Avg_Traffic_Time_Min',
    'Booking_Flag', 'Purchase_Quarter', 'Year', 'Quarter_Number'
]

# Drop rows with missing IDs (optional)
fact_sales = df[fact_columns].copy().dropna()

# Upload to PostgreSQL
fact_sales.to_sql('fact_sales', engine, if_exists='replace', index=False)

print("Star schema (fact & dim tables) created successfully!")