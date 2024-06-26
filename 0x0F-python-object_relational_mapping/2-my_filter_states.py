#!/usr/bin/python3

"""Filter states by user input"""


if __name__ == '__main__':

    import MySQLdb
    import sys

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states\
        WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
