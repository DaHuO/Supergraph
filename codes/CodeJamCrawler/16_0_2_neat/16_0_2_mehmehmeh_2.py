f = open('input.txt')
n = int(f.readline())

out = open('output.txt', 'w')

for i in range(n):
    ans = 0
    st = f.readline().strip()
    for j in range(1, len(st)):
        if st[j] != st[j-1]:
            ans += 1
    if (st[0] == '-' and (ans % 2) == 0) or (st[0] == '+' and (ans % 2) == 1):
        ans += 1

    out.write('case #{0}: {1}\n'.format(str(i + 1), ans))

out.close()
f.close()

