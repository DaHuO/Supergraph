import math
import itertools

def find_divisor(n):
    for i in range(2, int(math.sqrt(float(n))) + 1):
        if n % i == 0:
            return str(i)
    return None

def convert_to_base(num, base, N):
    result = 0
    for digit in num:
        N -= 1
        if digit == '1':
            result += math.pow(base, N)
    return int(result)

result = 0
N = 16
J = 50

print 'Case #1: '
counter = 0
numbers = ["".join(seq) for seq in itertools.product("01", repeat=N-2)]
for num in numbers:
    num = '1' + num + '1'
    divisors = []
    for b in range(2, 11):
        representation = convert_to_base(num, b, len(num))
        divisor = find_divisor(representation)
        if divisor is not None:
            divisors.append(divisor)
    if (len(divisors) == 9):
        print num + ' ' + ' '.join(map(str,divisors))
        counter += 1
        if counter == 50:
            break
