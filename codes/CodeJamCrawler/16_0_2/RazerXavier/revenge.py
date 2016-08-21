case = int(input())
for i in range(1,case+1):
    s = list(input())
    count = 0
    test = 0
    if len(s)==1:
        if s[0]=='-':
            print("Case #"+str(i)+": 1")
        else:
            print("Case #"+str(i)+": 0")
        continue
    while test<len(s):
        test = 0
        j = 0
        p1 = p2 = p3 = 0
        for d in range(len(s)):
            if s[d]=='+':
                test+=1
        for j in range(len(s)-1):
            if s[j]=='+' and s[j+1]=='-':
                p1 = 1
                break
            elif s[j]=='-' and s[j+1]=='+':
                p2 = 1
                break
            elif s[j+1]=='-' and j+1==len(s)-1:
                p3 = 1
                break
        if p1 == 1:
            count+=1
            for x in range(j+1):
                s[x] = '-'
        elif p2 == 1:
            count+=1
            for x in range(j+1):
                s[x] = '+'
        elif p3 == 1:
            count+=1
            for x in range(len(s)):
                s[x] = '+'
    print("Case #"+str(i)+":",count)

