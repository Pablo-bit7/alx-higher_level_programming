#!/usr/bin/python3
import os

os.environ['SQLALCHEMY_WARN_20'] = '1'

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    # Gather command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind it to the session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print((state.id, state.name))

    # Close session
    session.close()
