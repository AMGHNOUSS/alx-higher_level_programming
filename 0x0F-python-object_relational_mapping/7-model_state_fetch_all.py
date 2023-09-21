#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
if __name__ == '__main__':
    engine = create_engine(
        'mysql+pymysql://{}:{}@localhost:3306/{}'.format(user, root, bb)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
