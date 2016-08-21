import sys
import itertools
from math import sqrt, log

output_line = "Case #{X:d}:\n{answer}"

def is_not_prime(n):
    """Returns true if n is prime
    
    int -> Bool
    """
    if n > 2 and n % 2 == 0: return 2
    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return x
    else:
        return None

def is_coin(n):  # takes the str rep
    factors = []
    for base in range(2, 11):
        newint = int(n, base)
        factors.append(is_not_prime(newint))
    if not all(factors):
        return False
    return factors

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            N, J = map(int, inhandle.readline().split())


            coins = []
            for n in itertools.count(2 ** (N - 1) + 1, 2):
                n = bin(n)[2:]
            # for n in ['100011', '111111', '111001']:
                factors = is_coin(n)
                if factors:
                    coins.append((n, factors))
                    print(n)
                    print(factors)
                if len(coins) >= J:
                    break

            answers = [' '.join(itertools.chain([n], map(str, factors))) for n, factors in coins]

            outline = output_line.format(X=t + 1, answer='\n'.join(answers))
            print(outline, file=outhandle)
            print(outline)
