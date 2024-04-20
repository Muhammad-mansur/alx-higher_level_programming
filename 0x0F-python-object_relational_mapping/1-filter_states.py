#!/usr/bin/python3

"""1. Filter states"""


if __name__ == '__main__':

    import MySQLdb
    import sys

    """ connect to MySQL server """
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    """ create a cursor object """
    cur = conn.cursor()

    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    """ fetch all rows """
    rows = cur.fetchall()

    """ iterate through each row and display results """
    for row in rows:
        print(row)

    """ close the cursor """
    cur.close()

    """ close server connection """
    conn.close()
