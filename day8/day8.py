#!/usr/bin/python3
infile = './input'
count = 0
for line in open(infile):
    l = line.split('|')[1].strip()
    for w in l.split(' '):
        x = len(w)
        if x == 2 or x == 4 or x == 3 or x == 7:
            count += 1

print(count)
