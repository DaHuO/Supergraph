def to_sys(digits, k):
    s = 0
    for i in range(len(digits)):
        s += digits[i] * precalc[k][i]
    return s

def find_divisor(n):
    for i in range(3, int(n ** 0.5 + 1)):
        if(n % i == 0):
            return i
    return None

def get_digits(n):
    ans = []
    while n > 0:
        ans.append(n % 2)
        n //= 2
    return ans

precalc = [[], []]
for i in range(2, 11):
    precalc.append([i ** m for m in range(16)])

c = 0
for i in range(2 ** 15 + 1, 2 ** 16, 2):
    d = get_digits(i)
    flag = True
    div = []
    for j in range(2, 11):
        o = find_divisor(to_sys(d, j))
        if(o == None):
            flag = False
            break
        div.append(o)
    if flag:
        c += 1
        print("".join(str(v) for v in reversed(d)) + " " + " ".join(str(p) for p in div))
    if(c == 50):
        break
