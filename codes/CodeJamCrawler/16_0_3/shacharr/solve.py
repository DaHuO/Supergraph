import fileinput
import itertools

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

primes_base = sieve_for_primes_to(2**16)

def find_div(num):
    for d in primes_base:
        if num % d == 0:
            return d
        if d*d > num:
            return 1
    return 1

def is_coin(num):
    s = bin(num)[2:]
    res = []
    for i in range(2,11):
        div = find_div(int(s,i))
        if div == 1:
            return (False,[])
        res.append(div)
    return (True, res)


def collect_coins(N,J):
    coins = []
    for i in itertools.count(2**(N-1)+1,2):
        if i >= 2**N:
            break
        (coin,divs) = is_coin(i)
        if coin:
            coins.append((i,divs))
            if len(coins) >= J:
                return coins
    return coins


def format_coin(coin):
    b = bin(coin[0])[2:]
    return " ".join([b]+[str(x) for x in coin[1]])

def solve(i,N,J):
    coins = collect_coins(N,J)
    print "Case #%d:"%i
    for coin in coins:
        print format_coin(coin)


def main():
    it = fileinput.input()
    l = it.next()
    for i,l in enumerate(it,1):
        N,J = [int(x) for x in l.split()]
        solve(i,N,J)

if __name__ == "__main__":
    main()
