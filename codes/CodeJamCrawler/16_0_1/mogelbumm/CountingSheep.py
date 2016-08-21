'''
Created on 09.04.2016

@author: uscheller
'''
import sys

def solve(N):
    digits_seen = set()
    numbers_counted = set()
    i = 0
    while len(digits_seen) < 10:
        i += 1
        if N * i in numbers_counted:
            return "INSOMNIA"
        for digit in str(N * i):
            digits_seen.add(digit)
        numbers_counted.add(N * i)
    return N * i

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        N = int(data[0])
        data = data[1:]
        s += "Case #%d: %s\n" % (case, solve(N))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())
    
    
    
    