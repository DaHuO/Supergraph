__author__ = 'Kholofelo Moyaba'


# flip till i (from top)
def flip(pancakes, i, last):
    j = 0
    old_pancakes = pancakes[:]  # need to work on copy
    while j <= i:
        pancakes[j] = not old_pancakes[i-j]
        j += 1

    chain_end = 0

    # find end of chain of same sided from top
    while (chain_end <= last) and (pancakes[chain_end] is pancakes[0]):
        chain_end += 1

    return chain_end - 1


# algorithm: always flip longest chain from top: stop, if all true
def min_flips(pancakes):
    last = len(pancakes) - 1
    i = 0
    chain_end = -1  # unknown
    while True:  # no need for termination
        chain_end = flip(pancakes, chain_end, last)
        if (chain_end is last) and (pancakes[chain_end] == True):  # have chain till end of smileys
            return i
        i += 1


def boolify(x):
    return True if x is '+' else False

# ==================================
# Start
cases = int(raw_input())
case = 1
while cases >= case:
    sides = map(boolify, raw_input())
    print("Case #%s: %s" % (str(case), min_flips(sides)))
    case += 1
