def turnover(s):
    start=0
    end=len(s)-1
    count=0
    while end>=start:
        while s[end] and start<=end:
            end-=1
        if start>end:
            break
        tur=start
        while tur<end and s[tur]:
            tur+=1
        if start<tur:
            s[start:tur]=[0 for i in range(tur-start)]
            count+=1
        tmp=s[:end+1]
        tmp.reverse()
        for i in range(len(tmp)):
            tmp[i]=not tmp[i]
        s[:end+1]=tmp
        count+=1
    return count


ls=[]
with open('python/B-small-attempt0.in','r') as r:
    for lines in r:
        ls.append(lines.strip())
f=open('bbaa.txt','w')
nums=int(ls[0])
for i in range(nums):
    s=ls[i+1]
    array=[]
    for j in range(len(s)):
        if s[j]=='+':
            array.append(1)
        else:
            array.append(0)
    n=turnover(array)
    f.write('Case #%d: %d'%(i+1,n)+'\n')    
f.close()
