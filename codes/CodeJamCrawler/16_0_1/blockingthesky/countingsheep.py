inp = open('countingsheep.in', 'r')
def input():
    return int(inp.readline())

out = open('countingsheep.out', 'w')

T = input()
for t in range(1, T + 1):
    use = list('1234567890')
    N = input()
    if N == 0:
        out.write("Case #" + str(t) + ": INSOMNIA\n")
        continue
    cur = N
    for j in list(str(cur)):
        if j in use:
            use.remove(j)
    while len(use) != 0:
        cur += N
        for j in list(str(cur)):
            if j in use:
                use.remove(j)
    out.write("Case #" + str(t) + ": " + str(cur) + "\n")

out.close()
