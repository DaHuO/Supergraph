# -*- coding: utf-8 -*-
def asleep(N): #1692
    digits = set()

    start = N
    num = start # start counting from N
    
    while num > 0:
        # append all digits
        while num > 0:
            digit = num % 10
            digits.add(digit)
            if len(digits) >= 10:
                return start
            num /= 10
        num = start + N
        start += N
        
    return "INSOMNIA"

filename = 'A-large.in.txt'
with open(filename, 'r') as file, open('output_large.txt','w') as output:
    lines = [line for line in file]
    test_cases = int(lines[0])

    for i in range(1, test_cases+1):
        # process each case
        N = int(lines[i])
        output.write( "Case #%d: %s\n" % (i, asleep(N)) )
        
