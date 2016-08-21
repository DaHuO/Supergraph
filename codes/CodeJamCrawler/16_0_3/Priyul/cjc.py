import math

def isprime(num):
    for i in range(2,200):
        if(num%i) == 0 :
            return 1,i
    return 0,1

fin = open('C-large.in','r')
fout = open('op1.in','w')
T = int(fin.readline())
#for i in range(0,T+1):
str1 = "Case #1:\n"
fout.write(str1)
line = fin.readline()
words = line.split()
N = int(words[0])
#J=550
J = int(words[1])
counter = 0
for x in range( 2147483649,4294967295,2):
    if counter == J:
        break
    l = list()
    b = list()
    binary = bin(x)
    binary = binary[2:]
    b.append(binary)
    for y in range(2,11):
        nonprime,value= isprime(int(binary,y))
        if nonprime == 0:
            #l = []
            #b = []
            break
        else:
            l.append(str(value))
    if nonprime == 1:
        counter = counter+1 
        str1 = "".join(b)+ " " + " ".join(l) + "\n"
        if(str1 != " "):
            print(str1)
            fout.write(str1)
fin.close()
fout.close()

    
