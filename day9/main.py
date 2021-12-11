#!/usr/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

lines = []
for line in open(infile):
    lines.append([int(x) for x in list(line.strip())])

def part1(lines):
    s = 0
    candidates = []
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if j == 0:
                if line[j] < line[j+1]:
                    candidates.append((i, j))
            elif j == len(line)-1:
                if line[j] < line[j-1]:
                    candidates.append((i, j))
            else:
                if line[j] < line[j + 1] and line[j] < line[j - 1]:
                    candidates.append((i, j))

    for candidate in candidates:
        i = candidate[0]
        j = candidate[1]
        if i == 0:
            if lines[i+1][j] > lines[i][j]:
                s += lines[i][j] + 1
        elif i == len(lines)-1:
            if lines[i - 1][j] > lines[i][j]:
                s += lines[i][j] + 1
        else:
            if lines[i + 1][j] > lines[i][j] and lines[i-1][j] > lines[i][j]:
                s += lines[i][j] + 1

    return s


def part2(lines):
    pass

print(part2(lines))
