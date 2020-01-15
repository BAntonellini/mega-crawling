import sqlite3
import pandas as pd

dbname = "mega_cuits"
conn = sqlite3.connect(dbname + '.sqlite')

# dataframe
df = pd.read_excel('cuits.xlsx')
df.to_sql(name="cuits_existent", con=conn)