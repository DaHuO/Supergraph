def primes(num):
    for i in xrange(2, 17):
        if num % i == 0:
            return i
    return 0


def jamcoin(binary):
    numbers = representations(binary)
    return [primes(a) for a in numbers]


def representations(binary):
    length = len(binary)
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index, char in enumerate(binary):
        if char == '1':
            for i in range(len(result)):
                result[i] += (i + 2)**(length - index - 1)
    return result


def tobinary(num):
    return "{0:#b}".format(num)[2:]


with open('output16.txt', 'w') as out16:
    j16 = 0
    i = 0
    while j16 < 50:
        num16 = '1' + tobinary(i).zfill(16 - 2) + '1'
        jam16 = jamcoin(num16)
        i += 1
        if all(jam16):
            j16 += 1
            out16.write(num16 + ' ' + ' '.join(map(str, jam16)) + '\n')

with open('output32.txt', 'w') as out32:
    j32 = 0
    i = 0
    while j32 < 500:
        num32 = '1' + tobinary(i).zfill(32 - 2) + '1'
        jam32 = jamcoin(num32)
        i += 1
        if all(jam32):
            j32 += 1
            out32.write(num32 + ' ' + ' '.join(map(str, jam32)) + '\n')
