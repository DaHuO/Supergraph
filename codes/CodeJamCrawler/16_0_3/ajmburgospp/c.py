# lim = 10**8
# p = [-1]*lim
# p[0] = p[1] = 0
# plist = []
# for i in xrange(2, lim):
#     if p[i] == -1:
#         plist.append(i)
#         for j in xrange(i**2, lim, i):
#             p[j] = i

# def fac(x):
#     if x < lim:
#         return x if p[x] < 0 else p[x]
#     else:
#         for i in plist:
#             if x%i == 0:
#                 return i
#             if i*i > x:
#                 return x
#         i = plist[-1]
#         while i*i <= x:
#             if x%i == 0:
#                 return i
#         return x


# h = 2**15
# c = 0
# for i in xrange(2**13):
#     m = bin(h + i*2 + 1)[2:]
#     sols = []
#     ok = True
#     for i in xrange(2,11):
#         r = int(m, i)
#         f = fac(r)
#         if f == r:
#             ok = False
#             break
#         sols.append(str(f))
#     if ok:
#         c += 1
#         print m, ' '.join(sols)
#     if c == 50:
#         break

print """Case #1:
1000000000000001 11 271 5 2 7 2 3 2 7
1000000000000101 13 251 3 4751 173 3 53 109 3
1000000000000111 23 5 5 2 7 2 3 2 11
1000000000001001 73 757 3 19 19 3 5 19 3
1000000000001101 7 947 5 2 7 2 3 2 11
1000000000010011 3 7 5 2 7 2 3 2 7
1000000000011001 17 97 5 2 7 2 3 2 11
1000000000011011 7 1567 15559 6197 5 5 1031 7 83
1000000000011111 29 523 3 2 7 2 3 2 3
1000000000100101 5 7 5 2 7 2 3 2 7
1000000000101011 3 563 13 3 5 43 3 73 7
1000000000101111 5 17 3 2 37 2 5 2 3
1000000000110001 3 3169 5 2 7 2 3 2 11
1000000000110101 23 47 11 23 5 299699 43 239 59
1000000000110111 7 499 3 2 7 2 3 2 3
1000000000111011 17 41 3 2 73 2 17 2 3
1000000000111101 31 2 3 2 7 2 3 2 3
1000000001000011 11 61 5 2 7 2 3 2 11
1000000001001001 89 47 5 2 7 2 3 2 7
1000000001001111 3 3229 3 2 7 2 3 2 3
1000000001010101 47 7 13 3 5 17 3 53 7
1000000001010111 5 127 3 2 37 2 5 2 3
1000000001011001 103 2153 281 101 5 67 5 13 19
1000000001011011 3 7 3 2 7 2 3 2 3
1000000001011101 17 1699 3 2 1297 2 11 2 3
1000000001011111 59 113 7 157 19 1399 7 43 107
1000000001100001 7 5 5 2 7 2 3 2 11
1000000001100011 23 19 11 105491 5 47 11117 1787 127
1000000001100111 3 149 3 2 7 2 3 2 3
1000000001101011 5 5 3 2 37 2 5 2 3
1000000001101101 13 7 3 2 7 2 3 2 3
1000000001110011 113 863 3 2 7 2 3 2 3
1000000001110101 5 5 3 2 37 2 5 2 3
1000000001111001 19 2 3 2 7 2 3 2 3
1000000001111011 31 557 7 19 23 1129 7 5441 241
1000000001111101 127 1093 43 17 55987 23 7 7 31
1000000001111111 43 41 5 2 7 2 3 2 7
1000000010000011 167 2 11 2 58427 2 23 2 839
1000000010000101 11 919 5 2 7 2 3 2 11
1000000010001001 5 2 7 2 1933 2 29 2 157
1000000010010001 53 1021 5 2 7 2 3 2 7
1000000010010111 3 2 3 2 7 2 3 2 3
1000000010011001 7 1667 179 13 5 11 23 7 311
1000000010011011 73 757 3 2 13 2 47 2 3
1000000010011101 5 2 3 2 7 2 3 2 3
1000000010100011 3 1259 421 3 5 8893 3 67 17
1000000010100111 7 13 3 2 37 2 5 2 3
1000000010101001 3 3083 13 3 5 43 3 73 7
1000000010110011 47 43 3 2 11 2 204311 2 3
1000000010110101 7 443 3 2 7 2 3 2 3"""