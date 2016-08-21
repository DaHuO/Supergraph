fin = open("A-large.in")
fout = open("A-large.out", "w")

t = int(fin.readline())
for i in range(t):
    n = int(fin.readline())
    n1 = n
    s = set(list(str(n1)))
    if n == 0:
        print("Case #" + str(i + 1) + ": INSOMNIA", file=fout)
        continue
    while len(s) < 10:
        n1 += n
        s = s | set(list(str(n1)))
    print("Case #" + str(i + 1) + ": " + str(n1), file=fout)
fin.close()
fout.close()
