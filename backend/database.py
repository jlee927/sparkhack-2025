#
# Testing file for integrating postgres with python
# Concept that I would be using to manage this is Object-Relational-Mapping (ORM)
#
import objecttier
import psycopg2, os
from dotenv import load_dotenv

load_dotenv()
database, host, username, password, port = (os.getenv(var) for var in ("DATABASE", "HOST", "USERNAME", "PASSWORD", "PORT"))

conn = psycopg2.connect(database=database,
                         host=host,
                         user=username,
                         password=password,
                         port=port,
                         )

cursor = conn.cursor()
questions = objecttier.all_category_questions(conn, "Computer Science")

for q in questions:
    print(q.Question)
