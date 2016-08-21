import datetime
N = 6
J = 3


def factors(n):
    s = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    s.remove(1)
    s.remove(n)
    return s


def findfact(n):
    for x in range(2,int(n**0.5) + 1):
        if (n % x) == 0:
            return x
    return 0


def per(x, max_iter):
    ret = []
    found_num = 0
    n = x - 2
    for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        num_to_check = '1'+s+'1'
        is_suit = True
        factors_for_num = []
        for base in range(2,11):
            number = int(num_to_check, base)
            fac = findfact(number)
            if fac:
                factors_for_num.append(fac)
            else:
                is_suit = False
                break
        if is_suit:
            print num_to_check + ' ' + str(factors_for_num)
            found_num = found_num + 1
            if (found_num == max_iter):
                break


    #return ret

per(16,50)

#a = datetime.datetime.now()
#print primes(3000)

#print factors(320000000000)
#b = datetime.datetime.now()
#print(b-a)