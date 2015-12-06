__author__ = 'konzy'

f = open('day1file.txt', 'r')
input = f.read()

upCount = 0
downCount = 0
for c in input:
    if c == '(':
        upCount += 1
    else:
        downCount += 1
    if downCount > upCount:
        print("first time in basement" + str(upCount + downCount))
print("end floor: " + str(upCount - downCount))



