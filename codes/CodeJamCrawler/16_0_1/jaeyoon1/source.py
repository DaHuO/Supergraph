def merge_set(set_1, set_2):
    return set.union(set_1, set_2)


def split_number(number):
    num_list = []
    base = 10
    while number:
        num_list.append(number%base)
        number //= base
    return set(num_list)


def countsheep(number):
    number_set = set()
    if number == 0:
        return 'INSOMNIA'

    i = 1
    while len(number_set) < 10:
        number_set = (merge_set(number_set, split_number(number*i)))
        i += 1

    return number*(i-1)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    value = int(input())
    print("Case #{}: {}".format(i,countsheep(value)))


