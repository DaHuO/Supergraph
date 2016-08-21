import sys


def solve(s):
    digitCount = [0] * 10
    digitCount[0] = s.count('Z')
    digitCount[2] = s.count('W')
    digitCount[4] = s.count('U')
    digitCount[5] = s.count('F') - digitCount[4]
    digitCount[6] = s.count('X')
    digitCount[7] = s.count('V') - digitCount[5]
    digitCount[8] = s.count('G')
    digitCount[9] = s.count('I') - (digitCount[6] + digitCount[8] + digitCount[5])
    digitCount[1] = s.count('O') - (digitCount[0] + digitCount[2] + digitCount[4])
    digitCount[3] = s.count('R') - (digitCount[0] + digitCount[4])
    result = ""
    for i, d in enumerate(digitCount):
        result += str(i) * d

    return result



results = []


# Input
#
# 4
# OZONETOWER
# WEIGHFOXTOURIST
# OURNEONFOE
# ETHER
#
# Output
#
# Case #1: 012
# Case #2: 2468
# Case #3: 114
# Case #4: 3

with open(sys.argv[1]) as f:
    T = int(f.readline().rstrip())
    for i in xrange(T):
        S = f.readline().rstrip()
        results.append(solve(S))

for i, r in enumerate(results):
    print "Case #{0}: {1}".format(i + 1, r)
