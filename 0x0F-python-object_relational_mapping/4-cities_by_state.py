#!/usr/bin/python3
"""Join two tables."""
import sys
import MySQLdb as db
if __name__ == '__main__':
    conn = db.connect(
            host='localhost', user=sys.argv[1], port=3306,
            password=sys.argv[2], database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON states.id=cities.state_id
            ORDER BY cities.id ASC""")
    result = cursor.fetchall()
    for part in result:
        print(part)
    conn.close()
