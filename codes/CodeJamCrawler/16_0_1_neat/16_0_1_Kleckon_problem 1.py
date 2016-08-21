input_file = open("A-large.in")
output_file = open("A-small-output.txt", "w")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
case_number = 1

for n in input_file.readlines():
    seen_digits = list()
    n.strip()
    n = int(n)
    i = 1
    while True:
        number = n * i
        i += 1
        for digit in str(number):
            if int(digit) not in seen_digits:
                seen_digits.append(int(digit))
        seen_digits.sort()
        if digits == seen_digits:
            output_file.write("Case #{0}: {1}\n".format(case_number, number))
            break
        elif i > 100:
            output_file.write("Case #{0}: INSOMNIA\n".format(case_number))
            break
    case_number += 1

input_file.close()
output_file.close()
