n=int(input())
for i in range(1,n+1) :
        print("Case #{}:".format(i), end="")
        s=str(input())
        lth = len(s)
        a=0
        for j in range(0,lth-1) :
                if s[j]!=s[j+1] :
                        a=a+1

        if s[lth-1]=='-' :
                a=a+1

        print(" {}".format(a))

