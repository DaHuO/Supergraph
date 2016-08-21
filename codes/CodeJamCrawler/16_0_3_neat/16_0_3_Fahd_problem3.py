import math
T = input()
fle = open("output.txt","w")
fle.write("Case #1:"+"\n")
def divisor(n):
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i
def jamcoin(s):
    for i in xrange(s,1000):
        a = bin(i)[2:]
        a = "0"*(n-len(a))+a if len(a) < n else a
        a = "1"+a+"1"
        c = [int(a,I) for I in range(2,11)]
        if None not in [divisor(d) for d in c]:
            return [[a]+[divisor(d) for d in c],i]
N, J = map(int,raw_input().split())
s = 0
n = N-2
for w in range(J):
    lst = jamcoin(s)
    s = lst[1]+1
    ans = " ".join(str(a) for a in lst[0])
    fle.write(ans+"\n")
    print ans
fle.close()