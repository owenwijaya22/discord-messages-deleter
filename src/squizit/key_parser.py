import json, re
from nltk import flatten
def parse():
    with open('./data/messages.json', 'r') as file:
        data = flatten(json.load(file))
        keys = re.findall(r'`(\w*)`', " ".join(data))
        with open('./data/keys.json', 'w') as file:
            json.dump((keys), file)