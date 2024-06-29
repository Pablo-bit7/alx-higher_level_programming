#!/usr/bin/python3
"""
This script changes the name of a State object from the
database hbtn_0e_6_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state():
    """
    Connects to the MySQL database, updates the State object with id = 2
    to have the name "New Mexico".
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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update name of State object and commit change to database
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    update_state()
