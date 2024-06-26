#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.
The script takes three arguments: mysql username, mysql password,
and database name.
Results are sorted in ascending order by states.id.
"""

import sys
import MySQLdb


def printStatesStartingWithN():
    """
    Connects to the MySQL database and retrieves all states with a name
    starting with 'N' in ascending order by id.
    Prints each state as a tuple (id, name).
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

    # Define the query; select states with names ('N') ordered by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

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
    printStatesStartingWithN()
