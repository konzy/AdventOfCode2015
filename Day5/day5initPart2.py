__author__ = 'konzy'

import re

twiceWithoutOverlap = '(..).*\\1'
onceWithSpace = '(.).\\1'

f = open('day5file.txt', 'r')

nice = 0
for line in f.readlines():
    if re.search(twiceWithoutOverlap, line) and re.search(onceWithSpace, line):
        nice += 1
print(nice)

