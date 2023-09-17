#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database, port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for state in c.fetchall():
        print(state)