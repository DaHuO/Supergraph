__author__ = 'drathier'

"""

idea, flip . flip = no-op
can only flip from top
order of flips does not matter
sweep through, bottom to top, and flip whenever a pancake is facing the wrong way.
- keep track of if pancakes above are flipped or not, in a bool

"""


def m():
    n = input()
    a = []
    for _ in range(n):
        a += [raw_input()]

    num = 1
    for i in a:
        print "Case #{0}: {1}".format(num, s(i))
        num += 1

def s(a):
    flips = 0
    flipped = False
    for c in a[::-1]:
        #print "s", c, flipped, flips, a
        if (c == '+' and flipped) or (c == '-' and not flipped):
            flips += 1
            flipped = not flipped

    return flips

"""
print s("-"), 1
print s("-+"), 1
print s("+-"), 2
print s("+++"), 0
print s("--+-"), 3
"""
#print s("--+-+-+--+-++--+-+--+-++"), "?"

m()