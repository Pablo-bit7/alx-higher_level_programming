#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa using SQLAlchemy ORM.
The script takes three arguments: mysql username, mysql password,
and database name.
Results are sorted in ascending order by states.id.
"""

import sys
import warnings
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """
    State class mapped to the states table in the database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)


def printStatesStartingWithN(username, password, database_name):
    """
    Connects to the MySQL database using SQLAlchemy ORM and retrieves all states
    with a name starting with 'N' in ascending order by id.
    Prints each state as a tuple (id, name).
    """
    # Suppress deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Create a new SQLAlchemy engine instance
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database for states with names starting with 'N'
    states = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()

    # Print the states
    for state in states:
        print((state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    printStatesStartingWithN(username, password, database_name)
