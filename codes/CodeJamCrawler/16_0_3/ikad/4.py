import time

f = open("in.txt","r")

out = open("out.txt","w")

out.write("Case #1:\n")

def isPrime(n):

    start = time.time()

    if n % 2 == 0:

        return 2

    if n % 3 == 0:

        return 3

    i = 5

    w = 2

    while i * i <= n:

        end = time.time()

        if(end-start > .1): #theres plenty more fish in the sea

            return 0

        if n % i == 0:

            return i

        i += w

        w = 6 - w

    return 0



print (f.readline())

p=f.readline()

print (p)

n,j=map(int, p.split())

binary = 2**(n-1)

jc=0
while len(bin(binary))==n+2:

    if (bin(binary)[2:][:1] != bin(binary)[-1:]) or (bin(binary)[:-1]=='1' and bin(binary)[2:][:1]=='1'):

        #print bin(binary)+" "+bin(binary)[2:][:1] +" "+bin(binary)[-1:]

        binary+=1

        continue

    s=''

    x=0

    flag=0

    for i in range(2,11):

        num = int(bin(binary)[2:],i)

        z=isPrime(num)

        if(z):

            s+=str(z)+" "

            #s+=str(int(bin(binary)[2:],i))+" "

            x+=1

        else:

            flag=1

            break

    if flag:

        binary+=1

        continue

    if x==9:

        print (str(jc)+" :"+ bin(binary)[2:]+" "+s)
        out.write(bin(binary)[2:]+" "+s+"\n")

        jc+=1

    if jc==j:

        break

    binary+=1
f.close()
out.close()


