
digit_dict = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9
}

unique_dict = {
    "Z": "ZERO",
    "W": "TWO",
    "U": "FOUR",
    "G": "EIGHT",
    "X": "SIX",
}

rest_digit ={
    "O": "ONE",
    "R": "THREE",
    "F": "FIVE",
}


def solve(s):
    s = list(s)
    temp = list(s)
    digits = []

    for i in unique_dict.keys():
        if i in temp:
            while i in temp:
                for j in unique_dict[i]:
                    temp.remove(j)
                digits.append(digit_dict[unique_dict[i]])

    for i in rest_digit.keys():
        if i in temp:
            while i in temp:
                for j in rest_digit[i]:
                    temp.remove(j)
                digits.append(digit_dict[rest_digit[i]])

    while "V" in temp:
        for i in "SEVEN":
            temp.remove(i)
        digits.append(7)

    while "N" in temp:
        for i in "NINE":
            temp.remove(i)
        digits.append(9)

    digits = [str(i) for i in sorted(digits)]
    return "".join(digits)


T = int(raw_input())

for i in range(T):
    s = raw_input()
    print "Case #%s:" % str(i+1), solve(s)

