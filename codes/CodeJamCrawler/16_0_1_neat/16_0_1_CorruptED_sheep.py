from collections import defaultdict
import sys

def get_digits(N):
    digits = []
    while N:
        digit = N % 10
        digits.append(digit)
        N = N / 10
    return digits

class Counter(object):
    def __init__(self):
        self.digits = defaultdict(int)

    def count(self, digits):
        for d in digits:
            self.digits[d] += 1

    def done(self):
        return len(self.digits) == 10

def check(N):
    if N == 0:
        return "INSOMNIA"
    i = 1
    counter = Counter()
    while not counter.done():
        current_number = N * i
        digits = get_digits(current_number)
        counter.count(digits)
        i += 1
    return current_number

num_cases = int(sys.stdin.readline())

for i in xrange(num_cases):
    N = int(sys.stdin.readline())
    number = check(N)
    print "Case #{0}: {1}".format(i + 1, number)
