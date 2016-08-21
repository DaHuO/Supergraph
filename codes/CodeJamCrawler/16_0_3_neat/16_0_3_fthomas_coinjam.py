def main():
    n = 32
    j = 500
    factors = [0]*11
    with open("coinjam.out", "w") as fout:
        fout.write("Case #1:\n")
        i = '1' + "".join(['0']*(n-2)) + '1'
        while j != 0:
            for k in range(2, 11):
                tmp = factor(int(i, k))
                if tmp == -1:
                    break
                factors[k] = tmp
            else:
                fout.write("{0}".format(i))
                for k in range(2, 11):
                    fout.write(" {0}".format(factors[k]))
                fout.write("\n")
                j -= 1
            i = bin(int(i, 2) + 0b10)[2:]


def factor(n):
    """
    returns one factor of n, -1 if primes
    """
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i < 100:
        if n % i == 0:
            return i
        if n % (i+2) == 0:
            return i+2
        i += 6
    return -1


if __name__=="__main__":
    main()
