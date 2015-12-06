__author__ = 'konzy'

import re

atLeastThreeVowels = '[aeiou]{3}|[aeiou].*[aeiou].*[aeiou]'
oneDoubleLetter = '(.)\\1'
oneSequentialLetters = 'ab|cd|pq|xy'

f = open('day5file.txt', 'r')

nice = 0
for line in f.readlines():
    if re.search(atLeastThreeVowels, line) and re.search(oneDoubleLetter, line) \
            and not re.search(oneSequentialLetters, line):
        nice += 1
print(nice)




