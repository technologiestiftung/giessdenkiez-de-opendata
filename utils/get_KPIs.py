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

existing_df = pd.read_csv("daten/giessdenkiezKPIs.csv", sep=",")


def start_db_connection():
    """Loads database parameters from a .env-file and concects to the database.yy

    Raises:
        Exception: Connecting to the database was not successfull.

    Returns:
        class 'sqlalchemy.engine.base.Engine': The engine object for connecting to the database.
    """
    # load database parameters from .env
    load_dotenv()
    # check if all required environmental variables are accessible
    for env_var in ["PG_DB", "PG_PORT", "PG_USER", "PG_PASS", "PG_SERVER"]:
        if env_var not in os.environ:
            logger.error("❌ Environmental Variable {} does not exist".format(env_var))
    pg_server = os.getenv("PG_SERVER")
    pg_port = os.getenv("PG_PORT")
    pg_username = os.getenv("PG_USER")
    pg_password = os.getenv("PG_PASS")
    pg_database = os.getenv("PG_DB")

    # create databse connection url from variables
    conn_string = (
        "postgresql://"
        + pg_username
        + ":"
        + pg_password
        + "@"
        + pg_server
        + ":"
        + pg_port
        + "/"
        + pg_database
    )
    # connect to the database
    conn = create_engine(conn_string)

    try:
        conn.connect()
        logger.info("🗄  Database connection established")

        return conn
    # stop script if connection to database was not succesfull
    except:
        msg = f"❌ Could not establish a database connection to {conn_string}"
        logger.error(msg)
        raise Exception(msg)


def read_db_data(conn):
    """Load data about watered trees and information about trees from the database to a dataframe and to a geodataframe.

    Args:
        conn (class 'sqlalchemy.engine.base.Engine'): The engine object for connecting to the database.

    Returns:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.
    """

    # create query for selecting the data
    sql_query_adopt = "SELECT count(*) AS adoptedTrees, count(DISTINCT tree_id) AS uniqueAdoptedTrees, count(DISTINCT uuid) AS uniqueUsers FROM trees_adopted;"
    sql_query_water = "SELECT count(*) AS treesWatered, count(DISTINCT tree_id) AS uniqueTreesWatered, count(DISTINCT uuid) AS uniqueWateringUsers, SUM(amount::INTEGER) AS totalWaterAmount FROM trees_watered;"

    df_adopt = pd.read_sql_query(sql_query_adopt, conn)
    df_water = pd.read_sql_query(sql_query_water, conn)

    # create dataframe from sql values
    result = df_adopt.join(df_water)
    timestamp = datetime.now().date()
    result["datestamp"] = timestamp

    return result


def data_to_files(result):
    """Write data about watered trees and information about trees to csv and geojson files.

    Args:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.
    """

    # open csv in append mode 'a' to add dataframe to existing csv file
    result.to_csv("daten/giessdenkiezKPIs.csv", mode="a", index=False, header=False)
    logger.info("Data was written to csv-file: daten/giessdenkiez_KPIs.csv")


conn = start_db_connection()
result = read_db_data(conn)
data_to_files(result)
