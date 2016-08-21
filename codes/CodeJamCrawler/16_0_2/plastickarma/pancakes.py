def flip(pancakes):
    current_pancakes = pancakes
    no_of_pancakes = len(pancakes)
    iterations = 0

    def first_index(ch):
        for index, entry in enumerate(current_pancakes):
            if entry is ch:
                return index
        return no_of_pancakes

    def do_flip(limit):
        part = current_pancakes[:limit + 1]
        part = reversed(part)
        part = list(['-' if e is '+' else '+' for e in part])
        part.extend(current_pancakes[limit + 1:])
        return part

    while True:
        if '-' not in current_pancakes:
            return iterations
        iterations += 1

        # make + in front a minus
        if current_pancakes[0] is '+':
            next_minus = first_index('-')
            current_pancakes = do_flip(next_minus - 1)
            continue

        if current_pancakes[0] is '-':
            next_plus = first_index('+')
            current_pancakes = do_flip(next_plus - 1)
            continue


assert flip('-'.split()) is 1
assert flip('+'.split()) is 0
assert flip(list('-+')) is 1
assert flip(list('--+')) is 1
assert flip(list('--')) is 1
assert flip(list('---')) is 1
assert flip(list('+-')) is 2
assert flip(list('+--')) is 2
assert flip(list('+++')) is 0
assert flip(list('--+-')) is 3
assert flip(list('++-')) is 2
assert flip(list('-+-')) is 3
assert flip(list('+-+')) is 2
assert flip(list('+-+-')) is 4

for i in range(1, int(input()) + 1):
    print("Case #" + str(i) + ": " + str(flip(list(input()))))
