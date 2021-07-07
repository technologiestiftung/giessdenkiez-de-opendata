import logging
import pandas as pd
from utils.interact_with_db import start_db_connection
from utils.process_data import export_watering_data, export_kpis

# logger configuration
logger = logging.getLogger("root")
FORMAT = "[%(levelname)s %(name)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


logger.info("Starting script: GdK Open Data")

# Connect to the GdK Database, credentials are specified in environment variables
conn = start_db_connection()

# Get watering data from DB and write to files
sql_query = "SELECT t.id, t.lat, t.lng, t.bezirk, t.artdtsch, t.gattungdeutsch, t.strname, t.pflanzjahr, w.time, w.amount FROM trees_watered AS w JOIN trees_new AS t ON w.tree_id=t.id "
df_watering = pd.read_sql_query(sql_query, conn)

export_watering_data(df_watering)

# Get KPI data
sql_query_adopt = "SELECT count(*) AS adoptedTrees, count(DISTINCT tree_id) AS uniqueAdoptedTrees, count(DISTINCT uuid) AS uniqueUsers FROM trees_adopted;"
df_adopt = pd.read_sql_query(sql_query_adopt, conn)

sql_query_water = "SELECT count(*) AS treesWatered, count(DISTINCT tree_id) AS uniqueTreesWatered, count(DISTINCT uuid) AS uniqueWateringUsers, SUM(amount::INTEGER) AS totalWaterAmount FROM trees_watered;"
df_water = pd.read_sql_query(sql_query_water, conn)

export_kpis(df_adopt, df_water)

logger.info("Writting of GdK Open Data was successfull. End of script.")
