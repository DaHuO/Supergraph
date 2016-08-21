#import time
def converter(num, base):
    total = 0
    factor = 1
    while num != 0:
        total += (num % 10) * factor
        factor *= base
        num /= 10
    return total

def get_binary(num):
    total = 0
    factor = 1
    while num != 0:
        total += (num % 2) * factor
        factor *= 10
        num /= 2
    return str(total)


def check_prime(num):
    i = 2
    while i!= int(num**.5):
        if num%i == 0:
            return False
        i+=1
    return True

def get_divisor(num):
    i = 2
    while i!= int(num**.5):
        if num%i == 0:
            return i
        i+=1
        if i == 10**5 :
            break
        #print i
    return 0

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

def Fermat_test(num):
    begin = 2
    while gcd(begin, num) != 1:
        begin +=1
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(begin, num-1, num) == 1

def doer(N, J):
    N = int(N)
    J = int(J)
    total = 0
    current = 0
    while total != J:
        curr_bin = get_binary(current)
        mult = N-2-len(curr_bin)
        jamcoin = '1'+ '0'*mult + curr_bin + '1'
        jamcoin = int(jamcoin)
        if not Fermat_test(jamcoin):
            #print jamcoin, "begin"
            fl = True
            for i in range(2, 11):
                if Fermat_test(converter(jamcoin, i)):
                    fl = False
                    break
            #print jamcoin, fl
            if fl:
                res = []
                res.append(jamcoin)
                for i in range(2, 11):
                    res.append(get_divisor(converter(jamcoin, i)))
                if 0 not in res:
                    for i in res:
                        print i,
                    print
                    total +=1
        current += 1



if __name__ == '__main__':
    T = input()
    for i in range(T):
        N, J = raw_input().split()
        print 'Case #{}:'.format(i+1)
        doer(N, J)
    #print time.time() - start