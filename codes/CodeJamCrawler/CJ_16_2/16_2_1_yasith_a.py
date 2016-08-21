
def rec(digits, cur):
    if cur == 10:
        return []

    d2 = digits[:]
    curs = dvals[cur] 

    found = True
    for c in curs:
        if c in d2:
            d2.remove(c)
        else:
            found = False
            break

    if found:
        #print("Found {} in {}. Remaining {}".format(str(cur), str(digits), str(d2)))

        if len(d2) == 0:
            return [cur]

        t = rec(d2, cur)
        if t == []:
            f = rec(digits, cur+1)
            return f
        else:
            return [cur] + t

    else:
        return rec(digits, cur+1)

T = int(input())

dp = {}
dvals = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

for t in range(T):
    S = list(input())
    val = rec(S, 0)

    o = "Case #{}: {}".format(str(t+1), ''.join(map(str, val)))
    print(o)
