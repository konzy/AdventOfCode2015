__author__ = 'konzy'

f = open('day3file.txt', 'r')
board = [[False]*8000 for i in range(8000)]
START_VALUE = 4000
startX = START_VALUE
startY = START_VALUE
currentX = START_VALUE
currentY = START_VALUE
robotX = START_VALUE
robotY = START_VALUE
board[START_VALUE][START_VALUE] = True
santaMove = True
for c in f.read():
    if santaMove:
        if c == '^':
            currentY += 1
        elif c == 'v':
            currentY -= 1
        elif c == '<':
            currentX -= 1
        elif c == '>':
            currentX += 1
    else:
        if c == '^':
            robotY += 1
        elif c == 'v':
            robotY -= 1
        elif c == '<':
            robotX -= 1
        elif c == '>':
            robotX += 1
    if santaMove:
        santaMove = False
    else:
        santaMove = True
    board[robotX][robotY] = True
    board[currentX][currentY] = True
accumulator = 0
for vector in board:
    for element in vector:
        if element:
            accumulator += 1
print(accumulator)
