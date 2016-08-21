import numpy as np
from sympy import *

def eqs2matrix(eqs, syms, augment=False):
    s = Matrix([si.lhs - si.rhs if isinstance(si, Equality) else si for si in eqs])
    sym = syms
    j = s.jacobian(sym)
    rhs = -(s - j*Matrix(sym))
    rhs.simplify()
    if augment:
        j.col_insert(0, rhs)
    else:
        j = (j, rhs)
    return j

def solve_overdet(A, b):
    x_lstsq = np.linalg.lstsq(A,b)[0]
    Q,R = np.linalg.qr(A)
    Qb = np.dot(Q.T,b)
    return np.linalg.solve(R,Qb)

e = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
v = set(['E', 'G', 'F', 'I', 'H', 'O', 'N', 'S', 'R', 'U', 'T', 'W', 'V', 'X', 'Z'])
s = symbols('E G F I H O N S R U T W V X Z')
vs = dict(zip(v, s))
eqns = []
for i in xrange(10):
    z = 0
    for c in e[i]:
        z += vs[c]
    eqns.append(z)
z = np.mat(eqs2matrix(eqns, s)[0]).T

for tc in xrange(input()):
    inp = raw_input()
    counts = [[inp.count(c)] for c in v]
    sol = solve_overdet(z, np.mat(counts))
    ans = ''
    for i in xrange(len(sol)):
        if sol[i][0] > 0.5:
            ans += (str(i) * int(sol[i][0]+0.5))
    print "Case #%d: %s" % (tc+1, ans)
