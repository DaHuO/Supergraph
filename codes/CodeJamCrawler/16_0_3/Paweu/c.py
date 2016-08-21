import primefac

f = open('c.in', 'r').read().splitlines()
f = f[1:]
f = f[0].split(' ')


n, j = int(f[0]), int(f[1])


def isprime(num, base):
    n = int(num, base)
    p = primefac.primefac(n)
    data = 1
    try:
        data = p.next()
        p.next()
    except:
        return True, 1
    return False, data


def notprime_bulk(num):
    divisors = []
    for base in range(2, 11):
        v = isprime(num, base)
        if(v[0]):
            return False, 1
        divisors.append(str(v[1]))

    return True, divisors


def numgen(power):
    for x in xrange(2**power):
        yield "1" + str(bin(x)[2:].zfill(power)) + "1"

gen = numgen(n - 2)


output = "Case #1:\n"

for value in gen:
    v = notprime_bulk(value)
    if(v[0]):
        output += "{} {}\n".format(value, " ".join(v[1]))
        j-=1
        if j == 0:
            break
f = open('cx.out', 'w')
f.write(output)
