import sys
import random

def gen_random(l):
    return "1" + ''.join(random.choice(("0", "1")) for _ in range(l - 2)) + "1"


def find_divisor(n):
    for d in range(2, n):
        if ((n // d) * d) == n:
            return d
        if d * d > n:
            return None


def main(in_file):
    inf = open(in_file)
    outf = open(in_file + ".result", "w")

    numlines = int(inf.readline())

    for casenum in range(1, numlines + 1):
        (l, num) = map(lambda x: int(x), inf.readline().split(" "))

        res = ""
        done = set()
        while num > 0:
            cand = gen_random(l)
            if cand in done:
                continue

            bases = []
            for base in range(2, 11):
                val = int(cand, base)
                div = find_divisor(val)
                if div is None:
                    break
                bases.append(div)

            if len(bases) == 9:
                done.add(cand)
                res += "\n" + cand + " " + " ".join(map(lambda x: str(x), bases))
                sys.stderr.write(str(num) + " to go...\n")
                num -= 1

        result(casenum, res, outf)

    outf.close()
    inf.close()


def result(casenum, result, outf):
    s = "Case #%d: %s\n" % (casenum, result)
    sys.stdout.write(s)
    outf.write(s)


if __name__ == "__main__":
    main(sys.argv[1])
