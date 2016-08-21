#!/usr/bin/python

import sys

def prime_test(num):
    num = str(num)
    if num[-1] == '0': #10 - simple test so do it first
        return 10
    if int(num[-1]) % 2 == 0: #2
        return 2
    quick = 0
    for i in range(len(num)):
        if i % 2 == 0:
            quick += int(num[i])
        else:
            quick -= int(num[i])

    if num[-1] == '0' or num[-1] == '5': #5
        return 5
    if sum(map(int, list(num))) % 3 == 0: #3
        return 3
    
    #if num[-3:] #8 ... would be divisible by 2, ignore
    quick = int(num[:-1]) - int(num[-1])*2
    if quick != 0 and quick % 7 == 0:  #7 should test this last, probably expensive (or don't test)
        return 7

    #if num % 2 == 0:
    #    return 2
    #for x in range(3, int(num**0.5) + 1, 2):
    #    if num % x == 0:
    #        return x
    return True


def get_coins(N, J):
    #cur = "110011"
    #for i in range(2, 11):
    #    print('{:} in base {:} = {:}, prime = {:}'.format(cur, i, int(cur, base=i), prime_test(int(cur, base=i)))) 
    coins = list()
    cur = '1' + ('0'* (N-2)) + '1'
    while len(coins) < J and len(cur) == N:
        div = False
        divs = list()
        for thisBase in range(2,11):
            div = prime_test(int(cur, base=thisBase))
            if div != True:
                divs.append(div)
            else:
                cur = '{0:b}'.format(int(cur, base=2) + 2)
                break
        if div != True:
            coins.append
            divs.insert(0, cur)
            coins.append(divs)
            #print('got one!')
            #print(divs)
            cur = '{0:b}'.format(int(cur, base=2) + 2)
    return coins




with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        N, J = map(int, f.readline().split())
        coins = get_coins(N,J)
        print("Case #{:}:".format(case+1))
        
        for coin in coins:
            print(' '.join(map(str, coin)))


#N = 16
#J = 50
#N = 6
#J = 10**5
#coins = get_coins(N, J)
#print("Case #1:")



