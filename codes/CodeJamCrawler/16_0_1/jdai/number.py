f = open('A-large.in')
out = open('number.out', 'w')

def work(n):
    digits = set()
    i = 1
    while len(digits) < 10:
        s = str(i * n)
        for c in s:
            digits.add(c)
        i += 1
    return (i - 1) * n

for i in range(int(f.readline())):
    n = int(f.readline())
    result = 0
    if n == 0:
        result = 'INSOMNIA'
    else:
        result = work(n)
    out.write('Case #{}: {}\n'.format(i + 1, result))

