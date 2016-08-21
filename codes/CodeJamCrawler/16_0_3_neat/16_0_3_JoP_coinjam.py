import sys
import itertools

def isprime(n):
    if n < 2:
        return (False,-1)
    if n == 2:
        return (True,-1)
    if not n & 1: # if the last bit is set the number is even
        return (False, 2)

    # check odd numbers up until square root
    # (the cycle only contains numbers up to square root of n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return (False, i)
    return (True, -1)


T = int(sys.stdin.readline())
for i in range(1,T+1):
    N,J = map(lambda x: int(x), sys.stdin.readline().split(" "))

    print("Case #1:")
    all = ["".join(seq) for seq in itertools.product("01", repeat=N-2)]
    idx, nfound = 0, 0
    while nfound < J:
        binstr = "1" + all[idx] + "1"
        dividers = []
        ok = True
        for base in range(2,11):
            wasprime, val = isprime(int(binstr, base))
            dividers.append(str(val))
            if wasprime:
                ok = False
                break

        if ok:
            print("%s %s" % (binstr, " ".join(dividers)))
            nfound += 1
        idx += 1
