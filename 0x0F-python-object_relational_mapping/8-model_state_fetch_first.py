#!/usr/bin/python3

"""Model state"""


import sys
from model_state import Base, State
from sqlalchemy import session
from sqlalchemy import create_engine

# Create engine
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost:3306/{}'
    .format(sys.argv[1], sys.argv[2], sys.argv[3])
)

Base.metadata.create_all(engine)

# Create session
session = session(engine)

state = session.query(State).order_by(State.id).first()

if state:
    print('{}: {}'.format(state.id, state.name))
    
else:
    print('Nothing')
    
# Close session
session.close()