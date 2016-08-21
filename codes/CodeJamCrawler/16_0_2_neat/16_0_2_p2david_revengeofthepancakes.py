size =  "large"


def solve(cakes):
    stack_size = len(cakes)
    flip_times = 0
    for i in range(0, stack_size - 1):
        if cakes[i] != cakes[i+1]:
            flip_times = flip_times + 1
            cakes = flip(i+1, cakes)
    return flip_times if cakes[0] == "+" else (flip_times+1)

def flip(pos, cakes):
    first_half = ["-" if cakes[0] == "+" else "+"] * pos
    second_half = cakes[pos:]
    return first_half + second_half


f = open('B-%s-practice.in' % size)
o = open('B-%s-practice.out' % size, 'w')
n = int(f.readline())
for i in range(1, n+1):
    cakes = list(f.readline())[:-1]
    sol = solve(cakes)
    o.write("Case #%d: %s\n" % (i, sol))
f.close()
o.close()
