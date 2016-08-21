import collections


digits = (
    "ZERO",
    "TWO",
    "FOUR",
    "SIX",
    "EIGHT",
    "ONE",
    "THREE",
    "FIVE",
    "SEVEN",
    "NINE",
)
numbers = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
digits = tuple(map(collections.Counter, digits))

for case in range(int(input())):

    chars = collections.Counter(str.strip(input()))
    result = []
    for digit, number in zip(digits, numbers):

        while all(map(lambda ch: digit[ch] <= chars[ch], digit)):

            result.append(number)
            chars = chars - digit

    print(
        str.format(
            "Case #{}: {}",
            case + 1,
            str.join("", map(str, sorted(result)))
        )
    )
