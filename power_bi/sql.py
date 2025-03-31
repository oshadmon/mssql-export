import requests
import pandas as pd

CONN = "http://66.228.59.163:32349"

def basic_query(tables:list, destination:str='network', start_ts:str=None, end_ts:str=None, limit:int=0):
    base_table = tables.pop(0)
    query = "sql nov format=json and stat=false"
    if tables:
        query += f" and include=({','.join(tables)}) and extend=(@table_name) "


    query += f" select timestamp::ljust(19) as timestamp, millitm, status, marker, val::float(3) as val from {base_table}"
    if start_ts or end_ts:
        query += " where "
        if start_ts:
            query += f" timestamp >= '{start_ts}' and"
        if end_ts:
            query += f" timestamp <= '{end_ts}' and"

        query = query.rsplit(' and', 1)[0] + f" ORDER BY timestamp"
        if limit > 0:
            query += f" limit {limit}"

    headers = {
        "command": query,
        "User-Agent": "AnyLog/1.23",
        "destination": destination
    }

    try:
        response = requests.get(url=CONN, headers=headers, timeout=300)
        response.raise_for_status()
        data = response.json().get('Query', [])
        if not data:
            return pd.DataFrame()  # Return an empty DataFrame if no data
    except Exception as error:
        raise Exception(f"Error fetching data: {error}")

    return pd.DataFrame(data)  # Convert JSON data to DataFrame



# params should be based on user input from within PowerBI
tables = []
for i in range(28, 40):
    tables.append(f't{i}')
raw_data = basic_query(tables=tables, destination='network', start_ts='2025-02-02 00:00:00', end_ts='2025-02-05 23:59:59')
print(raw_data)