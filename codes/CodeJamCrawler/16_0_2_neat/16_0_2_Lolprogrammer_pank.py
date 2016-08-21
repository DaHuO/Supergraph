n = input()
ans = []
for i in range(0,n):
    s = raw_input()
    a = 0
    store = ""
    count = 0
    if len(s) == 1:
        if s == "+":
            count = 0
        else:
            count += 1
    if len(s) > 1:
        for l in range(1,len(s)):
            if s[a] == s[l]:
                store = s[l]
            if s[a] != s[l]:
                store = s[l]
                count += 1
            a+= 1
        if count == 1 and store == "-" and len(s) == 2:
            count += 1
        if s[len(s)-1] != s[len(s)-2] and store == "-" and len(s) > 2:
            count += 1
        if s[len(s)-1] == s[len(s)-2] and store == "-":
            count += 1
    ans.append(count)
for i in range(0,len(ans)):
    print "Case #"+str(i+1)+":"+" "+ str(ans[i])

