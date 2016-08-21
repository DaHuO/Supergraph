from math import sqrt, ceil
from itertools import count, islice

# FILENAME = "test"
FILENAME = "C-small-attempt0"
# FILENAME = "C-large"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME


def base10toN(num, n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep = {10: 'a',
               11: 'b',
               12: 'c',
               13: 'd',
               14: 'e',
               15: 'f',
               16: 'g',
               17: 'h',
               18: 'i',
               19: 'j',
               20: 'k',
               21: 'l',
               22: 'm',
               23: 'n',
               24: 'o',
               25: 'p',
               26: 'q',
               27: 'r',
               28: 's',
               29: 't',
               30: 'u',
               31: 'v',
               32: 'w',
               33: 'x',
               34: 'y',
               35: 'z'}
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if 36 > remainder > 9:
            remainder_string = num_rep[remainder]
        elif remainder >= 36:
            remainder_string = '(' + str(remainder) + ')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string + new_num_string
        current = current / n
    return new_num_string


# def primes(n):
#     if n == 2:
#         return [2]
#     elif n < 2:
#         return []
#     s = range(3, n + 1, 2)
#     mroot = n ** 0.5
#     half = (n + 1) / 2 - 1
#     i = 0
#     m = 3
#     while m <= mroot:
#         if s[i]:
#             j = (m * m - 3) / 2
#             s[j] = 0
#             while j < half:
#                 s[j] = 0
#                 j += m
#         i = i + 1
#         m = 2 * i + 3
#     return [2] + [x for x in s if x]


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def firstDivisor(n):
    for i in range(2, int(ceil(sqrt(n))) + 1):
        if (n % i) == 0:
            return i
    print "ERROR: n = %d" % n
    print int(ceil(sqrt(n)))
    return 0


def solve(lines):
    output = "\n"
    # Solve the problem
    n, limit = lines[0].split(" ")
    n = int(n)
    limit = int(limit)

    start = "1" + ("0" * (n - 2)) + "1"
    stop = "1" + ("1" * (n - 2)) + "1"
    start = int(start, 2)
    stop = int(stop, 2)

    # min_start = int(start, 2)
    # max_stop = int(stop, 2)
    # for i in range(3, 11):
    #     new_start = int(start, i)
    #     new_stop = int(stop, i)
    #     if new_start < min_start:
    #         min_start = new_start
    #     if new_stop > max_stop:
    #         max_stop = new_stop

    counter = 0

    for i in range(start, stop + 1, 2):
        binary = base10toN(i, 2)
        base = {2: i}

        if isPrime(float(base[2])):
            continue

        flag = False
        for j in range(3, 11):
            base[j] = int(binary, j)
            if isPrime(float(base[j])):
                flag = True
                continue
        if flag:
            continue

        output += binary

        for j in range(2, 11):
            output += " %d" % firstDivisor(base[j])

        counter += 1
        if counter >= limit:
            break
        else:
            output += "\n"

    return output

if __name__ == '__main__':
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")

    cases = int(input_file.readline())
    for case in range(1, cases + 1):  # Count case from 1, 2, ..., n
        input_lines = list()
        for i in range(LINE_PER_CASE):
            input_lines.append(input_file.readline()[:-1])  # Remove newline
        output_file.write("Case #%d: %s\n" % (
            case,
            solve(input_lines),
        ))

    input_file.close()
    output_file.close()
