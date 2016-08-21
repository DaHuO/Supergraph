# codejam



def solve(s):
    s=s+'+'
    a=0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            a+=1
    return a


text=open("C:\\Users\\Jon\\Dropbox\\0_codejam2016\\Qual_B\\B-large.in").read()


outfile=open("C:\\Users\\Jon\\Dropbox\\0_codejam2016\\Qual_B\\b_out.txt","w")


rows=[x for x in text.split('\n') if x]

allout=[]
N=rows[0]
for i in range(int(N)):
    n=rows[i+1]
    allout.append('Case #%d: %s'%(i+1,solve(n)))

out='\n'.join(allout)
print out
outfile.write(out)
outfile.close()
