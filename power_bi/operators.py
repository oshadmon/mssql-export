import requests
import ast
import pandas

CONN = "http://66.228.59.163:32349"

def get_operators():
    """
    From blockchain get tag and corresponding table name
    """
    get_operators = {}
    headers = {
        "command": "blockchain get operator bring.json [*][name] [*][ip] : [*][port]",
        "User-Agent": "AnyLog/1.23"
    }

    try:
        response = requests.get(url=CONN, headers=headers)
        response.raise_for_status()
    except Exception as error:
        raise Exception

    for row in ast.literal_eval(response.text):
        get_operators[row['name']] = f"{row['ip']}:{row['port']}"

    return pandas.DataFrame(list(get_operators.items()), columns=['name', 'conn'])

if __name__ == '__main__':
    print(get_operators())