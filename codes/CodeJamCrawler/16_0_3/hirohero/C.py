f = open('Coutput_large.txt','w')
prime = [True for i in range(20000)]

prime[0] = False
prime[1] = False

prime_list = []
for i in range(2, 10000):
    if prime[i]:
        prime_list.append(i)
        j = i
        while j + i < 10000:
            j = j + i
            prime[j] = False

def is_prime(x):
    for prime_number in prime_list:
        if prime_number * prime_number > x:
            break
        if x % prime_number == 0:
            return False
    return True

def nhiphan(x):
    tmp = ''
    while x > 0:
        tmp = tmp + str(x % 2)
        x = x // 2
    return tmp

def chuyen(s, x):
    mu = 1
    s = s[::-1]
    tmp = 0
    for i in range(len(s)):
        tmp = tmp + int(s[i]) * mu
        mu = mu * x
    return tmp

n = 32
t = 500
min_number = (1 << (n - 1)) + 1
max_number = 1 << n
print >> f, "Case #1:"

now = min_number
while now < max_number:
    ok = True
    np = nhiphan(now)
    for i in range(2, 11):
        x = chuyen(np, i)
        if is_prime(x):
            ok = False
            break
    if ok:
        t -= 1
        print >> f, np,
        for i in range(2, 11):
            x = chuyen(np, i)
            j = 0
            while x % prime_list[j] != 0:
                j += 1
            print >> f, prime_list[j],
        print >> f
        if t <= 0:
            break
    now += 2

f.close()

