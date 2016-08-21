limit_N = 10*10*10*10*10*10

def write_answer(index, input, answer):
    print("Case #%s: %s" % (index, answer))


def make_answer(input_number):
    digit_slot = {}
    insomnia = True
    for N in range(0, limit_N):
        number = int(input_number) * (int(N) + 1)

        for digit in str(number):
            digit_slot[digit] = True

        if len(digit_slot) == 10:
            insomnia = False
            break

    if insomnia:
        number = "INSOMNIA"

    return number


def main():
    f = open("A-large.in")

    lines = f.readlines()
    del lines[0]

    index = 1
    for line in lines:
        line = line.rstrip()

        answer = make_answer(line)
        write_answer(index, line, answer)

        index += 1

    f.close()


main()


