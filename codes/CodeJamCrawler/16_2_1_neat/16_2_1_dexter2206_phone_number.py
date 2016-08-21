
def reduce_word(origin, word, char):

    occur = origin.count(char)
    for k in range(occur):
        for s in word:
            origin = origin.replace(s, "", 1)
    return occur, origin


DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
          "EIGHT", "NINE"]

CHAR = [("SIX", "X"), ("ZERO", "Z"), ("EIGHT", "G"), ("THREE", "H"),
        ("FOUR", "R"), ("FIVE", "F"), ("SEVEN", "V"), ("TWO", "W"),
        ("ONE", "O"), ("NINE", "I")]

def decode_number(origin):
    occur = {}

    for char in CHAR:
        loc_occur, origin = reduce_word(origin, char[0], char[1])
        occur[char[0]] = loc_occur

    number = ""
    for ind, digit in enumerate(DIGITS):
        number = number + occur[digit] * str(ind)
    return number

def main():
    nb_tests = int(input())
    for test_no in range(nb_tests):
        origin = str(input())
        print("Case #{k}: {number}".format(k=test_no+1,
                                           number=decode_number(origin)))

if __name__ == "__main__":
    main()
