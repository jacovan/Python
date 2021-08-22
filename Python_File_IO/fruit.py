import json
with open('sample.json','r') as sample:
    test = json.load(sample)
    test['fruit'] = 'banana'
    with open ('sampleFruit.json','x') as new:
        json.dump(test,new,indent=4)