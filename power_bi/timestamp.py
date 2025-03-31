import requests
import ast
import pandas

CONN = "http://66.228.59.163:32349"

def get_ts():
    """
    From blockchain get tag and corresponding table name
    """
    timestamps = []
    headers = {
        "command": "sql nov format=json and stat=false and include=(t1) select timestamp::ljust(19) as timestamp from t0 group by timestamp",
        "User-Agent": "AnyLog/1.23",
        "destination": "network"
    }

    try:
        response = requests.get(url=CONN, headers=headers, timeout=120)
        response.raise_for_status()
    except Exception as error:
        raise Exception

    for row in ast.literal_eval(response.text)['Query']:
        timestamps.append(row['timestamp'])

    return pandas.DataFrame(timestamps, columns=['timestamp'])

if __name__ == '__main__':
    import time
    start = time.time()
    print(get_ts())
    print(time.time()-start)