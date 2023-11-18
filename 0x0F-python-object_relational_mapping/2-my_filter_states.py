#!/usr/bin/python3
"""Print reuslt based on the user info."""
if __name__ == '__main__':
    import MySQLdb as db
    import sys

    conn = db.connect(
            host='localhost', user=sys.argv[1], port=3306
            password=sys.argv[2], database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE'{}'".format(sys.argv[4]))
    res = cursor.fetchall()
    for result in res:
        print(result)
    conn.close()
