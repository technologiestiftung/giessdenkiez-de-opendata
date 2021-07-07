import logging
import csv
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger = logging.getLogger("root")
FORMAT = "[%(levelname)s %(name)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


def export_KPIs(df_adopt, df_water):
    """Add KPIs to existing csv file.

    Args:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.
    """
    existing_df = pd.read_csv("daten/giessdenkiezKPIs.csv", sep=",")

    result = df_adopt.join(df_water)
    timestamp = datetime.now().date()
    result["datestamp"] = timestamp

    # open csv in append mode 'a' to add dataframe to existing csv file
    result.to_csv("daten/giessdenkiezKPIs.csv", mode="a", index=False, header=False)
    logger.info("Data was written to csv-file: daten/giessdenkiez_KPIs.csv")



