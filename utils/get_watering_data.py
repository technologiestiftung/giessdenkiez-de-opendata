import logging
from datetime import datetime
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def read_watering_data(conn):
    """Load data about watered trees and information about trees from the database to a dataframe and to a geodataframe.

    Args:
        conn (class 'sqlalchemy.engine.base.Engine'): The engine object for connecting to the database.

    Returns:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.
    """

    # create query for selecting the data
    logger.info("Starting script: GdK Open Data")
    sql_query = "SELECT t.id, t.lat, t.lng, t.bezirk, t.artdtsch, t.gattungdeutsch, t.strname, t.pflanzjahr, w.time, w.amount FROM trees_watered AS w JOIN trees_new AS t ON w.tree_id=t.id "

    # import data and create dataframe
    # switch longitude and latitude columns, because they are named wrong
    df = df.rename(
        columns={
            "lat": "lng",
            "lng": "lat",
            "amount": "bewaesserungsmenge_in_liter",
            "time": "zeitpunkt_der_bewaesserung",
            "artdtsch": "baumart",
            "gattungdeutsch": "gattung",
        }
    )
    gdf = df.copy()

    # save data also in a geodataframe
    gdf = gpd.GeoDataFrame(gdf, geometry=gpd.points_from_xy(df.lng, df.lat))
    gdf = gdf.set_crs("EPSG:4326")

    return df, gdf


def data_to_files(df, gdf):
    """Write data about watered trees and information about trees to csv and geojson files.

    Args:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.

    Output: 
        daten/giessdenkiez_bewässerungsdaten.csv
        daten/giessdenkiez_bewässerungsdaten.geojson
    """

    # set path were files should be written  to
    file_path = "daten/giessdenkiez_bewässerungsdaten"

    timestamp = datetime.now()
    day = str(timestamp.strftime("%d-%m-%y"))

    # save as csv file
    df.to_csv(file_path + ".csv", index=False, sep=";")
    logger.info(
        "Data was written to csv-file " + file_path + ".csv" + " at " + str(timestamp)
    )

    # save as geodataframe
    gdf.to_file(file_path + ".geojson", driver="GeoJSON")
    logger.info(
        "Data was written to geojson-file "
        + file_path
        + ".geojson"
        + " at "
        + str(timestamp)
    )
