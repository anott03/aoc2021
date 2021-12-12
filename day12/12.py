#!/usr/bin/python3
import sys
from collections import defaultdict, deque

infile = sys.argv[1] if len(sys.argv) > 1 else "12.in"

N = defaultdict(list)
for line in open(infile):
    a, b = line.strip().split('-')
    N[a].append(b)
    N[b].append(a)

start = ('start', set(['start']))
Q = deque([start])
c = 0

while Q:
    pos, seen = Q.popleft()
    if pos == 'end':
        c += 1
        continue
    for y in N[pos]:
        if not y in seen:
            new_seen = set(seen)
            if y[0].islower():
                new_seen.add(y)
            Q.append((y, new_seen))
    print(Q)

print(c)
