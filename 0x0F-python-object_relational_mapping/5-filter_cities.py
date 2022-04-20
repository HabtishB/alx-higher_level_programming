#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
It takes four arguments, username, password, dbname and statename
(The searched paramater)
The script connects to the MySQL database server on localhost at
port 3306
Results are displayed in ascending order by cities.id
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states\
                    INNER JOIN cities ON states.id = cities.state_id\
                    WHERE states.name like %s\
                    ORDER BY cities.id ASC", (argv[4],))

    cities = cursor.fetchall()

    print(",".join([city[0] for city in cities]))
    cursor.close()
    db.close()
