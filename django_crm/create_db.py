import psycopg

#connect to db
database = psycopg.connect("host=localhost dbname=postgres user=postgres password=1")

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