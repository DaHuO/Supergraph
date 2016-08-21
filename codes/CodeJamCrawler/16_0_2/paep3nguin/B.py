#! python3

def main():
    with open("B-large.in") as in_file:
        with open("B-large.out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().strip()
                pancakes = [True if c == "+" else False for c in reversed(line)]
                n = 0
                while sum(pancakes) != len(pancakes):
                    n += 1
                    flip = pancakes.index(False)
                    pancakes = [not p if i >= flip else p for i, p in enumerate(pancakes)]

                print("Case #{0}: {1}".format(x + 1, n), file=fout)

if __name__ == "__main__":
    main()
