import string

letters = list(string.ascii_uppercase)
print letters

with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def find_plan(np):
    ans = []
    n = len(np)
    paties = letters[:n]
    d = dict(zip(paties, np))

    while d:
        pd = {}
        for k, v in d.iteritems():
            pd.setdefault(v, []).append(k)
        paired_keys = []
        unpaired_keys = []
        for k, v in pd.iteritems():
            if len(v) > 1:
                paired_keys.append(v)
            else:
                unpaired_keys.append(v)
        if paired_keys:
            for parties in unpaired_keys:
                for p in parties:
                    ans.append((str(p) + ' ') * d[p])
                    del d[p]
            for parties in paired_keys:
                for p in parties[:-2]:
                    ans.append((str(p) + ' ') * d[p])
                    del d[p]
                pp1 = parties[-1]
                pp2 = parties[-2]
                ans.append((str(pp1) + str(pp2) + ' ') * d[pp1])
                del d[pp1]
                del d[pp2]
        else:
            dd = sorted(pd.keys())[-2:]
            max1 = dd[1]
            max2 = dd[0]
            diff = max1 - max2
            ppp = pd[max1][0]
            ans.append((str(ppp) + ' ') * diff)
            d[ppp] = d[ppp] - diff

    ans = ''.join(ans)
    return ans

f = open('out.txt', 'w')
for j, i in enumerate(xrange(1, 2 * t, 2)):
    print '==========================='
    n = int(lines[i])
    np = [int(p) for p in lines[i + 1].split(' ')]
    assert len(np) == n
    plan = find_plan(np)
    f.write('Case #%s: %s \n' % (j+1, plan))
    print 'Case #%s: %s' % (j+1, plan)
f.close()
