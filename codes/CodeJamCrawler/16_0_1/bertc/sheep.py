# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 07:55:19 2016

@author: BCLAES
"""

def handle_case(N):
    if (0 == N):
        return "INSOMNIA"
    counter = 1
    not_seen = range(0,10) 
    while (len(not_seen) != 0):
        number = N
        while number:
            digit = number % 10
            if digit in not_seen:
                not_seen.remove(digit)
            number //= 10
        N = N/counter*(counter+1)
        counter += 1
    return N/counter*(counter-1)
        
print handle_case(0)
print handle_case(1)
print handle_case(2)
print handle_case(11)
print handle_case(1692)
print handle_case(1234567890)

solutions = []
with open("A-large.in") as f:
    test_cases = int(f.readline())
    for i in xrange(0,test_cases):
        m = long(f.readline())
        x = handle_case(m)
        strout = str.format("Case #{}: {}\n", i+1, x)
        solutions.append(strout)
with open("output.txt", "w") as out:
        out.writelines(solutions)