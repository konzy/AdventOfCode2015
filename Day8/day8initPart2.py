__author__ = 'konzy'
import re

codeCount = 0
encodedCount = 0

f = open('day8file.txt', 'r')

for line in f.readlines():
    line = line[0:len(line) - 1]
    codeCount += len(line)
    line += 'qq'
    line = re.sub('\"', 'qq', line)
    line = re.sub('\\\\', 'bb', line)
    encodedCount += len(line)
print(encodedCount - codeCount)