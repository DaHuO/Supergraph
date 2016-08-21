

import sys
import random

#in_filename = 'example.in'
#in_filename = 'B-small-attempt0.in'
#in_filename = 'A-large-practice.in'
in_filename = 'B-large.in'

#out_filename = 'example.out'
#out_filename = 'B-small-attempt0.out'
#out_filename = 'A-large-practice.out'
out_filename = 'B-large.out'

def generate_testcase():
    in_file = open(in_filename, 'w')
    out_msg = str(100)
    in_file.write(out_msg + "\n")
    for i in range(1, 101):
        num = random.randrange(0, 1000001)
        out_msg = str(num)
        in_file.write(out_msg + "\n")
    in_file.close()

#generate_testcase()


def flip(stack, index):
    count_negative = 0

    for i in range(0, index):
        if stack[i] == -1:
            stack[i] = 1
        elif stack[i] == 1:
            stack[i] = -1
            count_negative += 1

    return False


def convert(str):
    i = 0
    ret = []
    for c in str:
        if c == '+':
            ret.append(1)
        elif c == '-':
            ret.append(-1)
        else:
            ret.append(0)
        i += 1
    #ret[i] = 0
    return ret


def align(in_str):
    #in_str = "---+++--+----+++--"
    stack = convert(in_str)
    count = 0
    #print "  {0} {1}".format(len(stack), stack)

    for i in range(len(stack), 0, -1):
        if stack[i - 1] == -1:
            flip(stack, i)
            #print "    {0} {1} {2}".format(count, i, stack)
            count += 1
    return count

#sys.exit(0)


in_file = open(in_filename, 'r')
out_file = open(out_filename, 'w')

################################################################################
# number of case
line = in_file.readline()
num_of_cases = int(line)
case_index = 1

print "Total Case: " + str(num_of_cases)

while True:
    line = in_file.readline()
    if not line:
        break
    ################################################################################

    tokens = line.strip().split(' ')
    count = align(tokens[0])

    ################################################################################
    out_msg = "Case #{0}: {1}".format(case_index, count)
    print out_msg
    out_file.write(out_msg + "\n")
    case_index += 1

in_file.close()
out_file.close()
