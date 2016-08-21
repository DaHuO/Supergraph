fi=open('inp.in','r')
fo=open('outp.in','w')

t=int(fi.readline().rstrip('\n'))
outs=''
for case in range(1,t+1):
    s=fi.readline().rstrip('\n')
    l=len(s)
    a=[0 for i in range(26)]
    for i in range(l):
        a[ord(s[i])-ord('A')]+=1
    num=[0 for i in range(10)]
    num[0]+=a[ord('Z')-ord('A')]
    a[ord('E')-ord('A')]-=a[ord('Z')-ord('A')]
    a[ord('R') - ord('A')] -= a[ord('Z')-ord('A')]
    a[ord('O') - ord('A')] -= a[ord('Z')-ord('A')]
    a[ord('Z') - ord('A')]=0
    num[8]+=a[ord('G')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('G')-ord('A')]
    a[ord('I') - ord('A')]-=a[ord('G')-ord('A')]
    a[ord('H') - ord('A')]-=a[ord('G')-ord('A')]
    a[ord('T') - ord('A')]-=a[ord('G')-ord('A')]
    a[ord('G') - ord('A')]=0
    num[2]+=a[ord('W')-ord('A')]
    a[ord('T') - ord('A')]-=a[ord('W')-ord('A')]
    a[ord('O') - ord('A')]-=a[ord('W')-ord('A')]
    a[ord('W') - ord('A')]=0
    num[4]+=a[ord('U')-ord('A')]
    a[ord('F') - ord('A')]-=a[ord('U')-ord('A')]
    a[ord('O') - ord('A')]-=a[ord('U')-ord('A')]
    a[ord('R') - ord('A')]-=a[ord('U')-ord('A')]
    a[ord('U') - ord('A')]=0
    num[6]+=a[ord('X')-ord('A')]
    a[ord('S') - ord('A')]-=a[ord('X')-ord('A')]
    a[ord('I') - ord('A')]-=a[ord('X')-ord('A')]
    a[ord('X') - ord('A')]=0
    num[3]+=a[ord('R')-ord('A')]
    a[ord('T') - ord('A')]-=a[ord('R')-ord('A')]
    a[ord('H') - ord('A')]-=a[ord('R')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('R')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('R')-ord('A')]
    a[ord('R') - ord('A')]=0
    num[5]+=a[ord('F')-ord('A')]
    a[ord('I') - ord('A')]-=a[ord('F')-ord('A')]
    a[ord('V') - ord('A')]-=a[ord('F')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('F')-ord('A')]
    a[ord('F') - ord('A')]=0
    num[1]+=a[ord('O')-ord('A')]
    a[ord('N') - ord('A')]-=a[ord('O')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('O')-ord('A')]
    a[ord('O') - ord('A')]=0
    num[7]+=a[ord('S')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('S')-ord('A')]
    a[ord('V') - ord('A')]-=a[ord('S')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('S')-ord('A')]
    a[ord('N') - ord('A')]-=a[ord('S')-ord('A')]
    a[ord('S') - ord('A')]=0
    num[9]+=a[ord('I')-ord('A')]
    a[ord('N') - ord('A')]-=a[ord('I')-ord('A')]
    a[ord('N') - ord('A')]-=a[ord('I')-ord('A')]
    a[ord('E') - ord('A')]-=a[ord('I')-ord('A')]
    a[ord('I') - ord('A')]=0

    nn=''
    for i in range(0,10):
        nn+=(str(i)*num[i])
    outs+=('Case #'+str(case)+': '+nn+'\n')

fo.write(outs)
fi.close()
fo.close()