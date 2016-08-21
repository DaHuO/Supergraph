__author__ = 'pravesh'
from collections import Counter

file = open("test.in", "r").readlines()
T = int(file.pop(0))
i = 1

def list_intersection(L1, L2):
    l1 = L1[::]
    l2 = L2[::]
    l3 = []
    for l in l1:
        if l in l2:
            l3.append(l)
            l2.remove(l)
    return l3

def list_subtract(L1, L2):
    # L1 - L2
    c1 = Counter(L1)
    c2 = Counter(L2)
    l3 = []
    for k, v in c1.items():
        l3 = l3 + [k] * max(v - c2[k], 0)
    return l3

def get_number(N, number = ''):
    if not N:
        # we found an accurate fit
        return True, number
    for i, l in enumerate(['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']):
        letter = list(l)
        if len(list_intersection(letter, N)) == len(letter):
            result, _ = get_number(list_subtract(N, letter), number+str(i))
            if result:
                return True, _
    return False, ''


while i <= T:
    S = file.pop(0).strip()
    if S:
        print ("Case #%d:" % i, get_number(list(S))[1])
        i += 1
