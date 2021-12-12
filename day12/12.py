#!/usr/bin/python3
import sys
from collections import defaultdict, deque

infile = sys.argv[1] if len(sys.argv) > 1 else "12.in"

N = defaultdict(list)
for line in open(infile):
    a, b = line.strip().split('-')
    N[a].append(b)
    N[b].append(a)

start = ('start', set(['start']), None)
Q = deque([start])
c = 0

P2 = True  # true for part 2 answer, false for part 1 answer
while Q:
    pos, seen, twice = Q.popleft()
    if pos == 'end':
        c += 1
        continue
    for y in N[pos]:
        if y not in seen:
            new_seen = set(seen)
            if y[0].islower():
                new_seen.add(y)
            Q.append((y, new_seen, twice))
        elif P2 and y in seen and twice is None and y not in ['start', 'end']:
            Q.append((y, seen, y))

print(c)
