def counting_sheep(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    n = fin.readline().strip("\n")
    case_no = 1

    while case_no <= no_of_cases:
        start_n = int(n)
        numbers = [1] * 10

        if start_n == 0:
            fout.write("Case #" + str(case_no) + ": " + "INSOMNIA\n")
        else:
            while sum(numbers) > 0:
                numbers_in_n = list(n)
                for number in numbers_in_n:
                    numbers[int(number)] = 0
                last_number = n
                n = str(int(n) + start_n)
            fout.write("Case #" + str(case_no) + ": " + last_number + "\n")

        n = fin.readline().strip("\n")
        case_no += 1

    fin.close()
    fout.close()

counting_sheep("A-small-attempt0.in", "A-small-attempt0.out")
counting_sheep("A-large.in", "A-large.out")