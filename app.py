import pyodbc
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World Felix!</p>"

print("YES")

# Verbindingsinstellingen
server = 'datadbserverdamen.database.windows.net'
database = 'staging_elony'
username = 'admindamen'
password = 'uiop7890UIOP&*()'
driver = '{ODBC Driver 17 for SQL Server}'

# Verbind met de database
try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM tweet_elon_musk")  # Pas de query aan
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print("Fout bij verbinden:", e)

