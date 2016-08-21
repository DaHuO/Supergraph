"""Code jam Counting Sheep."""

import fileinput

for case, N in enumerate(fileinput.input()):
    if case == 0:
        continue

    N = int(N)

    if N == 0:
        print('Case #{}: INSOMNIA'.format(case))
        continue

    numbers = [False for x in range(10)]

    i = 1
    while True:
        for x in str(i*N):
            numbers[int(x)] = True
        if all(numbers):
            print('Case #{}: {}'.format(case, i*N))
            break
        i += 1
