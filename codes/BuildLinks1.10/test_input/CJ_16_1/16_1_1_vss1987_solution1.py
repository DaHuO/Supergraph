def solve(s):
    s = list(s)
    res = []
    res.append(s[0])
    for i in range(1, len(s)):
        if s[i] >= res[0]:
            res.insert(0, s[i])
        else:
            res.append(s[i])
    return ''.join([str(x) for x in res])

file = 'A-large'
inp = open(file+'.in', 'r').read().splitlines()
out = open(file+'.out', 'w')
case = 0
testcases = int(inp[0])
case = 0
for tc in range(1, testcases+1):
    res = solve(inp[tc])
    case += 1
    out.write('Case #' + str(case) + ': ' + str(res) + '\n')