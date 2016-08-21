
def as_base(coin, base):
    digits = len(coin)
    return sum([int(c) * base**(digits-k-1) for (k,c) in enumerate(coin)])

def find_factor(n):
    checks = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
              103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,
              199,211,223,227,229,233,239,241,251,257,263,269,271,277,281]

    for t in checks:
        if n % t == 0and t < n:
            return t

    return None

def verify_coin(coin, factors):
    for b in range(2, 11):
        factor = factors[b-2]
        if as_base(coin, b) % factor != 0:
            return False
    return True
    
def random_coin(n):
    import random as r
    while True:
        coin = '1' + ''.join([r.choice(['0', '1']) for x in range(n-2)]) + '1'
        factors = []
        for b in range(2, 11):
            f = find_factor(as_base(coin, b))
            if f:
                factors += [f]
            else:
                # print coin, 'is bad'
                break
        else:
            return (coin, factors)
    
def main():
    t = int(raw_input().strip()) # ignored
    n, j = raw_input().strip().split()
    n, j = int(n), int(j)
    coins = {}
    lines = []
    print 'Case #1:'
    while j > 0:
        coin, factors = random_coin(n)
        if not verify_coin(coin, factors):
            print 'bad coin', coin, str(factors)
        if coin in coins:
            continue
        coins[coin] = 'yes'
        j -= 1
        print coin + ' ' + ' '.join([str(f) for f in factors])

if __name__ == '__main__':
    main()

