import requests

count = 0
for i in range(0, 103):
    if i % 10 == 0:
        print(i, count)
    try:
        response = requests.get(url="http://66.228.59.163:32349", headers={"command": f"sql nov select count(*) from t{i}",
                                                                       "User-Agent": "AnyLog/1.23",
                                                                       "destination": "network"})
        count += int(response.json()['Query'][0]['count(*)'])
    except:
        print(i)
print(count)