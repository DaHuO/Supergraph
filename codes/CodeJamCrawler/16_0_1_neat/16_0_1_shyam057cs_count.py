fin = open("A-large.in", "r")
fout = open("Alarge.out", "w")

def count(N):
    a = set()
    i = 1
    digits = ['0','1','2','3','4','5','6','7','8','9']
    while True:
        t = i * N
        if t in a:
            return "Insomnia"
        else:
            a.add(t)
        s = str(t)
        for c in s:
            if c in digits:
                digits.remove(c)
                if len(digits) == 0:
                    return str(t)
        i = i + 1



N = int(fin.readline())
for n in range(1,N+1):
    fout.write("Case #%i: " %(n))
    N = int(fin.readline())
    fout.write(count(N))
    fout.write("\n")
fout.close()