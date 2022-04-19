#!/usr/bin/python3

"""
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %(state_name)s ORDER BY states.id ASC", {'state_name':sys.argv[4]})

    states = cursor.fetchall()
    for state in states:
        print(state)
