#!/usr/bin/python3
"""Display all values in the states table where name matches the argument."""
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name = `{}`".format(sys.argv[4]))
    for state in c.fetchall():
        print(state)
