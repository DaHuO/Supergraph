from collections import defaultdict
size =  "large"

s_numbers =  {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}

_1_group = ['U', 'Z', 'W', 'G', 'X']
_2_group = ['F', 'T', 'O', 'S']
_3_group = ['I']
lookup ={"Z":"ZERO", "U":"FOUR", "W":"TWO", "G":"EIGHT", "X":"SIX"}
_2_lookup = {"F":"FIVE", "T":"THREE", "O":"ONE", "S":"SEVEN"}
_3_lookup = {"I":"NINE"}

def solve(S):
    cap_digits = []

    for c in _1_group:
        while c in S:
            cap_digit = lookup[c]
            cap_digits.append(cap_digit)
            for r in cap_digit:
                S = S.replace(r,"", 1)

    for c in _2_group:
        while c in S:
            cap_digit = _2_lookup[c]
            cap_digits.append(cap_digit)
            for r in cap_digit:
                S = S.replace(r,"", 1)
    
    for c in _3_group:
        while c in S:
            cap_digit = _3_lookup[c]
            cap_digits.append(cap_digit)
            for r in cap_digit:
                S = S.replace(r,"", 1)

    digits = [s_numbers[cap] for cap in cap_digits]
    sol = "".join(map(str, sorted(digits)))
    print(sol)
    return sol

try:
    f = open('A-%s.in' % size)
    o = open('A-%s.out' % size, 'w')
    n = int(f.readline())

    for i in range(1, n+1):
        S = f.readline().strip()
        sol = solve(S)
        o.write("Case #%d: %s\n" % (i, sol))
finally:
    f.close()
    o.close()
