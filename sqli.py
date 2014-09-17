
# INSERT Command

#import sqlite3

#conn = sqlite3.connect("new.db")

#cursor = conn.cursor()

# insert data
#cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")

#cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes
#conn.commit()

# close the datatbase connection
#conn.close()


# above code rewritten using the with keyword
#import sqlite3
#with sqlite3.connect("new.db") as connection:
#    c = connection.cursor()
#    c.execute("INSERT INTO population VALUES('New York City', 'NY',8200000)")
#    c.execute("INSERT INTO population VALUES('San Francisco', 'CA',800000)")

# If you need to run many of the same
# SQL statements you can use the executemany()
# method to save time and eliminate unnecessary code

# executemany() method
#import sqlite3

#with sqlite3.connect("new.db") as connection:
#    c = connection.cursor()

#    # insert multiple records using a tuple
#    cities = [
#        ('Boston', 'MA', 600000),
#        ('Chicago', 'IL', 2700000),
#        ('Houston', 'TX', 2100000),
#        ('Phoenix', 'AZ', 1500000)
#    ]

    # insert data into table
#    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

# Importing data from a CSV file
# In many cases, you may need to insert thousands of records into
# your database, in which case the data is probably contained within
# an external CSV file  or possibly even from a different database.

# import from CSV
# import csv
# import sqlite3

# with sqlite3.connect("new.db") as connection:
    #c = connection.cursor()

    # open the csv file and assign it to a variable
    # employees = csv.reader(open("employees.csv", "rU"))

    # create a new table called employees
    # c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data into table
    # c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

# Try/Except
# Handling errors gracefully

# INSERT Command with Error Handler

import sqlite3

conn = sqlite3.connect("car.db")
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO car VALUES('Ford Mustang', '2007', 800)")
    cursor.execute("INSERT INTO car VALUES('Ford Camero', '2008', 80)")
    cursor.execute("INSERT INTO car VALUES('Ford Bronco', '2010', 20)")
    cursor.execute("INSERT INTO car VALUES('Honda Jazz', '2007', 5000)")
    cursor.execute("INSERT INTO car VALUES('Honda Etra', '2050', 800)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again..."

# close the database connection
conn.close()