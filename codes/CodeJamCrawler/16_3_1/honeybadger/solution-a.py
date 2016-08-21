"""
@author: umnik700@gmail.com
"""

from itertools import count

# INPUT_FILE = 'test-input.txt'
# OUTPUT_FILE = 'test-output.txt'

# INPUT_FILE = 'A-small-attempt0.in'
# OUTPUT_FILE = 'A-small-attempt0.out'

INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'

def process_case(n):
    result = []
    parties = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    senators = [(n[i], parties[i]) for i in xrange(len(n))]

    total = sum([i for i, _p in senators])
    while(total > 0):
        senators.sort()
        senators.reverse()

        # check if we should evacuate only 1
        s1, p1 = senators[0]
        if(s1 > 0):
            senators_1 = [(s1 - 1, p1)]
            senators_1 += senators[1:]
            if(is_balanced(senators_1)):
                # we can evacuate this one senator
                result += [p1]
                senators = senators_1
                total = sum([i for i, _p in senators])
                continue

            # evacuate 2
            s1, p1 = senators[0]
            s2, p2 = senators[1]
            if(s1 > 0 and s2 > 0):
                senators_2 = [(s1 - 1, p1), (s2 - 1, p2)]
                senators_2 += senators[2:]

                if(is_balanced(senators_2)):
                    # this is what we expect
                    result += ["{0}{1}".format(p1, p2)]
                    senators = senators_2
                    total = sum([i for i, _p in senators])
                    continue
                else:
                    raise Exception('not balanced')

    return ' '.join(result)


def is_balanced(senators):
    total = sum([i for i, _p in senators])
    if total == 0:
        return True
    for i, _p in senators:
        if (i * 1.0 / total) > 0.5:
            return False
    return True


total_tests = None
tests = []

with open(INPUT_FILE, 'rU') as f:

    input_data = list(f)
    index = 0
    while index < len(input_data):
        if(total_tests is None and index == 0):
            line = input_data[index].strip()
            total_tests = int(line)
            index += 1
            continue

        line = input_data[index].strip()
        how_many_tests = int(line)
        index += 1
        line = input_data[index].strip()
        input_values = [int(i) for i in line.strip().split(' ')]
        if(how_many_tests != len(input_values)):
            raise Exception('number of values is invalid in test')
        tests += [input_values]
        index += 1

print tests
if(total_tests != len(tests)):
    print 'tests', len(tests)
    raise Exception('invalid number of tests')

print '-' * 70
print 'input data'
print '-' * 70
for test in tests:
    print test
print '-' * 70

case_number = 0

with open(OUTPUT_FILE, 'wb') as o:
    for n in tests:
        case_number += 1

        result = process_case(n)

        print "Case #{0}: {1}".format(case_number, result)
        o.write("Case #{0}: {1}\n".format(case_number, result))
