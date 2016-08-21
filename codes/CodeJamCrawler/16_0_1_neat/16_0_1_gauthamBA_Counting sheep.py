for t in range(int(input())):
    n = int(input())
    if n == 0:
        print('Case #' + str(t + 1) + ': INSOMNIA')
    else:
        sleep = set()
        i = 1

        while len(sleep) != 10:
            sleep = sleep.union(set(str(n * i)))
            i += 1
        print('Case #' + str(t + 1) + ': ' + str(n * (i - 1)))
