__author__ = 'konzy'

f = open('day3file.txt', 'r')
board = [[None] * 8000] * 8000
startX = 4000
startY = 4000
currentX = startX
currentY = startY
board[startX][startY] = True
for c in f.read():
    if c == '^':
        currentY += 1
    elif c == 'V':
        currentY -= 1
    elif c == '<':
        currentX -= 1
    elif c == '>':
        currentX += 1
    board[currentX][currentY] = True
accumulator = 0
for vector in board:
    for element in vector:
        if element:
            accumulator += 1
print(accumulator)
