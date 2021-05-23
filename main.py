from flask import Flask, request, redirect, url_for
from flask import render_template
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"bd/database.db")
df = pd.read_sql("select * from dados_diarios_btc_brl", conn)

app = Flask(__name__)


@app.route('/dados')
def dados_btc():
    return df.to_json(orient='records')


app.run(debug=True)
