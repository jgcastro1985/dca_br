import pandas as pd
import sqlite3


df = pd.read_csv(r'bd/BTC_BRL_MercadoBTC.csv')
conn = sqlite3.connect(r"bd/database.db")

df.to_sql("dados_diarios_btc_brl", if_exists='append', con=conn)

conn.close()
