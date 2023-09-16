#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database, localhost= 3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()
