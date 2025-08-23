import pandas as pd
from sqlalchemy import create_engine

def upload_to_database(df: pd.DataFrame, table_name: str, db_url: str, schema: str = "public"):
    """Upload DataFrame to PostgreSQL database."""
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, schema=schema, if_exists="replace", index=False)
        print(f" Data uploaded successfully to {schema}.{table_name}")
    except Exception as e:
        print(f" Database upload failed: {e}")
