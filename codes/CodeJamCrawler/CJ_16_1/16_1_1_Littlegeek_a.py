inf = open('a.in','r')
out = open('a.out','w')

T = int(inf.readline())

for case in range(1,T+1):
    S = inf.readline().strip()
    st = S[0]
    for s in S[1:]:
        if (st[0] <= s):
            st = s + st
        else:
            st = st + s
    out.write('Case #' + str(case) + ': ' + st + '\n')

inf.close()
out.close()
