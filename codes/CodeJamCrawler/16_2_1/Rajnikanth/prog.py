t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":",
    s = raw_input()
    hs = [0]*26
    ls = []
    for i in s:
        hs[ord(i)-65]+=1
    if(hs[ord('z')-97]!=0):
        ls+=[0]*(hs[ord('z')-97])
        hs[ord('e')-97]-=hs[ord('z')-97]
        hs[ord('r')-97]-=hs[ord('z')-97]
        hs[ord('o')-97]-=hs[ord('z')-97]
        hs[ord('z')-97]-=hs[ord('z')-97]
    if(hs[ord('w')-97]!=0):
        ls+=[2]*(hs[ord('w')-97])
        hs[ord('t')-97]-=hs[ord('w')-97]
        hs[ord('o')-97]-=hs[ord('w')-97]
        hs[ord('w')-97]-=hs[ord('w')-97]
    if(hs[ord('u')-97]!=0):
        ls+=[4]*(hs[ord('u')-97])
        hs[ord('f')-97]-=hs[ord('u')-97]
        hs[ord('o')-97]-=hs[ord('u')-97]
        hs[ord('r')-97]-=hs[ord('u')-97]
        hs[ord('u')-97]-=hs[ord('u')-97]
    if(hs[ord('x')-97]!=0):
        ls+=[6]*(hs[ord('x')-97])
        hs[ord('s')-97]-=hs[ord('x')-97]
        hs[ord('i')-97]-=hs[ord('x')-97]
        hs[ord('x')-97]-=hs[ord('x')-97]
    if(hs[ord('g')-97]!=0):
        ls+=[8]*(hs[ord('g')-97])
        hs[ord('e')-97]-=hs[ord('g')-97]
        hs[ord('i')-97]-=hs[ord('g')-97]
        hs[ord('h')-97]-=hs[ord('g')-97]
        hs[ord('t')-97]-=hs[ord('g')-97]
        hs[ord('g')-97]-=hs[ord('g')-97]
    if(hs[ord('o')-97]!=0):
        ls+=[1]*(hs[ord('o')-97])
        hs[ord('n')-97]-=hs[ord('o')-97]
        hs[ord('e')-97]-=hs[ord('o')-97]
        hs[ord('o')-97]-=hs[ord('o')-97]
    if(hs[ord('t')-97]!=0):
        ls+=[3]*(hs[ord('t')-97])
        hs[ord('h')-97]-=hs[ord('t')-97]
        hs[ord('r')-97]-=hs[ord('t')-97]
        hs[ord('e')-97]-=hs[ord('t')-97]
        hs[ord('e')-97]-=hs[ord('t')-97]
        hs[ord('t')-97]-=hs[ord('t')-97]
    if(hs[ord('f')-97]!=0):
        ls+=[5]*(hs[ord('f')-97])
        hs[ord('i')-97]-=hs[ord('f')-97]
        hs[ord('v')-97]-=hs[ord('f')-97]
        hs[ord('e')-97]-=hs[ord('f')-97]
        hs[ord('f')-97]-=hs[ord('f')-97]
    if(hs[ord('s')-97]!=0):
        ls+=[7]*(hs[ord('s')-97])
        hs[ord('e')-97]-=hs[ord('s')-97]
        hs[ord('v')-97]-=hs[ord('s')-97]
        hs[ord('e')-97]-=hs[ord('s')-97]
        hs[ord('n')-97]-=hs[ord('s')-97]
        hs[ord('s')-97]-=hs[ord('s')-97]
    if(hs[ord('n')-97]!=0):
        ls+=[9]*(hs[ord('i')-97])
    ls.sort()
    ls = [str(i) for i in ls]
    print "".join(ls)
