import pandas as pd
import sqlite3

# leer consulta de sqlite y ponerla en un df de pandas
con = sqlite3.connect("mediciones.db")
df = pd.read_sql_query("SELECT * from nvo_reg", con)

# mostramos el resultado
print(df.head())

con.close()