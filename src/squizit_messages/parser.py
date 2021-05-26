import json, re
with open('./data/messages.json', 'r') as file:
    data = json.load(file)
    for x in data:
        for y in x:
            print(y)