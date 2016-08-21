Q = int(input())

for qu in range(1, Q+1):
    n = input()
    ans = 0
    state = -1

    for ch in n:
        if ch == '-' and state != 0:
            ans += 1
            state = 0
        elif ch == '+' and state != 1:
            ans += 1
            state = 1

    if ch[-1] == '+':
        ans -= 1
    print("Case #{}: {}".format(qu,ans))