import logging
from datetime import datetime
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def export_watering_data(df_watering):
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

    # prepare data
    # switch longitude and latitude columns, because they are named wrong
    df = df_watering.rename(
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

    # save as csv file
    df.to_csv(file_path + ".csv", index=False, sep=";")
    logger.info(
        "Watering data was written to csv-file " + file_path + ".csv" + " at " + str(timestamp)
    )

    # save as geodataframe
    gdf.to_file(file_path + ".geojson", driver="GeoJSON")
    logger.info(
        "Watering data was written to geojson-file "
        + file_path
        + ".geojson"
        + " at "
        + str(timestamp)
    )

def export_KPIs(df_adopt, df_water):
    """Add KPIs to existing csv file.

    Args:
        df_adopt: (DataFrame): KPIs about watered trees
        df_water: (DataFrame): KPIs about adoptes trees

    Output: 
        daten/giessdenkiez_KPIs.csv
    """

    # get existing df
    existing_df = pd.read_csv("daten/giessdenkiezKPIs.csv", sep=",")

    # preprocess data
    result = df_adopt.join(df_water)
    timestamp = datetime.now().date()
    result["datestamp"] = timestamp

    # open csv in append mode 'a' to add dataframe to existing csv file
    result.to_csv("daten/giessdenkiezKPIs.csv", mode="a", index=False, header=False)
    logger.info("KPI data was added to existing csv-file: daten/giessdenkiez_KPIs.csv")
