#!/usr/bin/python3
"""Execute sql queries using MySQLdb."""

import MySQLdb
import sys


def run():
    """Begin execution!"""
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    stateName = sys.argv[4]
    db = MySQLdb.Connect(host='localhost', user=user, passwd=password, db=database)
    cursor = db.cursor()

    # Execute command
    query = r"SELECT * FROM states WHERE states.name LIKE '{}' ORDER BY states.id".format(stateName)
    cursor.execute(query)

    # show results
    for row in cursor.fetchall():
        print(row)

    # clean up
    cursor.close()


if __name__ == '__main__':
    run()
