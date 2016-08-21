def brute_force(value):
    seen = {x: False for x in range(10)}
    multiplier = 1
    while multiplier < 1000:
        number = value * multiplier
        for character in str(number):
            seen[int(character)] = True
            if all(seen.values()):
                return number
        multiplier += 1
    return -1


def main():
    file = open('counting_sheep.in', 'r')
    lines = file.readlines()
    lines = [int(line.strip()) for line in lines]
    cases = lines[0]
    input_values = lines[1:]
    for case, value in enumerate(input_values):
        last_number = brute_force(value)
        if last_number < 0:
            print('Case #{}: INSOMNIA'.format(case + 1))
        else:
            print('Case #{}: {}'.format(case + 1, last_number))


if __name__ == '__main__':
    main()
