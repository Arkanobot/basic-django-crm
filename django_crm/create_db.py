import psycopg
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

#connect to db
database = psycopg.connect(f"host={db_host} dbname={db_name} user={db_user} password={db_password}")

#enable autocommit mode to create new db
database.autocommit = True

#prepare a cursor
cursor = database.cursor()

#create a new db
cursor.execute("CREATE DATABASE django_crm");
print("database created!")

#close the cursor and database
cursor.close()
database.close()