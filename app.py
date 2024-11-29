import psycopg2  # Import the psycopg2 library for working with PostgreSQL
from psycopg2 import Error  # Import the Error class for error handling

# Try-except block for handling errors during database interaction
try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        user="user",  # Username for accessing the database
        password="user_password",  # User password
        host="database",  # Host where the database is located
        port="5432",  # Port for connecting to the database
        database="db"  # Name of the database
    )

    # Create a cursor for executing SQL queries
    cursor = connection.cursor()

    # Query to select all data from the "employees" table
    query_select = "SELECT * FROM employees"

    # Execute the query
    cursor.execute(query_select)

    # Retrieve all results of the query as a list of tuples
    result = cursor.fetchall()

    # Print the data from the table to the screen
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    # Close the cursor
    cursor.close()

    # Commit changes to the database
    connection.commit()

    # Close the connection to the database
    connection.close()

# Exception handling
except (Exception, Error) as error:
    print("An error occurred while interacting with PostgreSQL: ", error)

    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    cursor.close()
    connection.commit()
    connection.close()

except (Exception, Error) as error:
    print("An error occurred while interacting with PostgreSQL:", error)

