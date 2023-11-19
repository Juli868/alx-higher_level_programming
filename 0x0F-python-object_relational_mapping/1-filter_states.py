#!/usr/bin/python3
"""Print all states wtih an N on the beginning of  states."""
if __name__ == '__main__':
    import MySQLdb as db
    import sys
    conn = db.connect(
            host='localhost', user=sys.argv[1], port=3306,
            password=sys.argv[2], database=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    result = cursor.fetchall()
    for part in result:
        print(part)
    conn.close()
