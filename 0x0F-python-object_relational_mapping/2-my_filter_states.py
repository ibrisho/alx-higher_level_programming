#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>

"""
2-my_filter_states.py
"""
import MySQLdb
import sys


def init_db():
    """initializes a db with MySQLdb"""
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    return db


def print_one_state(db):
    """prints one state from input DB"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '%{}%' "
                "ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_one_state(init_db())
