t = int(input())
for q in range(1, t + 1):
    s = input()
    res = [s[0]]
    for i in range(1,len(s)):
        if s[i] < res[0]:
            res.append(s[i])
        else:
            res.insert(0,s[i])
    result = "".join(str(x) for x in res)
    print("Case #{}: {} ".format(q,result))
