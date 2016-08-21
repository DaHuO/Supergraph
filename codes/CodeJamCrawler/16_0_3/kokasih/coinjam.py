import itertools
from sys import argv

def is_prime(num):
    if num % 2 == 0:
        return False, 2

    for factor in range(3, int(num**0.5), 2):
        if num % factor == 0:
            return False, factor

    return True, num

def solve(in_file, out_file):
    inp = open(in_file)
    out = open(out_file, 'w')
    _ = inp.readline() #skip number of test case
    length, target = map(int, inp.readline().split())
    target_bases = list(range(2, 11))

    found = 0

    out.write("Case #1:\n")
    for middles in itertools.product(["0", "1"], repeat=length - 2):
        src = "1" + "".join(middles) + "1"
        divs = []
        n = []
        for base in target_bases:
            num = int(src, base)
            prime, factor = is_prime(num)
            if prime:
                break
            else:
                n.append(num)
                divs.append(factor)

        if len(divs) == len(target_bases):
            found += 1
            out.write("{} {}\n".format(src, " ".join(map(str,divs))))

        if found == target:
            break

if __name__ == "__main__":
    solve(argv[1], argv[2])
