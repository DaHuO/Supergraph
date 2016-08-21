print "Case #1:"


def intToBase(intBefore, base):
  digits = []
  while intBefore:
    digits.append(str(intBefore % base))
    intBefore /= base
  digits.reverse()
  return ''.join(digits)


def isPrime(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    
    divisor = 3
    
    while divisor * divisor <= n and divisor < 1000:
        if n % divisor == 0:
            return divisor
        print divisor
        divisor += 2

    return -1

outputs = []
number = 2147484377
convert = intToBase(number, 2)

while len(outputs) < 350:
    bases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    divisors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print convert
    print number
    print ' ' 
    print ' '
    print ' '
    print ' ' 
    print ' '
    print ' '
    for base in range(2, 11):
        bases[base] = int(convert, base)
        print bases
        divisors[base] = str(isPrime(bases[base]))
        if divisors[base] == '-1':
            number += 2
            convert = intToBase(number, 2)
            break
    else:
        outputs.append(convert + ' ' + ' '.join(divisors[2:]))
        number += 2
        convert = intToBase(number, 2)
    
for i in outputs:
    print i
