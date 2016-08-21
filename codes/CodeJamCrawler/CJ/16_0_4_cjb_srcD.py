path = '/Users/bosley/Desktop/'
def openFile():
    f = open(path + "D-small.in")
    lines = [x.rstrip() for x in f.readlines()]
    n = int(lines[0])
    return n, lines

def go(n, lines):
    f = open(path + "D.out",'w')
    for i in range(0, n):
        l = lines[i+1].split(' ')
        l = [int(x) for x in l]
        k, c, s = l
        soln = solve(k, c, s)
        f.write('Case #{}: {}\n'.format(i+1, soln))
    f = open(path + "D.out")
    print f.read()
    
def mapbit(b, k, c):
    if c == 1:
        return b
    if c == 2:
        return b*k + b
    return b*(k**(c-1)) + mapbit(b,k,c-1)
def solve(k, c, s):
    l = []
    if k != s:
        return 'You told me k!=s'
    for b in range(0, k):
        l = l + [mapbit(b,k,c)+1]
    l = [str(x) for x in l]
    return ' '.join(l)

print mapbit(1, 2, 3)+1, mapbit(0, 2, 3)+1, mapbit(1, 3, 2)+1, mapbit(0,1,1)+1
n, lines = openFile()
go(n, lines)



