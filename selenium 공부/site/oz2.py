import json

with open('server.json') as s:
    json_obj = json.load(s)

print(json_obj)
