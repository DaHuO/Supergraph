from itertools import imap
import math
import json

def case_number(pos):
    return pos + 1

def print_case(case_no):
    print 'Case #{case_no}:'.format(case_no = case_no)

def clean_line(line):
    return line.replace('\r', '').replace('\n', '')

def max_applicable_loop(length):
    return 2**(length-2)

def is_divisible(value):
    # print 'Val', value
    for i in MyXRange(2, value / 2):
        if value % i == 0:
            return i

        # if i == 500: break
    return 0

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5L
    w = 2L

    # print 'N', n
    while i * i <= long(math.sqrt(n) / 2):
        if n % i == 0:
            return False

        # print 'iw', i, w
        i += w
        w = 6 - w

    return True

def process_binary(binary):
    result = {}
    for base in xrange(2, 11):
        if is_prime(int(binary, base)):
            return {}

    for base in xrange(2, 11):
        val = int(binary, base)
        # print 'Check', val, base
        divisor = is_divisible(val)

        if divisor:
            # print 'Divisible', val, divisor
            result[str(base)] = divisor

    return result

def is_result_valid(json):
    keys = list(imap(lambda x: int(x), json.keys()))
    keys = sorted(keys)
    keys = list(imap(lambda x: str(x), keys))
    # print ''.join(keys) == '2345678910'
    return ''.join(keys) == '2345678910'

def process(case, length, total_answer):
    print_case(case_number(case))

    counter = 0
    bound = max_applicable_loop(length)
    # print 'Bound', bound

    for binary in loop(length, bound):
        cancel = False
        # binary = '1000000000001011'
        result = process_binary(binary)

        if not is_result_valid(result):
            # print 'Continue', binary
            cancel = True
            continue

        counter += 1

        # print binary, json.dumps(result)

        if counter > total_answer:
            # print 'Max', binary
            break

        if not cancel:
            # print counter
            print binary, result["2"], result["3"] \
                        , result["4"], result["5"] \
                        , result["6"], result["7"] \
                        , result["8"], result["9"], result["10"]


def loop(size, max_value):
    for i in xrange(max_value):
        yield generate_binaries(size, i)

def generate_binaries(size, value):
    return '1{val:0>{max}b}1'.format(val=value, max=size-2)

def begin(file):
    with open(file) as input:
        input_size = long(input.readline())
        for no, line in enumerate(input):
            data = clean_line(line).split(' ')
            process(no, int(data[0]), int(data[-1]))

class MyXRange(object):
    def __init__(self, a1, a2=None, step=1):
        if step == 0:
            raise ValueError("arg 3 must not be 0")
        if a2 is None:
            a1, a2 = 0, a1
        if (a2 - a1) % step != 0:
            a2 += step - (a2 - a1) % step
        if cmp(a1, a2) != cmp(0, step):
            a2 = a1
        self.start, self.stop, self.step = a1, a2, step

    def __iter__(self):
        n = self.start
        while cmp(n, self.stop) == cmp(0, self.step):
            yield n
            n += self.step

    def __repr__(self):
        return "MyXRange(%d,%d,%d)" % (self.start, self.stop, self.step)

    # NB: len(self) will convert this to an int, and may fail
    def __len__(self):
        return (self.stop - self.start)//(self.step)

    def __getitem__(self, key):
        if key < 0:
            key = self.__len__() + key
            if key < 0:
                raise IndexError("list index out of range")
            return self[key]
        n = self.start + self.step*key
        if cmp(n, self.stop) != cmp(0, self.step):
            raise IndexError("list index out of range")
        return n

    def __reversed__(self):
        return MyXRange(self.stop-self.step, self.start-self.step, -self.step)

    def __contains__(self, val):
        if val == self.start: return cmp(0, self.step) == cmp(self.start, self.stop)
        if cmp(self.start, val) != cmp(0, self.step): return False
        if cmp(val, self.stop) != cmp(0, self.step): return False
        return (val - self.start) % self.step == 0

if __name__ == '__main__':
    begin('coin/input.txt')
