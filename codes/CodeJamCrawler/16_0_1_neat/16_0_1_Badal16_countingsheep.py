
def removedigits(num):
    for c in num:
        if int(c) in digits:
            digits.remove(int(c))

f = open('/Users/mac/Desktop/A-small-attempt0.in','r')
fout = open('/Users/mac/Desktop/output','w')
cases = int(f.readline())
casenum = 1
for line in f:
    digits = [0,1,2,3,4,5,6,7,8,9]
    N = line.strip()
    if N == '0':
        print >>fout, 'Case #%d: INSOMNIA'%(casenum)
        casenum +=1
        continue
    i=1
    while digits:
        #print N
        num = str(int(N)*i)
        removedigits(num)
        i +=1
    print >>fout, 'Case #%d:'%(casenum), num
    casenum += 1
f.close()
fout.close()