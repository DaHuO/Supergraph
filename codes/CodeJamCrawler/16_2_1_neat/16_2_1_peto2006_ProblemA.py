t = int(input())

letters = dict()
digits = [0]*10


def process_char(char, digit, count, others):
    global digits
    global letters
    digits[digit] = letters.get(char, 0)//count
    for o in others:
        letters[o] = letters.get(o, 0) - digits[digit]

for case in range(1, t+1):
    s = input()
    for ch in s:
        letters[ch] = letters.get(ch, 0) + 1
    process_char('G', 8, 1, "EIGHT")
    process_char('X', 6, 1, "SIX")
    process_char('S', 7, 1, "SEVEN")
    process_char('V', 5, 1, "FIVE")
    process_char('I', 9, 1, "NINE")
    process_char("U", 4, 1, "FOUR")
    process_char("H", 3, 1, "THREE")
    process_char("W", 2, 1, "TWO")
    process_char("N", 1, 1, "ONE")
    process_char("O", 0, 1, "ZERO")

    print("Case #", case, ": ", sep="", end="")
    for i in range(len(digits)):
        print(str(i)*digits[i], end="")
    print("")