# usage:  (py3 a.py < a.in) > a.out

import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+":", *a, file=sys.stderr, **k)
map = lambda *a: list(__builtins__.map(*a))

#---------------------------------------------

"""
my solution is O(n^2) in worst case -> should be ok for n = 1000
"""

def run(data):

    # print(map(int, ['1', '2']))

    out = data[0]

    for c in data[1:]:
        if c + out > out:
            out = c + out
        else:
            out = out + c

    return out

#---------------------------------------------

def read_case():
    return input()

for i in range(int(input())):
    outstr = "Case #"+str(i+1)+": "+str(run(read_case()))
    print(outstr, " @ t =", time.clock())
    __builtins__.print(outstr)



