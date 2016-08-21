def get_digits(num):

    if num == 0:
        return [0]

    digits = []
    while num > 0:
        digits.append(num % 10)
        num /= 10

    return digits


def get_last_number(num):
    num_set = set()
    i = 1
    while True:
        multiple = num * i
        num_set.update(get_digits(multiple))

        if len(num_set) == 10:
            break
        i += 1

    return multiple


T = input()
for t in range(T):
    num = input()

    if num == 0:
        print "Case #%d: INSOMNIA" % (t + 1)
        continue

    print "Case #%d: %d" % ((t + 1), get_last_number(num))
