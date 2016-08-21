'''
Created on 09-Apr-2016

@author: nigel
'''

import time, math, random, itertools

#calculates (a^b)%c
def modulo(a, b, c):
    res = 1
    y = a
    while(b>0):
        if(b%2 == 1):
            res = (res*y)%c
        y = (y*y)%c
        b /= 2
    return res%c
    

def is_composite_fermat(n):
    if (n<2):
        #need non trivial composites
        return False
    if ((n != 2) and (n%2 == 0)):
        return True
    for i in range(1):
        a = random.randint(1, n-1)
        if(modulo(a, (n-1), n) != 1):
            return True
    return False
    

#60077 and 1413760081 are giving incorrect output for below function
def is_composite_miller_rabin(n):
    if (n<2):
        #need non trivial composites
        return False
    if ((n != 2) and (n%2 == 0)):
        return True
    s = n-1
    while(s%2 == 0):
        s/=2
    for i in range(1):
        a = random.randint(1, n-1)
        temp = s
        mod = modulo(a, temp, n)
        while((temp != (n-1)) and (mod != 1) and (mod != (n-1))):
            mod = modulo(mod, mod, n)
            temp *= 2
        if((mod != (n-1)) and (temp%2 == 0)):
            return True
    return False


def find_div(base):
    div = [0 for i in xrange(9)]
    for i in xrange(9):
        n = base[i]
        #(int(math.sqrt(n)) + 1)
        if(n % 2 == 0):
            div[i] = 2
        else:
            for j in itertools.count(3, 2):
                if(j>100000):
                    return False
                if (n % j == 0):
                    div[i] = j
                    break
    return div


if __name__ == '__main__':
    #print is_composite_fermat(60077)
    #print is_composite_fermat(1413760081)
    start = time.time()
    f1 = open('c_large_output.in', 'w')
    f1.write("Case #1:\n")
    n = 0
    num = 0
    while(n < 500):
        print n
        flag_coin = True
        base = [0 for i in xrange(9)]
        rand_bin = '0b1' + format(num, '030b') + str(1)
        #print rand_bin
        for i in xrange(9):
            base[i] = int(rand_bin[2:], i+2)
            if(is_composite_fermat(base[i])):
                continue
            else:
                flag_coin = False
                break 
        if (flag_coin == True):
            #for i in range(9):
                #print(" " + str(base[i]))
            div = find_div(base)
            if(div != False):
                n += 1
                f1.write(rand_bin[2:])
                for i in xrange(9):
                    f1.write(" " + str(div[i]))
                f1.write('\n')
        num += 1
          
    f1.close()
    end = time.time()
    print end - start