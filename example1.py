# Using an infinite loop, continue to ask the user to enter the number of an
# operation that they’d like to perform. If they enter a number associated
# with a SQL function, then run that function. However, if they enter
# number not associated with a function, ask them
# to enter another number. If they enter the number 5, exit the program.

# prompt the user

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("example.db")

cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until user enters a valid operation number [1-5]
while True:
    # get user input
    x = raw_input(prompt)

    # if user enters any choice from 1-4
    if x in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

        # retrieve data
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        # fetchone() retrieves one record from the query
        get = cursor.fetchone()

        # output result to screen
        print operation + ": %f" % get[0]

    # if user enters 5
    elif x == "5":
        print "Exit"

        # exit loop
        break

# We asked the user to enter the operation they would like to perform
# (numbers 1-4), which queried the database and displayed either the average,
# minimum, maximum or sum (depending on the operation chosen).
# The loop continues forever until the user chooses 5 to break the loop.