__author__ = 'konzy'
import re
lightGrid = [[False]*10 for i in range(10)]

f = open('day6filetest.txt', 'r')

for line in f.readlines():
    line = line[5:len(line)]
    lineArray = re.split('[ ,\n]*', line)
    x1 = int(lineArray[1])
    y1 = int(lineArray[2])
    x2 = int(lineArray[4])
    y2 = int(lineArray[5])
    startX = min(x1, x2)
    endX = max(x1, x2)
    startY = min(y1, y2)
    endY = max(y1, y2)
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if lineArray[0] == 'on':
                lightGrid[x][y] += 1
            elif lineArray[0] == 'off':
                lightGrid[x][y] -= 1
            else:
                lightGrid[x][y] += 2
accumulator = 0
for x in range(10):
    for y in range(10):
        accumulator += lightGrid[x][y]
for vect in lightGrid:
    print(vect)
print(accumulator)