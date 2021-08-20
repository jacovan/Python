import re
word = "Ut"
with open ('sample.txt','r') as sample:
    for line in sample:
        if line.find(word) == -1:
            print(line, end='')
        