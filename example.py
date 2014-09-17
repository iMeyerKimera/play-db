# In this application we will be performing aggregations on 100 integers.
# Add 100 random integers, ranging from 0 to 100, to a new database called newnum.db .
# Prompt the user whether he or she would like to perform an
# aggregation (AVG, MAX, MIN, or SUM) or exit the program altogether.

# Import libraries (we need the random library because of the random variable piece)
import sqlite3
import random

# Establish connection and create newnum.db database
with sqlite3.connect("example.db") as connection:
    # open the cursor
    c = connection.cursor()

    # create table, "numbers", with value "num" as an integer
    # (the DROP TABLE command will remove the entire table if it exists so we can create a new one)
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int )")

    # Use for loop random function to insert 100 random values (0 to 100)
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100), ))