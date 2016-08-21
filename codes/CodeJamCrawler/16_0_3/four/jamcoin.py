from collections import defaultdict
prime_table = {}
def main():
    with open("jamcoin.txt") as data:
        cases = data.readline()
        caseno = 1
        for i in data.readlines():
            array = i.split()
            N, J = int(array[0]), int(array[1])
            print("Case #{}:".format(caseno))
            caseno +=1
            make_coin(N, J)

def shuffle(length):
    start = -1
    shorterlen = length-2
    while start < 2**(shorterlen)-1:
        start += 1
        middle = addzeroes(convert(start, 2), length-2)
        yield "1"+middle+"1"

def make_coin(length, n):
    """make n*coins of length length"""
    factors = defaultdict(list)
    found = 0
    for candidate in shuffle(length):
        if found == n:
            break
        for base in range(2, 11):
            if isprime(int(candidate, base)):
                break
            else:
                factors[candidate].append(onefactor(candidate, base))
                if len(factors[candidate]) == 9:
                    found += 1
    printed = 0
    for num, fac in factors.items():
        if printed == n:
            break
        if len(fac) == 9:
            print(num, end=" ")
            for i in fac:
                print(i, end=" ")
            print("\n", end="")
            printed += 1


def onefactor(n, base):
    coin = int(n, base)
    for i in range(2, coin):
        if coin%i == 0:
            return i
    print("Error, no non-trivial divisors found for ", coin)
    raise "error"


def isprime(n):
    n = int(n)
    if prime_table.get(n) != None:
        return prime_table[n]
    if n == 2:
        prime_table[n] = True
        return True
    if n < 2 or n%2 == 0:
        prime_table[n] = False
        return False
    i = 2
    while i*i <= n:
        if (n%i) == 0:
            prime_table[n] = False
            return False
        i += 1
    prime_table[n] = True
    return True

def convert(num, base):
    index = "0123456789ABCDEF"
    num = int(num)
    if num < base:
        return index[num]
    else:
        return convert(num//base, base)+index[num%base]


def addzeroes(number, minlen):
    add = 0
    length = len(number)
    if length < minlen:
        add = minlen-length
    return "0"*add+number
main()
