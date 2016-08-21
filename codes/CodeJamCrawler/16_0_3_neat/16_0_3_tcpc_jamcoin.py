from math import sqrt

def divisor(n):
    for i in range(2, min(int(sqrt(n)), 1000)):
        if n % i == 0:
            return i

    return -1

def divisors(jamcoin):
    res = []

    for b in range(2, 11):
        jamcoin_b = int(jamcoin, b)

        div = divisor(jamcoin_b)

        if div == -1:
            return []
        else:
            res.append(div)

    return res

if __name__ == "__main__":
    n = 16
    j = 50

    base = "".zfill(n-2)

    with open("C-small.out", "w") as output:
        output.write("Case #1:\n")

        count = 0

        while (count < j):
            print("1" + base + "1")

            divs = divisors("1" + base + "1")

            if (divs != []):
                output.write("1" + base + "1")

                for d in divs:
                    output.write(" " + str(d))

                output.write("\n")

                count += 1

            base = "{0:b}".format(int(base, 2) + 1).zfill(n-2)
