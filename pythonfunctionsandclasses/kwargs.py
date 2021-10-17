list = {'a':'1','b':'2','c':'3',}
def test(**kwargs):
    for key in list:
        print(key + ' = ' + list[key])
test()