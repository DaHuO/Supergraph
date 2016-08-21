def update_digits_seen(n, s):
    while n > 0:
        digit = n % 10
        s.add(digit)
        n //= 10

def solve(n):
    count = 1
    current_number = n
    last_number = None

    digits = set()

    while last_number != current_number:
        update_digits_seen(current_number, digits)

        if digits == set(range(0, 10)):
            return current_number

        last_number = current_number
        count += 1
        current_number = n * count

    return "INSOMNIA"


input_file = open("A-large.in", 'r')
lines = input_file.readlines()

output_file = open("Asmall.out", 'w')

input_size = int(lines[0])
for idx in range(1, input_size+1):
    input_num = int(lines[idx])
    line = "Case #{}: {}\n".format(idx, solve(input_num))
    output_file.write(line)