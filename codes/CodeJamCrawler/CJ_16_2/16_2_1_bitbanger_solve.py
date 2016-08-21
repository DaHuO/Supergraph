
import itertools
import sys

def to_str(i):
    if i == 0:
        return "ZERO"
    if i == 1:
        return "ONE"
    if i == 2:
        return "TWO"
    if i == 3:
        return "THREE"
    if i == 4:
        return "FOUR"
    if i == 5:
        return "FIVE"
    if i == 6:
        return "SIX"
    if i == 7:
        return "SEVEN"
    if i == 8:
        return "EIGHT"
    if i == 9:
        return "NINE"

def convert(nums):
    snums = []
    for i in nums:
        snums.append(to_str(i))

    s = ''.join(sorted(''.join(snums)))
    return s

lib = {}
for i in range(1,7):
    for perm in itertools.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9], i):
        lib[convert(perm)] = ''.join([str(x) for x in sorted(perm)])

#print lib

def solve(filename):
    with open(filename, 'r') as f:
        num_tests = int(f.readline())
        for i in xrange(num_tests):
            s = ''.join(sorted(f.readline().strip()))
            #if s not in lib:
            #    print "%s not found" % s

            #    continue
            assert s in lib
            ans = lib[s]

            print "Case #%d: %s" % (i + 1, ans)

solve(sys.argv[1])
