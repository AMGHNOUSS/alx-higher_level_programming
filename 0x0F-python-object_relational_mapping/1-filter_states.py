#!/usr/bin/python3
"""List all states with a name starting with N from hbtn_0e_0_usa."""
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
    c.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    for state in c.fetchall():
        print(state)
