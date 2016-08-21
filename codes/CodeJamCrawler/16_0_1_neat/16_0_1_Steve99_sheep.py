def check(dict):
    checker = 0
    for i in range(10):
        if i in dict:
            checker+=1
    if checker == 10:
        return True
    else:
        return False


def solve(n):
    dict = {}
    if n == 0:
        return 'INSOMNIA'

    for counter in range(1000):
        a = n*(counter+1)
        for i in str(a):
            if int(i) not in dict:
                dict[int(i)] = 1
        if check(dict):
            return a
    return 'INSOMNIA'

cases = int(input())
n = [int(input()) for _ in range(cases)]
for i in range(cases):
    print("Case #{}: {}".format(i+1, solve(n[i])))
