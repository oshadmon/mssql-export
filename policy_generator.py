import json
import requests

from mssql_get_data import MSSQL

server = r'localhost\SQLEXPRESS01'  # Use raw string (r'') for backslashes
database = 'LSPPDataLog'  # Database name

dataset = {}

mssql = MSSQL(server=server, db_name=database)

mssql.create_connection()

rows = mssql.execute_select(query=f"SELECT * FROM TagTable;")

mssql.disconnect()
policies = []

for row in rows:
    # root, values = row['TagName'].split("GlobalVars")
    tagindex = row['TagIndex']
    # _, section, table_name = values.split("\\")
    raw_policy = {
        "tag": {
            "path": row['TagName'].split("/",1)[-1].replace("\\", "/"),
            "dbms": "nov",
            "table": f"t{tagindex}",
            "index": tagindex,
            "type": row['TagType'],
            "data_type": row['TagDataType']
        }
    }

    new_policy=f"<new_policy={json.dumps(raw_policy)}>"
    headers = {
        "command": "blockchain insert where policy=!new_policy and local=true and master=!ledger_conn",
        "User-Agent": "AnyLog/1.23"
    }
    # try:
    #     response = requests.post(url="http://104.237.138.113:32049", headers=headers, data=new_policy)
    #     response.raise_for_status()
    # except Exception as error:
    #     print(new_policy)
    #     raise Exception

    policies.append(raw_policy)


with open('blockchain.json', 'w') as f:
    f.write(json.dumps(policies))

