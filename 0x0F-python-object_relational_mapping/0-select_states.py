#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
It takes 3 arguments: username, password and database
It runs on localhost port 3306, and the results muus be ordered in 
ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    states = cursor.fetchall()
    for state in states:
        print(state)
