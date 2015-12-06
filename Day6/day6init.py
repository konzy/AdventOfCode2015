__author__ = 'konzy'
import re
lightGrid = [[False]*1000 for i in range(1000)]

f = open('day6file.txt', 'r')

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
                lightGrid[x][y] = True
            elif lineArray[0] == 'off':
                lightGrid[x][y] = False
            else:
                if lightGrid[x][y]:
                    lightGrid[x][y] = False
                else:
                    lightGrid[x][y] = True
accumulator = 0
for x in range(1000):
    for y in range(1000):
        if lightGrid[x][y]:
            accumulator += 1
print(accumulator)
