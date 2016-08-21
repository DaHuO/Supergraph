import sys

def reverse(pancake):
    if pancake == '-':
        return '+'
    else:
        return '-'

def flip(pancakes):
    return list(map(reverse, pancakes[::-1]))

def isLastCorrect(pancakes, expected):
    return pancakes[-1] == expected

def solve(pancakes, pos='+'):
    if not pancakes:
        return 0
    #print("pancakes in:      %s" % pancakes)
    #print("flipped pancakes: %s" % flip(pancakes))
    if isLastCorrect(pancakes, pos):
        return solve(pancakes[:-1], pos)
    else:
        return solve(pancakes[:-1], reverse(pos)) + 1

numCases = int(sys.stdin.readline())
for i in range(numCases):
    pancakes = sys.stdin.readline().strip()
    res = solve(list(pancakes))
    print("Case #%s: %s" % (i+1, res))
