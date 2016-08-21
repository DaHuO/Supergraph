fo = open("C-large.out", 'w')

fo.write("Case #1:\n")

primes = []
def get_primes(n):
    global primes
    numbers = set(range(n,1 , -1))
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))

get_primes(65536)

def combinaciones(n):
    i = 0
    while (2**(n-2)>=i):
        res = bin(i)[2:]
        c = '1'+(n-2-len(res))*'0'+res+'1'
        yield c
        i+=1

def is_prime(n):
    for i in primes:
        if n % i == 0 and n != i:
            return False,i
    return True,n

def solve(num):
    div = []
    for b in range(2,11):
        cond, val = is_prime(int(num,b))
        if cond:
            return False
        else:
            div.append(val)
    return div

gen = combinaciones(32)
j = 0
for num in gen:
    s = solve(num)
    if s:
        sol = ""
        for e in s:
            sol += " "+str(e)
        fo.write(num+sol + '\n')
        print num, s
        j +=1
    if j >= 500:
        break
