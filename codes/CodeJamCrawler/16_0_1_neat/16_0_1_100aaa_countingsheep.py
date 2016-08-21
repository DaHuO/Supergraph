
import sys

def main(argv=sys.argv):
    output = open("A-large.out", "w")

    input = open("A-large.in", "r")
    number_of_tescases = int(input.readline())
    for case in range(1, number_of_tescases + 1):
        pick = int(input.readline())
        ret = solve(pick)
        if ret == -1:
            output.write("Case #" + str(case) + ": " + "INSOMNIA\n")
        else:
            output.write("Case #" + str(case) + ": " + str(ret) + "\n")

    output.close()
    input.close()

def solve(pick):
    iter = 1
    digits = {}
    history = []
    while True:
        current = pick * iter
        for p in str(current):
            digits[p] = True
        if len(digits) == 10:
            return current
        history.append(current)
        if determine_insomnia(history) == True:
            return -1
        iter += 1

def determine_insomnia(history):
    if len(history) < 101:
        return False
    digits = {}
    for t in history:
        digits[ str(t)[len(str(t)) - 1] ] = True
        if len(digits) == 10:
            return False
    if len(digits) < 10:
        return True



if __name__ == "__main__":
    main()