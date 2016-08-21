T = int(input())

def solution(K, C, S):
    s = []
    for i in range(K):
        res = i + 1
        for j in range(C - 1):
            res = (res - 1) * K + i + 1;
        s.append(res)
    return ' '.join(map(str, s))

for test in range(1, T + 1):
    K, C, S = map(int, input().split())
    print("Case #{0}: {1}".format(test, solution(K, C, S)))
