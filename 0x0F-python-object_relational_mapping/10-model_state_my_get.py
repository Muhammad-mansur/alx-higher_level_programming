#!/usr/bin/python3

"""Get a state"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
    )

    # Create session
    session = sessionmaker(bind=engine)
    session = session()

    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)

    else:
        print("Not found")

    session.close()
