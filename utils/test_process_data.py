import pandas as pd
import os
from process_data import export_watering_data, export_kpis
from interact_with_db import start_db_connection

conn = start_db_connection()

# Get watering data from DB and write to files
sql_query = "SELECT t.id, t.lat, t.lng, t.bezirk, t.artdtsch, t.gattungdeutsch, t.strname, t.pflanzjahr, w.time, w.amount FROM trees_watered AS w JOIN trees AS t ON w.tree_id=t.id "


def test_export_watering_data(tmpdir):
    df_watering = pd.read_sql_query(sql_query, conn)
    export_watering_data(df_watering,  str(tmpdir.join("out")))
    assert os.path.exists(tmpdir.join("out.csv"))
    assert os.path.exists(tmpdir.join("out.geojson"))
