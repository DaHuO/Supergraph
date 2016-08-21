import sys


def revenge_solver(pancakes):
    current_deck = []
    pancakes_deck = list(pancakes.strip())

    happy = "+"
    sad = "-"
    flip = 0

    current_deck.append(pancakes_deck[0])

    for pan in range(1, len(pancakes_deck)):
        if pancakes_deck[pan] == current_deck[pan - 1]:
            current_deck.append(pancakes_deck[pan])
        else:
            if pancakes_deck[pan] == happy:
                flip += 1
                for i in range(0, len(current_deck)):
                    current_deck[i] = happy
                current_deck.append(pancakes_deck[pan])
            else:
                flip += 1
                for i in range(0, len(current_deck)):
                    current_deck[i] = sad
                current_deck.append(pancakes_deck[pan])

    if current_deck[len(current_deck) - 1] == sad:
        flip += 1
    return flip


def pancakes_revenge(arg):
    f_in = open(arg, "r")
    # iter_total = int(f_in.readlines()[0])
    lines = f_in.readlines()[1:]
    f_in.close()
    print(len(lines))
    f_out = open("small_output.txt", "w")
    iter = 0
    for pancakes in lines:
        iter += 1
        flips = revenge_solver(pancakes)
        f_out.writelines(["Case #%d: " % iter, str(flips), "\n"])
    # if iter_total == iter:
    #     print("All solved!")
    f_out.close()


def main(argv):
    pancakes_revenge(argv)

if __name__ == '__main__':
    main(sys.argv[1])
