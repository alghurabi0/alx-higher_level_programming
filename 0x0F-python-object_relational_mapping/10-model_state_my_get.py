#!/usr/bin/python3
"""Scriptthe name passed as an argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ))
    Base.metadata.create_all(engine)
    Session = Session(bind=engine)

    session = Session()

    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
