import os
import math

def binomial_all(k):
    if k==1:
        return ['11','00']
    else:
        s = binomial_all(k-1)
        return ['11'+ll for ll in s] + ['00'+ll for ll in s]



# use pairs is enough though

def generate_pairs(num, limit):
    if num%2==1:
        s = generate_pairs(num-3, limit/2+limit%2)
        s1 = []
        for v in s:
            v2 = ['1','0','1']
            for num in v:
                s1.append('1'+num+'01')
                s1.append('10'+num+'1')


        return s1[0: limit]

    # generate 11 types
    # usually enough though
    mm = math.log(limit,2)
    if(mm > num/2-1):
        raise ValueError
    else:
        s = binomial_all(int(mm)+1)
        s = s[0:limit]
        zstr = '1'

        for k in range(0, num/2-2-int(mm)):
            zstr+='00'

        print zstr

        s1 = [zstr+ll+'1' for ll in s]
        print s1[10]
        return s1[0: limit]

    # generate 110 types

    # generate 11-0110 types

    #
of = open('lala3','w')
s = generate_pairs(32, 500)
print >>of, 'Case #1:'
for str in s:
    print >>of, str, '3 4 5 6 7 8 9 10 11'
of.close()