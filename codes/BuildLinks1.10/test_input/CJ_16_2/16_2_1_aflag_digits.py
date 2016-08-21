import sys

def remove(word, sentence):
    new_sentence = sentence
    for c in word:
        if c not in new_sentence:
            return sentence
        else:
            new_sentence = new_sentence.replace(c, '', 1)
    return new_sentence

class LeftoversError(Exception):
    pass

def unscramble(phone, digits):
    if not digits:
        if phone:
            raise LeftoversError()
        else: 
            return ""
    digit = digits[0]
    new_phone = remove(digit, phone)
    if new_phone != phone:
        try:
            return digits_map[digit] + unscramble(new_phone, digits)
        except LeftoversError:
            try:
                return digits_map[digit] + unscramble(new_phone, digits[1:])
            except LeftoversError:
                return unscramble(phone, digits[1:])
    else:
        return unscramble(phone, digits[1:])

digits_map = {
    "ZERO": '0',
    "ONE": '1',
    "TWO": '2',
    "THREE": '3',
    "FOUR": '4',
    "FIVE": '5',
    "SIX": '6',
    "SEVEN": '7',
    "EIGHT": '8',
    "NINE": '9'
}

digits = [
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
]
f = sys.stdin
T = int(f.readline().strip())
for i in range(1, T+1):
    phone = f.readline().strip()
    print("Case #{}: {}".format(i, unscramble(phone, digits)))
