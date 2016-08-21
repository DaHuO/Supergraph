with open("A-large.in.txt") as f:
    case_number = 0
    test_cases = 1
    for line in f:
        multiplier = 2
        if case_number > test_cases:
            break
        words = line.split()

        n = words[0]
        if case_number == 0:
            test_cases = int(n)
            case_number += 1
        else:
            digits = []
            for iteration in range(1, 100, 1):
                for item in sorted(set(list(n))):
                    if item not in digits:
                        digits.append(item)
                if len(digits) == 10:
                    break
                else:
                    n = str(int(words[0]) * multiplier)
                    multiplier += 1
                iteration += 1
            if len(digits) == 10:
                print("Case #{}: {}".format(case_number, n))
            else:
                print("Case #{}: INSOMNIA".format(case_number))
            case_number += 1
