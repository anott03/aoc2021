#!/usr/bin/python3
import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
pairs = {'>': '<', ']': '[', ')': '(', '}': '{'}
scores = {'>': 25137, ']': 57, ')': 3, '}': 1197}

ans = 0
for line in open(infile):
    S = deque()
    for c in line.strip():
        if c in list(pairs.values()):
            S.append(c)
            continue
        else:
            if S[-1] != pairs[c]:
                ans += scores[c]
                break
            else:
                S.pop()
print(ans)
