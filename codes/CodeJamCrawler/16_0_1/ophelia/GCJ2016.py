t = int(input())
flag = False
for loop in range(t):
    n = int(input())
    num = n
    print("Case #", end = "")
    print(loop+1, end = "")
    print(": ", end = "")
    if num == 0:
        ans = "INSOMNIA"
        print(ans)
        continue
    used = set([])
    for i in range(10000):
        s = set(list(str(num)))
        for j in s:
            used.add(j)
        if len(used) == 10:
            ans = num
            flag = True
            break
        num += n

    if flag:
        print(ans)
    else:
        print("INSOMNIA")



"""conv = [0] * 11

for i in range(2,11):
    """
