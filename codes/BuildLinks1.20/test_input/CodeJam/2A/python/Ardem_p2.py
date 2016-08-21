fin = open('B.in', 'r')
fout = open('file.out', 'w')
n = fin.readline()
chars = ['P','R','S']
cache = {}
def dp(n,vals):
    #print '*',vals
    if (vals[0],vals[1],vals[2]) in cache:
        return cache[(vals[0],vals[1],vals[2])]
    out = ''
    if sum(vals) <= 2:
        for i,v in enumerate(vals):
            if v == 1:
                out += chars[i]
        return out
    greater = map(lambda x:0 if x < 2**n/3. else 1,vals)
    #print '-',greater
    if sum(greater) == 2:
        for i,v in enumerate(greater):
            if v == 1:
                base = (max(vals)-1)/2
                temp = [base,base,base]
                temp[i] += 1
                #print temp,vals
                out += dp(n-1,temp)
    else:
        for i,v in enumerate(greater[::-1]):
            if v == 0:
                base = (max(vals))/2
                temp = [base,base,base]
                temp[2-i] -= 1
                #print temp,vals
                out += dp(n-1,temp)
    cache[(vals[0],vals[1],vals[2])] = out          
    return out
            
    
for l in range(int(n)):
    n,r,p,s = map(int,fin.readline().split())
    #print 2**n/3., r, p, s
    if max(map(lambda x:abs(2**n/3. - x),[p,r,s])) > 1:
        fout.write("Case #%d: IMPOSSIBLE\n"%(l+1))
    else:
        fout.write("Case #%d: %s\n"%(l+1,dp(n,[p,r,s])))
    
fin.close()
fout.close()
