


T = int(input().strip())
for i in range(T):

    S = input().strip()
    words = [S[0]]
    for letter in S[1:]:
        words = [letter + j for j in words] + [j + letter for j in words]

    print("Case #" + str(i + 1) + ": " + sorted(words)[-1])
