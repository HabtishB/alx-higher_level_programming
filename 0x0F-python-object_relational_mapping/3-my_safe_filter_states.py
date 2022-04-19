#!/usr/bin/python3
"""
This script is also the same as the first one that takes in arguments
and displays all values in the states of table hbtn_0e_0_usa where
the names matches the argument. But this script is safe from MySQL
injection becauase of the bound paramaters.
It takes four arguments, username, password, dbname and statename
(The searched paramater)
The script connects to the MySQL database server on localhost at
port 3306
Results are displayed on ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name = %(state_name)s\
                   ORDER BY states.id ASC", {'state_name': sys.argv[4]})

    states = cursor.fetchall()
    for state in states:
        print(state)
