#!/apollo/bin/env python
import argparse


def main():

    """Main."""
    parser = argparse.ArgumentParser(description="Node count check on cluster or host")
    parser.add_argument('-f', '--file')
    args = parser.parse_args()
    f = open(args.file)
    data = f.readlines()
    T = data[0].strip()
    output = open('workfile', 'w')
    for x in range(0, int(T)):
        pancakes = data[x+1].strip()
        pos = 0
        flips = 0
        while pos < len(pancakes):
            cur = pancakes[pos]
            flips += 1
            while pos+1 < len(pancakes) and cur == pancakes[pos+1]:
                pos += 1
            pos += 1
        if pancakes[-1] == '+':
            flips -= 1
        output.write("Case #{}: {}\n".format(x+1, flips))


if __name__ == '__main__':
    main()
