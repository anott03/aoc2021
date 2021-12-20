#!/usr/bin/python3
infile = './input'
P1 = 0
for line in open(infile):
    l = line.split('|')[1].strip()
    for w in l.split(' '):
        x = len(w)
        if x == 2 or x == 4 or x == 3 or x == 7:
            P1 += 1

def convert(s=''):
    n = [0 for _ in range(7)]
    for x in s:
        i = 'abcdefg'.index(x)
        n[i] = 1
    return ''.join([str(x) for x in n])

numbers = {
    0: convert('acfgeb'),
    1: convert('cf'),
    2: convert('acdeg'),
    3: convert('acdfg'),
    4: convert('bcdf'),
    5: convert('abdfg'),
    6: convert('abdfeg'),
    7: convert('acf'),
    8: convert('abcdefg'),
    9: convert('abcdfg')
}

for line in open(infile):
    imp, out = [x.strip().split(' ') for x in line.split('|')]
    for e in imp:
        x = convert(e)
