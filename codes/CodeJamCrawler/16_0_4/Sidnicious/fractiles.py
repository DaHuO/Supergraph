def need_to_check(k, c):
    for pos in range(k):
        yield sum(pos * pow(k, i) for i in range(k))

for case in range(int(input())):
    k, c, s = map(int, input().split())
    # to_check = list(need_to_check(k, c))
    to_check = list(range(k))
    print("Case #{}: {}".format(case+1,' '.join(map(lambda x: str(x+1), to_check))))
