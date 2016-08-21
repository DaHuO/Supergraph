import math

def GetNonTrivialDivisor(s):
    for j in range(2,int(math.ceil(math.sqrt(s)))):
        if s % j == 0:
            return j
        else:
            continue
    return -1

def GetAllNonTrivialDivisors(s):
    result = []
    ss = "{0:b}".format(s)
    for i in range(2,11):
        prime = GetNonTrivialDivisor(int(ss,i))
        if prime != -1:
            result.append(prime)
        else:
            return None
            
    return (s,result)

def getAnswer(n,j):
    jamcoines = []
    if n == 2:
        jamcoines = GetAllNonTrivialDivisors("11")
    else:
    
        for i in range(2**(n-2)):
            jamcoin = GetAllNonTrivialDivisors(i * 2 + 1 + 2**(n-1))
            if jamcoin is not None and len(jamcoines) < j:
                jamcoines.append(jamcoin)
            elif len(jamcoines) >= j:
                break
            
    return jamcoines
    


fi = open("input","r")
fo = open("output", "w")

t = int(fi.readline().strip())
n,j = map(int, fi.readline().strip().split())

result = getAnswer(n,j)
fo.write("Case #{0}:\n".format(1))
for i in result:
    fo.write("{0:b} {1}\n".format(i[0], " ".join(map(str, i[1]))))
          
fi.close()
fo.close()