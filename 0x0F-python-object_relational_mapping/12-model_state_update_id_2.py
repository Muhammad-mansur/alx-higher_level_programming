#!/usr/bin/python3

"""Update a state"""


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

    state = session.query(State).filter(id='2').first()
    # Update the name of id=2 to "New Mexico"
    state.name = "New Mexico"

    # Commit changes
    session.commit()

    # Close session
    session.close()