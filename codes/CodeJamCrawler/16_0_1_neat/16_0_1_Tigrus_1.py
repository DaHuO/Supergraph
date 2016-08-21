# coding: utf-8
import sys

test_number = None
case = 0

for line in sys.stdin:
    #print (line)
    if not test_number:
        test_number = line
        #print(line)
        #print (test_number)
        continue

    number = int(line)
    case += 1
    #print (number)
    if number == 0:
        result = "INSOMNIA"
        print ("Case #%s: %s" % (case, result))
        continue

    seen = set()
    #n = 2
    _number = number
    while len(seen) < 10:
        for x in str(_number):
            seen.add(int(x))
        result = _number
        _number += number
        #print (seen)
        #number = number*n
        #n += 1
    print ("Case #%s: %s" % (case, result))


