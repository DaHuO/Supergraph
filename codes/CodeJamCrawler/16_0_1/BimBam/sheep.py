def done( numbers ):
    for n in numbers:
        if not n: return False
    return True

def sheep(n):
    numbers = [0] * 10
    cnt = 1
    while True:
        cn = n * cnt
        while cn > 0:
            numbers[cn % 10] = True
            cn = cn / 10
        if all(numbers):
            return n * cnt
        if not n: return "INSOMNIA"
        cnt += 1         

with open("sheepLarge.in", "rb") as f:
    nOfCases = int(f.readline().strip())
    for i in range(nOfCases):
        n = int(f.readline().strip())
        s = sheep(n)
        print "Case #{}: {}".format( i + 1, s )