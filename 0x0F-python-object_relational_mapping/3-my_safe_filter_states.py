#!/usr/bin/python3
"""Safe from sql injections."""
import sys
import MySQLdb as db
if __name__ == '__main__':
    con = db.connect(
            host='localhost', user=sys.argv[1], port=3306,
            password=sys.argv[2], database=sys.argv[3])
    cursor = con.cursor()
    cursor.execute('SELECT * FROM states WHERE name LIKE %s', (sys.argv[4],))
    result = cursor.fetchall()
    for part in result:
        print(part)
    con.close()
