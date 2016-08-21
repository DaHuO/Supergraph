alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def plan(tc):
    s = ''
    while sum(tc)>0:
        m = max(tc)
        i1 = tc.index(m)
        tc[i1]-=1
        s += alphabet[i1]
        m = max(tc)
        if m==0:
            # caatare neam lahanit, si ar trebui ultimu pidar del bagat mai inainte
            s = s[:-4]+s[-1]+s[-2]+s[-4:-2]
            continue
        i2 = tc.index(m)
        tc[i2]-=1 
        s+= alphabet[i2]
        s+= ' '
        print tc
    print 'hui'
    return s   


f = open('input.txt', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    k = f.readline() #read number of parties but ignore it
    l = f.readline()
    l = l.split(' ')
    s = []
    for e in l:
        #print "'",e,"'"
        s.append(int(e))
    tcs.append(s)

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, plan(tcs[i])))
f.close()


