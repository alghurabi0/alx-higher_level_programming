#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a given state from the database hbtn_0e_4_usa.
    Uses parameterized query to prevent SQL injection.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        cur = db.cursor()

        query = """
            SELECT GROUP_CONCAT(cities.name
            ORDER BY cities.id ASC SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
        """
        cur.execute(query, (state_name,))

        result = cur.fetchone()

        if result and result[0]:
            print(result[0])
        else:
            print()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <usernaabase> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    filter_cities_by_state(username, password, database, state_name)
