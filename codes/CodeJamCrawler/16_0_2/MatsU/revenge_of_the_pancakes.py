from string import maketrans


def revenge_of_the_pancakes(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    intab = "+-"
    outtab = "-+"
    trantab = maketrans(intab, outtab)

    stack = fin.readline().strip("\n")
    case_no = 1

    while case_no <= no_of_cases:
        no_of_flips = 0
        while len(stack) > 0:
            if stack[len(stack) - 1] == '-':
                if stack[0] == '+':
                    try:
                        next_blank = stack.index('-')
                        stack = "-" * next_blank + stack[next_blank:]
                        no_of_flips += 1
                    except ValueError:
                        no_of_flips += 1
                        break

                stack = stack[::-1].translate(trantab)
                no_of_flips += 1

            stack = stack.rstrip('+')

        fout.write("Case #" + str(case_no) + ": " + str(no_of_flips) + "\n")
        stack = fin.readline().strip("\n")
        case_no += 1

    fin.close()
    fout.close()

revenge_of_the_pancakes("sample.in", "sample.out")
revenge_of_the_pancakes("B-small-attempt0.in", "B-small-attempt0.out")
revenge_of_the_pancakes("B-large.in", "B-large.out")