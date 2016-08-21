__author__ = 'tegjyot'

import numpy as np
import random
from itertools import product
import fileinput


def is_prime(a):

    return a%2!=0 and all(a % i for i in xrange(3, int(a**0.5), 2))

def generate_number_not_prime(N):
    while True:
        sizes=N-2
        s = list(np.random.randint(2, size=sizes))
        s.insert(0,1)
        s.append(1)
        str_s=''.join(str(i) for i in s)
        k_list=[]
        flag=1
        for i in range(2,11):
            base_str_s=int(str_s,i)
            if not is_prime(base_str_s):
                if base_str_s%2==0:
                    k_list.append(str(2))
                else:
                    for j in range(3,int(base_str_s**0.5),2):
                        if base_str_s%j==0:
                            k_list.append(str(j))
                            break
            else:
                flag=0
                break
        if flag==1:
            return str_s,k_list


if __name__ == "__main__":
    f = fileinput.input()
    T=int(f.readline())
    for case in range(1,T+1):
         Input = [int(x) for x in f.readline().split()]
         N=Input[0]
         K=Input[1]
         dict={}
         k=0
         print("Case #{0}:".format(case))
         while k<K:
            T=generate_number_not_prime(N)
            if T[0] in dict.keys():
                continue
            else:
                dict[T[0]]=T[1]
                k+=1
                print (T[0]+' '+ ' '.join(T[1]))
