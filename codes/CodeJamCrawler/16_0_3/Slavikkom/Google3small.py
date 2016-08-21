file = open('C:\\Users\\V\\Downloads\\Google11.txt','r')
f = file.read()
res = f.split("\n")
def getprime(n, a):
    k = 0
    l = 0
    while n >= 1:
        d = n % 10
        k = k + d * (a ** l) 
        n = n / 10
        l = l + 1
    i = 2
    while i <= (k ** 0.5):
        if k % i == 0:
            return i
        else:
            i = i + 1
    return 0
def getbin(a, n):
    b = []
    while a >= 1:
        d = a % 2
        b.append(d)
        a = a / 2
    k = len(b)
    while k < n - 2:
        b.append(0)
        k = k + 1
    ans = 1 + 10 ** (n - 1)
    k = 1
    for i in b:
        ans = ans + i * (10 ** k)
        k = k + 1
    return ans
#print res
T = int(res[0])
#T = int(input())
#print T
file.close()
file = open('C:\\Users\\V\\Downloads\\Google3small.txt','w')
for i in range(0, T):
    tt = res[i + 1]
    pp = tt.split(" ")
    #print pp
    n = int(pp[0])
    j = int(pp[1])
    #print n, j
    file.write("Case #" + str(i + 1) + ": " + "\n")
    k = 0
    m = 0
    while k < j and m < 50:
        a = 2 ** (n - 2) 
        for p in range(a):
            l = getbin(p, n)
            lis = []
            for o in range(2, 11):
                lis.append(getprime(l, o))
            if not 0 in lis:
                #print l, lis
                file.write(str(l) + " ")
                c = 0
                for v in lis:
                    if c < len(lis) - 1:
                        file.write(str(v) + " ")
                    else:
                        file.write(str(v) + "\n")
                    c = c + 1    
                k = k + 1
                if k >= j:
                    break
        m = m + 1       
file.close()        