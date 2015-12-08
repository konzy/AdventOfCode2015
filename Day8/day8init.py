__author__ = 'konzy'
import re

codeCount = 0
memoryCount = 0

f = open('day8file.txt', 'r')

for line in f.readlines():
    line = line[0:len(line) - 1]
    codeCount += len(line)
    line = line[1:len(line) - 1]
    line = re.sub('\\\\\\\\', 'b', line)
    line = re.sub('\\\\"', 'a', line)
    line = re.sub('\\\\x..', 'h', line)
    memoryCount += len(line)
print(codeCount - memoryCount)