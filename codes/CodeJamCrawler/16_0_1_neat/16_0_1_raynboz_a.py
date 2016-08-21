fin = open('ain.txt', 'r')
fout = open('aout.txt', 'w')

T = int(fin.readline())

def solve():
    N = int(fin.readline())
    if N == 0:
        return "INSOMNIA"
    digits = [0]*10
    count = 0
    i = 1

    while count < 10:
        x = str(i*N)
        for c in x:
            if not digits[int(c)]:
                count += 1
                digits[int(c)] = 1
        i += 1
    return (i-1)*N

for i in range(T):
    fout.write("Case #" + str(i+1) + ": " + str(solve()) + "\n")

fin.close()
fout.close()
