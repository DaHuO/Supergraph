import string
import collections


def get_top(c):

    letter, count = c.most_common(1)[0]
    if count == 1:

        c.pop(letter)

    else:

        c[letter] -= 1

    return letter


for case in range(int(input())):

    n = int(input())
    c = collections.Counter(
        dict(
            zip(
                string.ascii_uppercase,
                map(int, str.split(input()))
            ),
        )
    )

    result = []
    one_first = sum(c.values()) % 2 == 1
    while c:

        if one_first:

            result.append(get_top(c))
            one_first = False

        else:

            result.append(get_top(c) + get_top(c))

    print(str.format("Case #{}: {}", case + 1, str.join(" ", result)))
