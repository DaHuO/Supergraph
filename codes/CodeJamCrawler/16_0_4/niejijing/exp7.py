import os

fp = open('D-small-attempt0.in')
of = open('lala5','w')
s = map(lambda x: x.strip().split(' '), fp.readlines())
cnt = 0
for t in s[1:]:
    cnt += 1
    strn=''
    if t[1]=='1' and t[0]>t[2]:
        print >>of, 'Case #%d: IMPOSSIBLE' % cnt

    if t[0]==t[2]:
        for vn in range(1, int(t[0])+1):
            strn = strn + ' ' + str(vn)
        print >>of, 'Case #%d:%s' % (cnt, strn)

