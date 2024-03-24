import sqlite3
# import threading
from datetime import datetime

def insert_climate_data(
    temperature, humidity, pressure,
    latitude, longitude, elevation, satellite_count,
    x_direction, y_direction, z_direction):

    con = sqlite3.connect("ClimateData.db")
    cursor = con.cursor()

    create_climate_table_query = """
    CREATE TABLE IF NOT EXISTS ClimateData (
        DataId INTEGER PRIMARY KEY AUTOINCREMENT,
        Timestamp TEXT NOT NULL,
        Temperature REAL,
        Humidity REAL,
        Pressure REAL,
        Latitude REAL,
        Longitude REAL,
        Elevation REAL,
        SatelliteCount INTEGER,
        XDirection REAL,
        YDirection REAL,
        ZDirection REAL
    )
    """
    
    cursor.execute(create_climate_table_query)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # ここだけは平均化する必要ないからね
    print(timestamp)
    timestamp_str = str(timestamp)

    try:
        cursor.execute("INSERT INTO ClimateData (Timestamp) VALUES (timestamp_str)")
        # cursor.execute("INSERT INTO ClimateData (Timestamp) VALUES (CURRENT_TIMESTAMP)")            # Timestampの挿入
        # cursor.execute("INSERT INTO ClimateData (Timestamp) VALUES (datetime(CURRENT_TIMESTAMP, '+9 hours'))")
        cursor.execute("INSERT INTO ClimateData (Temperature) VALUES (?)", (temperature,))          # Temperatureの挿入
        cursor.execute("INSERT INTO ClimateData (Humidity) VALUES (?)", (humidity,))                # Humidityの挿入
        cursor.execute("INSERT INTO ClimateData (Pressure) VALUES (?)", (pressure,))                # Pressureの挿入
        cursor.execute("INSERT INTO ClimateData (Latitude) VALUES (?)", (latitude,))                # Latitudeの挿入
        cursor.execute("INSERT INTO ClimateData (Longitude) VALUES (?)", (longitude,))              # Longitudeの挿入
        cursor.execute("INSERT INTO ClimateData (Elevation) VALUES (?)", (elevation,))              # Elevationの挿入
        cursor.execute("INSERT INTO ClimateData (SatelliteCount) VALUES (?)", (satellite_count,))   # SatelliteCountの挿入
        cursor.execute("INSERT INTO ClimateData (XDirection) VALUES (?)", (x_direction,))           # XDirectionの挿入
        cursor.execute("INSERT INTO ClimateData (YDirection) VALUES (?)", (y_direction,))           # YDirectionの挿入
        cursor.execute("INSERT INTO ClimateData (ZDirection) VALUES (?)", (z_direction,))           # ZDirectionの挿入

    except sqlite3.Error as e:
    	print(f"SQLite error: {e}")
    	con.rollback()

    else:
        con.commit()

