import math


def coin_jam(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    n, goal = fin.readline().strip("\n").split(' ')
    n = int(n)
    goal = int(goal)

    case_no = 1
    no_of_jamcoins = 0

    multipliers = []
    for i in range(2, 11):
        multipliers.append([])
        for j in range(n):
            multipliers[i - 2].append(math.pow(i, j))

    while case_no <= no_of_cases:
        fout.write("Case #" + str(case_no) + ":\n")
        for i in range(int(math.pow(2, n-1)), int(math.pow(2, n))):
            if i % 2 == 0:
                continue

            binary = str(bin(i))[2:]
            binary = ("0" * (n - len(binary)) + binary)[::-1]
            numbers = [sum([int(binary[j]) * multipliers[k-2][j] for j in range(n)]) for k in range(2,11)]
            divisors = []
            for number in numbers:
                divisor = 2
                limit = math.ceil(math.sqrt(number))
                while divisor < limit:
                    if number % divisor == 0:
                        divisors.append(divisor)
                        break
                    divisor += 1

                if divisor >= limit:
                    break

            if len(divisors) == 9:
                fout.write(binary[::-1] + " ")
                for j in range(8):
                    fout.write(str(divisors[j]) + " ")
                fout.write(str(divisors[8]) + "\n")
                no_of_jamcoins += 1

            if no_of_jamcoins == goal:
                case_no += 1
                break

    fin.close()
    fout.close()

coin_jam("sample.in", "sample.out")
coin_jam("C-small-attempt0.in", "C-small-attempt0.out")
