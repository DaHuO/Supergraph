def sol(n):
    if n == 0:
        return "INSOMNIA"
    n0 = n
    digits = set()
    while digits != {0,1,2,3,4,5,6,7,8,9}:
        digits = digits | set([int(d) for d in str(n)])
        n += n0
    return str(n-n0)



fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    if case > 0:
        fOut.write("Case #"+str(case)+": "+sol(int(line))+"\n")
    case += 1