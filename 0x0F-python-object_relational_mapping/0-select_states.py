#!/usr/bin/python3
"""Script to print all info in a table named states."""
if __name__ == '__main__':
    import MySQLdb as db
    conn = db.connect( host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.atgv[3])
    cursor = conn.cursor()
    result = cursor.fetchall('states')
    for part in result:
        print(part)
