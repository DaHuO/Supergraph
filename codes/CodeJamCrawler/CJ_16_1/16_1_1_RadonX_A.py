

T = int(input())

for i in range(1, T+1):
    print("Case #",i,": ",sep="",end="")
    S = input()
    ans = S[0]
    for i in range(1, len(S)):
        if (S[i] < ans[0]):
            ans = ans + S[i]
        elif (S[i] > ans[0]):
            ans = S[i] + ans
        else:
            # find 1st diff
            j = 1
            while (j < i):
                if (S[i] == ans[j]):
                    j = j+1
                else: break
            if (j == i):
                ans = ans + S[i]
            else:
                if (ans[j] < S[i]):
                    ans = S[i] + ans
                else:
                    ans = ans + S[i]
    print(ans)
