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

def test(str_):
    l = len(str_)
    d = [0] * l
    e = [0] * l
    for i in xrange(l):
        if i == 0:
            if str_[i] == '+':
                d[i] = 0
                e[i] = 1
            else:
                d[i] = 1
                e[i] = 0
        else:
            if str_[i] == '+':
                d[i] = min(d[i - 1], e[i - 1] + 1)
                e[i] = min(e[i - 1] + 2, d[i - 1] + 1) 
            else:
                d[i] = min(e[i - 1] + 1, d[i - 1] + 2)
                e[i] = min(e[i - 1], d[i - 1] + 1)
    return d[l - 1]

# print test("--+-")  # 3
# print test("+++")  # 0 
# print test("+-")  # 2
# print test("+")  # 0
# print test("-")  # 1

                     
if __name__ == "__main__":
    testcases = input()
        
    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        k = test(cipher)
        print("Case #%i: %i" % (caseNr, k))
