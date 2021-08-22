import json
with open('sample.json','r') as sample:
    test = json.load(sample)
    print(test['name'])