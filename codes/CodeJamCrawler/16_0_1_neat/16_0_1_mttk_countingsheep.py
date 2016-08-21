
def solve(n):
    if n == 0: return 'INSOMNIA'
    digits = set()
    k = 1
    while len(digits) < 10:
        digits = digits.union(set(str(k*n)))
        k+=1
    return str((k-1) * n)

with open('A-large.in', 'r') as input:
    with open('output.txt', 'w') as output:
        t = int(input.readline().strip())
        for i in range(t):
            s = solve(int(input.readline().strip()))
            output.write('Case #{}: {}\n'.format(i+1, s))
