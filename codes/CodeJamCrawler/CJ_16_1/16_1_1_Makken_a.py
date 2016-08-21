def a(S):
    retStr =[]
    for i,letter in enumerate(S):
        if retStr == []:
            retStr.append(S[i])
            continue

        if S[i] >= retStr[0]:
            retStr.insert(0, S[i])
        else:
            retStr.append(S[i])

    return "".join(retStr)

for item in range(1, int(input()) + 1):
    S = input()
    print("Case #{}: {}".format(item, a(S)))

