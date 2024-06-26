#!/usr/bin/python3

"""Cities by states"""


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

    query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC"

    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
