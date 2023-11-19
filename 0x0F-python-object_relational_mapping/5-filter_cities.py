#!/usr/bin/python3
"""Join two tables."""
import sys
import MySQLdb as db
if __name__ == '__main__':
    conn = db.connect(
            host='localhost', user=sys.argv[1], port=3306,
            password=sys.argv[2], database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s ORDER BY cities.id ASC""", (sys.argv[4],))
    result = cursor.fetchall()
    tmp = [row[0] for row in result]
    print(*tmp, sep=',')
    conn.close()
