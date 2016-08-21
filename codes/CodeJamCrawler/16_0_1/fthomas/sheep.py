def main():
    with open("sheep.out", "w") as fout:
        with open("A-large.in", "r") as fin:
            fin.readline()
            line = fin.readline()
            i = 1
            while line != "":
                tmp = sleep_on(int(line))
                if tmp == -1:
                    fout.write("Case #{}: INSOMNIA\n".format(i))
                else:
                    fout.write("Case #{0}: {1}\n".format(i, tmp))
                i += 1
                line = fin.readline()

def sleep_on(n):
    if n == 0:
        return -1
    seen = [False]*10
    first = True
    i = 1
    orig = n
    power = 10
    while seen != [True]*10:
        n = i * orig
        tmp = n
        while tmp != 0:
            seen[tmp % 10] = True
            tmp = tmp // 10
        if not first:
            if n % power == 0:
                orig = n
                i = 1
                power *= 10
        else:
            i += 1
    return n


if __name__=="__main__":
    main()
