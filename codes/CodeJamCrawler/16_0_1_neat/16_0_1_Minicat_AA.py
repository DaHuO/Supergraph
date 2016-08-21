def solve(num):
    if num == 0:
        return 'INSOMNIA'
    seen = [False] * 10
    last = num
    count = 0
    while True and count < 1000:
        for digit in str(last):
            seen[int(digit)] = True
        if False not in seen:
            return last
        last += num
        count += 1
    return 'INSOMNIA' #??


inp = open('A-large.in')
outp = open('Alarge.out', 'w')

T = int(inp.readline())

for i in range(1, T+1):
    num = int(inp.readline().rstrip())
    outp.write('Case #{}: {}\n'.format(i, solve(num)))
    print solve(num)

inp.close()
outp.close()
