import logging
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


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

    print(conn_string)

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
    sql_query = "SELECT count(*) AS adoptedTees FROM trees_adopted; \
        SELECT count(DISTINCT tree_id) AS uniqueAdoptedTrees FROM trees_adopted; \
        SELECT count(DISTINCT uuid) AS uniqueUsers FROM trees_adopted; \
        SELECT count(*) AS treesWatered FROM trees_watered; \
        SELECT count(DISTINCT tree_id) AS uniqueTreesWatered FROM trees_watered; \
        SELECT count(DISTINCT uuid) AS uniqueWateringUsers FROM trees_watered; \
        SELECT SUM (amount::INTEGER) AS total from trees_watered;"

    # import data and create dataframe
    df = pd.read_sql_query(sql_query, conn)

    print(df)

    # switch longitude and latitude columns, because they are named wrong
    # df = df.rename(
    #     columns={
    #         "lat": "lng",
    #         "lng": "lat",
    #         "amount": "bewaesserungsmenge_in_liter",
    #         "time": "zeitpunkt_der_bewaesserung",
    #         "artdtsch": "baumart",
    #         "gattungdeutsch": "gattung",
    #     }
    # )
    return df


def data_to_files(df):
    """Write data about watered trees and information about trees to csv and geojson files.

    Args:
        watered_trees_df: (DataFrame): Watering and tree data that is currently stored in the database.
        watered_trees_gdf: (GeoDataFrame): Watering and tree data that is currently stored in the database with geometry.
    """

    # set path were files should be written  to
    file_path = "daten/giessdenkiez_KPIs"
    timestamp = datetime.now()

    # save as csv file
    df.to_csv(file_path + ".csv", index=False, sep=";")
    logger.info(
        "Data was written to csv-file " + file_path + ".csv" + " at " + str(timestamp)
    )
