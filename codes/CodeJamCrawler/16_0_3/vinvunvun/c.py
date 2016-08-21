import math

f = open('c.txt', 'r')
output = open('cr.txt','w')


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False, n/2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False, i
    return True, None

result = []
f.readline()
for line in f.readlines():
    s = line.split(" ")
    n = int(s[0])
    j = int(s[1])

    s = list("0"*n)
    s[0] = '1'
    s[-1] = '1'
    s = "".join(s)
    i = 0
    bases = [2,3,4,5,6,7,8,9,10]

    while i != j:
        print(s)
        prime = False
        ks = []
        not_primes = []
        for base in bases:
            value = int(s, base)
            p, factor = is_prime(value)
            if p:
                prime = True
                break
            else:
                not_primes.append(value)
                ks.append(factor)

        if not prime:
            print(not_primes)
            result.append(s + " " + " ".join([str(k) for k in ks]))
            i += 1

        s = "{0:b}".format(int(s, 2) + 2)


print result
i = 1

output.write("Case #1:\n")
for r in result:
    output.write(r+"\n")
    i += 1
