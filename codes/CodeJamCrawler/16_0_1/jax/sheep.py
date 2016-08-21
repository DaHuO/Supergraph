#!/usr/bin/python
import sys


NUMBERS = [False for x in xrange(10)]


def output(case_nr, result):
    case_nr = str(case_nr)
    result = str(result)
    sys.stdout.write("Case #{}: {}\n".format(case_nr, result))


def get_indices_from_numbers(nr):
    indices = set()
    while nr > 0:
        indices.add(nr % 10)
        nr = nr / 10
    return list(indices)


def detect_insomnia(nr):
    if get_indices_from_numbers(nr) == get_indices_from_numbers(nr * 2):
        return True
    return False


def count():
    cases = int(sys.stdin.readline().strip())
    for i in xrange(cases):
        nr = int(sys.stdin.readline().strip())
        N = nr
        if detect_insomnia(nr):
            output(i+1, "INSOMNIA")
            continue
        
        while True:
            for x in get_indices_from_numbers(nr):
                NUMBERS[x] = True
            if all(NUMBERS):
                output(i+1, nr)
                break
            else:
                nr += N
        
        for x in xrange(10):
            NUMBERS[x] = False
        

if __name__ == '__main__':
    count()

