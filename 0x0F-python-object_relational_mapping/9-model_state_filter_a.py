#!/usr/bin/python3

"""Filter"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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
    
    # Query for state objects containing the letter 'a'
    states_a = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()
    
    for state in states_a:
        print('{}: {}'.format(state.id, state.name))

    # Close session
    session.close()