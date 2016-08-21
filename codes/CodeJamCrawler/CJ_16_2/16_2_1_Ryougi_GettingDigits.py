import sys

DIGITS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

def info():
    counts = {}
    for i in range(26):
        c = chr(ord('A')+i)
        n = 0
        for d in DIGITS:
            if c in d:
                n+=1
        counts[c] = n
    # return counts
    print counts

def preProcess():
    ma = {}
    for d in DIGITS:
        for c in d:
            if c in ma:
                ma[c].append(d)
            else:
                tmp = [d]
                ma[c] = tmp

    ind = []
    for k in sorted(ma, key=lambda k: len(ma[k]), reverse=False):
        ind.append(k)

    return ma, ind

def isEmpty(counts):
    for k in counts:
        if counts[k]>0:
            return False
    return True

def contain(d, counts):
    tmp = counts.copy()
    for c in d:
        if c in tmp and tmp[c]>0:
            tmp[c]-=1
        else:
            return False, counts
    return True, tmp

def toCounts(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c]+=1
        else:
            counts[c]=1       
    return counts

def toPhoneNum(counts, ma, ind):
    re = []
    if isEmpty(counts):
        valid = True
    else:
        for c in ind:
            if c in counts and counts[c]>0:
                for cand in ma[c]:

                    flag, tmp = contain(cand, counts)
                    if flag:
                        re.append(cand)
                        v, restRe = toPhoneNum(tmp, ma, ind)
                        if v:
                            re.extend(restRe)
                            valid = True
                            return valid, re
                        else:
                            valid = False
                    else:
                        valid = False
                        
    return valid, re

def toNumber(re):
    m = {}
    for i in range(10):
        m[DIGITS[i]] = i

    newRe = []
    for d in re:
        newRe.append(m[d])
    newRe.sort()

    num = ''
    for n in newRe:
        num += str(n)
    return num


f = open('../data/GD/A-large.in', 'r')
ma, ind = preProcess()
t = int(f.readline().strip())
for i in range(t):
    counts = toCounts(f.readline().strip())
    valid, re = toPhoneNum(counts, ma, ind)
    print 'Case #%d: %s' % (i+1, toNumber(re))


