#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
The script takes four arguments: mysql username, mysql password,
database name, and state name.
Results are sorted in ascending order by cities.id.
"""

import sys
import MySQLdb


def list_cities_by_state():
    """
    Connects to the MySQL database and retrieves all cities of a given state
    in ascending order by id.
    Prints each city as a comma-separated string.
    """

    # Gather command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)

    # Create cursor object to execute queries
    cursor = db.cursor()

    # Define query to select cities of a given state ordered by id
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    try:
        # Execute the query
        cursor.execute(query, (state_name,))

        # Fetch all rows and print them as comma-separated values
        rows = cursor.fetchall()
        print(", ".join([row[1] for row in rows]))

    except MySQLdb.Error as e:
        print(f"Error executing MySQL query: {e}")
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    list_cities_by_state()
