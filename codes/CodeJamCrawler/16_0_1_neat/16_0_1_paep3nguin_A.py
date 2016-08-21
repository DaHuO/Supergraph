#! python3

def main():
    with open("A-large.in") as in_file:
        with open("A-large.out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().strip()
                digits = set()
                n = 0
                orig = int(line)
                end = 'INSOMNIA'
                if orig != 0:
                    while len(digits) != 10:
                        n += orig
                        for c in str(n):
                            digits.add(c)
                            if len(digits) == 10:
                                break
                    end = n

                print("Case #{0}: {1}".format(x + 1, end), file=fout)

if __name__ == "__main__":
    main()
