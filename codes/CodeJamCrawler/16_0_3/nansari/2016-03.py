import itertools


t = int(raw_input())


def isprime(n):
    divisor = 5
    prime = True
    if n < 2:
        prime = False
    elif n < 4:
        prime = True
    elif n % 2 == 0 or n % 3 == 0:
        prime = False
    else:
        while n >= divisor ** 2:
            if n % divisor == 0 or n % (divisor + 2) == 0:
                prime = False
                break
            divisor += 6
    return prime


def get_divisor(n):
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            break
        else:
            divisor += 1
    return divisor


for x in xrange(1, t + 1):
    n, j = (int(value) for value in raw_input().split())
    print("Case #%d:" % x)
    jamcoins = 1
    for value in itertools.product(xrange(2), repeat=n - 2):
        if jamcoins > j:
            break
        output = "".join(["1"] + [str(hue) for hue in value] + ["1"])
        outputs = [output]
        is_jamcoin = True
        for base in xrange(2, 11):
            temp = long(output, base=base)
            if isprime(temp):
                is_jamcoin = False
                break
            else:
                outputs.append(get_divisor(temp))
        if is_jamcoin:
            temp = "%s " * 10
            print(temp % tuple(outputs))
            jamcoins += 1
