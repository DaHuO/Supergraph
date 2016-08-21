import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i > 0:
            line = line[:-1]
            n = int(line)
            insomnia = False
            done = False
            if n == 0:
                insomnia = True
            else:
                num = 0
                seen = []
                for k in range(10):
                    seen.append(False)
                while not done:
                    num += n
                    numstr = str(num)
                    for c in numstr:
                        d = int(c)
                        seen[d] = True
                    done = True
                    for k in range(10):
                        if not seen[k]:
                            done = False
            print("Case #%i: %s" % (i, "INSOMNIA" if insomnia else str(num)))

if __name__ == "__main__":
    main()
