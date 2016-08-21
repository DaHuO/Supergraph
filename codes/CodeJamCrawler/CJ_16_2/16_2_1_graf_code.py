import sys

digits = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"}

from collections import Counter

def solve_test(inp):
    x = (inp.readline().strip())
    counts = Counter(x)
    digits = ''
    digits += '0' * counts['Z']
    digits += '1' * (counts['O'] -( counts['Z'] + counts['W'] + counts['U'] ))
    digits += '2' * counts['W']
    digits += '3' * (counts['H'] - counts['G'])
    digits += '4' * counts['U']
    digits += '5' * (counts['F'] - counts['U'])
    digits += '6' * counts['X']
    digits += '7' * (counts['S'] - counts['X'])
    digits += '8' * counts['G']
    digits += '9' * (counts['I'] - (counts['G'] + counts['X'] + counts['F'] - counts['U']))


    return ''.join(sorted(digits))


inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()