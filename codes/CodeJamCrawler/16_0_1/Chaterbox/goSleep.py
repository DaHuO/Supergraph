f=open("/Users/macbookPro/downloads/res.txt",'w')
def goSleep(N):
    if N==0:
        return "INSOMNIA"
    n=str(N)
    digits={i for i in n}
    j=1
    while(len(digits)!=10):

       n = str(N*j)
       s={i for i in n}
       digits.update(s)
       print(digits)
       j+=1
    return n
x=int(input())
for i in range(x):
    f.write("Case #" + str(i + 1) + ": " + goSleep(int(input())))
    f.write("\n")