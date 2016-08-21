from math import sqrt;
import random

def generate_coin(n):
    coin = "1"
    for i in range(n - 2):
        coin += str(random.randint(0, 1)) 
    coin += "1"
    return coin

def is_prime(n):
    if (n <= 2):
        return True
    limit = int(sqrt(n))
    for i in range(2, limit):
        if (n % i == 0):
            return False
    return True

def is_coin(c):
    for i in range(2, 11):
        if is_prime(int(c, i)):
            return False 
    return True

def find_divisors(c):
    result = ""
    for i in range(2, 11):
        result += str(find_divisor(int(c, i)))
        result += " "
    return result

def find_divisor(i):
    for j in range (2, int(sqrt(i))):
        if (i % j == 0):
            return j

def main():
    f = open(input())
    t = f.readline()
    a = f.readline().split()
    n = int(a[0])
    j = int(a[1])
    d = dict()
    print("Case #1:")
    count = 0
    while count != j:
        coin = generate_coin(n)
        if is_coin(coin) and not coin in d.keys():
            d[coin] = True
            print("%s %s" % (str(coin), find_divisors(coin)))
            count += 1

if __name__ == "__main__":
    main()
