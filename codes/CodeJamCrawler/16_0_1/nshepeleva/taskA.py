import sys


def sheep_conter(line):
    sheep_list = []
    sheep_str = line.strip()
    sheep_int = int(sheep_str)
    indexer = 0

    while len(sheep_list) < 10:
        indexer += 1
        sheep = sheep_int * indexer
        sheep_str = str(sheep)
        if sheep_str[0] != str(0):
            for chr in sheep_str:
                if chr in sheep_list:
                    pass
                else:
                    sheep_list.append(chr)
        else:
            sheep_str = "INSOMNIA"
            break
    return sheep_str


def sheep_stuff(arg):
    f_in = open(arg, "r")
    lines = f_in.readlines()[1:]
    f_in.close()
    print(len(lines))
    f_out = open("small_output.txt", "w")
    iter = 0
    for line in lines:
        iter += 1
        sheep_str = sheep_conter(line)
        f_out.writelines(["Case #%d: " % iter, sheep_str, "\n"])
        # print(sheep_str)
    f_out.close()


def main(argv):
    sheep_stuff(argv)

if __name__ == '__main__':
    main(sys.argv[1])