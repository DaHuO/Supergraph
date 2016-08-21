from itertools import product
from collections import defaultdict

def main(filename):
    # f = iter(open(filename, "r").readlines())

    # t = int(next(f))
    # for e, _ in enumerate(range(t)):
    #     g = int(next(f).strip())
    #     print("Case #{}: {}".format(e+1, find(g)))

    res = find(1)

    print("Case #1:")
    for (num, div_list) in res:
        print("{} {}".format(num, " ".join([str(j) for j in div_list])))



def first_divisor(n):
    # all other even numbers are not primes
    if not n & 1: 
        return (True, 2)

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, 1000, 2):
        if n % x == 0:
            return (True, x)

    return (False, 1)

def find(llll):
    n = 32
    divisor_length = 500

    onlyres = []

    # every two
    for i in product(range(2), repeat=(n-2)):
        found = True
        current_divisor = []

        for j in range(2, 11):

            n_string = [1] + list(i) + [1]

            two = reversed([j**l for l in range(n)])
            number = sum([b1*b2 for (b1, b2) in zip(n_string, two)])

            (numberBool, div) = first_divisor(number)

            if numberBool:
                # current_divisor.append((j, n_string, two, number, div))
                current_divisor.append(div)
                continue
            else:
                found = False
                break

        if not found:
            continue
        else:
            onlyres.append(("".join([str(o) for o in n_string]), current_divisor))

        if len(onlyres) == divisor_length:
            return onlyres


if __name__ == "__main__":

    filename = "test"
    filename = "A-small-attempt0.in"
    
    filename = "A-large.in"
    main(filename)
