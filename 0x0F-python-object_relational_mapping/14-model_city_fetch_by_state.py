#!/usr/bin/python3

""" Cities in state"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    cities = session.query(State, City).join(City).order_by(City.id).all()

    # Iterate and print results
    for state, city in cities:
        print("{}: {} {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
