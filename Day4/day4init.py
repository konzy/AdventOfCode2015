__author__ = 'konzy'

import hashlib
secretKey = 'iwrupvqb'
secretKey2 = 'iwrupvqb'

exHash = hashlib.md5()
exHash.update('abcdef609043')
print(exHash.hexdigest())

count = 0
found = False
digest = ''
while not found:
    m = hashlib.md5()
    m.update(secretKey)
    count += 1
    m.update(str(count))
    digested = m.hexdigest()
    found = digested.startswith('000000')
print(count)
