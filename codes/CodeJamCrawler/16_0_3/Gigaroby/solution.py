import click
import math


def pad(coin, n):
    if len(coin) < n:
        return "0"*(n-len(coin)) + coin

    return coin

def read_coin(coin, base):
    c = reversed(coin)
    acc = 0
    for i, val in enumerate(c):
        if val == '1':
            acc += (base ** i)

    return acc

def is_prime(n):
    if n <= 1:
        return False, 0
    elif n <= 3:
        return True, n
    elif n % 2 == 0:
        return False, 2
    elif n % 3 == 0:
        return False, 3

    i = 5
    while i ** 2 <= n:
        if n % i == 0:
            return False, i

        if n % (i+2) == 0:
            return False, i+2

        i = i + 6

    return True, 0

def compute(coin):
    divisors = []
    for base in range(2, 11):
        print("trying coin " + coin + " in base " + str(base))
        prime, divisor = is_prime(read_coin(coin, base))
        if prime:
            return False, []

        divisors.append(divisor)


    return True, divisors



def gen_coin(size):
    current = 0
    while current < (2**size):
        coin = "1{}1".format(pad(bin(current)[2:], size-2))
        current += 1
        ok, divs = compute(coin)
        if ok:
            yield coin, divs


@click.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def main(in_file, out_file):
    in_file.readline()
    J, N = (int(x) for x in in_file.readline().strip().split(' '))

    out_file.write("Case #1:\n")
    for i, (coin, proof) in enumerate(gen_coin(J)):
        out_file.write(coin + " " +  " ".join([str(x) for x in proof]) + "\n")
        if i == (N-1):
            break


    

if __name__ == '__main__':
    main()
