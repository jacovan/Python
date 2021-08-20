import re
word = re.compile(r'^Ut')
with open ('sample.txt','r') as sample:
    for line in sample:
        if word.search(line) == None:
            print (line, end='')
