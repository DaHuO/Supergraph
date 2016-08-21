t=input()
value=set()
c = 1
while not (t is 0):
    n=input()
    t=t-1
    count=1
    if n==0:
        print "Case #" + str(c) + ": " + "INSOMNIA"
    else:
        while len(value) is not 10:
            tot=count*n
            value=value.union(list(str(tot)))
            count=count+1
        print "Case #" + str(c) + ": " , tot
    c = c + 1
    value=set()
