import pyodbc
import json

# Define the connection parameters
server = r'localhost\SQLEXPRESS01'  # Use raw string (r'') for backslashes
database = 'LSPPDataLog'  # Database name

# Define the connection string for Windows Authentication
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Fetch all table names in LSPPDataLog database
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    tables = [table.TABLE_NAME for table in cursor.fetchall()]

    # Dictionary to store table data
    db_data = {"database": database, "tables": {}}

    for table in tables:
        query = f"SELECT TOP 5 * FROM [{table}]"  # Fetch first 5 rows
        cursor.execute(query)

        # Fetch column names
        columns = [column[0] for column in cursor.description]

        # Fetch row data and convert to dictionary
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Store in JSON structure
        db_data["tables"][table] = rows

    # Close connection
    cursor.close()
    conn.close()

    # Convert to JSON and print
    json_output = json.dumps(db_data, indent=4)
    print(json_output)

except pyodbc.Error as e:
    print("Error:", e)
