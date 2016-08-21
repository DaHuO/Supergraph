
ans = []


def get_count(num):
    x = [False] * 10
    i = 1
    while False in x:
        prod = num * i
        while prod > 0:
            rem = prod % 10
            x[rem] = True
            prod /= 10
        i += 1
    return (i-1) * num


def pre_compute():
    for i in range(1000002):
        if i == 0:
            ans.append("INSOMNIA")
        elif i == 1:
            ans.append(10)
        else:
            ans.append(get_count(i))

pre_compute()

for case in range(input()):
    num = input()
    print "Case #"+str((case+1))+": "+str(ans[num])
