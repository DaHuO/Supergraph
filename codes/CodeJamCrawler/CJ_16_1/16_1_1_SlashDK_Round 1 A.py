t=input()
for i in range (0,int(t)):
    c=input()
    l=""
    start=c[0]
    end=c[0]
    for char in c:
        s1=l+char
        s2=char+l
        if(s1>=s2):
            l=s1
        else:
            l=s2
    print("Case #"+str(i+1)+": " + l)