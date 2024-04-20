#!/usr/bin/python3

"""All cities by state"""


if __name__ == '__main__':

    import sys
    import MySQLdb

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = conn.cursor()

    que = "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"

    cur.execute(que, [sys.argv[4]])

    query_rows = cur.fetchall()

    print(', '.join(row[0] for row in query_rows))

    cur.close()
    conn.close()
