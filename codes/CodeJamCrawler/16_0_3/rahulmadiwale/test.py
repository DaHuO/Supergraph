def check(num):
    for i in range( 2, int(num**.5) + 2 ):
        if num % i == 0:
            return i
            break
    return -1

def create_num( num, base ):
    i = 1
    temp = 0
    while num > 0:
            temp = temp + (num % 10) * i
            i = i*base
            num = num / 10
    return temp

def valid(num):
    a = str(num)
    for i in range(2,10):
        if str(i) in a:
            return False
    if num % 10 == 1:
        return True
    else: return False

found = 0
a = 1000000000000001
print "Case #1:"

while found < 50:
    factors = []
    if valid(a) :
        for bases in range(2, 11):
            num = create_num(a, bases)
            res = check(num)
            if res == -1:
                break
            else:
                factors.append(res)
    if len(factors) == 9:
        print a,
        for e in factors:print e,
        found = found + 1
        print
    a = a + 1

