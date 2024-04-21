#!/usr/bin/python3

"""Delete states"""


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

    states = session.query(State).filter(state.name.like('%a')).all()

    # If name containing letter the 'a' is present, delete it
    for state in states:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()
