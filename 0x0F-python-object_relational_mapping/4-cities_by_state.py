#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
Results are sorted in ascending order by cities.id.
"""

import sys
import MySQLdb


def printAllCities():
    """
    Connects to the MySQL database and retrieves all cities
    in ascending order by id.
    Prints each city as a tuple (id, name, state_name).
    """

    # Gather command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Define query to select cities with state names ordered by cities.id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error executing MySQL query: {e}")
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    printAllCities()
