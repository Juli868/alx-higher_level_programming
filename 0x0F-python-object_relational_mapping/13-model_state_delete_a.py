#!/usr/bin/python3
"""Delete data from a table."""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for delete in session.query(State).filter(State.name.like('%a%')):
        session.delete(delete)
    session.commit()
