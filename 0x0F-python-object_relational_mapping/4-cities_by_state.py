#!/usr/bin/python3
"""Display all cities from the database hbtn_0e_4_usa."""
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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities, \
        states WHERE states.id = cities.state_id;")
    for state in c.fetchall():
        print(state)
