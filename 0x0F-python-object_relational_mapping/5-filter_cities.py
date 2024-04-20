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
    
    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC")
    
    row = cur.fetchall()
    
    for rows in r