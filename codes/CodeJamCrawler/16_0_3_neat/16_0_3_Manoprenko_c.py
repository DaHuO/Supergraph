def find_d(x):
    i = 2
    while i < 10000 and i * i <= x:
        if x % i == 0:
            return i
        i += 1
    return -1

def test(mask, N):
    divs = []
    for bs in range(2, 11):
        cp = 1
        nm = 0
        for i in range(N):
            if ((mask >> i) & 1) == 1:
                nm += cp
            cp *= bs
        
        d = find_d(nm)
        if d == -1:
            return False
        divs.append(d)
    print(str(bin(mask))[2:], ' '.join(map(str, divs)), file=fout)
    return True

fout = open('c-asnwer-big.txt', 'w')
print('Case #1:', file=fout)
N = 32
J = 500
mask = (1 << (N - 1)) + 1;
while J > 0:
    if test(mask, N):
        J -= 1
    mask += 2

