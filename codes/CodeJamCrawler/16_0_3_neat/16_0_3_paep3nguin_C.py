#! python3

import itertools

def main():
    with open("C-large.in") as in_file:
        with open("C-large.out", "w") as fout:
            in_file.readline()

            N, J = [int(i) for i in in_file.readline().strip().split(' ')]
            jamcoins = []

            for n in range(2**(N-2)):
                coin = "1" + "{:0>{}}".format(bin(n)[2:], N - 2) + "1"
                entry = [coin]
                for b in range(2, 11):
                    rep = int(coin, b)
                    d = divisors(rep)
                    if d:
                        entry.append(d)
                    else:
                        break
                if len(entry) == 10:
                    jamcoins.append(entry)
                if len(jamcoins) == J:
                    break

            print("Case #1:", file=fout)
            for j in jamcoins:
                print(" ".join([str(n) for n in j]), file=fout)

def divisors(n):
    for i in range(2, 20):
        if n % i == 0:
            return i
    return False

if __name__ == "__main__":
    main()
