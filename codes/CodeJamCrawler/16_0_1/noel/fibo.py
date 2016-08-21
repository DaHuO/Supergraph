for T in range(int(input())):
    s = list(input())
    fin = s[0]
    l = len(s)
    for i in range(1, l):
        if fin[0] <= s[i]:
            fin = s[i] + fin
        else:
            fin = fin + s[i]
    print("Case #" + str(T+1) + ": " + fin)

