from collections import defaultdict
nums = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE"
}

d = defaultdict(int, nums)


def remove_num(s, num):
    for item in list(d[num]):
        s = s.replace(item, '', 1)
    return s


def get_phone_number(s):
    res = list()
    if 'Z' in s:
        while "Z" in s:
            s = remove_num(s, 0)
            res.append(0)
    if 'W' in s:
        while "W" in s:
            s = remove_num(s, 2)
            res.append(2)

    if "X" in s:
        while "X" in s:
            s = remove_num(s, 6)
            res.append(6)

    if "G" in s:
        while "G" in s:
            s = remove_num(s, 8)
            res.append(8)

    if "H" in s:
        while "H" in s:
            s = remove_num(s, 3)
            res.append(3)

    if "R" in s:
        while "R" in s:
            s = remove_num(s, 4)
            res.append(4)

    if "O" in s:
        while "O" in s:
            s = remove_num(s, 1)
            res.append(1)

    if "F" in s:
        while "F" in s:
            s = remove_num(s, 5)
            res.append(5)

    if "I" in s:
        while "I" in s:
            s = remove_num(s, 9)
            res.append(9)

    while "S" in s:
        s = remove_num(s, 7)
        res.append(7)

    return "".join(map(str, sorted(res)))

with open("large.in") as infile:
    with open("large.out", "w+") as outfile:
        num_cases = int(infile.readline())

        for row in range(1, num_cases + 1):
            s = infile.readline().strip()
            res = get_phone_number(s)
            outfile.write("Case #{0}: {1}\n".format(row, res))
