import os

def main():
    with open("B-large.out", "w") as fout:
        with open("B-large.in", "r") as fin:
            line = fin.readline()
            line = fin.readline()
            i = 1
            while line != "":
                num = num_flips(line.strip())
                fout.write("Case #{0}: {1}\n".format(i, num))
                line = fin.readline()
                i += 1

def num_flips(s):
    s += '+'
    sign = s[0]
    count = 0
    for pan in s:
        if pan != sign:
            sign = pan
            count += 1
    return count

if __name__=="__main__":
    main()
