import sys
from functools import lru_cache
import math

# Pre calculating the small data-set with 16 50

@lru_cache(maxsize=None)
def divisor(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return -1

def toBinary(i):
    result = []
    while i:
        result.append(i % 2)
        i //= 2
    return result

def bases(i, values):
    a = toBinary(i)
    results = []
    for base in range(0, 9):
        current = values[base]
        for exponent in range(len(a)):
            if a[exponent]:
                current += (base + 2) ** (exponent + 1)
        results.append(current)
    return results

def solve(n, j):
    values = [0] * 9
    for base in range(9):
        values[base] = 1 + (base + 2) ** (n - 1)
    current = 0
    results = []
    while len(results) < j:
        bs = bases(current, values)
        divs = [divisor(x) for x in bs]
        if -1 not in divs:
            results.append((bs[8], divs))
        current += 1
    return results

def run_test(case_number, generator):
    n, j = (int(x) for x in next(generator).split())
    results = solve(n, j)
    print('Case #%d:' % case_number)
    for result in results:
        print(str(result[0]), ' '.join([str(x) for x in result[1]]))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()