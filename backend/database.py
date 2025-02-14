#
# Testing file for integrating postgres with python
# Concept that I would be using to manage this is Object-Relational-Mapping (ORM)
#

import psycopg2, os
from dotenv import load_dotenv

load_dotenv()
database = os.getenv("DATABASE")
host = os.getenv("HOST")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

conn = psycopg2.connect(database=database,
                         host=host,
                         user=username,
                         password=password,
                         port=port,
                         )

cursor = conn.cursor()
cursor.execute("SELECT * FROM Question")
print(cursor.fetchall())


