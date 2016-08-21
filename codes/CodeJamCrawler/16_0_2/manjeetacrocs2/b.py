t=int(input())
j=1
for _ in range(t):
    count=0;done=0
    str1=input()
    l1=list(str1)
    if l1.count('+')==len(l1):
        print("Case #{}: {}".format(j,count));j+=1; continue
    x=0
    while len(str1)!=l1.count('+'):
        step=0;x=0
        while x<len(str1) and l1[x]=='-':
            l1[x]='+'; x+=1; step=1
        if step!=0:
            count+=1
            step=0
        if l1.count('+')==len(l1):
            print("Case #{}: {}".format(j,count));j+=1; done=1; break
        x=0
        if done!=1:
            while x<len(str1) and l1[x]=='+':
                l1[x]='-'; x+=1; step=1
            if step!=0:
                count+=1
    