from sqlalchemy import create_engine
from urllib.parse import quote_plus


SERVER = r".\SQLSERVERSS"
DATABASE = "weather_etl"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    "mssql+pyodbc:///?odbc_connect="
    + quote_plus(connection_string)
)


def load_weather(df):
    df.to_sql(
        "weather_observations",
        con=engine,
        if_exists="append",
        index=False,
    )