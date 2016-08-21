# codejam



def solve(n):

    if n==0:
        return "INSOMNIA"
    
    seen=set()
    m=0

    for i in range(1000):
        m=m+n
        seen.update(str(m))
        if len(seen)==10:
            return str(m)


text=open("C:\\Users\\Jon\\Dropbox\\codejam2016\\A-large.in").read()

outfile=open("C:\\Users\\Jon\\Dropbox\\codejam2016\\a_large_out.txt","w")


rows=[int(x) for x in text.split('\n') if x]

allout=[]
N=rows[0]
for i in range(N):
    n=rows[i+1]
    allout.append('Case #%d: %s'%(i+1,solve(n)))

out='\n'.join(allout)
print out
outfile.write(out)
outfile.close()
