import sys
import os



def solve(n):
    cycle_detector = set()
    digits_seen = set()

    number = n
    while True:
        if number in cycle_detector:
            return 'INSOMNIA'

        number_as_str = str(number)
        for digit in number_as_str:
            digits_seen.add(digit)

        if len(digits_seen) == 10:
            return number

        cycle_detector.add(number)
        number += n
    

def read_input():
    with open(sys.argv[1]) as input_file:
        T = int(input_file.readline())
        for i in xrange(T):
            N = int(input_file.readline())
            answer = solve(N)
            print 'Case #{}: {}'.format(i+1, answer)

            
if __name__ == "__main__":
    read_input()
