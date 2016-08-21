inp = open('A-large.in', 'r')
output = open('output.txt', 'w')
T = int(inp.readline().strip())
out = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for x in range(T):
    N = int(inp.readline().strip())
    if N == 0:
        output.write("Case #{0}: INSOMNIA\n".format(x+1))
        continue
    i = 0
    res = set()
    while res != out:
        i += 1
        temp = i * N
        res.update(set(str(temp)))
    output.write("Case #{0}: {1}\n".format(x+1, temp))
inp.close()
output.close()
