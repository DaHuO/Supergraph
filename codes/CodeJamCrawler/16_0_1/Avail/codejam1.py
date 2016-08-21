# Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster.
# First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on.
# Whenever she names a number, she thinks about all of the digits in that number.
# She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least
# once so far as part of any number she has named.
# Once she has seen each of the ten digits at least once, she will fall asleep.
#
# Bleatrix must start with N and must always name (i + 1) × N directly after i × N.
# For example, suppose that Bleatrix picks N = 1692. She would count as follows:
#
# N = 1692. Now she has seen the digits 1, 2, 6, and 9.
# 2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
# 3N = 5076. Now she has seen all ten digits, and falls asleep.
# What is the last number that she will name before falling asleep?
#  If she will count forever, print INSOMNIA instead.
#
# Input
#
# The first line of the input gives the number of test cases, T.
# T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.
#
# Output
# For each test case, output one line containing Case
# #x: y, where x is the test case number (starting from 1) and y is the last number that
# # Bleatrix will name before falling asleep, according to the rules described in the statement.
import sys
LIMIT = 10000

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as inf:
    with open(outfile, 'w') as outf:
        test_case = 1
        t = inf.readline()
        for line in inf.readlines():
            a =  set()
            i = 1

            while len(a) < 10 and i < LIMIT:
                num = i * int(line)
                [a.add(c) for c in str(num)]
                i += 1

            if test_case != 1:
                outf.write('\n')

            if i < LIMIT:
                outf.write("Case #{}: {}".format(test_case, int(line)*(i-1)) )
            else:
                outf.write("Case #{}: INSOMNIA".format(test_case) )

            test_case += 1
