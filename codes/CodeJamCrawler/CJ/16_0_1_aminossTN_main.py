from utils import calculate


T = int(input())


for test in range(T):
    N = int(input())
    output = calculate(N)
    print('Case #{}: {}'.format(test + 1, output))

