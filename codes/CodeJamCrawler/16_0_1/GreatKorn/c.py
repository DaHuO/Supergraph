def solve(s, t):
    st = set()
    ss = int(s)
    if s == '0':
        fout.write("Case #{0}: INSOMNIA\n".format(t))
    else:
        i = 2
        while len(st) != 10:
            st |= set(s)
            s = str(ss * i)
            i += 1
        fout.write("Case #{0}: {1}\n".format(t, int(s) - ss))

fout = open("output.txt", "w")
T = int(input())
for i in range(1, T + 1):
    solve(input(), i)
fout.close()
            