from collections import OrderedDict 

DIGITS = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}

MARKERS = OrderedDict([
    (0, ["Z", ""]),
    (2, ["W", ""]),
    (4, ["U", ""]),
    (6, ["X", ""]),
    (8, ["G", ""]),
    (1, ["O", "W"]),
    (3, ["H", "G"]),
    (5, ["F", "U"]),
    (7, ["S", "X"]),
])

def solve(in_):
    out = []

    for digit, markers in MARKERS.items():
        marker, nm = markers[0], markers[1]
        #print("Testing", marker, in_)
        if marker in in_:
            #print("Possible", marker, in_)
            digit_here = True
            while digit_here:
                for letter in DIGITS[digit]:
                    if letter not in in_:
                        digit_here = False
                        break
                if digit_here:
                    for letter in DIGITS[digit]:
                        ix = in_.find(letter)
                        if ix >= 0:
                            in_ = in_[0:ix] + in_[ix+1:]
                    out.append(str(digit))

    for digit, letters in DIGITS.items():
        if digit in MARKERS:
            continue
        #print("Testing", letters, in_)
        digit_here = True
        while digit_here:
            for letter in letters:
                if letter not in in_:
                    digit_here = False
                    break
            if digit_here:
                #print("Found", letters, in_)
                for letter in letters:
                    ix = in_.find(letter)
                    if ix >= 0:
                        in_ = in_[0:ix] + in_[ix+1:]
                out.append(str(digit))
    if len(in_) > 0:
        print("FFFFFFFFFFFFFFFFFF", in_)
    out.sort()
    return "".join(out)


    

def main():
    t = int(input())
    for i in range(1, t + 1):
        in_ = input()
        print("Case #{}: {}".format(i, solve(in_)))

if __name__ == "__main__":
    main()
