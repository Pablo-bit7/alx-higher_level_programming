#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state():
    """
    Connects to the MySQL database, adds a new State object with
    the name "Louisiana", and prints the new state's id.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add new State object to session and commit to database
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()


if __name__ == "__main__":
    add_state()
