T = int(input())

for t in range(T):
    elo = raw_input()

    i = 1
    ans = elo[0]
    while i < len(elo):
        ans_a = ans + elo[i]
        ans_b = elo[i] + ans

        ans = max(ans_a, ans_b)
        i += 1

    print("Case #" + str(t+1) + ": " + str(ans))

