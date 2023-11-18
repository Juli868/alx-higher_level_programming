#!/usr/bin/python3
"""Script to print all info in a table named states."""
if __name__ == '__main__':
    import MySQLdb as db
    import sys
    conn = db.connect( host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states')
    result = cursor.fetchall()
    for part in result:
        print(part)
    conn.close
