T = int(input())

def solution():
    n, m = map(int, input().split())
    if (2 ** (n - 2) < m):
        return "IMPOSSIBLE\n"
    table = [[0] * n for i in range(n)]
    for i in range(1, n):
        for j in range(i + 1, n):
            table[i][j] = 1
    if (2 ** (n - 2) == m):
        for i in range(1, n):
            table[0][i] = 1
    else:
        s = bin(m)[2:]
        s = '0' * (n - 1 - len(s)) + s + '0'
        for i in range(n):
            table[0][i] = int(s[i])
    answer = "POSSIBLE\n"
    for i in range(n):
        answer += ''.join(map(str, table[i])) + '\n'
    return answer

for t in range(1, T + 1):
    print("Case #%s:" % t, solution(), end='')
    
    
