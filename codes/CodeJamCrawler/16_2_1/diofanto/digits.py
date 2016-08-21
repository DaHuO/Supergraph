def trans(s):
    a = {}
    for c in s:
        if c in a:
            a[c] += 1
        else:
            a[c] = 1
    return a

def remove_digit(s, d):
    res = True
    for i, c in enumerate(d):
        if c in s and s[c] > 0:
            s[c] -= 1
        else:
            res = False
            break
    if not res:
        for j in range(i):
            s[d[j]] += 1
    return res

def add_digit(s, d, i):
    for c in d:
        if i > 0:
            s[c] += i

d_to_n = {"ZERO":"0", "ONE":"1", "TWO":"2", "THREE":"3", "FOUR":"4", "FIVE":"5", "SIX":"6", "SEVEN":"7", "EIGHT":"8", "NINE":"9"}
def aux(s, d, res):
    rem = sum(s.values())
    if not d:
        if rem == 0:
            return res
        else:
            return ""
    res1 = aux(s, d[1:], res)
    if res1 != "":
        return res1
    i = 0
    while remove_digit(s, d[0]):
        res = res + d_to_n[d[0]]
        res1 = aux(s, d[1:], res)
        if res1 != "":
            return res1
        i += 1
    add_digit(s, d[0], i)
    return ""


def digits(s):
    d = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    m = {}
    for num in d:
        for letter in num:
            if letter not in m:
                m[letter] = []
            if num not in m[letter]:
                m[letter].append(num)
    s_t = trans(s)
    return aux(s_t, d, "")

for t in range(1, int(input()) + 1):
    print("Case #{0}: {1}".format(t, digits(input())))
