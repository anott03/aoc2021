#!/usr/bin/python3
import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
pairs = {'>': '<', ']': '[', ')': '(', '}': '{'}
points = {'>': 25137, ']': 57, ')': 3, '}': 1197}

ans = 0
for line in open(infile):
    D = deque()
    for c in line.strip():
        if c in list(pairs.values()):
            D.append(c)
            continue
        else:
            if D[-1] != pairs[c]:
                ans += points[c]
                break
            else:
                D.pop()

print("Part 1: ", ans)

points = {'(': 1, '[': 2, '{': 3, '<': 4}
P = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = []

scores = []
for line in open(infile):
    line = line.strip()
    D = deque()

    corrupt = False
    for c in line.strip():
        if c in list(pairs.values()):
            D.append(c)
            continue
        else:
            if D[-1] != pairs[c]:
                corrupt = True
                break
            else:
                D.pop()

    if not corrupt:
        soln = ''
        for x in D:
            soln = P[x] + soln

        s = 0
        for x in soln:
            s *= 5
            s += points[pairs[x]]

        scores.append(s)

scores.sort()
print("Part 2: ", scores[len(scores)//2])
