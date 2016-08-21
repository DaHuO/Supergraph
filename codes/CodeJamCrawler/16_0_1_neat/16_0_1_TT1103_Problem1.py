'''
Created on Apr 8, 2016

@author: TigerZhao
'''

f=open("A-large.in","r")
fout=open("test1.out","w")
cases = int(f.readline().strip())

def solve(n):
    seen=set()
    i =1;
    curNum = n
    while len(seen)<10:
        curNum = i*n 
        s = str(curNum)
        for x in xrange(len(s)):
            c = s[x]
            seen.add(c)
        i+=1
    return curNum
    

for i in xrange(cases):
    n= int(f.readline().strip())
    
    if n==0:
        fout.write("Case #{0}: INSOMNIA\n".format(i+1))
    else:
        fout.write("Case #{0}: {1}\n".format(i+1,str(solve(n))))



fout.close()
f.close()