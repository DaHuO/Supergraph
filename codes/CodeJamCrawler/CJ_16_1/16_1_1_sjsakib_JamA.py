t = int(raw_input())

for i in range(t):
    s = raw_input()
    n = s[0]
    for j in range(1,len(s)):
        if(s[j]>=n[0]):
            n = s[j]+n
        else:
            n = n+s[j]
    print "Case #{}: {}".format(i+1,n)
