infile = "./input"

lines = []
for line in open(infile):
    lines.append(line)

draws = [int(x) for x in lines[0].split(',')]
del lines[0]
del lines[0]

boards = []
while len(lines) > 0:
    board = []
    for line in lines[0:5]:
        board.append([int(x) for x in line.split()])
    boards.append(board)
    del lines[0:6]

win = False
win_board = None
win_draw = None
while len(draws) > 0 and not win:
    draw = draws[0]
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if draw in boards[i][j]:
                k = boards[i][j].index(draw)
                boards[i][j][k] = -1

    for board in boards:
        for i in range(len(board)):
            if sum(board[i]) == -5:
                win_board = board
                win_draw = draw
                win = True

        for i in range(5):
            s = 0
            for j in range(5):
                s += board[j][i]
            if s == -5:
                win_board = board
                win_draw = draw
                win = True

    del draws[0]

s = 0
for i in range(5):
    for j in range(5):
        if not win_board[i][j] == -1:
            s += win_board[i][j]

print("p1", s * win_draw)

for row in win_board:
    print(row)
