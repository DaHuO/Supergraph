import math

def get_number(base, string):
    index = len(string) - 1
    number = 0
    for i in string:
        d = int(i)
        number += d * pow(base, index)
        # print index
        index -= 1
    return number


def get_non_trivial_divisor(number):
    factor = 1
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            factor = i
            break
    return factor

def is_jam_coin(string):
    factors = []
    for i in range(2, 11):
        f = get_non_trivial_divisor(get_number(i, string))
        if f == 1:
            return False, -1
        factors.append(f)
    return True, factors

def get_binary_string(number, length):
    res = ""
    while number > 0:
        r = number % 2
        number = number / 2
        res = str(r) + res 
    a = length - len(res)
    if a < 0:
        a = 0
    for i in range(a):
        res = "0" + res
    return res

def print_jam_coins(n, j):
    count = 0
    for i in range(pow(2, n - 2)):
        c = "1" + get_binary_string(i, n-2) + "1"
        r, f = is_jam_coin(c)
        if r:
            s = ""
            for k in f:
                s += " "
                s += str(k)
            s.strip()
            
            print c, s
            count += 1
        if count == j:
            break

t = int(raw_input())

for i in range(t):
    n, j = raw_input().split()
    n = int(n)
    j = int(j)

    print "Case #1:"
    print_jam_coins(n, j)

    
