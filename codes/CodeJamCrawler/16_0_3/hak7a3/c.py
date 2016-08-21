# -*- code:utf-8 -*-
import math

# 合成数判定
def is_not_prime(n):
    if n & 1 == 0 :
        return True
    else :
        return pow(2, n-1, n) != 1

# 正解っぽいものの素因数探し
def show(target):
    print(target, end = " ")
    for n in range(2, 10):
        val = int(target, n)
        for k in range(2, int(math.sqrt(val)) + 1):
            if val % k == 0 :
                print(k, end = " ")
                break            
    val = int(target, 10)
    for k in range(2, int(math.sqrt(val)) + 1):
        if val % k == 0 :
            print(k)
            break
        
def calc(N, J):
    j = 0
    for i in range(pow(2, N-2)):
        target = ("{0:b}".format(pow(2, N-2) + i)) + "1"
        tmp = True
        for n in range(2, 11):
            tmp &= is_not_prime(int(target, n))
        if tmp:
            show(target)
            j += 1
        if j == J: break
 
 
print("Case #1:")
calc(16,50)