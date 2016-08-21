T = eval(input())
for i in range(1,1+T):
    S = list(input())
    temp = []
    for c in S:
        if not temp:
            temp.append(c)
        else:
            if temp[0] <= c:
                temp.insert(0,c)
            else:
                temp.append(c)
    print("Case #{}: {}".format(i,"".join(temp)))
