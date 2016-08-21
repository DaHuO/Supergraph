fin = open('A-large.in')
lines = fin.readlines()
fin.close()

fout = open('sheep_large_answer.txt','w')

def f(N):
    digits = 0
    i = 0
    while digits != 0b1111111111:
        i += 1
        X = i*N
        while X > 0:
            digits |= 2**(X % 10)
            X = X // 10
    return i


T = int(lines[0])
for t in range(T):
    N = int(lines[t+1])
    if N != 0:
        i = f(N)
        fout.write("Case #%d: %d\n" % (t+1, i*N))
        #print(N, i*N)
    else:
        fout.write("Case #%d: INSOMNIA\n" % (t+1))
        print(N, "INSOMNIA")

fout.close()
