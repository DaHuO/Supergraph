def divisor(d):
    global prime
    if d in prime:
        return -1
    for i in prime:
        if i!= d and d%i == 0:
            return i
    return -1

def solve(n, j):
    jamCoin = ['0']*n
    jamCoin[0] = jamCoin[n-1] = '1'

    result = []

    count = 1
    b = list(bin(count)[2:])
    while len(b) <= n-2:

        for i in range(n-2, 0, -1):
            if len(b) == 0: break
            jamCoin[i] = b.pop()

        jamCoinStr = ''.join(jamCoin)
        res = list()
        res.append(jamCoinStr)
        for i in range(2, 11):
            d = int(jamCoinStr, i)
            div = divisor(d)
            if div == -1:
                break
            else:
                res.append(div)
        if len(res) == 10:
            result.append(res)
            if len(result) == j:
                return result
        count += 1
        b = list(bin(count)[2:])


file = 'C-large'
inp = open(file+'.in', 'r').read().splitlines()
out = open(file+'.out', 'w')
prime = set([int(p) for p in open('prime', 'r').read().splitlines()])
case = 0
testcases = int(inp[0])
for tc in range(1, testcases+1, 1):
    s = inp[tc].split()
    result = solve(int(s[0]), int(s[1]))
    case += 1
    res = ''
    for r in result:
        res += '\n'
        res += ''.join(str(r[0]))
        for i in r[1:]:
            res += ' '
            res += str(i)
    out.write('Case #' + str(case) + ':' + res)

