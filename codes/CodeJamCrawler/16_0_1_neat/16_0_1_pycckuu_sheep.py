# from __future__ import print_function
import fileinput


with open('A-large.in', 'r') as f:
    lines = f.read().splitlines()

f1 = open('output', 'w+')

n = int(lines[0])


def sleep_count(test_case):
    if test_case == 0:
        return 'INSOMNIA'
    return collect_numbers(test_case)


def collect_numbers(test_case):
    seen = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
    i = 1
    while True:
        test_case_i = i * test_case
        for ch in str(test_case_i):
            seen[int(ch)] = True
            if all(seen.values()) == True:
                return test_case_i
        i += 1


for j in xrange(1, n + 1):
    result = sleep_count(int(lines[j]))
    f1.write("Case #%i: %s\n" % (j, result))
    print ("Case #%i: %s" % (j, result))


# collect_numbers(int(lines[2]))
