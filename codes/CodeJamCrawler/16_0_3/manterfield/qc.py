# Used this lib:
# https://pypi.python.org/pypi/primefac
from primefac import multifactor
from itertools import product


def readint(): return int(raw_input())

_ = raw_input()

N, J = raw_input().split()
N = int(N)
J = int(J)

j = 0

print "Case #1:"
for jc in product("01", repeat=N-1):
    jc = "1" + "".join(jc)

    if not jc.endswith("1"):
        continue

    try:
        answer = jc
        for i  in range(2, 11):
            dec = int(jc, i)
            fac = multifactor(dec)

            if fac == dec:
                raise Exception("It's a prime")
            else:
                answer += " " + str(fac)

        j += 1
        print answer
    except Exception as e:
        pass

    if j >= J:
        break
