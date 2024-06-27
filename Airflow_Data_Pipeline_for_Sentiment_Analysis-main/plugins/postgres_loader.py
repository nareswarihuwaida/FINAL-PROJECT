# Import modul
from sqlalchemy import create_engine
import pandas as pd

def load(data, table_name):
    # String koneksi ke PostgreSQL
    conn_string = 'postgresql://airflow:airflow@postgres:5432/data_warehouse'

    # Membuat engine SQLAlchemy
    engine = create_engine(conn_string)

    # Menggunakan engine untuk memuat data ke PostgreSQL
    data.to_sql(table_name, con=engine, if_exists='append', index=False)

    print("Successfully loaded to Postgres")
