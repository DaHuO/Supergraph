import sys
import os

MAX_DIVISOR = 1000

def as_string(number):
    return bin(number)[2:]

def as_base(number, base):
    result = 0
    for digit in number[:-1]:
        if digit == '1':
            result += 1
        elif digit == '0':
            pass
        else:
            print 'bad digit'

        result *= base        

    return result + 1

def test(number):
    divisors = []
    for base in xrange(2, 11):
        num_as_base = as_base(number, base)

        found = False
        for divisor in xrange(2, MAX_DIVISOR):
            if num_as_base % divisor == 0:
                divisors.append(divisor)
                found = True
                break

        if not found:
            return False

    print number + ' ' + ' '.join(['{:d}'.format(d) for d in divisors])
    return True

def solve(N, J):
    number = 2**(N-1) + 1

    found = 0
    while True:
        if found == J:
            return

        if test(as_string(number)):
            found += 1

        number += 2

def read_input():
    with open(sys.argv[1]) as input_file:
        T = int(input_file.readline())
        for i in xrange(T):
            line = input_file.readline()
            N, J = map(int, line.split())
            print 'Case #{}:'.format(i+1)
            answer = solve(N, J)
            
if __name__ == "__main__":
    read_input()
