import functools
import itertools

# adapted from:
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    try:
        return set(functools.reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    except TypeError:
        return None

def isJamCoin(sbin):
    # sbin = str(ibin)
    try:
        return [factors(int(sbin, i)).pop() for i in range(2, 11)]
    except AttributeError:
        return None

def generateCandidates(n):
    return ['1'+''.join(x)+'1' for x in itertools.product(['0','1'], repeat=n-2)]

# print(isJamCoin(100011))
# print(isJamCoin(111111))
# print(isJamCoin(111001))
# print()
# print(isJamCoin(110111))
# print(isJamCoin(111101))

j = 50
n = 16
# jamcoins = []
found = 0
candidates = generateCandidates(n)
i = 0
while(found < j and i < len(candidates)):
    factor_list = isJamCoin(candidates[i])
    if factor_list:
        # jamcoins.append((candidates[i], factor_list))
        found += 1
        print("%s %s" % (candidates[i], ' '.join([str(f) for f in factor_list])))
    i += 1
# print("%d %s" jamcoins)

#
# print(generateCandidates(3))
# print(generateCandidates(4))
# print(generateCandidates(5))
# print(generateCandidates(6))
