#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_14_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities():
    """
    Connects to the MySQL database and fetches all City objects.
    Prints each city's id, name, and state name in the specified format.
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

    # Query all City objects, join with State table to get state names
    cities = (session.query(City, State)
              .join(State, City.state_id == State.id)
              .order_by(City.id)
              .all())

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    fetch_cities()
