N = 32
J = 500
pows = {}
for i in range(2, 11):
    pows[i] = {0: 1, 1: i}
    for k in range(2, 32):
        pows[i][k] = pows[i][k-1]*i;


def number(s, base):
    numb = 0
    for i in range(N):
        numb += pows[base][i]*((s >> i) & 1)
    return numb


def has_divisor(a):
    for m in range(2, 101):
        if a % m == 0:
            return True
    return False


def get_divisor(a):
    for m in range(2, 101):
        if a % m == 0:
            return m
    return None


cnt = 0
n = (1 << (N-1)) + 1
l = []


while cnt < J and n < 1 << N:
    for i in range(2, 11):
        num_in_base = number(n, i)
        if not has_divisor(num_in_base):
            break
        if i == 10 and has_divisor(num_in_base):
            cnt += 1
            l.append(n)
    n += 2

if n < 1 << N:
    print 'Case #1:'
    for num in l:
        print bin(num)[2:], " ".join([str(get_divisor(x)) for x in [number(num, k) for k
                                                                    in range(2, 11)]])


