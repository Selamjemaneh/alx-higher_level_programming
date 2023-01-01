#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name=BINARY '{}'
            ORDER BY states.id""".format(argv[4]))
    a = c.fetchall()
    for i in a:
        print(i)
