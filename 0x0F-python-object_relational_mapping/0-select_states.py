#!/usr/bin/python3

""" Get all states """


if __name__ = '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
        host="locahost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()