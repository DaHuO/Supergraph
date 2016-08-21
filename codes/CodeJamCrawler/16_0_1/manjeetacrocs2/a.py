t=int(input()); j=1;
for _ in range(t):
    str1=input()
    if int(str1)==0:
        print("Case #{}: INSOMNIA".format(j))
        j+=1
        continue
    s=set(); s|=set(list(str1))
    sum1=int(str1);count=0
    while len(s)!=10:
        sum1+=int(str1); l3=list(str(sum1)); s|=set(l3)
    print("Case #{}: {}".format(j,sum1))
    j+=1