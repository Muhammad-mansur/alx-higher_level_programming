#!/usr/bin/python3

"""All states via SQLAlchemy"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )

    Base.metadata.create_all(engine)

    # Create session
    Session = Session(engine)

    # Query for all state objects
    states = Session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    Session.close()
