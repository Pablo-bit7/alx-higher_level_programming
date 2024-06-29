#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Connects to the MySQL database and deletes all State objects
    with a name containing the letter 'a'.
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

    # Query all State objects with a name containing 'a'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete each State object found
    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    delete_states_with_a()
