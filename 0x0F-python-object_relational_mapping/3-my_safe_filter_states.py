#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys


def safe_filter_states(username, password, database, state_name):
    """
    Displays all values in the states table where name matches the argument.
    Uses parameterized query to prevent SQL injection.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        cur = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

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
        print("Usage: {} <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    safe_filter_states(username, password, database, state_name)
