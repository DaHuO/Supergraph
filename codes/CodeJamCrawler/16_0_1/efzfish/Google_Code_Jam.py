
# coding: utf-8

# In[ ]:

import numpy as np

num = int(raw_input())
sheep = []
for i in range(num):
    sheep.append(int(raw_input()))


def sleep(x):
    if x == 0:
        return 'INSOMNIA'
    else:
        i = 1
        flag = 0
        set_digit = []
        while(flag == 0):
            set_digit += map(int, str(x*i))
            if (set(set_digit) == set(range(10))):
                flag = 1
                break
            i += 1
        return x*i

for i in range(num):
    print 'Case #{}: {}'.format(i+1, sleep(sheep[i]))



