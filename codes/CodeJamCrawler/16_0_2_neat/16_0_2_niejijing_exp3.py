import os

def rindex(s, ch):
    m = 0;
    while m!=-len(s):
        m -= 1
        if s[m]==ch:
            return len(s)+m

    raise ValueError




def find_flip(sk, ch):
    if ch == '+':
        if sk==['-']:
            return 1
        try:
            idx = rindex(sk,'-')
        except:
            return 0

        return 1 + find_flip(sk[0:idx+1], '-')
    if ch == '-':
        if sk==['+']:
            return 1
        try:
            idx = rindex(sk,'+')
        except:
            return 0

        return 1 + find_flip(sk[0:idx+1], '+')


fp = open('B-large.in')
of = open('lala2-large','w')
fp.seek(0, 0)
s = map(lambda x: list(x)[0:-1], fp.readlines())
s = s[1:]
seq = 0
for l in s:
    seq += 1
    print >>of, 'Case #%d: %d' % (seq, find_flip(l, '+'))

of.close()
fp.close()