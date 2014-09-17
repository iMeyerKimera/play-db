# aggregating and calculating data returned from a SELECT statement.

#Function    Result
#--------    ------
#AVG()       Returns the average value from a group
#COUNT()     Returns the number of rows from a group
#MAX()       Returns the largest value from a group
#MIN()       Returns the smallest value from a group
#SUM()       Returns the sum of a group of values

# SQLite Functions
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a disctionary of sql queries
    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population"
    }

    # run each sql query item in the dictionary
    for keys, values in sql.iteritems():
        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print keys + ":", result[0]

# Homework
# Add another table to accompany your “inventory” table called “orders”. This table
# should have the following fields: “make”, “model”, and “order_date”. Make sure to
# only include makes and models for the cars found in the inventory table.
# Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD).
# Finally output the car’s make and model on one line, the quantity on another line,
# and then the order_dates on subsequent lines below that.

# Using the COUNT() function, calculate the total number of orders for each make and
# model. Output the car’s make and model on one line, the quantity on
# another line, and then the order count on the next line.
