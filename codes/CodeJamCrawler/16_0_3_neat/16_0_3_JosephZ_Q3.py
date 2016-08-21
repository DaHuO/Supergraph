
import math
def primecheck(t):
    for i in range(2,min(int(t**0.5+1),100)):
        if t%i==0:
            return False
    return True

def divisorreturn(t):
    for i in range(2,int(t**0.5+1)):
        if t%i==0:
            return str(i)	

N=30
result=[]
for i in range(int("1"*N,2)+1):
    temp=bin(i)[2:]
    while len(temp)<N:
        temp="0"+temp
    num="1"+temp+"1"
    switch=True
    for j in range(2,11):
        if primecheck(int(num,j)):
            switch=False
            break
    if switch:
        print(num)
        result.append(num)
        if len(result)==500:
            break

f2=open("output_2.txt",'w+')
f2.write("Case #1:\n")
for i in range(len(result)):
    line=str(result[i])
    for j in range(2,11):
        line=line+" "+divisorreturn(int(result[i],j))
    line=line+"\n"
    f2.write(line)
f2.close()
print("done")


