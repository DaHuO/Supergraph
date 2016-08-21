size =  "large"


def solve(delta):
    solved = False
    digits = set()
    visited = dict()
    num = 0
    while not solved:
        num = num + delta
        if num in visited:
            return "INSOMNIA"
        
        digits = digits.union(set(str(num)))
        if len(digits) == 10:
            return str(num)
        visited[num] = 1


f = open('A-%s-practice.in' % size)
o = open('A-%s-practice.out' % size, 'w')
n = int(f.readline())
for i in range(1, n+1):
    num = int(f.readline())
    sol = solve(num)
    o.write("Case #%d: %s\n" % (i, sol))
f.close()
o.close()
