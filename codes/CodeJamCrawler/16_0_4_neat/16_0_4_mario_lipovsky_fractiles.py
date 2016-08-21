def convert(l, base):
    res = 0
    for digit in l:
        res = res*base + digit
    return res

def solve():
    K, C, S = map(int, input().split())
    
    if K > S*C:
        return "IMPOSSIBLE"

    r = list(range(K)) + [0] * C
    ans = []

    for i in range(K // C + int(K % C != 0)):
        ans.append(convert(r[(i*C):(i*C+C)], K) + 1)

    return " ".join(map(str, ans))

T = int(input())

for t in range(T):
    print("Case #{}: {}".format(t+1, solve()))