import sys

def find_word(line):
    my_dic = []
    for i in line:
        if not my_dic:
            my_dic.append(i)
        else:
            new_dic = []
            for el in my_dic:
                new_dic.append(el + i)
                new_dic.append(i + el)
            my_dic = new_dic
    res = sorted(my_dic)
    return res[len(res)-1]


def game_play(arg):
    f_in = open(arg, "r")
    lines = f_in.readlines()[1:]
    f_in.close()
    print(len(lines))
    f_out = open("small_output.txt", "w")
    iter = 0
    for line in lines:
        iter += 1
        word = find_word(line)
        f_out.writelines(["Case #%d: " % iter, word])
    f_out.close()

def main(argv):
    game_play(argv)

if __name__ == '__main__':
    main(sys.argv[1])
