# Batch Weather ETL Pipeline

A beginner-friendly batch ETL pipeline built with Python, pandas, and SQL Server.

The pipeline extracts current weather data from the Open-Meteo public API, transforms the data using pandas, and loads the cleaned records into Microsoft SQL Server.

## Architecture

```text
Open-Meteo API
      │
      ▼
   Extract
      │
      ▼
 Python / requests
      │
      ▼
   Transform
      │
      ▼
 Python / pandas
      │
      ▼
     Load
      │
      ▼
 SQLAlchemy + pyodbc
      │
      ▼
 Microsoft SQL Server
      │
      ▼
     SSMS
```

## Technologies

* Python
* pandas
* requests
* SQLAlchemy
* pyodbc
* Microsoft SQL Server
* SQL Server Management Studio (SSMS)
* Windows Task Scheduler

## Project Structure

```text
batch-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── logs/
├── .gitignore
├── README.md
├── requirements.txt
├── pipeline.py
└── run_pipeline.bat
```

## How It Works

### 1. Extract

`extract.py` sends a request to the Open-Meteo API and retrieves the current weather data.

The API provides values such as:

* Observation time
* Temperature
* Relative humidity
* Wind speed
* Weather code

### 2. Transform

`transform.py` converts the API response into a pandas DataFrame.

The transformation also converts the API timestamp into a proper datetime value so it can be stored in SQL Server.

### 3. Load

`load.py` connects to SQL Server using SQLAlchemy and pyodbc.

The pipeline inserts the transformed weather data into:

```text
weather_etl.dbo.weather_observations
```

The database also prevents duplicate observations based on:

```text
city + observed_at
```

## Database Schema

The pipeline uses the following table:

```sql
CREATE TABLE weather_observations (
    id INT IDENTITY(1,1) PRIMARY KEY,
    observed_at DATETIME2 NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    city VARCHAR(100),
    weather_code INT,
    loaded_at DATETIME2 DEFAULT GETDATE()
);
```

A unique constraint is used to prevent duplicate observations:

```sql
UNIQUE (city, observed_at)
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd batch-etl-pipeline
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure SQL Server

Create a database named:

```text
weather_etl
```

Then create the `weather_observations` table using the SQL schema described above.

### 5. Configure the SQL Server connection

Open:

```text
src/load.py
```

Set the SQL Server name:

```python
SERVER = r"YOUR_SERVER_NAME"
```

For example:

```python
SERVER = r".\SQLEXPRESS"
```

The project currently uses Windows Authentication:

```text
Trusted_Connection=yes
```

Make sure the SQL Server instance is running and that your Windows account has permission to access the database.

## Running the Pipeline

From the project directory:

```powershell
python pipeline.py
```

The pipeline will:

1. Request current weather data.
2. Transform the API response.
3. Check whether the observation already exists.
4. Insert a new observation into SQL Server if necessary.

Example output:

```text
Data to load:
        observed_at  temperature  humidity  wind_speed       city  weather_code
0  2026-10-02 10:45        23.2        35       23.4  Amsterdam             2

Inserted observation: Amsterdam 2026-10-02 10:45:00
Data loaded successfully!
```

If the observation already exists:

```text
Skipping existing observation: Amsterdam 2026-10-02 10:45:00
```

## Querying the Data

Open SQL Server Management Studio and run:

```sql
USE weather_etl;

SELECT *
FROM dbo.weather_observations
ORDER BY observed_at DESC;
```

## What I Learned

This project was built to practice the fundamentals of data engineering:

* Calling a public REST API
* Working with JSON data
* Python functions
* pandas DataFrames
* Data type conversion
* SQL table design
* SQL Server
* Database connections
* SQLAlchemy
* pyodbc
* ETL architecture
* Duplicate handling
* Basic automation
* Git and GitHub

## Future Improvements

Possible next steps:

* Add multiple cities
* Add historical weather data
* Add logging
* Add better error handling
* Store API responses as raw JSON
* Add data-quality checks
* Create SQL analytics queries
* Build a dashboard with Power BI
* Run the pipeline automatically with Windows Task Scheduler

## Data Source

Weather data is provided by the Open-Meteo API:

https://open-meteo.com/

## License

This project is intended as a learning project.
