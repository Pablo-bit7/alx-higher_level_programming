#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """
    Connects to the MySQL database, retrieves the first State object,
    and prints it. If the table is empty, prints 'Nothing'.
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

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    fetch_first_state()
