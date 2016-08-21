
def solve(n0):
    digit = {}
    if(n0 == 0):
        return "INSOMNIA"
    n = 0
    while len(digit) < 10:
        n += n0
        for c in str(n):
            digit[c] = True
    return str(n)

t = int(raw_input())

for i in range(1, t+1):
    n = int(raw_input())
    print "Case #" + str(i) +": "+ solve(n)
