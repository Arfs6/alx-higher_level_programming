#!/usr/bin/python3
"""Execute sql queries using MySQLdb."""

import MySQLdb
import sys


def run():
    """Begin execution!"""
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    stateName = sys.argv[4]
    db = MySQLdb.Connect(
            host='localhost', user=user, passwd=password, db=database)
    cursor = db.cursor()

    # Execute command
    query = "SELECT cities.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE BINARY states.name LIKE ('{}')\
            ORDER BY cities.id\
            ".format(stateName)
    cursor.execute(query)

    # show results
    results = cursor.fetchall()
    resultsStr = ''
    for idx, row in enumerate(results):
        if idx > 0:
            resultsStr += ', '
        resultsStr += row[0]

    print(resultsStr)

    # clean up
    cursor.close()


if __name__ == '__main__':
    run()
