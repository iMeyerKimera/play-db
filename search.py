# SELECT statement
#import sqlite3

#with sqlite3.connect("new.db") as connection:
#    c = connection.cursor()

    # use a for loop to iterate through
    # the database, printing the results line by line
#    for row in c.execute("SELECT firstname, lastname from employees"):
#        print row

# output the data with just the values by
# removing the unicode characters altogether:
import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()

    c.execute("SELECT Model, Make, Quantity from car")

    # c.execute("SELECT Quantity from car WHERE Make = 'Ford' ")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2]
