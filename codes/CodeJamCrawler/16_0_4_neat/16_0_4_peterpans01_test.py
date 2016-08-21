# def test(N):
#     if N == 0:
#         return -1
#     result = [_ for _ in xrange(10)]
#     for i in xrange(1, 10001):
#         k = N * i
#         m = str(k)
#         for s in m:
#             temp = int(s)
#             if temp in result:
#                 result.remove(int(s))
#         if len(result) == 0:
#             return k
#     return -1

# print test(1)
# print test(5)
# print test(15)
# print test(19)

# def test(str_):
#     l = len(str_)
#     d = [0] * l
#     e = [0] * l
#     for i in xrange(l):
#         if i == 0:
#             if str_[i] == '+':
#                 d[i] = 0
#                 e[i] = 1
#             else:
#                 d[i] = 1
#                 e[i] = 0
#         else:
#             if str_[i] == '+':
#                 d[i] = min(d[i - 1], e[i - 1] + 1)
#                 e[i] = min(e[i - 1] + 2, d[i - 1] + 1) 
#             else:
#                 d[i] = min(e[i - 1] + 1, d[i - 1] + 2)
#                 e[i] = min(e[i - 1], d[i - 1] + 1)
#     return d[l - 1]

import math
##def is_prime(n):
##    if n % 2 == 0 and n > 2: 
##        return 2
##    for i in range(3, int(math.sqrt(n)) + 1, 2):
##        if n % i == 0:
##            return i
##    return 1
##def convert_to_decmial(str_, base):
##    r = 0
##    for i in xrange(len(str_) - 1, -1, -1):
##        if str_[i] == '1':
##            r += math.pow(base, len(str_) - 1 - i)
##    return r

##def test(K, C, S):
##    count = 0
##    for num in xrange(2 ** (N - 1) + 1, 2 ** N, 2):
##        if count >= J:
##            break
##        if num > 3:
##            result = ""
##            str_ = bin(num)[2:].zfill(N)
##            result += str_ + " "
##            # print str_
##            b = True
##            for base in xrange(2, 11):
##                k = convert_to_decmial(str_, base)
##                # print k
##                d = is_prime(k)
##                if d > 1:
##                    result += str(d) + " "
##                else:
##                    b = False
##                    continue
##            if b:
##                print result
##                count += 1

# test(6, 3)

# print test("--+-")  # 3
# print test("+++")  # 0 
# print test("+-")  # 2
# print test("+")  # 0
# print test("-")  # 1
import itertools
def xor_string(a,b):
    c="0"*len(a)
    for k in xrange(len(a)):
        if a[k] != b[k]:
            c[k]='1'
    return c
def test(K, C, S):
    if K == 1:
        if S < 1:
            return "IMPOSSIBLE"
        else:
            return "1"
    if C == 1:
        if S < K:
            return "IMPOSSIBLE"
        else:
            return " ".join([str(_) for _ in xrange(1,K+1)])
##    res = []
##    p = "".join(['0' for _ in xrange(K-1)])
##    for seq in itertools.product("01", repeat=K-1):
##        k = xor_string(p,"".join(seq))
##        for i in xrange(len(k)):
##            if k[i] == '1':
##                if (i+2) not in res:
##                    res.append(i+2)
##    if S < len(res):
    if S < K-1:
        return "IMPOSSIBLE"
    else:
        #res.sort()
        return " ".join([str(_) for _ in xrange(2,K+ 1)])

##print "(2,3,2) :",test(2,3,2)
##print "(1,1,1) :",test(1,1,1)
##print "(2,1,1) :",test(2,1,1)
##print "(2,1,2) :",test(2,1,2)
##print "(3,2,3) :",test(3,2,3)



                     
if __name__ == "__main__":
    testcases = input()
         
    for caseNr in xrange(1, testcases + 1):
        K, C, S = raw_input().split()
        res = test(int(K), int(C), int(S))
        print("Case #%i: %s" % (caseNr, res))
        #print("Case #1:")
        
        
