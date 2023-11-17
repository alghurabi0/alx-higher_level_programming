#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


def list_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        # Create a cursor object to execute queries
        cur = db.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the rows as a tuple of tuples
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract username, password, and database from command line arguments
    username, password, database = sys.argv[1:]

    # Call the list_states function with provided arguments
    list_states(username, password, database)
