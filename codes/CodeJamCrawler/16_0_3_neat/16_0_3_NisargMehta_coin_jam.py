def isprime(n):
    flag = 0
    for i in range(2,n//2):
        if(i>50000):
            return True
        if(n%i == 0):
            flag= 1
            break
    if(flag == 0):
        return(True)
    else:
        return(False)

# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
def getDivisor(n):
    div = []
    for i in range(2,n//2):
        if(i>50000):
            return False
        if(n%i == 0):
            return i

# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
def comb(l):
    import itertools
    output = []
    for s in itertools.product(range(2),repeat=l-2):
        no = "1"
        for s1 in s:
            no += str(s1)
        no += "1"
        output.append(no)
        if(len((output)) > 30000):
            break
    return(output)

# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

tc = int(input())
for i in range(tc):
    n,j = map(int,input().split())
    print("Case #"+str(i+1)+":")
    com = comb(n)
    #print(com)
    output = []
    for c in com:
        leave = 0 #to avoid adding value in output list if it is prime...
        valList = [int(c)]
        for base in range(2,11):
            val = int(c,base)
            #print("base:",base)
            if(isprime(val)):
                leave = 1
                break
            div = getDivisor(val)
            if(div == False):
                continue
            valList.append(div)
        #print("ValList:",valList)
        if(leave == 0):
            output.append(valList)
            if(len(output) >= j):
               break
#print(len(output))
for i in range(j):
    for a in output[i]:
        print(a,end=" ")
        #print(len(output))
    print()
#print(len(output))
