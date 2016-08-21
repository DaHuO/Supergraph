import sys
import math

def toCoin(x):
    text = bin(x)[2:]
    while len(text) < n - 2:
        text = "0" + text
    return "1" + text + "1"

def isPrime(n):
    if n == 2 or n == 3:
        return -1
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1
    if n == 10000000011010111 or n==1853020194166333 or n == 10110011111111111 or n == 4294983937 or n == 94207 or n == 2821122000691 or n == 2821109909011 or n == 282103269068801:
        return -1
    if n % 1152846547 == 0:
        return 1152846547
    if n% 197123 == 0:
        return 197123
    try:
        #print("test " + str(n))
        for i in range(3, min(int(math.sqrt(n)) + 1, 50000),2):
            if n % i == 0:
                return i
    except ValueError:
        print("ValueError " + str(n))
        return -1 
    return -1

def convert(number, system):
    r = 0
    for n in number:
        r += pow(system, int(number))
    return r

n = 32
j = 500
print("Case #1:")

numbers = []
vnumbers = []
index = 0
found = 0
while found < j:
    vnumbers = numbers[:]
    if len(numbers) < 9:
        for system in range(2, 11):
            numbers.append(1 + pow(system, n-1))
    else:
        coin = toCoin(index)[1:n-1]
        vcoin = toCoin(index-1)[1:n-1]

        for c in range(n-2):
            if not coin[c] == vcoin[c]:
                for system in range(2, 11):
                    diff = pow(system, n-2-c)
                    if coin[c] == "1":
                        numbers[system - 2] += diff
                    else:
                        numbers[system - 2] -= diff

    #print(toCoin(index))
    results = []
    for number in numbers:
        result = isPrime(number)
        if result is -1:
            # number is prime
            #if number > 1000000000:
            #    print(str(number))
            break
        results.append(str(result))

    if len(results) == 9:
        # found coinjam
        text = toCoin(index) + " "
        text += " ".join(results)
        print(text)
        #print(numbers)
        found += 1

    index += 1