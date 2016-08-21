import time
input_file = open("input.dat", 'r')

def isPrime(n):
    start = time.time()
    for i in xrange(2,int(n**0.5)+1):
        if time.time() - start > 0.05:
            return (True, None)
        if n%i==0:
            return (False, i)

    return (True, None)

wasted = input_file.readline()

size, quantity = map(int, input_file.readline().split(" "))

jamcoin = ['0'] * size
jamcoin[0] = '1'
jamcoin[-1] = '1'
jamcoin = ''.join(jamcoin)

print "Case #1:"

total_cnt = 0
while total_cnt < quantity:
    # print ' >', jamcoin
    is_jamcoin = True
    divisors = []
    for base in range(2, 11):
        num = int(jamcoin, base)
        res = isPrime(num)
        if res[0]: # it's prime
            is_jamcoin = False
            break
        else:
            divisors.append(res[1])

    if is_jamcoin:
        print jamcoin, " ".join(map(str, divisors))
        total_cnt += 1

    x = int(jamcoin, 2)
    x = x + 2
    jamcoin = bin(x)[2:]




