#!/usr/bin/python3
"""
This script lists all states with a name matching the provided argument
from the database hbtn_0e_0_usa.
The script takes four arguments: mysql username, mysql password,
database name, and state name searched.
Results are sorted in ascending order by states.id.
This script is safe from SQL injections.
"""

import sys
import MySQLdb


def printStatesMatchingNameSafely():
    """
    Connects to the MySQL database and retrieves all states with a name
    matching the provided argument in ascending order by id.
    Prints each state as a tuple (id, name).
    This function uses parameterized queries to prevent SQL injection.
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

    # Define query to select states with a name matching the argument
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute the query with parameterized input
        cursor.execute(query, (state_name,))

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
    printStatesMatchingNameSafely()
