#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

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

    # Define the query to select all states ordered by id
    query = "SELECT * FROM states ORDER BY id ASC"

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

