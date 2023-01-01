#!/usr/bin/python3
"""
sort with ascending order
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id""")
    a = c.fetchall()
    for i in a:
        print(i)
