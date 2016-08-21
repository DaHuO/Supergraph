def get_divisor(num):
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i
    return None

N = 16
J = 50

print 'Case #1:'
for num in xrange(2 ** (N - 1), 2 ** N):
    binary = "{0:b}".format(num)
    if binary[0] != '1' or binary[-1] != '1' or len(binary) != N:
        continue
    divisors = []
    for base in xrange(2, 11):
        number = int(binary, base)
        divisor = get_divisor(number)
        if divisor:
            divisors.append(divisor)
        else:
            break

    if len(divisors) != 9:
        continue
    J -= 1
    print binary, ' '.join(str(x) for x in divisors)
    if J == 0:
        break
