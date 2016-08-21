import sys
from itertools import permutations
sys.setrecursionlimit(200000)


nums =  ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
M = dict()

for number, n in enumerate(nums):
    for comb in permutations(n, len(n)):
        M[''.join(comb)] = number

bad = set()
def rec(a, cnt, number):
    if number == 10:
        if any(cnt.values()):
            return []
        else:
            return [""]
    if number > 0 and cnt[ord("Z")]:
        return []
    if number > 4 and cnt[ord("O")]:
        return []
    if  number > 2 and cnt[ord("W")]:
        return []
    if  number > 6 and cnt[ord("X")]:
        return []
    if  number > 7 and cnt[ord("V")]:
        return []
    if  number > 4 and cnt[ord("U")]:
        return []
    if  number > 5 and cnt[ord("F")]:
        return []

    num = nums[number]
    _cnt = dict(cnt)
    alternatives = []

    for n in num:
        n = ord(n)
        _cnt[n] -= 1
        if _cnt[n] < 0:
            #for alt in rec(a, dict(cnt), number + 1):
            #    alternatives.append(alt)
            break
    else:
        for alt in rec(a, _cnt, number):
            alternatives.append(str(number) + alt)
            if alternatives:
                break
    if not alternatives:
        for alt in rec(a, cnt, number + 1):
            alternatives.append(alt)


    return alternatives

def solve(M, a):
    bad.clear()
    cnt = {n:0 for n in range(100)}
    for k in a:
        cnt[ord(k)] += 1
    a = rec(a, cnt, 0)
    assert len(a) == 1
    return a[0]

if __name__ == "__main__":
    f = open("A.in")

    lines = f.read().splitlines()
    interp_line = lambda x: map(int, x.split(" "))
    for idx, line in enumerate(lines[1:]):
        print "Case #%d: %s" % (1+idx, solve(M, line))

    f.close()
