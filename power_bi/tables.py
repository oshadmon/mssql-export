import requests
import ast
import pandas

CONN = "http://66.228.59.163:32349"

def get_tables():
    """
    From blockchain get tag and corresponding table name
    """
    tags = {}
    headers = {
        "command": "blockchain get tag bring.json [*][path] [*][table]",
        "User-Agent": "AnyLog/1.23"
    }

    try:
        response = requests.get(url=CONN, headers=headers)
        response.raise_for_status()
    except Exception as error:
        raise Exception

    for row in ast.literal_eval(response.text):
        tags[row['path'].split("GlobalVars/")[-1]] = row['table']

    return pandas.DataFrame(list(tags.items()), columns=['Tag', 'Table'])

if __name__ == '__main__':
    print(get_tables())