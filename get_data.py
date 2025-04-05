import datetime
import random
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from mssql_connector import MSSQL

# Load policies
with open('blockchain.json', 'r') as f:
    policies = json.load(f)

# Database connection details
server = r'localhost\SQLEXPRESS01'
database = 'LSPPDataLog'
mssql = MSSQL(server=server, db_name=database)
mssql.create_connection()

# Target servers (for load balancing)
conns = ['173.255.196.108:32149', '170.187.157.30:32149']

# Date range
start_time = datetime.datetime.strptime('2024-12-16 11:51:49.000', "%Y-%m-%d %H:%M:%S.%f")
end_time = datetime.datetime.strptime('2025-03-27 09:00:27.000', "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(hours=1)

# Configurations
BATCH_SIZE = 100
MAX_RETRIES = 3


def send_request(conn, headers, batch, data):
    """Send batch data with retries."""
    url = f"http://{conn}"
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.put(url, headers=headers, data=json.dumps(batch))
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}, Retrying {attempt + 1}/{MAX_RETRIES}")
    # Log failed batch
    with open(f"{data}.0.json", 'a') as f:
        f.write(json.dumps(batch) + ",\n")
    return False


def store_data(data_set):
    """Processes and sends data in parallel batches."""
    with ThreadPoolExecutor(max_workers=len(conns)) as executor:
        futures = []
        last_conn = None

        for data in data_set:
            conn = last_conn
            while conn == last_conn:  # Ensure no two consecutive requests go to the same connection
                conn = random.choice(conns)
            last_conn = conn  # Update last connection used

            dbms, table = data.split(".")
            headers = {
                'type': 'json',
                'dbms': dbms,
                'table': table,
                'mode': "streaming",
                'Content-Type': 'text/plain',
                "User-Agent": "AnyLog/1.23"
            }

            # Process in batches
            for i in range(0, len(data_set[data]), BATCH_SIZE):
                batch = data_set[data][i:i + BATCH_SIZE]
                futures.append(executor.submit(send_request, conn, headers, batch, data))

        # Wait for all requests to complete
        for future in as_completed(futures):
            future.result()  # Ensure all requests complete before moving to next batch


while start_time <= end_time:
    new_end_time = start_time + datetime.timedelta(days=1)

    # Fetch data from MSSQL
    start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
    new_end_time_str = new_end_time.strftime('%Y-%m-%d %H:%M:%S')
    query = f"SELECT * FROM [FloatTable] WHERE [DateAndTime] >= '{start_time_str}' AND [DateAndTime] <= '{new_end_time_str}' ORDER BY [DateAndTime]"

    rows = mssql.execute_select(query=query)
    publish_data = {}

    # Process rows
    for row in rows:
        table_name = None
        dbms = None
        for policy in policies:
            if row['TagIndex'] == policy['tag']['index']:
                table_name = policy['tag']['table']
                dbms = policy['tag']['dbms']
                break

        if not table_name or not dbms:
            continue  # Skip if no matching policy

        key = f"{dbms}.{table_name}"
        if key not in publish_data:
            publish_data[key] = []

        row['timestamp'] = row.pop('DateAndTime').strftime('%Y-%m-%d %H:%M:%S')
        row.pop('TagIndex')

        publish_data[key].append(row)

    if publish_data:
        store_data(publish_data)  # Send data in parallel

    start_time = new_end_time  # Move to the next batch

mssql.disconnect()
