def go(n):
    a = {'0': False, '1': False, '2': False, '3': False, '4': False,
         '5': False, '6': False, '7': False, '8': False, '9': False}

    cnt = 0
    if n != 0:
        while any([not el for el in a.values()]):
            cnt += 1
            str_n = str(n * cnt)
            for el in str_n:
                a[el] = True
        return n * cnt
    else:
        return "INSOMNIA"

t = int(input())
for i in range(1, t + 1):
    boo = int(input())
    answer = go(boo)
    print("Case #{}: {}".format(i, answer))
