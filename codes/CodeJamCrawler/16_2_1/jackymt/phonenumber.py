l = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')
count = {}
for i, k in enumerate(l):
    x = {}
    for c in k:
        if c not in x:
            x[c] = 0
        x[c] += 1
    count[i] = x


def possible(s):
    i_count = {}
    for c in s:
        if c not in i_count:
            i_count[c] = 0
        i_count[c] += 1
    rs = []
    for k, v in count.iteritems():
        ok = True
        for c, x in v.iteritems():
            need = x
            have = i_count.get(c, 0)
            if need > have:
                ok = False
        if ok:
            rs.append(k)
    return rs

def take(i, s):
    i_count = {}
    for c in s:
        if c not in i_count:
            i_count[c] = 0
        i_count[c] += 1
    rs = []
    v = count[i]
    for c, x in v.iteritems():
        need = x
        have = i_count.get(c, 0)
        i_count[c] = have - need
    rs = []
    for k, v in i_count.iteritems():
        if v > 0:
            rs.extend([k] * v)

    return ''.join(rs)
            

def solution(s):
    p = possible(s)
    r = []
    if not p:
        return None
    else:
        for kp in p:
            r.append(kp)
            rm = take(kp, s)
            if rm == '':
                return r
            else:
                t = solution(rm)
                if not t:
                    r = r[:-1]
                    continue
                r.extend(t)
                return r
    return r

def _soln(s, p):
    r = []
    for kp in p:
        r.append(kp)
        rm = take(kp, s)
        _soln()

'''
def solution(s):
    l = ('ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE')
    count = {}
    for i, k in enumerate(l):
        x = {}
        for c in k:
            if c not in x:
                x[c] = 0
            x[c] += 1
        count[i] = x
    i_count = {}
    for c in s:
        if c not in i_count:
            i_count[c] = 0
        i_count[c] += 1
    rs = []
    items = sorted((k, v) for k, v in count.items())
    cur = 0
    while cur < 10:
        k, v = items[cur]
        ok = True
        for c, x in v.iteritems():
            need = x
            have = i_count.get(c, 0)
            if need > have:
                ok = False
        if ok:
            rs.append(k)
            for c, x in v.iteritems():
                need = x
                have = i_count.get(c, 0)
                i_count[c] = have - need
        else:
            cur += 1
    for k, v in i_count.iteritems():
        if v > 0:
            print k

'''

with open('input', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            line = line.strip('\n')
            x = solution(line)
            x = ''.join(map(str, x))
            print "Case #{}: {}".format(i, x)

'''
print solution('OFREEVSRZUEON')
print solution('OURNEONFOE')
print solution('ONOENEXIS')
'''