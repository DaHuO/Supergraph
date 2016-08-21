t = int(raw_input())
for i in range(t):
    n = 0
    x = int(raw_input())
    if x != 0 :
        num = [0,1,2,3,4,5,6,7,8,9]
        em = []
        while(num != em):
            n+=1
            x_d = list(str(n*x))
            for y in x_d:
                if int(y) in num:
                    num.remove(int(y))
            t-=1

        print "Case #"+ str(i+1)+": "+str(n*x)

    else:
        print "Case #"+ str(i+1)+": INSOMNIA"
