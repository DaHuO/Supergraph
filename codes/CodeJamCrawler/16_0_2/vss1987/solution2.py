
def solve(str):
    flip = 0
    st = list(str)
    for i in range(len(st)-1, -1, -1):
        if st[i] == '-':
            flip += 1
            for j in range(i+1):
                if st[j] == '+': st[j] = '-'
                else: st[j] = '+'
    return flip



file = 'B-large'
inp = open(file+'.in', 'r').read().splitlines()
out = open(file+'.out', 'w')
case = 0
testcases = int(inp[0])
for tc in range(1, testcases+1, 1):
    result = solve(inp[tc])
    case += 1
    out.write('Case #' + str(case) + ': ' + str(result) + '\n')