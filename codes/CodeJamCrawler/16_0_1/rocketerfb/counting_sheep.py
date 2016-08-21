#!/usr/bin/python
import sys, getopt

def main(argv):
    inputfile = argv[0]
    fi = open(inputfile, 'r')
    line = fi.readline()
    case = 1
    max_iter = 10
    digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    line = fi.readline()
    fo = open('output.txt', 'w')
    while line:
        N = int(line)
        iter_cnt = 0
        curr_digits = list(str(N))
        val = 0
        while set(curr_digits) != digits and iter_cnt < max_iter:
            val += N
            digits_of_val = list(str(val))
            if not (set(curr_digits) - set(digits_of_val)):
                iter_cnt += 1
            curr_digits = list(set(curr_digits) | set(digits_of_val))
            #print "Value:", val, " Current digits:", curr_digits
        if iter_cnt == max_iter:
            fo.write("Case #" + str(case) + ": INSOMNIA\n")
        else:
            fo.write("Case #" + str(case) + ": " + str(val) + '\n')
        case += 1
        line = fi.readline()
    fi.close()
    fo.close()

if __name__ == "__main__":
    main(sys.argv[1:])
