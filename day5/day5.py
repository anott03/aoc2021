infile = "./input"

points = {}

P2 = True
for line in open(infile):
    [s, e] = line.split(' -> ')
    start = [int(s.split(',')[0]), int(s.split(',')[1])]
    end = [int(e.split(',')[0]), int(e.split(',')[1])]

    if start[0] == end[0]:
        r = range(start[1], end[1]+1)
        if start[1] > end[1] + 1:
            r = range(end[1], start[1]+1)
        for i in r:
            if str((start[0], i)) not in points:
                points[str((start[0], i))] = 1
            else:
                points[str((start[0], i))] += 1
    elif start[1] == end[1]:
        r = range(start[0], end[0]+1)
        if start[0] > end[0] + 1:
            r = range(end[0], start[0]+1)
        for i in r:
            if str((i, start[1])) not in points:
                points[str((i, start[1]))] = 1
            else:
                points[str((i, start[1]))] += 1

    # diagonals (pt 2)
    else:
        if not P2:
            continue

        r1 = list(range(start[0], end[0]+1))
        if start[0] > end[0]:
            r1 = list(range(start[0], end[0]-1, -1))

        r2 = list(range(start[1], end[1]+1))
        if start[1] > end[1]:
            r2 = list(range(start[1], end[1]-1, -1))

        for i in range(len(r1)):
            key = str((r1[i], r2[i]))
            if key not in points:
                points[key] = 1
            else:
                points[key] += 1

count = 0
for k in points:
    if points[k] > 1:
        count += 1

print(count)
