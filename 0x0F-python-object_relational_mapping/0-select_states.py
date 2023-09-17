#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], 
                        db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for state in c.fetchall():
        print(state)