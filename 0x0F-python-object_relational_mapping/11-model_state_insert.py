#!/usr/bin/python3

"""Add a new state"""


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

    # Create new state
    new_state = State(name="Louisiana")

    # Use session.add to add the new state
    session.add(new_state)

    # Commit new_state
    session.commit()

    # Print new state id
    print(new_state.id)

    # Close session
    session.close()