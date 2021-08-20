lines = []
with open ('sample.txt','r') as sample:
    for line in sample:
        lines.append(line)
print(lines[0])