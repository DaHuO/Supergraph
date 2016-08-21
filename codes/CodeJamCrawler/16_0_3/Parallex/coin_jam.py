import math, random
import sys
import threading
from time import sleep
import _thread as thread

def cdquit(fn_name):
    # print to stderr, unbuffered in Python 2.
    sys.stderr.flush() # Python 3 stderr is likely buffered.
    thread.interrupt_main() # raises KeyboardInterrupt

def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, cdquit, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer


def from_decimal(base_10, base):
    # max is 10
    if base_10 == 0:
        return 0
    digits = []
    log = math.floor(math.log(base_10, base))
    while log != -1:
        digit = base_10 // base**log
        base_10 -= digit * base**log
        digits.append(str(digit))
        log -= 1
    return int("".join(digits))

def is_prime(n, k=5):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    d = n - 1
    # obtain n - 1 in the form 2^s * d where
    # d is odd
    s = 0
    while d % 2 == 0:
        d /= 2
        s += 1
    # k is a parameter that determines the accuracy of a test
    for i in range(k):
        # generate a in the range [2..n-1]
        a = random.randint(2, n-1)
        x = pow(a, int(d), n)   # equivalent to a**d mod n
        if x == 1 or x == n-1:
            continue
        for r in range(s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                # next i
                break
        else:
            return False
    # n is probably prime
    else:
        return True

@exit_after(1)
def pollard_rho(n):
    """Attempt to find a factor of n.
       Effective when n has a small prime factor."""
    g = lambda x : (pow(x, 2, n) + 1) % n
    x, y, d = 2, 2, 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    else:
        return d

def gcd(a, b):
    """Return gcd of a and b."""
    while b:
        a, b = b, a % b
    return a

def get_valid_coins(coin_length):
    # first and last digit must be a 1 and the number can
    # only consist of 1s and 0s
    # hence there are 2**(coin_length-2) possible coins
    for i in range(0, 2**(coin_length-2), 2):
        binary = str(bin(i))[2:]
        zeros = coin_length-2 - len(binary)
        yield ("1"+"".join(["0"]*zeros)+binary+"1")
        
def total_comp(n):
    divisors = []
    for base in range(2, 11):
        base10 = int(str(n), base)
        if is_prime(base10):
            return False
        else:
            try:
                divisor = pollard_rho(base10)
            except:
                #took too long
                return False
            divisors.append(divisor)
    else:
        return divisors

with open("out_large.txt", "w") as file:
    file.write("Case #1:\n")
            
length = 32
jamcoins = 500
valid_jamcoins = 0

for pot_coin in get_valid_coins(length):
    if valid_jamcoins == jamcoins:
        break
    divisors = total_comp(pot_coin)
    if divisors:
        print(pot_coin)
        valid_jamcoins += 1
        #output
        with open("out_large.txt", "a") as file:
            file.write(str(pot_coin))
            for divisor in divisors:
                file.write(" "+str(divisor))
            file.write("\n")
