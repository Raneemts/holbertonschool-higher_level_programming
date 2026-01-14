#!/usr/bin/python3
"""
Lists all cities of a given state (safe from SQL injection)
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row[0])

    cursor.close()
    db.close()
