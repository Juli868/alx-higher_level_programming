#!/usr/bin/python3
"""Script to print all info in a table named states."""
if __name__ == '__main__':
    import MySQLdb as db
    import sys
    conn = db.connect( host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    print(conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states'
    print(cursor.fetchall())
    conn.close
