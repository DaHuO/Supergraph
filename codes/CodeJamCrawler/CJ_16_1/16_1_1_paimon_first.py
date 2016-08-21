from collections import deque

def solve(s):
    result = deque()
    for char in s:
        if result and result[0] <= char:
            result.appendleft(char)
        else:
            result.append(char)
    return ''.join(result)

answer = 'Case #{}: {}'
n_tests = int(input())
for i in range(n_tests):
    s = input()
    print(answer.format(i + 1, solve(s)))
