
x=open("A-large.in","r")
s=x.read().split()



def sleep(n):                    # n is string
    if n=="0":return "INSOMNIA"
    a={0,1,2,3,4,5,6,7,8,9}
    b={int(i) for i in n}
    i=2
    while(a!=b):
        x=str(i*int(n))
        i+=1
        b.update({int(i) for i in x})
    return x
        
a=int(s[0])
output = open("output.txt","w")

for i in range(a):
    output.write("Case #"+str(i+1)+": "+sleep(s[i+1])+"\n")

output.close()
x.close()
