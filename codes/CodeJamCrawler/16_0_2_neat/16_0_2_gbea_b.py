T = int(raw_input())


def flip(array, i):
    return [not a for a in array[:i]] + array[i:]

for t in range(T):
    res = 0
    s = raw_input()
    pancakes = [x == '+' for x in s]

    while False in pancakes:
        first = pancakes[0]
        i = 0
        while i < len(pancakes) and pancakes[i] == first:
            i += 1

        pancakes = flip(pancakes, i)
        res += 1

    print("Case #{0}: {1}".format(t+1, res))
