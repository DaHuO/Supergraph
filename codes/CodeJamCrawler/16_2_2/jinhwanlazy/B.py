from itertools import product

def s(CJ, p):
    ret = list(CJ)
    for i, n in enumerate(p):
        ret[idx[i]] = n
    return ''.join(ret)

def bfk(CJ):
    l = len(CJ)//2
    c = int(CJ[:l])
    j = int(CJ[l:])
    return abs(c - j), c, j

for case in range(int(input())):
    C, J = map(list, input().split())
    CJ = C+J
    idx = [i for i, c in enumerate(CJ) if c == '?']
    ps = product('0123456789', repeat=len(idx))
    fixed = (s(CJ, p) for p in ps)
    ans = min(fixed, key=bfk)
    l = len(C)
    print("Case #%d:" % (case+1), ans[:l], ans[l:])




#     for i in range(len(C)):
#         if i == 0:
#             if C[i] == '?' and J[i] != '?':
#                 C[i] = J[i]
#             elif C[i] != '?' and J[i] == '?':
#                 J[i] = C[i]
#             elif C[i] == J[i] == '?':
#                 C[i] = J[i] = '0'
#         else:
#             Cp = C[:i]
#             Jp = J[:i]
#             if C[i] == J[i] == "?":
#                 if Cp == Jp:
#                     C[i] = J[i] = '0'
#                 elif Cp > Jp:
#                     C[i] = '0'
#                     J[i] = "9"
#                 else:
#                     C[i] = '9'
#                     J[i] = '0'
#             elif C[i] == "?":
#                 if Cp == Jp:
#                     C[i] = J[i]
#                 elif Cp > Jp:
#                     C[i] = '0'
#                 else:
#                     C[i] = '9'
#             elif J[i]  == '?':
#                 if Cp == Jp:
#                     J[i] = C[i]
#                 elif Cp > Jp:
#                     J[i] = '9'
#                 else:
#                     J[i] = '0'

#    print("Case #%d:" % (case+1), ''.join(C), ''.join(J))
