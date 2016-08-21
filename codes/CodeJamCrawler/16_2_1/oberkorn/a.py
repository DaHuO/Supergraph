#!/usr/bin/env python
import fileinput


def remove_number(m, number):
        for c in list(number):
                m[c] -= 1
                if m[c] == 0:
                        del m[c]

def solve(a):
        mchars = {}
        out = []
        for c in list(a):
            if mchars.has_key(c):
                    mchars[c] += 1
            else:
                    mchars[c] = 1
        # step 1
        for c in [('Z', 0, "ZERO"), ('U', 4, "FOUR"), ('X', 6, "SIX"), ('G', 8, "EIGHT"), ('W', 2, "TWO")]:
                if mchars.has_key(c[0]):
                        for i in range(mchars[c[0]]):
                            out.append(c[1])
                            remove_number(mchars, c[2])
        # step 2
        for c in [('H', 3, "THREE"), ('R', 3, "THREE"), ('T', 3, "THREE"), ('F', 5, "FIVE")]:
                if mchars.has_key(c[0]):
                        for i in range(mchars[c[0]]):
                            out.append(c[1])
                            remove_number(mchars, c[2])

        # step 3
        for c in [('I', 9, "NINE"), ('V', 7, "SEVEN"), ('O', 1, "ONE")]:
                if mchars.has_key(c[0]):
                        for i in range(mchars[c[0]]):
                            out.append(c[1])
                            remove_number(mchars, c[2])
        return out

def main():
        firstline=True
        case = 0
        for line in fileinput.input():
                if firstline:
                        firstline=False
                        continue
                a = line.strip()
                case += 1
                b = solve(a)
                print "Case #%i: %s" % (case, "".join(map(str, sorted(b))))


if __name__ == "__main__":
        main()
