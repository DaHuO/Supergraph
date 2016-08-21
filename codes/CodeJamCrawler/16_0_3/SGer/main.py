import random
import itertools
import math

def is_prime(number):
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False

    odd_part = number - 1

    times_two = 0

    while odd_part % 2 == 0:
        odd_part //= 2
        times_two += 1

    for time in range(3):
        while True:
            random_num = random.randint(2, number)-1
            if (random_num != 0) and (random_num != 1):
                break

        random_nump = pow(random_num, odd_part, number)

        if (random_nump != 1) and (random_nump != number - 1):
            iteration = 1

            while (iteration <= times_two - 1) and (random_nump != number - 1):
                random_nump = pow(random_nump, 2, number)
                iteration += 1
            if random_nump != number - 1:
                return False
    return True


def valid_jamcoin(n):
    base2 = int(n, 2)
    base3 = int(n, 3)
    base4 = int(n, 4)
    base5 = int(n, 5)
    base6 = int(n, 6)
    base7 = int(n, 7)
    base8 = int(n, 8)
    base9 = int(n, 9)
    base10 = int(n, 10)
    if is_prime(base2) or is_prime(base3) or is_prime(base4) or is_prime(base5) or is_prime(base6) \
            or is_prime(base7) or is_prime(base8) or is_prime(base9) or is_prime(base10):
        return False
    else:
        return True


def find_divisors(n):
    basex = []
    for i in range(2, 11):
        basex.append(int(n, i))
    #print(basex)
    divisors = []
    for num in basex:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                break
    return divisors

# main
infile = open("C-small-attempt1.in",'r')
outfile= open("c3.out",'w')
T = int(infile.readline())
n,j = infile.readline().split()
n = int(n)
j = int(j)

all = []
for x in map(''.join, itertools.product('01', repeat=n-2)):
    all.append(x)

jamcoins = []
start = '1'
end = '1'
k = 0
jc = start + all[k] + end
i = 0
while i < j:
# while jc != start + all[-1] + end:
    # print(jc)
    if valid_jamcoin(jc):
        if jc not in jamcoins:
            jamcoins.append(jc)
            i += 1
    k += 1
    jc = start + all[k] + end
if i != j:
    jc = start + all[-1] + end
    if valid_jamcoin(jc):
        jamcoins.append(jc)

outfile.write("Case #" + str(T) + ':\n')
for jamcoin in jamcoins:
    divisors = find_divisors(jamcoin)
    result = ''
    for divisor in divisors:
        result += ' ' + str(divisor)
    outfile.write(jamcoin + result + '\n')
infile.close()
outfile.close()