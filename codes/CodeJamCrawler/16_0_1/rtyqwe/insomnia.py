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
        N = data[x+1].strip()
        awake = True
        if int(N) == 0:
            awake = False
        flags = [False for ran in range(0, 10)]
        multiplier = 1
        while awake:
            for c in str(multiplier * int(N)):
                if not flags[int(c)]:
                    flags[int(c)] = True
            if all(flag is True for flag in flags):
                awake = False
            else:
                multiplier += 1
        if int(N)*multiplier is 0:
            output.write("Case #{}: INSOMNIA\n".format(x+1))
        else:
            output.write("Case #{}: {}\n".format(x+1, int(N)*multiplier))

if __name__ == '__main__':
    main()
