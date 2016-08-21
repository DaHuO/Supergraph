

import sys
import random

#in_filename = 'example.in'
#in_filename = 'A-small-attempt0.in'
#in_filename = 'A-large-practice.in'
in_filename = 'A-large.in'

#out_filename = 'example.out'
#out_filename = 'A-small-attempt0.out'
#out_filename = 'A-large-practice.out'
out_filename = 'A-large.out'

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

bitmap = {}
bitcount = 0

def init_bitmap():
    global bitmap
    global bitcount

    for i in range(0, 10):
        bitmap[i] = 0
    bitcount = 0

init_bitmap()

def check_map(num_str):
    global bitmap
    global bitcount

    for c in num_str:
        i = int(c)
        if bitmap[i] == 0:
            bitcount += 1
        bitmap[i] += 1;

    return bitcount == 10


def check_N(N):
    i = 1
    if N == 0:
        return 0

    init_bitmap()
    while True:
        num = N * i
        num_str = str(num)
        ret = check_map(num_str)
        #print "{0} {1} {2}".format(num_str, bitcount, bitmap)
        if ret:
            break
        i += 1

    return i


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
    N = int(tokens[0])

    #print "# Case #{0}: {1}".format(case_index, N)
    max = check_N(N)

    ################################################################################
    if max == 0:
        out_msg = "Case #{0}: INSOMNIA".format(case_index)
    else:
        out_msg = "Case #{0}: {1}".format(case_index, N * max)
    print out_msg
    out_file.write(out_msg + "\n")
    case_index += 1

in_file.close()
out_file.close()
