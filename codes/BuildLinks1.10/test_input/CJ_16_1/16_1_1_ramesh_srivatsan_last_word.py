t = int(raw_input())
for _ in range(t):
    s = str(raw_input())
    l = ''
    for i in range(len(s)):
        if l!='':
            if ord(s[i])>=ord(l[0]):
                l = s[i]+l
            else:
                l = l+s[i]
        else:
            l = l + s[i]
    print('Case #'+str(_+1)+': '+l)
