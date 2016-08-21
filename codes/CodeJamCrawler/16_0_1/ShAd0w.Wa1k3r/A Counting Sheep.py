#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2016 - Qualifiers - Counting Sheep
#
# Author:      Ashish Nitin Patil
#
# Created:     09-04-2016
# Copyright:   (c) Ashish Nitin Patil 2016
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    if N == 0:
        last_number = 'INSOMNIA'
    else:
        digits_seen = set()
        multiplier = 1
        while len(digits_seen) != 10:
            last_number = N*multiplier
            multiplier += 1
            for digit in str(last_number):
                digits_seen.add(digit)
    print("Case #{0}: {1}".format(test_case, last_number))
