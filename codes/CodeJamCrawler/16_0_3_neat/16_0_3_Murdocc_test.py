
def check(s):
    n=len(s)
    for i in range(len(s)-1,-1,-1):
        if(s[i]=='-'):
            return i
    return -1


def rotate(idx,s):
    n=len(s)
    k=''
    for i in range(idx+1):
        if(s[i]=='-'):
            k=k+'+'
        else:
            k=k+'-'
    finalr=''.join(reversed(k))+s[idx+2:n]
    return finalr

n=int(raw_input())
for i in range(n):
    s=raw_input()
    count=0
    for j in range(len(s)):
        temp=check(s)
        if(temp==-1):
            break
        else:
            count+=1
            s=rotate(temp,s)
    print("Case #{}: {}".format(i+1,count))



