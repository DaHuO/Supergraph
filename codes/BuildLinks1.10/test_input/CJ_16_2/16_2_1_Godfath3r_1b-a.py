from pprint import pprint

input_filename = 'A-large.in'
output_filename = 'A-large.out'


def are_all_chars_in(number, string):
    for ch in reversed(number):
        if ch in string:
            string.remove(ch)
        else:
            return False
    return True

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
h = []
for num in numbers:
    h.append(''.join([x for x in reversed(sorted(num))]))
sorts = []
for x in sorted(h):
    sorts.append(x)
i = 0
numbers_dict = {}
for num in numbers:
    numbers_dict[''.join([x for x in reversed(sorted(num))])] = i
    i += 1
pprint(numbers_dict)
results = []


# Read from input file
with open(input_filename, 'r') as _file:
    T = int(_file.readline())
    for _ in range(T):
        given = sorted(_file.readline().strip())
        # print given
        length = len(given)
        final_nums = []
        i = len(sorts)-1
        while i >= 0:
            # print 'Checking number:', sorts[i]
            g = given[:]
            if are_all_chars_in(sorts[i], given):
                for char in sorts[i]:
                    g.remove(char)
                # print sorts[i]
                final_nums.append(sorts[i])
                i += 1
            given = g[:]
            i -= 1
        # print final_nums
        assert len(''.join(final_nums)) == length, "something is wrong {} {}".format(len(''.join(final_nums)), length)
        digits = []
        for num in final_nums:
            digits.append(numbers_dict[''.join([x for x in reversed(sorted(num))])])
        digits = sorted(digits)
        results.append(digits)

# Write to output
i = 1
with open(output_filename, 'w') as _file:
    for res in results:
        _file.write('Case #{}: {}\n'.format(i, ''.join(map(str, [x for x in res]))))
        i += 1