import logging
from get_trees_watered import start_db_connection, read_db_data, data_to_files


# logger configuration
logger = logging.getLogger('root')
FORMAT = "[%(levelname)s %(name)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

print("Hello Open Data World")


#conn = start_db_connection()
#watered_trees_df, watered_trees_gdf = read_db_data(conn)
#data_to_files(watered_trees_df,watered_trees_gdf)