import sys

def get_digits(n):
        yield n % 10
        if n >= 10:
            yield from get_digits(n//10)

def last_number_naive(initial):
    digits_seen = set()
    seen_numbers = set()
    multiplier = 0
    while len(digits_seen) < 10 and initial * (multiplier + 1) not in seen_numbers:
        multiplier += 1
        current = initial * multiplier
        current_digits = set(get_digits(current))
        digits_seen |= current_digits
        seen_numbers.add(current)
        # print(multiplier, current, current_digits)
        # print(digits_seen)

    return current

assert set(get_digits(10)) == {0, 1}

for i, line in enumerate(open(sys.argv[1])):
    initial = int(line)
    if i == 0:
        continue

    # print('New: {}'.format(initial))
    current = last_number_naive(initial)
    print('Case #{}: {}'.format(i, current if current > 0 else 'INSOMNIA'))

