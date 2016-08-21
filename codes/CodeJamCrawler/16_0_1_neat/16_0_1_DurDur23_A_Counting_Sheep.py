"""
File: A_Counting_Sheep.py

Author: Sung Uk Ryu

Solution for Google Code Jam 2016, Qualification Round: A. Counting Sheep
"""

f = open('A-large.in', 'r')
out = open('A-large.out', 'w')
n = int(f.readline())

for i in range(1, n+1):
    number = int(f.readline())
    last_number = number
    checker = map(str, range(10))
    for j in range(100):
        digits = str(last_number)
        for digit in digits:
            if digit in checker:
                checker.remove(digit)
        if len(checker) == 0:
            out.write('Case #%d: %d\n' % (i, last_number))
            break
        else:
            last_number += number
    if len(checker) != 0:
        out.write('Case #%d: %s\n' % (i, 'INSOMNIA'))

f.close()
out.close()
