import re

p = re.compile('-+')
print(p.findall('-+-+-+-+'))


def func(line):#line[0]=='-'
    #中间有多少的 ---
    if line[0]=='-':
        return (len(p.findall(line))-1)*2
    else:
        return (len(p.findall(line))-1)*2+1


with open('A-small-attempt0.in') as f:
    n = int(f.readline())

    for i in range(n):
        line = f.readline()
        ans = func(line)
        if ans==-2:
            ans = 1
        elif ans ==-1:
            ans=0
        else:
            ans+=1
        print("Case #%d: %d"%((i+1),ans))


