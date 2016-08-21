
def write_answer(index, answer):
    print("Case #%s: %s" % (index, answer))


def main():
    f = open("D-small-attempt1.in")

    lines = f.readlines()
    case = lines[0].rstrip()

    for index in range(1, int(case) + 1):
        line = lines[index].rstrip()
        list_item = line.split()

        K = int(list_item[0])
        C = int(list_item[1])
        S = int(list_item[2])

        answer = ''
        for i in range(1, int(K) + 1):
            answer += str(i) + " "

        write_answer(index, answer)

        index += 1

    f.close()


main()
