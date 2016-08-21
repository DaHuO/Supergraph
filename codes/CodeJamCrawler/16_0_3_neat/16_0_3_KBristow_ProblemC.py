def process_line(line):
    line_split = line.split()
    length = int(line_split[0])
    number = int(line_split[1])
    candidate = get_initial_jam_coin_candidate(length)
    jam_coins = []
    divisor_set = []
    history = {}
    counter = 0
    while len(jam_coins) < number:
        number_divisors = test_candidate(candidate, history)
        if len(number_divisors) > 0:
            jam_coins += [candidate]
            divisor_set += [number_divisors]
            print str(len(jam_coins)) + ": " + jam_coins[-1]

        candidate = str(bin(long(candidate, 2) + 2))[2:]
        counter += 1

    result = "\n"
    for i in range(0, len(jam_coins)):
        new_line = str(jam_coins[i])
        for divisor in divisor_set[i]:
            new_line += " " + str(divisor)
        result += new_line + "\n"

    return result


def test_candidate(candidate, history):
    divisors = []
    numbers = []
    for i in range(2, 11):
        number_in_base = long(candidate, i)
        result = -1
        if number_in_base not in history:
            result = is_prime(number_in_base, 1000)
        if result != -1 and result is not True:
            divisors += [result]
            numbers += [number_in_base]
        else:
            history[number_in_base] = True
            return []
    # print candidate
    # print numbers
    # print divisors
    return divisors


def is_prime(number, cap):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0:
        return 2
    elif number % 3 == 0:
        return 3

    i = 5
    permutations = 1
    while i * i <= number and permutations < cap:
        if number % i == 0:
            return i
        elif number % (i + 2) == 0:
            return i + 2
        i += 6
        permutations += 1

    if permutations == cap:
        return -1

    return True


def get_initial_jam_coin_candidate(length):
    candidate = "1" + "0" * (length - 2) + "1"
    return candidate

year = 2016
problem_set = "LargeC"

with open(problem_set, 'r') as file_handle:
    lines = file_handle.readlines()


output_str = ""
for i in range(1, len(lines)):
    output_str += "Case #" + str(i) + ": " + str(process_line(lines[i])) + "\n"


output_str = output_str.strip()
print output_str
with open(str(year) + problem_set + ".out", "w") as file_handle:
    file_handle.write(output_str)


