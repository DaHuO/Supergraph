input = open('A-large.in', 'r')
output = open('A-large.out', 'w')
N = int(input.readline())
for case in range(1, N + 1):
    print("Case #", case, sep = "", end = ": ", file = output)
    start = input.readline().rstrip()
    startn = int(start)
    if startn == 0:
        ans = "INSOMNIA"
    else:
        digits = set(start)
        lastnum = startn
        while len(digits) < 10:
            lastnum += startn
            digits |= set(str(lastnum))
        ans = lastnum
    print(ans, file = output)
input.close()
output.close()