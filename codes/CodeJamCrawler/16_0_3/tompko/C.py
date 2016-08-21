import itertools

def base(i, n):
    ret = 0
    mul = 1
    for s in reversed(i):
        ret += int(s) * mul
        mul *= n
    return ret

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def is_jam(n):
    if n[0] != "1" or n[-1] != "1":
        return False
    if len(n) != N:
        return False
    for b in range(2, 11):
        x = base(n, b)
        if is_prime(x):
            return False
    return True

N = 32
J = 500
start, stop = 2, 100000

jams_divs = {}
jams = []

count = 0
for seq in itertools.product("01", repeat=N-2):
    jam = "1" + "".join(seq) + "1"
    d = {}
    for b in range(2, 11):
        x = base(jam, b)
        for s in range(start, stop):
            if s == x: break
            if x % s == 0:
                d[b] = s
                break
    if len(d) == 9:
        jams.append((jam, d))
        continue
    jams_divs[jam] = d
    if len(jams) >= J:
        break

seen = set()

while len(jams) < J:
    for j, d in jams_divs.items():
        if j in seen: continue
        for b in range(2, 11):
            if b in d: continue
            x = base(j, b)
            for s in range(start, stop):
                if s == x: continue
                if x % s == 0:
                    d[b] = s
                    break
        if len(d) == 9:
            print(len(jams))
            jams.append((j, d))
            seen.add(j)
        if len(jams) >= J:
            break
    start, stop = stop, stop + 100000

print("Case #1:")
for j, d in jams:
    print(j, " ".join([str(d[i]) for i in range(2, 11)]))
