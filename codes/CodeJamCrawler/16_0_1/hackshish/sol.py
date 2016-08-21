#!/usr/bin/python
b_rep = (1,2,4,8,16,32,64,128,256,512)

def func(num):
    if num == 0:
        return 'INSOMNIA'
    d_score = 0
    itr = 0
    while (d_score != 1023):
        itr += 1
        n_num = num * itr
        while (n_num != 0): 
            d_score |= b_rep[n_num % 10]
            n_num /= 10
    return num * itr

t = int(raw_input())
for i in xrange(1, t + 1):
    print "Case #{}: {}".format(i, func(int(raw_input())))
