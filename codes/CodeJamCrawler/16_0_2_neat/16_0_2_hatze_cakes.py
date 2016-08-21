import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i > 0:
            line = line[:-1]
            groups = 0
            current = 'x'
            for char in line:
                if char != current:
                    groups += 1
                    current = char
            n = groups - 1
            start = 0 if line[0] == '+' else 1
            if (start + n % 2) == 1:
                n += 1
            print("Case #%i: %i" % (i, n))

if __name__ == "__main__":
    main()
