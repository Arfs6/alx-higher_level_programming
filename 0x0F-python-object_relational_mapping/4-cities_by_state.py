#!/usr/bin/python3
"""Execute sql queries using MySQLdb."""

import MySQLdb
import sys


def run():
    """Begin execution!"""
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.Connect(
            host='localhost', user=user, passwd=password, db=database)
    cursor = db.cursor()

    # Execute command
    query = "SELECT cities.id, cities.name, states.name AS state_name\
            FROM cities\
            JOIN states on cities.state_id = states.id \
            ORDER BY cities.id"
    cursor.execute(query)

    # show results
    for row in cursor.fetchall():
        print(row)

    # clean up
    cursor.close()


if __name__ == '__main__':
    run()
