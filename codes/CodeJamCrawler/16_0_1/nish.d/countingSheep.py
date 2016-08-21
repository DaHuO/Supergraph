def digits(n):
    c=0
    i=1
    rec=set()
    if(n==0):
        return "INSOMNIA"
    while(c!=10):
        t=n*i
        s=str(t)
        rec.update(x for x in s)
        #print(rec)
        c=len(rec)
        i=i+1
    return t
#t=int(input())
d=0
readinp=open("A-large.in", 'r')
#print("YO")
target=open("output.txt", 'w')
t=int(readinp.readline())
while(t!=0):
    t=t-1
    d=d+1
    #n=int(input())
    n=int(readinp.readline())
    #print(n)
    #print("Case #" + str(d)+ ": " + str(digits(n)))
    target.write("Case #" + str(d)+ ": " + str(digits(n)))
    target.write("\n")
