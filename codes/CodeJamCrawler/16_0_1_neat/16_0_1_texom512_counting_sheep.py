__author__ = 'texom512'

t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        res = 'INSOMNIA'
    else:
        nums = set()
        round = 1
        while nums != set(range(10)):
            res = n * round
            nums = nums.union(map(int, tuple(str(res))))
            round += 1

    print('Case #{}: {}'.format(i + 1, res))
