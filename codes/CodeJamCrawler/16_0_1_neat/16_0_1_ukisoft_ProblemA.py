
for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print('Case #' + str(_ + 1) + ': INSOMNIA')
        continue
    counted = {str(i): False for i in range(10)}
    j = 1
    now = N
    _now = str(now)
    while False in counted.values():
        now = N * j
        _now = str(now)
        for i in counted.keys():
            if counted[i] is True:
                continue
            if i in _now:
                counted[i] = True
        j += 1
    print('Case #' + str(_ + 1) + ': ' + _now)
