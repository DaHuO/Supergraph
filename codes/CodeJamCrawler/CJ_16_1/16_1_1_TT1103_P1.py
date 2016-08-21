'''
Created on Apr 14, 2016

@author: TigerZhao
'''
f=open("A-large.in","r")
fout=open("test1.out","w")
cases = int(f.readline().strip())

def solve(word):
    ans=""
    for n in word:
        if len(ans)==0:
            ans=n 
        elif n >= ans[0]:
            ans=n+ans 
        else:
            ans=ans+n 
            
    return ans
    
for i in xrange(cases):
    n= list(f.readline().strip())
    
    fout.write("Case #{0}: {1}\n".format(i+1,solve(n)))
