FILENAME = 'A-large'
all_digits = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 0})

with open('{}.in'.format(FILENAME), 'r') as f:
    input = list(map(int, f.read().split()))
    # print(input, type(input), type(input[0]))

with open('{}.out'.format(FILENAME), 'w') as f:
    for n in range(1, input[0] + 1):
        number = input[n]
        if number == 0:
            f.write('Case #{}: INSOMNIA\n'.format(n))

        else:
            digits_set = set()
            i = 1
            while True:
                current = number * i
                digits_set.update(set(map(int, str(current))))
                if not (all_digits - digits_set):
                    f.write('Case #{name}: {value}\n'.format(name=n, value=current))
                    break
                else:
                    i += 1
