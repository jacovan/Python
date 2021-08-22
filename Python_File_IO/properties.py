import json
with open('sample.json','r') as properties:
    test = json.load(properties)
    for key in test:
        print(key)