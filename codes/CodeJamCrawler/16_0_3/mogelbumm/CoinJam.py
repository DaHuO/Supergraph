'''
Created on 09.04.2016

@author: uscheller
'''
import sys
import math

def value_by_base(s, base):
    value = 0;
    for i in range(len(s)):
        if s[len(s) - i - 1] == "1":
            value += base ** i
    #print "value_by_base(%s, %d): %d" % (s, base, value)
    return value

def nontrivial_divisor(p):
    for i in range(2, int(math.sqrt(p) + 1)):
        if p % i == 0:
            return i
    return -1

def is_jamcoin(s):
    for base in range(2, 11):
        if nontrivial_divisor(value_by_base(s, base)) == -1:
            return False
    return True

def possible_jamcoins(N):
    n = N - 2
    s = "0" * n
    yield "1" + s + "1"
    while s != "1" * n:
        for i in range(n - 1, 0 ,-1):
            if s[i] == "0":
                s = s[:i] + "1" + ("0" * (n - i - 1))
                yield "1" + s + "1"
                break

def solve(N, J):
    solutions = []
    for coin in possible_jamcoins(N):
        if is_jamcoin(coin):
            s = str(coin) + " "
            for base in range(2, 11):
                s += str(nontrivial_divisor(value_by_base(coin, base))) + " "
            solutions.append(s)
            #print "I found %d jamcoins so far" % len(solutions)
        if len(solutions) == J:
            return "\n".join(solutions)

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        N, J = [int(x) for x in data[0].split()]
        data = data[1:]
        s += "Case #%d:\n%s" % (case, solve(N, J))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())
    
    
    
    