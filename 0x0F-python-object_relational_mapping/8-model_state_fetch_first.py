#!/usr/bin/python3

"""Model state"""


import sys
from model_state import Base, State
from sqlalchemy.orm import Sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3])
    )

    Base.metadata.create_all(engine)

    # Create session
    Session = Sessionmaker(bind=engine)
    Session = Session()

    state = Session.query(State).order_by(State.id).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    
    else:
        print("Nothing")
    
    # Close session
    Session.close()