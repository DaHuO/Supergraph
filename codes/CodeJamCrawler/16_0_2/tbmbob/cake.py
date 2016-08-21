import numpy as np

for i in range(int(input())):
    print('Case #%d: ' % (1+i), end='')
    s = input() + '+'
    array = np.array([c == '+' for c in s])
    diff = np.diff(array)
    print(sum(diff))
