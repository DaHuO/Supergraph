#this will give the last number needed before the cow has seen all the numbers

def countingSheep(n):
    if n == 0:
        return "INSOMNIA"
    else:
        listofNums = [False]*10
        i =1
        n1 = n
        while not (allTrue(listofNums)):
            n1 = n*i
            #print(n1)
            for k in str(n1):
                listofNums[int(k)] = True;
            i+= 1
        return n1

def allTrue(n):
    for n1 in n:
        if not n1:
            return False
    return True

#print(countingSheep(1692))


allnums = [0]*1000001
for i in range(0,len(allnums)):
    allnums[i]=countingSheep(i)

f = open('A2.in', 'r')
f1 = open('A2out.txt','w')
print(f.readline())
i = 1
for line in f:
    print("Case #%d: %s "%(i ,allnums[int(line)] ))
    f1.write("Case #%d: %s \n"%(i ,allnums[int(line)] ))
    i += 1
