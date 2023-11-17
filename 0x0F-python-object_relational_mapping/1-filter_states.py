#!/usr/bin/python3
"""
Script that le starting with N from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Lists all stame starting with N from the database hbtn_0e_0_usa.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    filter_states(username, password, database)
