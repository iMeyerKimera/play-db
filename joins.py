# -*- coding: utf-8 -*-
# joining data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""
      SELECT population.city, population.population,
      regions.region FROM population, regions
      WHERE population.city = regions.city ORDER BY population.city ASC
    """)

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print

# Take a look at the SELECT statement.
# Since we are using two tables, fields in the SELECT statement must adhere
# to the following format: table_name.column_name (i.e., population.city ).
# In addition, to eliminate duplicates, as both tables include the city name,
# we used the WHERE clause as seen above.
# finally organize the outputted results and clean up the code so it’s more compact