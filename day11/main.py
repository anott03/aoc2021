#!/usr/bin/python3
import sys
import itertools

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

X = []
for line in open(infile):
    X.append([int(x) for x in line.strip()])

ct = 0
def flash(r, c):
    global ct
    ct += 1
    X[r][c] = -1
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<len(X) and 0<=cc<len(X[0]) and X[rr][cc] != -1:
                X[rr][cc] += 1
                if X[rr][cc] >= 10:
                    flash(rr, cc)

for t in range(100):
    for r in range(len(X)):
        for c in range(len(X[0])):
            X[r][c] += 1
    for r in range(len(X)):
        for c in range(len(X[0])):
             if X[r][c] == 10:
                 flash(r, c)
    for r in range(len(X)):
        for c in range(len(X[0])):
            if X[r][c] == -1:
                X[r][c] = 0

print(ct)
