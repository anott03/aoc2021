#!/usr/bin/python3
import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "14.in"

inp = open(infile).read().split('\n\n')
s = inp[0]
prs = inp[1].strip().split('\n')

ops = {}
for p in prs:
    x, y = p.split(' -> ')
    ops[x] = y

for _ in range(10):
    new_s = ""
    for i in range(len(s)-1):
        x = s[i:i+2]
        new_s += s[i]
        if x in ops:
            new_s += ops[x]
    new_s += s[len(s)-1]
    s = new_s

counts = defaultdict(int)
for c in s:
    counts[c] += 1

print(max(counts.values()) - min(counts.values()))
