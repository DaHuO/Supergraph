har = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
vij = {'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}
for x in xrange(int(raw_input())):
    astr = list(raw_input())
    clone = astr
    ans = []
    while len(clone) != 0 and any(ji in clone for ji in 'WGXZU'):
        if 'W' in clone:
            for j in 'TWO':
                clone.remove(j)
            ans.append('TWO')
        if 'G' in clone:
            for j in 'EIGHT':
                clone.remove(j)
            ans.append('EIGHT')
        if 'X' in clone:
            for j in 'SIX':
                clone.remove(j)
            ans.append('SIX')
        if 'Z' in clone:
            for j in 'ZERO':
                clone.remove(j)
            ans.append('ZERO')
        if 'U' in clone:
            for j in 'FOUR':
                clone.remove(j)
            ans.append('FOUR')
    #print ans,clone
    while len(clone) != 0:
        if 'O' in clone and 'N' in clone:
            for j in 'ONE':
                clone.remove(j)
            ans.append('ONE')
        elif 'T' in clone and 'R' in clone:
            for j in 'THREE':
                clone.remove(j)
            ans.append('THREE')
        elif 'F' in clone and 'V' in clone:
            for j in 'FIVE':
                clone.remove(j)
            ans.append('FIVE')
        elif 'S' in clone  and 'V' in clone:
            for j in 'SEVEN':
                clone.remove(j)
            ans.append('SEVEN')
        elif 'I' in clone and 'N' in clone:
            for j in 'NINE':
                clone.remove(j)
            ans.append('NINE')


    res = []
    for xi in ans:
        res.append(vij[xi])
    print 'Case #'+str(x+1)+':',''.join(map(str,sorted(res)))
