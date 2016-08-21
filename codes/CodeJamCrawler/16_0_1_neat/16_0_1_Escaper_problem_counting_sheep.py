case = 1


def sleepy_number(number):
        number = int(number)
        if 0 <= number <= 1000000:
            if number == 0:
                return "Case #{0}: ".format(case) + "INSOMNIA"
            digits_in_mind = []
            i = 2
            num_to_comp = int(number)
            while True:
                [digits_in_mind.append(int(num)) for num in str(num_to_comp) if int(num) not in digits_in_mind]
                if sum(digits_in_mind) == 45 and 0 in digits_in_mind:
                    return "Case #{0}: ".format(case) + str(num_to_comp)
                num_to_comp = number * i
                i += 1

with open("A-large.in") as input_f:
    read = [line.strip() for line in input_f.readlines()]
    T = int(read[0])
    for i in range(1, len(read)):
        print(sleepy_number(read[i]))
        case += 1
