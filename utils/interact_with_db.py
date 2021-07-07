import logging
import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def start_db_connection():
    """Loads database parameters from a .env-file and concects to the database.

    Raises:
        Exception: Connecting to the database was not successfull.

    Returns:
        class 'sqlalchemy.engine.base.Engine': The engine object for connecting to the database.
    """

    # load database parameters from .env
    load_dotenv()

    logger.info("Starting db connection...")
    # check if all required environmental variables are accessible
    for env_var in ["PG_DB", "PG_PORT", "PG_USER", "PG_PASS", "PG_SERVER"]:
        if env_var not in os.environ:
            logger.error("❌Environmental Variable {} does not exist".format(env_var))
    # declare variables for database parameters
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