import math
file = open("C-small-attempt0.in","r")
contents = file.readlines()
N = contents[1].strip().split(" ")[0]
J = contents[1].strip().split(" ")[1]
N=16
J=50
file.close()
results=[]

def not_prime(n):
    for i in range(3,int(math.sqrt(n)) + 1, 2):
        if n % 2 == 0:
            return 2
        if n % i == 0:
            return i
    return "prime"

gen="1"+"0"*(int(N)-2)+"1"
results=[]
while len(results)<int(J):
    failed=False
    tests=[]
    temp=[]
    for i in range(2,11):
        tests.append(int(gen,i))
    for test in tests:
        x = not_prime(test)
        if x!="prime":
            temp.append(str(x))
        else:
            failed=True
            break
    if failed==False:
        results.append([gen]+temp)
        temp=[]
    gen = str(bin(int(gen,2)+2)[2:])
print(results)
file=open("C-small-attempt0.out","w")
file.write("Case #1:\n")
for a in range(len(results)):
    file.write((" ").join(results[a])+"\n")
file.close()
        
