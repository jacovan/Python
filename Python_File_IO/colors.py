import json
with open('sample.json','r') as properties:
    test = json.load(properties)
    for color in test['colors']:
        print(color)