case = int(input())
for z in range(1,case+1):
    s = input()
    ns = s[0]
    for i in range(1, len(s)):
        if s[i] >= ns[0]:
            ns = s[i]+ns
        else:
            ns = ns+s[i]
    print("Case #"+str(z)+":",ns)
