t=input()

for j in range(t):
    s=raw_input()
    n=len(s)
    ans=s[:1]
    for i in range(1,n):
        if s[i:i+1]>=ans[:1]:
            ans=s[i:i+1]+ans
        else:
            ans=ans+s[i:i+1]
    out='Case #'+str(j+1)+': '+ans
    print out
