a = input('Enter some text\n')
b = input('Enter some more text\n')
def combine(a,b):
    combo = " ".join([a,b])
    print (combo)
    return;
if __name__=="__main__":
    combine(a,b);
else:
    print ('__name__ != __main__')