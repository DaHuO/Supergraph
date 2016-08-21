f=open('Test.in', 'r')
out=open('out.out','w')
T=int(f.readline())

def sheep(n):
    if n=="0":
        return "INSOMNIA"
    else:
        print(n)
        s=1
        digits=[x  for x in range(10)]
        while(len(digits)!= 0):
            print(s)
            a=str(int(n)*s)
            s=s+1
            for i in range(len(a)):
                if int(a[i])in digits:
                    digits.remove(int(a[i]))
        return a

for i in range(T):
    #print ("Case #"+str(i)+":"+sheep((f.readline()).strip()))
    out.write("Case #"+str(i+1)+": "+sheep((f.readline()).strip())+"\n")
