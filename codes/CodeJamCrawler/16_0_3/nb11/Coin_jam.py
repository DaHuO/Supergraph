import math

def yacsu(n):
    i=2
    while i<n:
        if n%i == 0:
            return i
        i = i+1

def isPrime(n):
    P = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            P = False
            break
    return P

def convert(n, base):
    l = len(n)
    if n[l-1] == '1':
        r=1
    else:
        r=0
    l = l-1
    i=1
    while l > 0:
        i = i*base
        if n[l-1] == '1':
            r = r + i
        l = l-1
    return r

temp=0
def result(s):
    global temp
    l = int(s)

    coin = "1"
    pre = bin(temp)
    pre = pre.replace("b","")

    preLen = len(pre)

    while preLen < l-2:
        coin = coin+"0"
        preLen = preLen+1
    coin = coin+pre
    coin = coin+"1"

    key = coin
    i=2
    while i <= 10:
        k = convert(coin,i)

        if isPrime(k):
            temp=temp+1
            return result(s)


        key = key + " " + str(yacsu(k))
        i = i+1

    temp = temp +1
    print key
    return key


def coin_jam():
    f = open("C-small-attempt1.in", "r")
    case = int(f.readline() )

    N_J = f.readline()
    N_J = N_J.split()

    N = N_J[0]
    J = N_J[1]

    f2 = open("output.txt","w")
    i=1
    while i <= case:
        f2.write( "Case #" + str(i) + ":\n")
        j=0
        while j < int(J):
            f2.write( result(N) + "\n" )
            j = j+1
        i = i+1

    f2.close()
    f.close()
coin_jam()