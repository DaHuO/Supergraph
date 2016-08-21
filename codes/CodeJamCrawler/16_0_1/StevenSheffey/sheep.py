import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()][1:]

def sheep_count(number):
    if number == 0:
        return 'INSOMNIA'
    cur_number = number
    found_digits = [False] * 10
    num_sheep = 0
    while True:
        num_sheep += 1
        for digit in map(int, str(cur_number)):
            found_digits[digit] = True
        if not(all(found_digits)):
            cur_number += number
        else:
            break
    return cur_number



for case, number in enumerate(data):
    print("CASE #{:d}: {}".format(case+1, sheep_count(number)))
