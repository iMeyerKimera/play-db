# Create a SQLite3 database and table

import sqlite3

# create a new database if the database doesnt already exist
conn = sqlite3.connect("car.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute(
    """CREATE TABLE car(Make TEXT, Model TEXT, Quantity INT)

    """)

# close the database connection
conn.close()