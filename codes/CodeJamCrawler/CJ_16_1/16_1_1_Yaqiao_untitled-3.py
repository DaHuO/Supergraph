ls=[]
with open('A-large.in','r') as r:
    for lines in r:
        ls.append(lines.strip())
nums=int(ls[0])
f=open('A1_result.txt','w')
for i in range(nums):
    s=ls[i+1]
    ans=s[0]
    for j in range(1,len(s)):
        if ord(s[j])>=ord(ans[0]):
            ans=s[j]+ans
        else:
            ans=ans+s[j]
    f.write('Case #%d: %s'%(i+1,ans)+'\n')
f.close()
        