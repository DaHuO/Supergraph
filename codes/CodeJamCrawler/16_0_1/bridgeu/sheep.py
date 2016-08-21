f = open('A-large.in')
T = int(f.readline())
f1 = open('A-large.out', 'wc')

for i in range(T):
    N = [int(x) for x in f.readline().split()][0]
    f1.write("Case #%i: " % (i+1))
    if N == 0:
        f1.write("INSOMNIA\n")
        continue

    seen = [False] * 10

    for i in range(1, 1000000):
        n = N*i
        for digit in [int(x) for x in str(n)]:
            seen[digit] = True
        if all(seen):
            f1.write(str(n))
            f1.write("\n")
            break
