#!/usr/bin/python

import sys

def count_flip(s):
    count = 0
    tmp = s[0]
    for i in range(1, len(s)):
        if s[i] != tmp:
            count += 1
            tmp = s[i]
    if tmp != "+":
        count += 1
    return count

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r") as input, open(output_file, "w") as output:
        t = int(input.readline())
        for i in range(1, t + 1):
            c = count_flip(input.readline().rstrip())
            output.write("Case #{}: {}\n".format(i, c))

if __name__ == "__main__":
    main()
