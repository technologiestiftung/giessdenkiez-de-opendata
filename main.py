import logging
from utils.interact_with_db import start_db_connection
from utils.get_watering_data import read_watering_data, data_to_files

# logger configuration
logger = logging.getLogger('root')
FORMAT = "[%(levelname)s %(name)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


logger.info("Starting script: GdK Open Data")

# Connect to the GdK Database, credentials are specified in environment variables
conn = start_db_connection()

watered_trees_df, watered_trees_gdf = read_watering_data(conn)
data_to_files(watered_trees_df,watered_trees_gdf)