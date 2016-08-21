__author__ = 'chonnakan'
import sys
sys.setrecursionlimit(10000)

was_flipped = []
ans = 99999999


def check_pancakes(pancakes):
    for p in pancakes:
        if p == '-':
            return False
    return True


def flip_pancakes(pos, pancakes):
    flipped = ''

    for i in range(pos-1, -1, -1):
        #print pancakes[i]
        if pancakes[i] == '-':
            flipped += '+'
        elif pancakes [i] == '+':
            flipped += '-'
    for i in range(pos, len(pancakes)):
        flipped += pancakes[i]
    return flipped


def check_q(q, fl):
    count = 0
    for f in fl:
        if f not in q:
            count += 1
    return count

def solve(pancakes):
    level = 0
    q = [pancakes]
    h = 0
    l = 1
    #print h, l

    if check_pancakes(pancakes):
        return level

    fl = []
    for i in range(h, l):
        for j in range(1, len(pancakes)+1):
            fl.append(flip_pancakes(j, pancakes))
    level += 1

    count = 0
    for ff in fl:
        if ff not in q:
            q.append(ff)
            count += 1
            if check_pancakes(ff):
                return level
    h = l
    l = l+count

    #print h, l
    #print q

    while count > 0 :
        for i in range(h, l):
            for j in range(1, len(pancakes)+1):
                #print q[i]
                fl.append(flip_pancakes(j, q[i]))
        level += 1
        count = 0
        for ff in fl:
            if ff not in q:
                q.append(ff)
                count += 1
            if check_pancakes(ff):
                return level

        h = l
        l = l+count
        #print h, l
        #print q
    print q








f = open('B-small-attempt0.in')
cases = int(f.readline())

for c in range(1, cases+1):
    was_flipped = []
    ans = 99999999
    pancakes = f.readline().replace('\n', '').replace('\r', '')

    print 'Case #%d: %d' % (c, solve(pancakes))
