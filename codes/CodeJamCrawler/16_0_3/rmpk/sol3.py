from functools import reduce

file = open('C-small-attempt0.in', 'r')
count1 = file.readline()
count1.strip()
secinput = file.readline()
yoyo = secinput.split(' ')

in1 = int(yoyo[0].strip())
in2 = (yoyo[1].strip())


x = ['0' for i in range(in1-1)]
y = ['1' for i in range(in1)]
x = '1'+ ''.join(x)
y = ''.join(y)
start = int(x,2)
stop = int(y,2)

numlist = []

for i in range(start,stop):
    num = bin(i).split('0b')[1]
    numlist.append(num)

def check1(a):
    toremove = []
    for i in range(len(a)):
        j = a[i]
        if j[-1]!='1':
            toremove.append(i)
    for i in toremove:
        a[i] = 'Yo'
    
    return a

finnum = check1(numlist)
finnum = [x for x in finnum if x!='Yo']

def is_prime(a):
    if a==2:
        return True
    if not a&1:
        return False
    return pow(2,a-1,a)==1

def checkprime(a):
    diffbase = [int(a,i) for i in range(2,11)]
    for i in diffbase:
        j = is_prime(i)
        if j==True:
            return False
    return diffbase

findiv = []

finbin = []
for i in finnum:
    j = checkprime(i)
    if j == False:
        continue
    finbin.append(i)
    findiv.append(j)
    if len(findiv)==in2:
        break

def getdiv(n):
    a = list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5)+1) if n%i ==0))))
    a.sort()
    x = a[len(b)//2]
    return x

finlist = []

for i in findiv:
    templist = []
    for j in i:
        v = getdiv(j)
        templist.append(v)
    finlist.append(templist)

file.close()

file1 = open("Output.txt", "w")

file1.write('Case #1:\n')
for i in range(50):
    b = [str(x) for x in finlist[i]]
    x1 = ' '.join(b)
    file1.write('{} {}\n'.format(int(finbin[i]), x1))
file1.close()