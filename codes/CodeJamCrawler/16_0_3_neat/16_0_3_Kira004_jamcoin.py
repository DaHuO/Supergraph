from sys import argv
from math import sqrt
class Solution(object):
    def jamcoin(self, n, j):
        res = []
        
        def genCode(code):
            carry = 1
            code = list(map(int, code))
            for i in range(len(code)-1,-1,-1):
                if carry == 0:
                    break
                else:
                    code[i] += carry
                    carry = code[i]-1
                    code[i] %= 2
            return  "".join(map(str, code))

        def kBase(s, k):
            n = len(s)-1
            val = 0
            for c in s:
                if c == '1':
                    val += k**n
                n -= 1
            return val

        def isPrime(val):
            limit = min(int(10e6), int(sqrt(val)))
            for i in range(2, limit+1):
                if val % i == 0:
                    return i
            return -1

        #test
        code = "0"*(n-2)
        while len(res) < j:
            jam = ["1"+code+"1"]
            code = genCode(code)
            for i in range(2, 11):
                kk = kBase(jam[0], i)
                t = isPrime(kk)
                if t == -1:
                    break
                jam.append(str(t))
            if len(jam) == 10: 
                res.append(jam) 

        return res
            

if __name__ == "__main__":
    filename = argv[1]
    try:
        f = open(filename)
        nf = open(filename[:-2]+"out", "w")

        sol = Solution()
        n = int(f.readline())
        for i in range(n):
            nn, jj = list(map(int, f.readline().strip().split()))
            t = sol.jamcoin(nn, jj)
            nf.write("Case #%d:\n" % (i+1))
            for j in range(jj):
                for k in range(len(t[j])):
                    nf.write("%s " %t[j][k])
                nf.write("\n")
    except IOError:
        print ("No such file: %s" % filename)
