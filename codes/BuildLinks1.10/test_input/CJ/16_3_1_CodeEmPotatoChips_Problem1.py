import sys

f1 = open("A-large.in", "r")
f2 = open("output.txt", "w")

t = int(f1.readline())
z = 0

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while(t > 0):
    z+=1
    n = int(f1.readline())
    k = f1.readline().split()
    arr = []
    for s in range(0, len(k)):
        k[s] = int(k[s])
    

    flag = 0
    i=0
    count = 0
    

    while(flag == 0):
        if k[i]!=0:
            k[i]-=1
            flag = 0
            arr.append(alpha[i])
            count = 0
        else:
            count+= 1

        i+=1

        if i >= n:
            i=0

        if count >= n:
            break

    f2.write("Case #"+str(z)+": ")

    if len(arr)%2!=0:
        #sys.stdout.write(arr.pop()+"\t")
        f2.write(arr.pop())
        while(len(arr) > 0):
            f2.write(" "+arr.pop()+""+arr.pop())

    else:
        st = ""
        while(len(arr) > 0):
            st+=arr.pop()+""+arr.pop()+" "
        st = st[:-1]
        f2.write(st)
    
        
    
    t-=1

    f2.write("\n")


f1.close()
f2.close()
